import unittest

import api.favorite
import api.media
import api.upper


class MyTestCase(unittest.TestCase):
    def test_request_favorite(self):
        """
        测试获取收藏夹信息
        """
        favorite_id: int = 1561982153
        resp = api.favorite.request_favorite(favorite_id)
        print(resp)
        self.assertEqual(resp.code, 0)
        self.assertEqual(resp.message, '0')
        self.assertIsNotNone(resp.title)
        self.assertIsNotNone(resp.media_count)

    def test_request_favorite_content(self):
        """
        测试获取收藏夹一页内容
        """
        favorite_id: int = 1561982153
        page_number: int = 1
        resp = api.favorite.request_favorite_content(favorite_id, page_number)
        print(resp)
        self.assertEqual(resp.code, 0)
        self.assertEqual(resp.message, '0')
        self.assertIsNotNone(resp.medias)
        for media in resp.medias:
            self.assertIsNotNone(media.id)
            self.assertIsNotNone(media.title)
            self.assertIsNotNone(media.cover)
            self.assertIsNotNone(media.intro)
            self.assertIsNotNone(media.page)
            self.assertIsNotNone(media.duration)
            self.assertIsNotNone(media.upper_mid)
            self.assertIsNotNone(media.upper_name)
            self.assertIsNotNone(media.ctime)
            self.assertIsNotNone(media.pubtime)
            self.assertIsNotNone(media.fav_time)
            self.assertIsNotNone(media.bv_id)
            self.assertIsNotNone(media.first_cid)

    def test_request_user_detail(self):
        """
        测试获取用户信息
        """
        upper_id: int = 346563107
        resp = api.upper.request_user_detail(upper_id)
        print(resp)
        self.assertEqual(resp.code, 0)
        self.assertEqual(resp.message, '0')
        self.assertIsNotNone(resp.mid)
        self.assertIsNotNone(resp.name)
        self.assertIsNotNone(resp.sign)

    def test_request_upper_content(self):
        """
        测试获取UP主投稿一页内容
        """
        upper_id: int = 346563107
        page_number: int = 1
        resp = api.upper.request_upper_content(upper_id, page_number)
        print(resp)
        self.assertEqual(resp.code, 0)
        self.assertEqual(resp.message, '0')
        self.assertIsNotNone(resp.media_count)
        self.assertIsNotNone(resp.medias)
        for media in resp.medias:
            self.assertIsNotNone(media.title)
            self.assertIsNotNone(media.created)
            self.assertIsNotNone(media.length)
            self.assertIsNotNone(media.aid)
            self.assertIsNotNone(media.bv_id)

    def test_request_media_detail(self):
        """
        测试获取单一投稿信息
        """
        bv_id: str = 'BV1i8411S7Zy'
        resp = api.media.request_media_detail(bv_id)
        print(resp)
        self.assertEqual(resp.code, 0)
        self.assertEqual(resp.message, '0')
        self.assertIsNotNone(resp.bv_id)
        self.assertIsNotNone(resp.aid)
        self.assertIsNotNone(resp.videos)
        self.assertIsNotNone(resp.pic)
        self.assertIsNotNone(resp.title)
        self.assertIsNotNone(resp.pubdate)
        self.assertIsNotNone(resp.ctime)
        self.assertIsNotNone(resp.desc)
        self.assertIsNotNone(resp.duration)
        self.assertIsNotNone(resp.owner_id)
        self.assertIsNotNone(resp.pages_cid_list)

    def test_request_media_pages(self):
        """
        测试获取投稿分p信息
        """
        bv_id: str = 'BV1i8411S7Zy'
        resp = api.media.request_media_pages(bv_id)
        print(resp)
        self.assertEqual(resp.code, 0)
        self.assertEqual(resp.message, '0')
        self.assertIsNotNone(resp.pages)
        for page in resp.pages:
            self.assertIsNotNone(page.cid)
            self.assertIsNotNone(page.part)
            self.assertIsNotNone(page.duration)
            self.assertIsNotNone(page.first_frame)

    def test_request_media_audio_video(self):
        """
        测试获取投稿音视频url
        """
        # https://api.bilibili.com/x/player/playurl?fnval=976&bvid=BV1i8411S7Zy&cid=1204741650
        bv_id: str = 'BV1i8411S7Zy'
        cid: int = 1204741650
        audio_list, video_list = api.media.request_media_audio_video(bv_id, cid)
        print(audio_list)
        print(video_list)
        self.assertGreater(len(audio_list), 0)
        self.assertGreater(len(video_list), 0)
        for url in audio_list:
            self.assertEqual(type(url), str)
        for url in video_list:
            self.assertEqual(type(url), str)


if __name__ == '__main__':
    unittest.main()
