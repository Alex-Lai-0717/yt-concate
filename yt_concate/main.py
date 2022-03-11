from yt_concate.pipeline.steps.preflight import PreFlight
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.initialize import InitializeYT
from yt_concate.pipeline.steps.download_caption import DownloadCaption
from yt_concate.pipeline.steps.read_caption import ReadCaption
from yt_concate.pipeline.steps.search import Search
from yt_concate.pipeline.steps.download_videos import DownloadVideos
from yt_concate.pipeline.steps.postflight import PostFlight
from yt_concate.pipeline.pipeline import Pipeline
from utils import Utils
from yt_concate.pipeline.steps.step import StepException

CHANNEL_ID = 'UCphTF9wHwhCt-BzIq-s4V-g'


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'Earth',

    }

    steps = [
        PreFlight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaption(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        PostFlight(),
    ]
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
