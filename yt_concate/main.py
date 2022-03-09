from yt_concate.pipeline.Steps.get_video_list import GetVideoList
from yt_concate.pipeline.Steps.Step import StepException

from yt_concate.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UCoSrY_IQQVpmIRZ9Xf-y93g'

def main():
    inputs = {
        'channel_id': CHANNEL_ID

    }

    steps = [
        GetVideoList(),

    ]
    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
