# Bilibili API

### 获取收藏夹信息

https://api.bilibili.com/x/v3/fav/resource/list?pn=1&ps=20&keyword=&order=mtime&type=0&tid=0&platform=web&jsonp=jsonp&
media_id={收藏夹ID}

简化：https://api.bilibili.com/x/v3/fav/resource/list?ps=1& media_id={收藏夹ID}

### 获取收藏夹一页内容

https://api.bilibili.com/x/v3/fav/resource/list?keyword=&order=mtime&type=0&tid=0&platform=web&jsonp=jsonp&
ps={每页个数,最多20个}&media_id={收藏夹ID}&pn={从1开始页数}

https://api.bilibili.com/x/v3/fav/resource/list?ps=20& media_id={收藏夹ID}&pn={从1开始页数}

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
      }
    ],
    "has_more": false
  }
}
```

### 视频分p信息

https://api.bilibili.com/x/player/pagelist?jsonp=jsonp& bvid={视频bvid}

https://api.bilibili.com/x/player/pagelist? bvid={视频bvid}

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
    }
  ]
}
```

### 获取投稿的音频、视频URL

https://api.bilibili.com/x/player/playurl?qn=120&type=&otype=json&fourk=1&fnver=0&fnval=976&
bvid={投稿bvid}&cid={分P的cid}

https://api.bilibili.com/x/player/playurl?fnval=976& bvid={投稿bvid}&cid={分P的cid}

