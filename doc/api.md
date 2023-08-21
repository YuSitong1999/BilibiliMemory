# Bilibili API

接口格式及示例， **返回值仅列出实际使用的** 。

### 获取收藏夹信息

https://api.bilibili.com/x/v3/fav/resource/list?pn=1&ps=20&keyword=&order=mtime&type=0&tid=0&platform=web&jsonp=jsonp&
media_id={收藏夹ID}

简化（每页条数设为1）：https://api.bilibili.com/x/v3/fav/resource/list?ps=1& media_id={收藏夹ID}

示例：https://api.bilibili.com/x/v3/fav/resource/list?ps=1&media_id=1561982153

```json5
{
  "code": 0,
  "message": "0",
  "data": {
    "info": {
      "title": "测试",
      "media_count": 6,
    },
  },
}
```

### 获取收藏夹一页内容

https://api.bilibili.com/x/v3/fav/resource/list?keyword=&order=mtime&type=0&tid=0&platform=web&jsonp=jsonp&
ps={每页个数,最多20个}&media_id={收藏夹ID}&pn={从1开始页数}

简化：https://api.bilibili.com/x/v3/fav/resource/list?ps=20& media_id={收藏夹ID}&pn={从1开始页数}

示例：https://api.bilibili.com/x/v3/fav/resource/list?ps=20&media_id=1561982153&pn=1

```json5
{
  "code": 0,
  "message": "0",
  "data": {
    "info": {
      "title": "测试",
      "media_count": 4
    },
    "medias": [
      {
        "id": 380440390,
        "title": "我对《妇女权益保障法(修订草案）》的意见",
        "cover": "http://i1.hdslb.com/bfs/archive/205ac1275b3f41b6dd2da56b3f6d94ce3a1dcebb.jpg",
        "intro": "提意见有用，而且很有必要！如果法律不明确，游戏女性角色好看没准也算性骚扰。\r\n更新和精简版见视频P1\r\n妇女权益保障法(修订草案）征求意见（2022年1月22日截止）\r\nhttp://www.npc.gov.cn/flcaw/userIndex.html?lid=ff8081817ddb134a017deac847ed20e0\r\n我发现有许多有令人担忧之处，特别是第2、17、28、50、53、56、66、70、76条，见视频P1\r\n\r\n所有建议见P2，关于：\r\n第一章 总则：第2条 特别措施应合理，第9（",
        "page": 2,
        "duration": 1985,
        "upper": {
          "mid": 95451953,
          "name": "小木曾春希",
        },
        "ctime": 1641193911,
        "pubtime": 1641193911,
        "fav_time": 1648883396,
        "bv_id": "BV13Z4y1S7Zc",
        "ugc": {
          "first_cid": 478500783
        }
      },
    ],
    "has_more": false
  }
}
```

### 获取用户个人信息

参考：https://github.com/SocialSisterYi/bilibili-API-collect/issues/631#issuecomment-1558747661

https://api.bilibili.com/x/space/acc/info?mid=1210635994&token=&platform=web&web_location=1550101&w_rid=1bed297950ed9cc00f1a8b6a4812f7c0&wts=1689997416

简化：https://api.bilibili.com/x/space/acc/info? mid={用户ID}&w_rid={?}&wts={?}

w_rid={?}&wts={?}需要通过复杂方式生成

```json5
{
  "code": 0,
  "message": "0",
  "data": {
    "mid": 1210635994,
    "name": "吴尽意",
    "sign": "「谁字仁者为无尽意？」",
  }
}
```

### 获取UP主一页投稿内容

https://api.bilibili.com/x/space/wbi/arc/search?mid=95451953&ps=30&tid=0&pn=1&keyword=&order=pubdate&platform=web&web_location=1550101&order_avoided=true&w_rid=8df75ab74f83eb0636b3f833446492a9&wts=1690023737

简化：https://api.bilibili.com/x/space/wbi/arc/search? ps={每页个数，最多50}&mid={UP主ID}&pn={页码，从1开始}&w_rid={?}&wts={?}

```json5
{
  "code": 0,
  "message": "0",
  "data": {
    "list": {
      "vlist": [
        {
          "title": "阿富汗巨量锂矿馋哭五角大楼：本来都是我的！",
          "created": 1689934850,
          "length": "15:41",
          "aid": 231160012,
          "bvid": "BV1i8411S7Zy",
        },
      ],
    },
    "page": {
      "pn": 1,
      "ps": 50,
      "count": 981
    },
  }
}
```

