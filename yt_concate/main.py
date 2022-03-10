from yt_concate.pipeline.Steps.get_video_list import GetVideoList
from yt_concate.pipeline.Steps.download_caption import DownloadCaption
from yt_concate.pipeline.Steps.Step import StepException
from yt_concate.pipeline.pipeline import Pipeline
from utils import Utils
from yt_concate.pipeline.Steps.preflight import PreFlight
from yt_concate.pipeline.Steps.postflight import PostFlight

CHANNEL_ID = 'UCoSrY_IQQVpmIRZ9Xf-y93g'


def main():
    inputs = {
        'channel_id': CHANNEL_ID

    }

    steps = [
        PreFlight(),
        GetVideoList(),
        DownloadCaption(),
        PostFlight(),
    ]
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
