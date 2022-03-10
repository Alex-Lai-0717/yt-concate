from yt_concate.pipeline.Steps.get_video_list import GetVideoList
from yt_concate.pipeline.Steps.download_caption import DownloadCaption
from yt_concate.pipeline.Steps.Step import StepException
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.Steps.read_caption import ReadCaption
from yt_concate.pipeline.Steps.preflight import PreFlight
from yt_concate.pipeline.Steps.postflight import PostFlight
from utils import Utils

CHANNEL_ID = 'UCoSrY_IQQVpmIRZ9Xf-y93g'


def main():
    inputs = {
        'channel_id': CHANNEL_ID

    }

    steps = [
        PreFlight(),
        GetVideoList(),
        DownloadCaption(),
        ReadCaption(),
        PostFlight(),
    ]
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
