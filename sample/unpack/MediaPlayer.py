#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from GUI import Ui_MainWindow
import pandas as pd

class myMainWindow(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)

        # 設定影片播放位置 = videoWidget        
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.videoWidget)

        # 設定按鈕響應事件
        self.openVideoFileButton.clicked.connect(self.openVideoFile)   # open video file
        self.openCaptionFileButton.clicked.connect(self.openCaptionFile)    # open caption file
        self.playOrPauseButton.clicked.connect(self.playOrPause)       # play or pause
        
        # 進度條
        self.durationSlider.setEnabled(False)
        self.player.durationChanged.connect(self.getDuration)
        self.player.positionChanged.connect(self.getPosition)
        self.durationSlider.sliderMoved.connect(self.updatePosition)
        
        # 字幕
        self.captionExist = False
        self.player.positionChanged.connect(self.updateCaption)
        
    # 開啟影片檔案
    def openVideoFile(self):
        self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl(filter='Videos (*.mp4 *.avi *.mkv)')[0]))  # 選取影片
        self.player.play()
        
    # 開啟字幕檔案
    def openCaptionFile(self):
        path = QFileDialog.getOpenFileName(filter='*.csv') # 選取字幕
        if path[0] != '':
            self.captionExist = True
            self.caption = pd.read_csv(path[0])

    # 取得影片總長度
    def getDuration(self, duration):
        self.durationSlider.setRange(0, duration)
        self.durationSlider.setEnabled(True)
        self.displayTime(duration)
        
    # 取得影片播放進度位置
    def getPosition(self, position):
        self.durationSlider.setValue(position)
        self.displayTime(self.durationSlider.maximum() - position)
        
    # 更新進度
    def updatePosition(self, position):
        self.player.setPosition(position)
        self.displayTime(self.durationSlider.maximum() - position)
        self.updateCaption(position)
        
    # 更新字幕
    def updateCaption(self, position):
        if not self.captionExist:
            return
        
        # 每次影片進度更新，在字幕列表中尋找對應時間段的字幕
        position = int(position/1000)
        for i in range(len(self.caption)):
            if i == 0:
                continue
            elif self.caption.iat[i-1, 1] <= position < self.caption.iat[i, 1]:
                self.speakerLabel.setText(self.caption.iat[i-1, 2])
                self.textLabel.setText(self.caption.iat[i-1, 3])
                
    # 播放或暫停
    def playOrPause(self):
        if self.player.state() == 1:
            self.player.pause()
        elif self.player.state() == 2 or self.durationSlider.value() != 0:
            self.player.play()
      
    # 顯示剩餘時間
    def displayTime(self, ms):
        m = int(ms/60000)
        s = int((ms % 60000) / 1000)
        self.durationLabel.setText('{}:{}'.format(m, s))
    
    # 結束應用程式，同時結束影片播放器
    def closeEvent(self, event):
        self.player.stop()


# In[2]:


import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = myMainWindow()
    window.show()
    sys.exit(app.exec_())

