import os
from pprint import pprint

from .Step import Step
from yt_concate.settings import CAPTIONS_DIR


class ReadCaption(Step):
    def __init__(self):
        pass

    def process(self, data, inputs, utils):
        data = {}
        for caption_file in os.listdir(CAPTIONS_DIR):
            captions = {}
            with open(os.path.join(CAPTIONS_DIR, caption_file), 'r') as f:
                time_line = False
                time = None
                caption = None

                for line in f:
                    line = line.strip()
                    if '-->' in line:
                        time_line = True
                        time = line
                        continue
                    if time_line:
                        caption = line
                    captions[caption] = time  # 字幕與時間形成字典
                    time_line = False
            data[caption_file] = captions  # 影片檔名與字幕形成字典
        pprint(data)
        return data
