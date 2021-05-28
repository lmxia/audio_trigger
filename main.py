# This is a sample Python script.

# Press F10 to execute it or replace it with your code.
# Press Double to search everywhere for classes, files, tool windows, actions, and settings.
from snowboy import snowboydecoder


def detected_callback():
    print("hotword detected")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    detector = snowboydecoder.HotwordDetector("snowboy/resources/zijinshan.pmdl", sensitivity=0.5, audio_gain=1)
    detector.start(detected_callback)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
