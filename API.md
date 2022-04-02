# Bilibili API

### 用户信息

https://api.bilibili.com/x/space/acc/info?mid={用户ID}

### 用户创建的所有收藏夹

https://api.bilibili.com/x/v3/fav/folder/created/list-all?up_mid={用户ID}

### 收藏夹内投稿

https://api.bilibili.com/x/v3/fav/resource/list?media_id={收藏夹ID}&pn={从1开始页数}&ps={每页个数最多20个}&keyword=&order=mtime&type=0&tid=0&platform=web&jsonp=jsonp

### 视频分p信息

https://api.bilibili.com/x/player/pagelist?bvid={视频bvid}&jsonp=jsonp