### 单一投稿信息

https://api.bilibili.com/x/web-interface/view/detail? bvid= {视频bvid}

示例：https://api.bilibili.com/x/web-interface/view/detail?bvid=BV1i8411S7Zy

```json5
{
  "code": 0,
  "message": "0",
  "data": {
    "View": {
      "bvid": "BV1i8411S7Zy",
      "aid": 231160012,
      "videos": 1,
      "pic": "http://i0.hdslb.com/bfs/archive/6e3329e234a29862cefe20317b96c9be5a4df026.jpg",
      "title": "阿富汗巨量锂矿馋哭五角大楼：本来都是我的！",
      "pubdate": 1689934850,
      "ctime": 1689934850,
      "desc": "",
      "duration": 941,
      "owner": {
        "mid": 346563107,
        "name": "波士顿圆脸",
        "face": "https://i2.hdslb.com/bfs/face/f8f0fc4114bb06a87481abe12faa006a383cbe6d.jpg"
      },
      "pages": [
        {
          "cid": 1204741650,
          "part": "阿富汗巨量锂矿馋哭五角大楼：本来都是我的！",
          "duration": 941,
        }
      ],
    },
  }
}
```

### 视频分p信息

https://api.bilibili.com/x/player/pagelist?jsonp=jsonp& bvid={视频bvid}

简化：https://api.bilibili.com/x/player/pagelist? bvid={视频bvid}

示例：https://api.bilibili.com/x/player/pagelist?BV1i8411S7Zy

```json5
{
  "code": 0,
  "message": "0",
  "data": [
    {
      "cid": 1204741650,
      "part": "阿富汗巨量锂矿馋哭五角大楼：本来都是我的！",
      "duration": 941,
      "first_frame": "http://i1.hdslb.com/bfs/storyff/n230721a22o9hhwoh9ryu03amnjt4jfi_firsti.jpg"
    }
  ]
}
```

### 获取投稿的音频、视频URL

https://api.bilibili.com/x/player/playurl?qn=120&type=&otype=json&fourk=1&fnver=0&fnval=976& bvid={投稿bvid}&cid={分P的cid}

简化：https://api.bilibili.com/x/player/playurl?fnval=976& bvid={投稿bvid}&cid={分P的cid}

示例：https://api.bilibili.com/x/player/playurl?fnval=976&bvid=BV1i8411S7Zy&cid=1204741650