```json
{
  "code": 0,
  "message": "0",
  "ttl": 1,
  "data": {
    "from": "local",
    "result": "suee",
    "message": "",
    "quality": 32,
    "format": "flv480",
    "timelength": 152255,
    "accept_format": "hdflv2,flv_p60,flv,flv720,flv480,mp4",
    "accept_description": [
      "超清 4K",
      "高清 1080P60",
      "高清 1080P",
      "高清 720P",
      "清晰 480P",
      "流畅 360P"
    ],
    "accept_quality": [
      120,
      116,
      80,
      64,
      32,
      16
    ],
    "video_codecid": 7,
    "seek_param": "start",
    "seek_type": "offset",
    "dash": {
      "duration": 153,
      "minBufferTime": 1.5,
      "min_buffer_time": 1.5,
      "video": [
        {
          "id": 80,
          "baseUrl": "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30080.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=cosbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=038d3bad40f798103ccc3afd98522756\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=0,3\u0026agrr=1\u0026bw=141608\u0026logo=80000000",
          "base_url": "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30080.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=cosbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=038d3bad40f798103ccc3afd98522756\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=0,3\u0026agrr=1\u0026bw=141608\u0026logo=80000000",
          "backupUrl": [
            "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30080.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=cosbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=038d3bad40f798103ccc3afd98522756\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=1,3\u0026agrr=1\u0026bw=141608\u0026logo=40000000",
            "https://upos-sz-mirrorcosb.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30080.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=cosbbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=fa80ed96d519c6e42dad0f4807bbbb6c\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=2,3\u0026agrr=1\u0026bw=141608\u0026logo=40000000"
          ],
          "backup_url": [
            "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30080.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=cosbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=038d3bad40f798103ccc3afd98522756\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=1,3\u0026agrr=1\u0026bw=141608\u0026logo=40000000",
            "https://upos-sz-mirrorcosb.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30080.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=cosbbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=fa80ed96d519c6e42dad0f4807bbbb6c\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=2,3\u0026agrr=1\u0026bw=141608\u0026logo=40000000"
          ],
          "bandwidth": 1131634,
          "mimeType": "video/mp4",
          "mime_type": "video/mp4",
          "codecs": "avc1.640032",
          "width": 1920,
          "height": 1080,
          "frameRate": "29.412",
          "frame_rate": "29.412",
          "sar": "1:1",
          "startWithSap": 1,
          "start_with_sap": 1,
          "SegmentBase": {
            "Initialization": "0-979",
            "indexRange": "980-1371"
          },
          "segment_base": {
            "initialization": "0-979",
            "index_range": "980-1371"
          },
          "codecid": 7
        },
        {
          "id": 80,
          "baseUrl": "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30077.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=cosbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=28834e7a25725b0b7ec9b5a31b61c2c2\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=0,3\u0026agrr=1\u0026bw=72130\u0026logo=80000000",
          "base_url": "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30077.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=cosbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=28834e7a25725b0b7ec9b5a31b61c2c2\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=0,3\u0026agrr=1\u0026bw=72130\u0026logo=80000000",
          "backupUrl": [
            "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30077.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=cosbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=28834e7a25725b0b7ec9b5a31b61c2c2\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=1,3\u0026agrr=1\u0026bw=72130\u0026logo=40000000",
            "https://upos-sz-mirrorcosb.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30077.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=cosbbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=ffb81f5d9ffc0c5057186b786ae4561a\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=2,3\u0026agrr=1\u0026bw=72130\u0026logo=40000000"
          ],
          "backup_url": [
            "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30077.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=cosbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=28834e7a25725b0b7ec9b5a31b61c2c2\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=1,3\u0026agrr=1\u0026bw=72130\u0026logo=40000000",
            "https://upos-sz-mirrorcosb.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30077.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=cosbbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=ffb81f5d9ffc0c5057186b786ae4561a\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=2,3\u0026agrr=1\u0026bw=72130\u0026logo=40000000"
          ],
          "bandwidth": 576418,
          "mimeType": "video/mp4",
          "mime_type": "video/mp4",
          "codecs": "hev1.1.6.L150.90",
          "width": 1920,
          "height": 1080,
          "frameRate": "30.303",
          "frame_rate": "30.303",
          "sar": "1:1",
          "startWithSap": 1,
          "start_with_sap": 1,
          "SegmentBase": {
            "Initialization": "0-1043",
            "indexRange": "1044-1435"
          },
          "segment_base": {
            "initialization": "0-1043",
            "index_range": "1044-1435"
          },
          "codecid": 12
        },
        {
          "id": 64,
          "baseUrl": "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30064.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=cosbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=0edbaf23faac500b9049f4069635cb45\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=0,3\u0026agrr=1\u0026bw=58445\u0026logo=80000000",
          "base_url": "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30064.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=cosbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=0edbaf23faac500b9049f4069635cb45\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=0,3\u0026agrr=1\u0026bw=58445\u0026logo=80000000",
          "backupUrl": [
            "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30064.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=cosbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=0edbaf23faac500b9049f4069635cb45\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=1,3\u0026agrr=1\u0026bw=58445\u0026logo=40000000",
            "https://upos-sz-mirrorcosb.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30064.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=cosbbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=b0e7b48335d7fc943f2bf5917c6c0384\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=2,3\u0026agrr=1\u0026bw=58445\u0026logo=40000000"
          ],
          "backup_url": [
            "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30064.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=cosbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=0edbaf23faac500b9049f4069635cb45\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=1,3\u0026agrr=1\u0026bw=58445\u0026logo=40000000",
            "https://upos-sz-mirrorcosb.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30064.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=cosbbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=b0e7b48335d7fc943f2bf5917c6c0384\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=2,3\u0026agrr=1\u0026bw=58445\u0026logo=40000000"
          ],
          "bandwidth": 467056,
          "mimeType": "video/mp4",
          "mime_type": "video/mp4",
          "codecs": "avc1.640028",
          "width": 1280,
          "height": 720,
          "frameRate": "29.412",
          "frame_rate": "29.412",
          "sar": "1:1",
          "startWithSap": 1,
          "start_with_sap": 1,
          "SegmentBase": {
            "Initialization": "0-977",
            "indexRange": "978-1369"
          },
          "segment_base": {
            "initialization": "0-977",
            "index_range": "978-1369"
          },
          "codecid": 7
        },
        {
          "id": 64,
          "baseUrl": "https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30066.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=hwbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=51413824ad5bed2d6a445a494377d3e5\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=0,3\u0026agrr=1\u0026bw=30140\u0026logo=80000000",
          "base_url": "https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30066.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=hwbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=51413824ad5bed2d6a445a494377d3e5\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=0,3\u0026agrr=1\u0026bw=30140\u0026logo=80000000",
          "backupUrl": [
            "https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30066.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=hwbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=51413824ad5bed2d6a445a494377d3e5\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=1,3\u0026agrr=1\u0026bw=30140\u0026logo=40000000",
            "https://upos-sz-mirrorhwb.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30066.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=hwbbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=4853f82dbbfa8a2bc4179de77739cefe\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=2,3\u0026agrr=1\u0026bw=30140\u0026logo=40000000"
          ],
          "backup_url": [
            "https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30066.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=hwbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=51413824ad5bed2d6a445a494377d3e5\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=1,3\u0026agrr=1\u0026bw=30140\u0026logo=40000000",
            "https://upos-sz-mirrorhwb.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30066.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=hwbbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=4853f82dbbfa8a2bc4179de77739cefe\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=2,3\u0026agrr=1\u0026bw=30140\u0026logo=40000000"
          ],
          "bandwidth": 240863,
          "mimeType": "video/mp4",
          "mime_type": "video/mp4",
          "codecs": "hev1.1.6.L120.90",
          "width": 1280,
          "height": 720,
          "frameRate": "30.303",
          "frame_rate": "30.303",
          "sar": "1:1",
          "startWithSap": 1,
          "start_with_sap": 1,
          "SegmentBase": {
            "Initialization": "0-1043",
            "indexRange": "1044-1435"
          },
          "segment_base": {
            "initialization": "0-1043",
            "index_range": "1044-1435"
          },
          "codecid": 12
        },
        {
          "id": 32,
          "baseUrl": "https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30032.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=hwbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=11acde4b86dc3b61c6dc25e2d57f249f\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=0,3\u0026agrr=1\u0026bw=30455\u0026logo=80000000",
          "base_url": "https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30032.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=hwbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=11acde4b86dc3b61c6dc25e2d57f249f\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=0,3\u0026agrr=1\u0026bw=30455\u0026logo=80000000",
          "backupUrl": [
            "https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30032.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=hwbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=11acde4b86dc3b61c6dc25e2d57f249f\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=1,3\u0026agrr=1\u0026bw=30455\u0026logo=40000000",
            "https://upos-sz-mirrorhwb.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30032.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=hwbbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=153c44fa3b1f4c2cf3822f95a27fd98f\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=2,3\u0026agrr=1\u0026bw=30455\u0026logo=40000000"
          ],
          "backup_url": [
            "https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30032.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=hwbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=11acde4b86dc3b61c6dc25e2d57f249f\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=1,3\u0026agrr=1\u0026bw=30455\u0026logo=40000000",
            "https://upos-sz-mirrorhwb.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30032.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=hwbbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=153c44fa3b1f4c2cf3822f95a27fd98f\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=2,3\u0026agrr=1\u0026bw=30455\u0026logo=40000000"
          ],
          "bandwidth": 243378,
          "mimeType": "video/mp4",
          "mime_type": "video/mp4",
          "codecs": "avc1.64001F",
          "width": 852,
          "height": 480,
          "frameRate": "29.412",
          "frame_rate": "29.412",
          "sar": "1:1",
          "startWithSap": 1,
          "start_with_sap": 1,
          "SegmentBase": {
            "Initialization": "0-978",
            "indexRange": "979-1370"
          },
          "segment_base": {
            "initialization": "0-978",
            "index_range": "979-1370"
          },
          "codecid": 7
        },
        {
          "id": 32,
          "baseUrl": "https://upos-sz-mirrorali.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30033.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=alibv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=452033aa98ea471c4d5d530cd2476da3\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=0,1\u0026agrr=1\u0026bw=26394\u0026logo=80000000",
          "base_url": "https://upos-sz-mirrorali.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30033.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=alibv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=452033aa98ea471c4d5d530cd2476da3\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=0,1\u0026agrr=1\u0026bw=26394\u0026logo=80000000",
          "backupUrl": null,
          "backup_url": null,
          "bandwidth": 210927,
          "mimeType": "video/mp4",
          "mime_type": "video/mp4",
          "codecs": "hev1.1.6.L120.90",
          "width": 852,
          "height": 480,
          "frameRate": "30.303",
          "frame_rate": "30.303",
          "sar": "1:1",
          "startWithSap": 1,
          "start_with_sap": 1,
          "SegmentBase": {
            "Initialization": "0-1043",
            "indexRange": "1044-1435"
          },
          "segment_base": {
            "initialization": "0-1043",
            "index_range": "1044-1435"
          },
          "codecid": 12
        },
        {
          "id": 16,
          "baseUrl": "https://upos-sz-mirrorali.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30011.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=alibv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=cf1afd1014e467bdbfab7789730a339e\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=0,1\u0026agrr=1\u0026bw=26425\u0026logo=80000000",
          "base_url": "https://upos-sz-mirrorali.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30011.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=alibv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=cf1afd1014e467bdbfab7789730a339e\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=0,1\u0026agrr=1\u0026bw=26425\u0026logo=80000000",
          "backupUrl": null,
          "backup_url": null,
          "bandwidth": 211175,
          "mimeType": "video/mp4",
          "mime_type": "video/mp4",
          "codecs": "hev1.1.6.L120.90",
          "width": 640,
          "height": 360,
          "frameRate": "30.303",
          "frame_rate": "30.303",
          "sar": "1:1",
          "startWithSap": 1,
          "start_with_sap": 1,
          "SegmentBase": {
            "Initialization": "0-1041",
            "indexRange": "1042-1433"
          },
          "segment_base": {
            "initialization": "0-1041",
            "index_range": "1042-1433"
          },
          "codecid": 12
        },
        {
          "id": 16,
          "baseUrl": "https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30016.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=hwbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=3a89bae1c6c5a255f0f697e5915fdc1c\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=0,3\u0026agrr=1\u0026bw=41288\u0026logo=80000000",
          "base_url": "https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30016.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=hwbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=3a89bae1c6c5a255f0f697e5915fdc1c\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=0,3\u0026agrr=1\u0026bw=41288\u0026logo=80000000",
          "backupUrl": [
            "https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30016.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=hwbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=3a89bae1c6c5a255f0f697e5915fdc1c\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=1,3\u0026agrr=1\u0026bw=41288\u0026logo=40000000",
            "https://upos-sz-mirrorhwb.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30016.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=hwbbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=0cd768691745c87a64d02e6929c6e2b8\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=2,3\u0026agrr=1\u0026bw=41288\u0026logo=40000000"
          ],
          "backup_url": [
            "https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30016.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=hwbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=3a89bae1c6c5a255f0f697e5915fdc1c\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=1,3\u0026agrr=1\u0026bw=41288\u0026logo=40000000",
            "https://upos-sz-mirrorhwb.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30016.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=hwbbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=0cd768691745c87a64d02e6929c6e2b8\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=2,3\u0026agrr=1\u0026bw=41288\u0026logo=40000000"
          ],
          "bandwidth": 329948,
          "mimeType": "video/mp4",
          "mime_type": "video/mp4",
          "codecs": "avc1.64001E",
          "width": 640,
          "height": 360,
          "frameRate": "29.412",
          "frame_rate": "29.412",
          "sar": "1:1",
          "startWithSap": 1,
          "start_with_sap": 1,
          "SegmentBase": {
            "Initialization": "0-985",
            "indexRange": "986-1377"
          },
          "segment_base": {
            "initialization": "0-985",
            "index_range": "986-1377"
          },
          "codecid": 7
        }
      ],
      "audio": [
        {
          "id": 30280,
          "baseUrl": "https://upos-sz-mirrorali.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=alibv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=b12b21c1f4a067b8ec666f04ef55baf3\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=0,1\u0026agrr=1\u0026bw=39957\u0026logo=80000000",
          "base_url": "https://upos-sz-mirrorali.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=alibv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=b12b21c1f4a067b8ec666f04ef55baf3\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=0,1\u0026agrr=1\u0026bw=39957\u0026logo=80000000",
          "backupUrl": null,
          "backup_url": null,
          "bandwidth": 319124,
          "mimeType": "audio/mp4",
          "mime_type": "audio/mp4",
          "codecs": "mp4a.40.2",
          "width": 0,
          "height": 0,
          "frameRate": "",
          "frame_rate": "",
          "sar": "",
          "startWithSap": 0,
          "start_with_sap": 0,
          "SegmentBase": {
            "Initialization": "0-907",
            "indexRange": "908-1311"
          },
          "segment_base": {
            "initialization": "0-907",
            "index_range": "908-1311"
          },
          "codecid": 0
        },
        {
          "id": 30216,
          "baseUrl": "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30216.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=cosbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=000cd3e417187ab488d9122e88c74a5f\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=0,3\u0026agrr=1\u0026bw=8429\u0026logo=80000000",
          "base_url": "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30216.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=cosbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=000cd3e417187ab488d9122e88c74a5f\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=0,3\u0026agrr=1\u0026bw=8429\u0026logo=80000000",
          "backupUrl": [
            "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30216.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=cosbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=000cd3e417187ab488d9122e88c74a5f\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=1,3\u0026agrr=1\u0026bw=8429\u0026logo=40000000",
            "https://upos-sz-mirrorcosb.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30216.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=cosbbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=76b4dd2c3c5b37d3e7648210a18e9149\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=2,3\u0026agrr=1\u0026bw=8429\u0026logo=40000000"
          ],
          "backup_url": [
            "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30216.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=cosbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=000cd3e417187ab488d9122e88c74a5f\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=1,3\u0026agrr=1\u0026bw=8429\u0026logo=40000000",
            "https://upos-sz-mirrorcosb.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30216.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=cosbbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=76b4dd2c3c5b37d3e7648210a18e9149\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=2,3\u0026agrr=1\u0026bw=8429\u0026logo=40000000"
          ],
          "bandwidth": 67324,
          "mimeType": "audio/mp4",
          "mime_type": "audio/mp4",
          "codecs": "mp4a.40.2",
          "width": 0,
          "height": 0,
          "frameRate": "",
          "frame_rate": "",
          "sar": "",
          "startWithSap": 0,
          "start_with_sap": 0,
          "SegmentBase": {
            "Initialization": "0-940",
            "indexRange": "941-1344"
          },
          "segment_base": {
            "initialization": "0-940",
            "index_range": "941-1344"
          },
          "codecid": 0
        },
        {
          "id": 30232,
          "baseUrl": "https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30232.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=hwbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=65ad9e4335d2836d591cb516f85c4a01\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=0,3\u0026agrr=1\u0026bw=16629\u0026logo=80000000",
          "base_url": "https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30232.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=hwbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=65ad9e4335d2836d591cb516f85c4a01\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=0,3\u0026agrr=1\u0026bw=16629\u0026logo=80000000",
          "backupUrl": [
            "https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30232.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=hwbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=65ad9e4335d2836d591cb516f85c4a01\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=1,3\u0026agrr=1\u0026bw=16629\u0026logo=40000000",
            "https://upos-sz-mirrorhwb.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30232.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=hwbbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=94993c68df139cb43ae6c66f4ae35716\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=2,3\u0026agrr=1\u0026bw=16629\u0026logo=40000000"
          ],
          "backup_url": [
            "https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30232.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=hwbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=65ad9e4335d2836d591cb516f85c4a01\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=1,3\u0026agrr=1\u0026bw=16629\u0026logo=40000000",
            "https://upos-sz-mirrorhwb.bilivideo.com/upgcxcode/18/59/556835918/556835918-1-30232.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1660383237\u0026gen=playurlv2\u0026os=hwbbv\u0026oi=3528247817\u0026trid=bbd6b792db664f3991d20e4dea0a5bb3u\u0026mid=0\u0026platform=pc\u0026upsig=94993c68df139cb43ae6c66f4ae35716\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform\u0026bvc=vod\u0026nettype=0\u0026orderid=2,3\u0026agrr=1\u0026bw=16629\u0026logo=40000000"
          ],
          "bandwidth": 132813,
          "mimeType": "audio/mp4",
          "mime_type": "audio/mp4",
          "codecs": "mp4a.40.2",
          "width": 0,
          "height": 0,
          "frameRate": "",
          "frame_rate": "",
          "sar": "",
          "startWithSap": 0,
          "start_with_sap": 0,
          "SegmentBase": {
            "Initialization": "0-907",
            "indexRange": "908-1311"
          },
          "segment_base": {
            "initialization": "0-907",
            "index_range": "908-1311"
          },
          "codecid": 0
        }
      ],
      "dolby": null,
      "flac": null
    },
    "support_formats": [
      {
        "quality": 120,
        "format": "hdflv2",
        "new_description": "4K 超清",
        "display_desc": "4K",
        "superscript": "",
        "codecs": [
          "avc1.640034",
          "hev1.1.6.L153.90"
        ]
      },
      {
        "quality": 116,
        "format": "flv_p60",
        "new_description": "1080P 60帧",
        "display_desc": "1080P",
        "superscript": "60帧",
        "codecs": [
          "avc1.640032",
          "hev1.1.6.L150.90"
        ]
      },
      {
        "quality": 80,
        "format": "flv",
        "new_description": "1080P 高清",
        "display_desc": "1080P",
        "superscript": "",
        "codecs": [
          "avc1.640032",
          "hev1.1.6.L150.90"
        ]
      },
      {
        "quality": 64,
        "format": "flv720",
        "new_description": "720P 高清",
        "display_desc": "720P",
        "superscript": "",
        "codecs": [
          "avc1.640028",
          "hev1.1.6.L120.90"
        ]
      },
      {
        "quality": 32,
        "format": "flv480",
        "new_description": "480P 清晰",
        "display_desc": "480P",
        "superscript": "",
        "codecs": [
          "avc1.64001F",
          "hev1.1.6.L120.90"
        ]
      },
      {
        "quality": 16,
        "format": "mp4",
        "new_description": "360P 流畅",
        "display_desc": "360P",
        "superscript": "",
        "codecs": [
          "avc1.64001E",
          "hev1.1.6.L120.90"
        ]
      }
    ],
    "high_format": null
  }
}
```
