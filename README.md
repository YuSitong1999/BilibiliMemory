# Bilibili Memory 哔哩哔哩记忆

## 介绍

将 [哔哩哔哩（Bilibili，又称B站）](https://www.bilibili.com/) 指定收藏夹中、UP主的或单独的投稿中的视频， 下载备份到本地磁盘，避免线上视频被删除。

支持通过每次更新后生成的网页，查看本地投稿信息。

Get videos in user created favorite folders on [bilibili](https://www.bilibili.com/), and save them to the local disk to
prevent the online videos from being deleted.

使用 [FFmpeg](http://ffmpeg.org/) 合并m4s音频和视频，元数据保存到 SQLite3。

~~详细介绍(已过时)：[B站收藏备份工具设计和实现](https://blog.csdn.net/u010834463/article/details/126310063)~~

## 运行

### 编辑备份目标

* status 查看备份目标
* add/addm/addu 增加备份目标 收藏夹/投稿/UP主 和限制条件
* rm/rml 删除备份 目标/目标限制条件 条目

```
python main.py aim
    status
    add <收藏夹ID1>[,<收藏夹ID2>,...,<收藏夹IDN>] [-a <最早发布时间>] [-d <投稿时长秒数>]
    addm <投稿BV ID1>[,...,<投稿BV IDN>]
    addu <UP主 ID1>[,...,<UP主 IDN>] [-a <最早发布时间>] [-d <最长投稿时长秒数>]
    rm <备份目标ID1>[,...,<备份目标IDN>]
    rml <备份目标限制条件ID1>[,...,<备份目标限制条件IDN>]
```

示例：
```shell
# 查看备份目标状态
python .\main.py aim status

# 将收藏夹 1561982153 中最早发布时间为 2022-08-01 的投稿添加为备份目标
python .\main.py aim add 1561982153 -a '2022-08-01'

# 将 UP主 1210635994 的最早发布时间为 '2023-07-01' 且 最长投稿时长为 60 秒的投稿添加为备份目标
python .\main.py aim addu 1210635994 -a '2023-07-01' -d 60

# 将投稿 BV1om4y1y7Cz 添加为备份目标
python .\main.py aim addm BV1om4y1y7Cz
```

最早发布时间 格式2022-09-10

### 同步备份目标对应的文件

查看需要执行的操作，确认后执行，执行后更新所有投稿信息网页。

```
python main.py update
```

## 配置

[config_example.json5](config_example.json5) 首次执行时复制为 config.json5

## TODO

根据使用体验争取不时更新 ~~如果有时间的话~~

- [x] 增加、查看和删除备份目标收藏夹、UP主和投稿
- [x] 改用SQLite3保存数据
- [x] 支持配置目录
- [ ] 支持使用cookie下载私密收藏夹
- [ ] 改为Web服务进行增加、查看和删除操作
- [ ] 支持从第三方平台获取丢失投稿信息
- [ ] 支持更新已下载但被up主更新的视频
