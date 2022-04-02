# Bilibili API

### 用户信息

https://api.bilibili.com/x/space/acc/info?mid={用户ID}

```json
{
  "code": 0,
  "message": "0",
  "ttl": 1,
  "data": {
    "mid": 64993,
    "name": "矢泽日香",
    "sex": "保密",
    "face": "http://i1.hdslb.com/bfs/face/4106b95eb62c5bec4731be3826324ab7d2d6e0e3.jpg",
    "face_nft": 0,
    "sign": "微博： www.weibo.com/1777594171",
    "rank": 10000,
    "level": 6,
    "jointime": 0,
    "moral": 0,
    "silence": 0,
    "coins": 0,
    "fans_badge": false,
    "fans_medal": {
      "show": true,
      "wear": true,
      "medal": {
        "uid": 64993,
        "target_id": 1276787,
        "medal_id": 371,
        "level": 1,
        "medal_name": "伯爵",
        "medal_color": 6067854,
        "intimacy": 199,
        "next_intimacy": 201,
        "day_limit": 1500,
        "medal_color_start": 6067854,
        "medal_color_end": 6067854,
        "medal_color_border": 6067854,
        "is_lighted": 1,
        "light_status": 1,
        "wearing_status": 1,
        "score": 199
      }
    },
    "official": {
      "role": 0,
      "title": "",
      "desc": "",
      "type": -1
    },
    "vip": {
      "type": 2,
      "status": 1,
      "due_date": 1692979200000,
      "vip_pay_type": 1,
      "theme_type": 0,
      "label": {
        "path": "",
        "text": "年度大会员",
        "label_theme": "annual_vip",
        "text_color": "#FFFFFF",
        "bg_style": 1,
        "bg_color": "#FB7299",
        "border_color": ""
      },
      "avatar_subscript": 1,
      "nickname_color": "#FB7299",
      "role": 3,
      "avatar_subscript_url": "http://i0.hdslb.com/bfs/vip/icon_Certification_big_member_22_3x.png"
    },
    "pendant": {
      "pid": 2511,
      "name": "初音未来13周年",
      "image": "http://i1.hdslb.com/bfs/garb/item/4f8f3f1f2d47f0dad84f66aa57acd4409ea46361.png",
      "expire": 0,
      "image_enhance": "http://i1.hdslb.com/bfs/garb/item/fe0b83b53e2342b16646f6e7a9370d8a867decdb.webp",
      "image_enhance_frame": "http://i1.hdslb.com/bfs/garb/item/127c507ec8448be30cf5f79500ecc6ef2fd32f2c.png"
    },
    "nameplate": {
      "nid": 74,
      "name": "大会员2018年度勋章",
      "image": "http://i2.hdslb.com/bfs/face/421179426c929dfeaed4117461c83f5d07ffb148.png",
      "image_small": "http://i1.hdslb.com/bfs/face/682001c2e1c2ae887bdf2a0e18eef61180c48f84.png",
      "level": "稀有勋章",
      "condition": "2018.6.26-7.8某一天是年度大会员"
    },
    "user_honour_info": {
      "mid": 0,
      "colour": null,
      "tags": [
      ]
    },
    "is_followed": false,
    "top_photo": "http://i1.hdslb.com/bfs/space/cb1c3ef50e22b6096fde67febe863494caefebad.png",
    "theme": {
    },
    "sys_notice": {
    },
    "live_room": {
      "roomStatus": 1,
      "liveStatus": 0,
      "url": "https://live.bilibili.com/53719?broadcast_type=0&is_room_feed=0",
      "title": "矢泽日香的直播间",
      "cover": "https://s1.hdslb.com/bfs/static/blive/live-assets/common/images/no-cover.png",
      "roomid": 53719,
      "roundStatus": 0,
      "broadcast_type": 0,
      "watched_show": {
        "switch": true,
        "num": 6,
        "text_small": "6",
        "text_large": "6人看过",
        "icon": "https://i0.hdslb.com/bfs/live/a725a9e61242ef44d764ac911691a7ce07f36c1d.png",
        "icon_location": "",
        "icon_web": "https://i0.hdslb.com/bfs/live/8d9d0f33ef8bf6f308742752d13dd0df731df19c.png"
      }
    },
    "birthday": "",
    "school": {
      "name": ""
    },
    "profession": {
      "name": "",
      "department": "",
      "title": "",
      "is_show": 0
    },
    "tags": null,
    "series": {
      "user_upgrade_status": 3,
      "show_upgrade_window": false
    },
    "is_senior_member": 1
  }
}
```

