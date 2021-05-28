# This is a sample Python script.

# Press F10 to execute it or replace it with your code.
# Press Double to search everywhere for classes, files, tool windows, actions, and settings.
from snowboy import snowboydecoder
from robot import utils, Player, constants, logging

logger = logging.getLogger(__name__)


def detected_callback():
    def start_record():
        utils.setRecordable(True)
        logger.info('开始录音')

    Player.play(constants.getData('beep_hi.wav'), onCompleted=start_record, wait=True)


def audioRecorderCallback(fname):
    print(fname)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    detector = snowboydecoder.HotwordDetector("snowboy/resources/zijinshan.pmdl", sensitivity=0.5, audio_gain=1)
    detector.start(detected_callback=detected_callback,
                   audio_recorder_callback=audioRecorderCallback)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
