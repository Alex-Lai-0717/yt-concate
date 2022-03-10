from pytube import YouTube

from .Step import Step
from .Step import StepException


class DownloadCaption(Step):
    def process(self, data, inputs, utils):

        for url in data:
            print("downloading caption for", url)
            if utils.caption_file_exists(url):
                print("found existing caption file:" + utils.get_video_id(url) + '.txt')
                continue

            try:
                source = YouTube(url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except (AttributeError, KeyError):
                print("Error when downloading caption for", url)
                continue

            text_file = open(utils.get_caption_filepath(url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
