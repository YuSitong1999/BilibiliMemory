# Bilibili Memory 哔哩哔哩记忆

## 介绍

保存 [哔哩哔哩](https://www.bilibili.com/) 收藏的视频

Save your favorite videos at [bilibili](https://www.bilibili.com/) to disk.

使用 [FFmpeg](http://ffmpeg.org/) 合并m4s音频和视频

## 运行

```
python main.py {userID}
```

## TODO

### 基本功能

- [x] 保存用户基本信息和公开收藏夹信息
- [x] 保存收藏夹中的收藏条目信息
- [x] 下载收藏条目的视频
- [ ] 支持下载分p视频
- [ ] 增量下载新收藏的视频

### 其他功能

- [ ] 支持更新已下载但被up主更新的视频
- [ ] 支持利用cookies下载私密收藏的视频

### 配置

- [ ] 支持配置输出目标文件夹
- [ ] 支持配置用户ID
- [ ] 支持配置元数据(当前已有视频的数据)所在位置
- [ ] 支持配置临时文件夹

