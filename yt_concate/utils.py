import os
from settings import CAPTIONS_DIR
from settings import VIDEOS_DIR
from settings import DOWNLOADS_DIR


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def get_video_id(url):
        return url.split('watch?v=')[-1]  # [-1]=倒數數回來最後一個

    def get_caption_filepath(self, url):
        return os.path.join(CAPTIONS_DIR, self.get_video_id(url) + '.txt')

    def create_dirs(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)  # 如果資料夾已經存在,不回報錯誤
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)

    def caption_file_exists(self, url):
        path = self.get_caption_filepath(url)
        return os.path.exists(path) and os.path.getsize(path) > 0

    def get_video_list_filepath(self, channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def video_list_file_exists(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0