### 用户创建的所有收藏夹

https://api.bilibili.com/x/v3/fav/folder/created/list-all?up_mid={用户ID}

https://api.bilibili.com/x/v3/fav/folder/created/list-all?up_mid=95451953

```json
{
  "code": 0,
  "message": "0",
  "ttl": 1,
  "data": {
    "count": 12,
    "list": [
      {
        "id": 49776653,
        "fid": 497766,
        "mid": 95451953,
        "attr": 0,
        "title": "默认收藏夹",
        "fav_state": 0,
        "media_count": 771
      },
      {
        "id": 1062845153,
        "fid": 10628451,
        "mid": 95451953,
        "attr": 22,
        "title": "学习",
        "fav_state": 0,
        "media_count": 16
      },
      {
        "id": 1185648053,
        "fid": 11856480,
        "mid": 95451953,
        "attr": 2,
        "title": "UP学习",
        "fav_state": 0,
        "media_count": 7
      }
    ],
    "season": null
  }
}
```

### 收藏夹内投稿

https://api.bilibili.com/x/v3/fav/resource/list?media_id={收藏夹ID}&pn={从1开始页数}&ps={每页个数最多20个}&keyword=&order=mtime&type=0&tid=0&platform=web&jsonp=jsonp

```json
{
  "code": 0,
  "message": "0",
  "ttl": 1,
  "data": {
    "info": {
      "id": 1561982153,
      "fid": 15619821,
      "mid": 95451953,
      "attr": 22,
      "title": "测试",
      "cover": "http://i1.hdslb.com/bfs/archive/205ac1275b3f41b6dd2da56b3f6d94ce3a1dcebb.jpg",
      "upper": {
        "mid": 95451953,
        "name": "小木曾春希",
        "face": "http://i2.hdslb.com/bfs/face/c64dd9d24b2e913ddb47151d3391068844f02a47.jpg",
        "followed": true,
        "vip_type": 1,
        "vip_statue": 0
      },
      "cover_type": 2,
      "cnt_info": {
        "collect": 0,
        "play": 0,
        "thumb_up": 0,
        "share": 0
      },
      "type": 11,
      "intro": "",
      "ctime": 1648801335,
      "mtime": 1648801335,
      "state": 0,
      "fav_state": 0,
      "like_state": 0,
      "media_count": 4
    },
    "medias": [
      {
        "id": 380440390,
        "type": 2,
        "title": "我对《妇女权益保障法(修订草案）》的意见",
        "cover": "http://i1.hdslb.com/bfs/archive/205ac1275b3f41b6dd2da56b3f6d94ce3a1dcebb.jpg",
        "intro": "提意见有用，而且很有必要！如果法律不明确，游戏女性角色好看没准也算性骚扰。\r\n更新和精简版见视频P1\r\n妇女权益保障法(修订草案）征求意见（2022年1月22日截止）\r\nhttp://www.npc.gov.cn/flcaw/userIndex.html?lid=ff8081817ddb134a017deac847ed20e0\r\n我发现有许多有令人担忧之处，特别是第2、17、28、50、53、56、66、70、76条，见视频P1\r\n\r\n所有建议见P2，关于：\r\n第一章 总则：第2条 特别措施应合理，第9（",
        "page": 2,
        "duration": 1985,
        "upper": {
          "mid": 95451953,
          "name": "小木曾春希",
          "face": "http://i2.hdslb.com/bfs/face/c64dd9d24b2e913ddb47151d3391068844f02a47.jpg"
        },
        "attr": 0,
        "cnt_info": {
          "collect": 944,
          "play": 68884,
          "danmaku": 110
        },
        "link": "bilibili://video/380440390",
        "ctime": 1641193911,
        "pubtime": 1641193911,
        "fav_time": 1648883396,
        "bv_id": "BV13Z4y1S7Zc",
        "bvid": "BV13Z4y1S7Zc",
        "season": null,
        "ogv": null,
        "ugc": {
          "first_cid": 478500783
        }
      },
      {
        "id": 969856933,
        "type": 2,
        "title": "已失效视频",
        "cover": "http://i0.hdslb.com/bfs/archive/be27fd62c99036dce67efface486fb0a88ffed06.jpg",
        "intro": "-",
        "page": 1,
        "duration": 232,
        "upper": {
          "mid": 295617827,
          "name": "我是未来的光",
          "face": "http://i0.hdslb.com/bfs/face/member/noface.jpg"
        },
        "attr": 1,
        "cnt_info": {
          "collect": 15,
          "play": 13203,
          "danmaku": 1
        },
        "link": "bilibili://video/969856933",
        "ctime": 1601907864,
        "pubtime": 1601907864,
        "fav_time": 1648806783,
        "bv_id": "BV13p4y1Y75K",
        "bvid": "BV13p4y1Y75K",
        "season": null,
        "ogv": null,
        "ugc": {
          "first_cid": 242543306
        }
      },
      {
        "id": 201451751,
        "type": 2,
        "title": "已失效视频",
        "cover": "http://i0.hdslb.com/bfs/archive/be27fd62c99036dce67efface486fb0a88ffed06.jpg",
        "intro": "-",
        "page": 1,
        "duration": 40,
        "upper": {
          "mid": 188769473,
          "name": "上班摸鱼王小二",
          "face": "http://i2.hdslb.com/bfs/face/e2f98c2dc1984efbd47e263236121020d176b971.jpg"
        },
        "attr": 9,
        "cnt_info": {
          "collect": 125,
          "play": 66866,
          "danmaku": 28
        },
        "link": "bilibili://video/201451751",
        "ctime": 1595739336,
        "pubtime": 1595739336,
        "fav_time": 1648806775,
        "bv_id": "BV1Dh411o7AQ",
        "bvid": "BV1Dh411o7AQ",
        "season": null,
        "ogv": null,
        "ugc": {
          "first_cid": 216724322
        }
      },
      {
        "id": 411494,
        "type": 2,
        "title": "【星际争霸2 】一颗165杀的核弹",
        "cover": "http://i2.hdslb.com/bfs/archive/14f6b468c165275da12859c220634aa53ee1a690.jpg",
        "intro": "youtube 转自YouTube, 玩家是宗师棒子选手slayerdragon：可怜的ghost完成使命之后被无良玩家送掉",
        "page": 2,
        "duration": 77,
        "upper": {
          "mid": 64993,
          "name": "矢泽日香",
          "face": "http://i1.hdslb.com/bfs/face/4106b95eb62c5bec4731be3826324ab7d2d6e0e3.jpg"
        },
        "attr": 0,
        "cnt_info": {
          "collect": 110,
          "play": 109604,
          "danmaku": 83
        },
        "link": "bilibili://video/411494",
        "ctime": 1497368481,
        "pubtime": 1355020479,
        "fav_time": 1648801337,
        "bv_id": "BV16x411F7Xi",
        "bvid": "BV16x411F7Xi",
        "season": null,
        "ogv": null,
        "ugc": {
          "first_cid": 630336
        }
      }
    ],
    "has_more": false
  }
}
```

### 视频分p信息

https://api.bilibili.com/x/player/pagelist?bvid={视频bvid}&jsonp=jsonp

https://api.bilibili.com/x/player/pagelist?bvid=BV1v5411K7t2

```json
{
  "code": 0,
  "message": "0",
  "ttl": 1,
  "data": [
    {
      "cid": 355300860,
      "page": 1,
      "from": "vupload",
      "part": "9-1",
      "duration": 268,
      "vid": "",
      "weblink": "",
      "dimension": {
        "width": 1920,
        "height": 1080,
        "rotate": 0
      }
    },
    {
      "cid": 355303241,
      "page": 2,
      "from": "vupload",
      "part": "9-2",
      "duration": 1420,
      "vid": "",
      "weblink": "",
      "dimension": {
        "width": 1920,
        "height": 1080,
        "rotate": 0
      }
    },
    {
      "cid": 355305447,
      "page": 3,
      "from": "vupload",
      "part": "9-3 9 of 13",
      "duration": 1259,
      "vid": "",
      "weblink": "",
      "dimension": {
        "width": 1920,
        "height": 1080,
        "rotate": 0
      }
    }
  ]
}
```