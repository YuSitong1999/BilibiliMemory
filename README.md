# Bilibili Memory 哔哩哔哩记忆

## 介绍

将 [哔哩哔哩（Bilibili，又称B站）](https://www.bilibili.com/) 收藏夹中收藏的视频， 下载备份到本地磁盘，避免线上视频被删除。

Get videos in user created favorite folders on [bilibili](https://www.bilibili.com/), and save them to the local disk to
prevent the online videos from being deleted.

使用 [FFmpeg](http://ffmpeg.org/) 合并m4s音频和视频

详细介绍：[B站收藏备份工具设计和实现](https://blog.csdn.net/u010834463/article/details/126310063)

## 运行

### 编辑配置

编辑config.ini

### 编辑备份目标

* status 查看备份目标
* add 增加备份目标收藏夹和条件
* rm 删除备份目标条目

```
python main.py aim
    status
    add <收藏夹ID1>[,<收藏夹ID2>,...,<收藏夹IDN>] [-t <最早发布时间>] [-l <投稿时长>]
    rm <备份目标收藏夹序号> [备份目标条件序号1,...,备份目标条件序号N]
    addm <投稿BV ID1>[,<投稿BV ID2>,...,<投稿BV IDN>]
    rmm <投稿BV ID1>[,<投稿BV ID2>,...,<投稿BV IDN>]
    addu <UP主 ID1>[,<UP主 ID2>,...,<UP主 IDN>] [-t <最早发布时间>] [-l <投稿时长>]
    rmu <备份目标UP主序号> [备份目标UP主条件序号1,...,备份目标UP主条件序号N]
```

### 同步备份目标对应的文件

查看需要执行的操作，确认后执行

```
python main.py update
```

### 清除旧日志文件

删除旧日志文件。保留旧日志个数，缺省为10，至少为1(当前日志)。

```
python main.py clear [保留旧日志个数]
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
        * aim.json 备份目标收藏夹和筛选条件
        * local.json 本地现有投稿的bv_id
        * deleted.json 本地保存线上已删除的bv_id
        * lost.json 已丢失收藏的残余信息
    * tmp \ 临时目录
        * tmp_[audio|video].m4s 正在下载的视频音频文件（同时只有一个，因此无需分P）
        * tmp_media \(_[pageID]\) .mp4 已合并的较靠前分P
        * tmp_[dateTime].log 日志临时文件

## 程序流程

### 备份目标

#### 增加备份目标

向备份目标加入收藏夹和筛选条件（发布时间戳和时长）。
同一收藏夹满足多个条件中任一，就是备份目标。

#### 删除备份目标

从备份目标中删除指定编号的收藏夹，或收藏夹的筛选条件。

#### 显示所有备份目标

显示所有备份目标收藏夹，和每个收藏夹的所有筛选条件。

### 更新

#### 查看更新计划并执行

* 读取更新备份目标aim.json
* 读取本地已备份投稿和已删除投稿信息
* 按条件获取收藏夹中投稿信息，分为未删除投稿信息和已删除投稿残余信息
* 创建执行计划：
    * 新收藏（本地不存在，线上未删除）：下载投稿
    * 新删除（本地存在，线上有残留记录）：更新本地备份状态
    * 新丢失（本地不存在，线上有残留记录）：下载残留记录
* 询问是否执行更新

## TODO

根据使用体验争取不时更新 ~~如果有时间的话~~

- [x] 增加、显示、删除备份目标收藏夹
- [x] 查看将要更新的视频信息
- [x] 执行更新
- [x] 自动删除旧日志，只保留最近10个日志文件
- [x] 支持强制备份指定BV的投稿
- [x] 支持设置备份目标UP主
- [ ] 对于有阅读价值的数据，保存为JSON的同时，另行保存为CSV
- [ ] 支持配置目录
- [ ] 另行按收藏夹保存全部投稿
- [ ] 支持使用cookie下载私密收藏夹
- [ ] 支持更新已下载但被up主更新的视频
- [ ] 支持从第三方平台获取丢失投稿
