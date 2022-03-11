from pytube import YouTube

from yt_concate.settings import VIDEOS_DIR
from .step import Step


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])  # 迴避掉相同的影片
        print("videos to download=", len(yt_set))
        for yt in yt_set:
            url = yt.url

            if utils.video_file_exists(yt):
                continue

            print("downloading", url)
            YouTube(url).streams.filter(res="720p").first().download(output_path=VIDEOS_DIR, filename=yt.id + '.mp4')

        return data
