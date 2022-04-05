# Bilibili Memory 哔哩哔哩记忆

## 介绍

获取在 [哔哩哔哩](https://www.bilibili.com/) 收藏夹中收藏的视频， 保存到本地磁盘，避免线上视频被删除。

Get videos in user created favorite folders on [bilibili](https://www.bilibili.com/), and save them to the local disk to
prevent the online videos from being deleted.

使用 [FFmpeg](http://ffmpeg.org/) 合并m4s音频和视频

## 运行

### 编辑配置

编辑config.ini

### 编辑元数据

-o

* add 增加目标收藏夹和条件
* rm 删除目标收藏夹和条件
* status 查看元数据

-f 目标收藏夹

-t 最早日期

-l 时长限制

```
python main.py meta
    -o [add | rm | status]
    [-f <folderID1>[,<folderID2>,...,<folderIDn>]]
    [-t <afterDate>]
    [-l <lengthLimit>]
```

### 同步元数据对应的文件

-o

* status 查看需要下载的内容
* run 执行同步操作

```
python main.py update
    -o [status | run]
```

## 文件保存结构

* output \ 输出目录
    * all \ 保存所有下载合并后的投稿文件
        * [bv_id] \( \_[pageID] \) .mp4 视频
        * [bv_id].json 投稿信息
        * [bv_id].jpg 封面图片
    * deleted \ 已被删除的投稿文件
        * 同上3类的硬链接
        * [bv_id]_[validatedTitle].name 投稿标题标记
        * [bv_id] \( \_[pageID] \) \_[validatedPageTitle].name 投稿分P标题标记
    * meta \ 元数据目录
        * aim.json 目标收藏夹和过滤条件
        * local.json 本地现有投稿的bv_id
        * deleted.json 本地保存线上已删除的bv_id
        * lost.json 已丢失收藏的残余信息
    * tmp \ 临时目录
        * tmp_[audio|video].m4s 正在下载的视频音频文件（同时只有一个，因此无需分P）
        * tmp_media \(_[pageID]\) .mp4 已合并的较靠前分P
        * tmp_[dateTime].log 日志临时文件

## 程序流程

### 元数据

#### 增加收藏夹

读取aim，加入新收藏夹和筛选条件

#### 删除收藏夹

读取aim，删除指定编号的信息

#### 显示所有元数据

读取aim，输出到屏幕

### 更新

#### 查看将要更新的视频信息

* 读取aim.json
* 按条件获取收藏夹中媒体信息，去除重复，输出到屏幕，分别显示新增和已丢失投稿

#### 执行更新

* 检查local的现有投稿，被删除的从all硬链接到deleted
* 读取aim.json
* 按条件获取收藏夹中媒体信息，去除重复，分为新增和已丢失投稿
    * 新的投稿下载到all，同时更新local.json
    * 新的已丢失信息写入lost.json

## TODO

### 功能

- [x] 设置元数据
- [x] 显示元数据
- [x] 删除元数据
- [x] 查看将要更新的视频信息
- [x] 执行更新
- [ ] 支持使用cookie下载私密收藏夹
- [ ] 支持更新已下载但被up主更新的视频