```json5
{
  "code": 0,
  "message": "0",
  "data": {
    "dash": {
      "video": [
        {
          "id": 32,
          "baseUrl": "https://xy106x116x200x169xy.mcdn.bilivideo.cn:8082/v1/resource/1204741650-1-100110.m4s?agrr=0&build=0&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&bvc=vod&bw=21641&deadline=1690007061&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&gen=playurlv2&logo=A0000001&mcdnid=1003163&mid=0&nbs=1&nettype=0&oi=1875329039&orderid=0%2C3&os=mcdn&platform=pc&sign=4d63af&traceid=trixjpNfUbwGhd_0_e_N&uipk=5&uparams=e%2Cuipk%2Cnbs%2Cdeadline%2Cgen%2Cos%2Coi%2Ctrid%2Cmid%2Cplatform&upsig=0bd3e85d599b2251127ee9bc0c6e36bb",
          "base_url": "https://xy106x116x200x169xy.mcdn.bilivideo.cn:8082/v1/resource/1204741650-1-100110.m4s?agrr=0&build=0&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&bvc=vod&bw=21641&deadline=1690007061&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&gen=playurlv2&logo=A0000001&mcdnid=1003163&mid=0&nbs=1&nettype=0&oi=1875329039&orderid=0%2C3&os=mcdn&platform=pc&sign=4d63af&traceid=trixjpNfUbwGhd_0_e_N&uipk=5&uparams=e%2Cuipk%2Cnbs%2Cdeadline%2Cgen%2Cos%2Coi%2Ctrid%2Cmid%2Cplatform&upsig=0bd3e85d599b2251127ee9bc0c6e36bb",
          "backupUrl": [
            "https://xy183x94x183x14xy.mcdn.bilivideo.cn:4483/upgcxcode/50/16/1204741650/1204741650-1-100110.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=mcdn&oi=1875329039&trid=00008c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=0bd3e85d599b2251127ee9bc0c6e36bb&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=1003163&bvc=vod&nettype=0&orderid=0,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=21641&logo=A0000001",
            "https://upos-sz-mirrorali.bilivideo.com/upgcxcode/50/16/1204741650/1204741650-1-100110.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=alibv&oi=1875329039&trid=8c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=9a1ce80f0319028ee66f8fce145e457e&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=21641&logo=40000000"
          ],
          "backup_url": [
            "https://xy183x94x183x14xy.mcdn.bilivideo.cn:4483/upgcxcode/50/16/1204741650/1204741650-1-100110.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=mcdn&oi=1875329039&trid=00008c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=0bd3e85d599b2251127ee9bc0c6e36bb&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=1003163&bvc=vod&nettype=0&orderid=0,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=21641&logo=A0000001",
            "https://upos-sz-mirrorali.bilivideo.com/upgcxcode/50/16/1204741650/1204741650-1-100110.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=alibv&oi=1875329039&trid=8c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=9a1ce80f0319028ee66f8fce145e457e&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=21641&logo=40000000"
          ],
        },
        {
          "id": 32,
          "baseUrl": "https://xy120x87x106x39xy.mcdn.bilivideo.cn:8082/v1/resource/1204741650-1-100047.m4s?agrr=0&build=0&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&bvc=vod&bw=47535&deadline=1690007061&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&gen=playurlv2&logo=A0000001&mcdnid=1003163&mid=0&nbs=1&nettype=0&oi=1875329039&orderid=0%2C3&os=mcdn&platform=pc&sign=609c7f&traceid=trLeipoZkfasuo_0_e_N&uipk=5&uparams=e%2Cuipk%2Cnbs%2Cdeadline%2Cgen%2Cos%2Coi%2Ctrid%2Cmid%2Cplatform&upsig=722bd341199639bde3a073fac1805715",
          "base_url": "https://xy120x87x106x39xy.mcdn.bilivideo.cn:8082/v1/resource/1204741650-1-100047.m4s?agrr=0&build=0&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&bvc=vod&bw=47535&deadline=1690007061&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&gen=playurlv2&logo=A0000001&mcdnid=1003163&mid=0&nbs=1&nettype=0&oi=1875329039&orderid=0%2C3&os=mcdn&platform=pc&sign=609c7f&traceid=trLeipoZkfasuo_0_e_N&uipk=5&uparams=e%2Cuipk%2Cnbs%2Cdeadline%2Cgen%2Cos%2Coi%2Ctrid%2Cmid%2Cplatform&upsig=722bd341199639bde3a073fac1805715",
          "backupUrl": [
            "https://xy183x94x183x14xy.mcdn.bilivideo.cn:4483/upgcxcode/50/16/1204741650/1204741650-1-100047.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=mcdn&oi=1875329039&trid=00008c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=722bd341199639bde3a073fac1805715&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=1003163&bvc=vod&nettype=0&orderid=0,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=47535&logo=A0000001",
            "https://upos-sz-mirrorali.bilivideo.com/upgcxcode/50/16/1204741650/1204741650-1-100047.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=alibv&oi=1875329039&trid=8c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=b175e1e6b928675a90b12b23deb9f450&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=47535&logo=40000000"
          ],
          "backup_url": [
            "https://xy183x94x183x14xy.mcdn.bilivideo.cn:4483/upgcxcode/50/16/1204741650/1204741650-1-100047.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=mcdn&oi=1875329039&trid=00008c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=722bd341199639bde3a073fac1805715&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=1003163&bvc=vod&nettype=0&orderid=0,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=47535&logo=A0000001",
            "https://upos-sz-mirrorali.bilivideo.com/upgcxcode/50/16/1204741650/1204741650-1-100047.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=alibv&oi=1875329039&trid=8c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=b175e1e6b928675a90b12b23deb9f450&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=47535&logo=40000000"
          ],
        },
        {
          "id": 16,
          "baseUrl": "https://xy27x42x224x15xy.mcdn.bilivideo.cn:8082/v1/resource/1204741650-1-100109.m4s?agrr=0&build=0&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&bvc=vod&bw=15223&deadline=1690007061&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&gen=playurlv2&logo=A0000001&mcdnid=1003163&mid=0&nbs=1&nettype=0&oi=1875329039&orderid=0%2C3&os=mcdn&platform=pc&sign=c08b0d&traceid=trRlSRnabYoizW_0_e_N&uipk=5&uparams=e%2Cuipk%2Cnbs%2Cdeadline%2Cgen%2Cos%2Coi%2Ctrid%2Cmid%2Cplatform&upsig=e8033591cca5dad757b0b0e24ef34c76",
          "base_url": "https://xy27x42x224x15xy.mcdn.bilivideo.cn:8082/v1/resource/1204741650-1-100109.m4s?agrr=0&build=0&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&bvc=vod&bw=15223&deadline=1690007061&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&gen=playurlv2&logo=A0000001&mcdnid=1003163&mid=0&nbs=1&nettype=0&oi=1875329039&orderid=0%2C3&os=mcdn&platform=pc&sign=c08b0d&traceid=trRlSRnabYoizW_0_e_N&uipk=5&uparams=e%2Cuipk%2Cnbs%2Cdeadline%2Cgen%2Cos%2Coi%2Ctrid%2Cmid%2Cplatform&upsig=e8033591cca5dad757b0b0e24ef34c76",
          "backupUrl": [
            "https://xy183x94x183x14xy.mcdn.bilivideo.cn:4483/upgcxcode/50/16/1204741650/1204741650-1-100109.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=mcdn&oi=1875329039&trid=00008c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=e8033591cca5dad757b0b0e24ef34c76&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=1003163&bvc=vod&nettype=0&orderid=0,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=15223&logo=A0000001",
            "https://upos-sz-mirrorali.bilivideo.com/upgcxcode/50/16/1204741650/1204741650-1-100109.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=alibv&oi=1875329039&trid=8c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=05bfb920f596935037b7f1af109b2e00&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=15223&logo=40000000"
          ],
          "backup_url": [
            "https://xy183x94x183x14xy.mcdn.bilivideo.cn:4483/upgcxcode/50/16/1204741650/1204741650-1-100109.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=mcdn&oi=1875329039&trid=00008c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=e8033591cca5dad757b0b0e24ef34c76&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=1003163&bvc=vod&nettype=0&orderid=0,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=15223&logo=A0000001",
            "https://upos-sz-mirrorali.bilivideo.com/upgcxcode/50/16/1204741650/1204741650-1-100109.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=alibv&oi=1875329039&trid=8c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=05bfb920f596935037b7f1af109b2e00&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=15223&logo=40000000"
          ],
        },
        {
          "id": 16,
          "baseUrl": "https://xy183x94x183x14xy.mcdn.bilivideo.cn:4483/upgcxcode/50/16/1204741650/1204741650-1-100046.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=mcdn&oi=1875329039&trid=00008c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=65f584d230b910933c963da20a666ad8&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=1003163&bvc=vod&nettype=0&orderid=0,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=27757&logo=A0000001",
          "base_url": "https://xy183x94x183x14xy.mcdn.bilivideo.cn:4483/upgcxcode/50/16/1204741650/1204741650-1-100046.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=mcdn&oi=1875329039&trid=00008c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=65f584d230b910933c963da20a666ad8&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=1003163&bvc=vod&nettype=0&orderid=0,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=27757&logo=A0000001",
          "backupUrl": [
            "https://upos-sz-mirrorcoso1.bilivideo.com/upgcxcode/50/16/1204741650/1204741650-1-100046.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=coso1bv&oi=1875329039&trid=8c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=bd23787abd2d847968ca3abe00a7f463&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=27757&logo=40000000",
            "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/50/16/1204741650/1204741650-1-100046.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=cosbv&oi=1875329039&trid=8c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=e3aa7f96b379fa6a9dc37169968bd260&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=2,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=27757&logo=40000000"
          ],
          "backup_url": [
            "https://upos-sz-mirrorcoso1.bilivideo.com/upgcxcode/50/16/1204741650/1204741650-1-100046.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=coso1bv&oi=1875329039&trid=8c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=bd23787abd2d847968ca3abe00a7f463&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=27757&logo=40000000",
            "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/50/16/1204741650/1204741650-1-100046.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=cosbv&oi=1875329039&trid=8c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=e3aa7f96b379fa6a9dc37169968bd260&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=2,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=27757&logo=40000000"
          ],
        }
      ],
      "audio": [
        {
          "id": 30280,
          "baseUrl": "https://xy111x113x195x86xy.mcdn.bilivideo.cn:8082/v1/resource/1204741650-1-30280.m4s?agrr=0&build=0&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&bvc=vod&bw=27277&deadline=1690007061&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&gen=playurlv2&logo=A0000001&mcdnid=1003163&mid=0&nbs=1&nettype=0&oi=1875329039&orderid=0%2C3&os=mcdn&platform=pc&sign=a7893c&traceid=trBWelFCeWCRpy_0_e_N&uipk=5&uparams=e%2Cuipk%2Cnbs%2Cdeadline%2Cgen%2Cos%2Coi%2Ctrid%2Cmid%2Cplatform&upsig=51247c602aae920883c288aa30003c2e",
          "base_url": "https://xy111x113x195x86xy.mcdn.bilivideo.cn:8082/v1/resource/1204741650-1-30280.m4s?agrr=0&build=0&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&bvc=vod&bw=27277&deadline=1690007061&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&gen=playurlv2&logo=A0000001&mcdnid=1003163&mid=0&nbs=1&nettype=0&oi=1875329039&orderid=0%2C3&os=mcdn&platform=pc&sign=a7893c&traceid=trBWelFCeWCRpy_0_e_N&uipk=5&uparams=e%2Cuipk%2Cnbs%2Cdeadline%2Cgen%2Cos%2Coi%2Ctrid%2Cmid%2Cplatform&upsig=51247c602aae920883c288aa30003c2e",
          "backupUrl": [
            "https://xy183x94x183x14xy.mcdn.bilivideo.cn:4483/upgcxcode/50/16/1204741650/1204741650-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=mcdn&oi=1875329039&trid=00008c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=51247c602aae920883c288aa30003c2e&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=1003163&bvc=vod&nettype=0&orderid=0,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=27277&logo=A0000001",
            "https://upos-sz-mirrorali.bilivideo.com/upgcxcode/50/16/1204741650/1204741650-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=alibv&oi=1875329039&trid=8c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=c10f72062362d08314e75d87b82222c7&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=27277&logo=40000000"
          ],
          "backup_url": [
            "https://xy183x94x183x14xy.mcdn.bilivideo.cn:4483/upgcxcode/50/16/1204741650/1204741650-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=mcdn&oi=1875329039&trid=00008c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=51247c602aae920883c288aa30003c2e&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=1003163&bvc=vod&nettype=0&orderid=0,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=27277&logo=A0000001",
            "https://upos-sz-mirrorali.bilivideo.com/upgcxcode/50/16/1204741650/1204741650-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=alibv&oi=1875329039&trid=8c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=c10f72062362d08314e75d87b82222c7&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=27277&logo=40000000"
          ],
        },
        {
          "id": 30216,
          "baseUrl": "https://xy218x104x233x71xy.mcdn.bilivideo.cn:8082/v1/resource/1204741650-1-30216.m4s?agrr=0&build=0&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&bvc=vod&bw=8339&deadline=1690007061&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&gen=playurlv2&logo=A0000001&mcdnid=1003163&mid=0&nbs=1&nettype=0&oi=1875329039&orderid=0%2C3&os=mcdn&platform=pc&sign=2a71ba&traceid=trMzeHtZewtsPl_0_e_N&uipk=5&uparams=e%2Cuipk%2Cnbs%2Cdeadline%2Cgen%2Cos%2Coi%2Ctrid%2Cmid%2Cplatform&upsig=ea51b895bc24bba1ab1194cfd08d3e1c",
          "base_url": "https://xy218x104x233x71xy.mcdn.bilivideo.cn:8082/v1/resource/1204741650-1-30216.m4s?agrr=0&build=0&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&bvc=vod&bw=8339&deadline=1690007061&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&gen=playurlv2&logo=A0000001&mcdnid=1003163&mid=0&nbs=1&nettype=0&oi=1875329039&orderid=0%2C3&os=mcdn&platform=pc&sign=2a71ba&traceid=trMzeHtZewtsPl_0_e_N&uipk=5&uparams=e%2Cuipk%2Cnbs%2Cdeadline%2Cgen%2Cos%2Coi%2Ctrid%2Cmid%2Cplatform&upsig=ea51b895bc24bba1ab1194cfd08d3e1c",
          "backupUrl": [
            "https://xy183x94x183x14xy.mcdn.bilivideo.cn:4483/upgcxcode/50/16/1204741650/1204741650-1-30216.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=mcdn&oi=1875329039&trid=00008c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=ea51b895bc24bba1ab1194cfd08d3e1c&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=1003163&bvc=vod&nettype=0&orderid=0,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=8339&logo=A0000001",
            "https://upos-sz-mirrorcoso1.bilivideo.com/upgcxcode/50/16/1204741650/1204741650-1-30216.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=coso1bv&oi=1875329039&trid=8c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=717bac56003acf8f7048aedcd99719b7&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=8339&logo=40000000"
          ],
          "backup_url": [
            "https://xy183x94x183x14xy.mcdn.bilivideo.cn:4483/upgcxcode/50/16/1204741650/1204741650-1-30216.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=mcdn&oi=1875329039&trid=00008c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=ea51b895bc24bba1ab1194cfd08d3e1c&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=1003163&bvc=vod&nettype=0&orderid=0,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=8339&logo=A0000001",
            "https://upos-sz-mirrorcoso1.bilivideo.com/upgcxcode/50/16/1204741650/1204741650-1-30216.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=coso1bv&oi=1875329039&trid=8c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=717bac56003acf8f7048aedcd99719b7&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=8339&logo=40000000"
          ],
        },
        {
          "id": 30232,
          "baseUrl": "https://xy42x237x162x226xy.mcdn.bilivideo.cn:8082/v1/resource/1204741650-1-30232.m4s?agrr=0&build=0&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&bvc=vod&bw=17894&deadline=1690007061&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&gen=playurlv2&logo=A0000001&mcdnid=1003163&mid=0&nbs=1&nettype=0&oi=1875329039&orderid=0%2C3&os=mcdn&platform=pc&sign=340a00&traceid=trRdIKskUCfncA_0_e_N&uipk=5&uparams=e%2Cuipk%2Cnbs%2Cdeadline%2Cgen%2Cos%2Coi%2Ctrid%2Cmid%2Cplatform&upsig=6463fc6c70709af190a8ed3245d6f9d9",
          "base_url": "https://xy42x237x162x226xy.mcdn.bilivideo.cn:8082/v1/resource/1204741650-1-30232.m4s?agrr=0&build=0&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&bvc=vod&bw=17894&deadline=1690007061&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&gen=playurlv2&logo=A0000001&mcdnid=1003163&mid=0&nbs=1&nettype=0&oi=1875329039&orderid=0%2C3&os=mcdn&platform=pc&sign=340a00&traceid=trRdIKskUCfncA_0_e_N&uipk=5&uparams=e%2Cuipk%2Cnbs%2Cdeadline%2Cgen%2Cos%2Coi%2Ctrid%2Cmid%2Cplatform&upsig=6463fc6c70709af190a8ed3245d6f9d9",
          "backupUrl": [
            "https://xy183x94x183x14xy.mcdn.bilivideo.cn:4483/upgcxcode/50/16/1204741650/1204741650-1-30232.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=mcdn&oi=1875329039&trid=00008c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=6463fc6c70709af190a8ed3245d6f9d9&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=1003163&bvc=vod&nettype=0&orderid=0,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=17894&logo=A0000001",
            "https://upos-sz-mirror08h.bilivideo.com/upgcxcode/50/16/1204741650/1204741650-1-30232.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=08hbv&oi=1875329039&trid=8c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=dcd9a2ef948c5cb1e9f7cb089d7c3140&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=17894&logo=40000000"
          ],
          "backup_url": [
            "https://xy183x94x183x14xy.mcdn.bilivideo.cn:4483/upgcxcode/50/16/1204741650/1204741650-1-30232.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=mcdn&oi=1875329039&trid=00008c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=6463fc6c70709af190a8ed3245d6f9d9&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=1003163&bvc=vod&nettype=0&orderid=0,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=17894&logo=A0000001",
            "https://upos-sz-mirror08h.bilivideo.com/upgcxcode/50/16/1204741650/1204741650-1-30232.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1690007061&gen=playurlv2&os=08hbv&oi=1875329039&trid=8c5e039da2fd4dc2b3a89018c3ef0129u&mid=0&platform=pc&upsig=dcd9a2ef948c5cb1e9f7cb089d7c3140&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&buvid=08ACC7F3-1632-61B2-ABBC-749F9AD64B8716559infoc&build=0&agrr=0&bw=17894&logo=40000000"
          ],
        }
      ],
    },
  }
}
```
