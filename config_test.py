import unittest

import config


class MyTestCase(unittest.TestCase):
    def test_load_config(self):
        config.load_config()
        self.assertIsNotNone(config.log_file_path)
        self.assertIsNotNone(config.sqlite3_file)
        self.assertIsNotNone(config.all_media_path)


if __name__ == '__main__':
    unittest.main()
