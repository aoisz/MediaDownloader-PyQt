# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UIDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import time
from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PySide6.QtCore import QThread
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from VideoPlayer import *   
from QEditText import *
from pytube import YouTube
from pytube.exceptions import RegexMatchError
import pytube.request
from downloadThread import *
import youtube_dl
import os
import time
from ResolutionOption import ResolutionOption
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = ".\\platform\\"

pytube.request.default_range_size = 1048576

class Ui_MainWindow(QWidget):
    update_progress = QtCore.pyqtSignal(int)
    update_status = QtCore.pyqtSignal(str)
    file_size = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 450)
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint |QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowMaximizeButtonHint)
        MainWindow.setWindowIcon(QtGui.QIcon('.\\icon\\download.png'))
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.linkEditTxt = MyQTextEdit(self.centralwidget)
        self.linkEditTxt.setGeometry(QtCore.QRect(10, 10, 501, 31))
        self.linkEditTxt.setObjectName("textEdit")
        self.linkEditTxt.setFocus(False)
        self.downloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downloadButton.setGeometry(QtCore.QRect(680, 10, 101, 31))
        self.downloadButton.setObjectName("pushButton")

        self.downloadButton.clicked.connect(self.choise)

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setGeometry(QtCore.QRect(20,395,772,31))
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        self.progressBar.setEnabled(True)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(520, 10, 151, 31))
        self.comboBox.setObjectName("comboBox")

        self.resolution_option = ResolutionOption(self.centralwidget)
        self.resolution_option.setGeometry(QtCore.QRect(10, 60, 772, 340))

        # self.videoPlayer = VideoPlayer(self.centralwidget)
        # self.videoPlayer.setGeometry(QtCore.QRect(10, 60, 772, 340))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.setPlaceHolder()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Media Downloader"))
        MainWindow.setWindowIcon(QtGui.QIcon(
            '.\\icon\\download_frame_icon.png'))
        self.downloadButton.setText(_translate("MainWindow", "Search"))
        self.downloadButton.setIcon(QtGui.QIcon('.\\icon\\search.png'))

        comboBoxList = ["Youtube", "Facebook"]       
        self.comboBox.addItems(comboBoxList)
        self.comboBox.setEditable(False)
        #icon youtube
        iconytb = QtGui.QIcon('.\\icon\\youtube.png')
        self.comboBox.setItemIcon(0,iconytb)
        #icon facebook
        iconfb = QtGui.QIcon('.\\icon\\facebook.png')
        self.comboBox.setItemIcon(1,iconfb)


        # self.thread = DownloadThread(self.download_from_youtube)

    def setPlaceHolder(self):
        if (self.linkEditTxt.toPlainText() == ""):
            self.linkEditTxt.setText("Paste link here")
            self.linkEditTxt.setStyleSheet("QTextEdit {color:black}")
    
       
# # #cái gốc
#     def download_from_youtube(self, link):
#         link = self.linkEditTxt.toPlainText()
#         print("Download link: " + link) # Print the link to see if it's correct
#         try:
#             youtubeObj = YouTube(link)
#         except RegexMatchError:
#         # Handle the error here
#             print("Invalid YouTube link")
#             return

#         youtubeObj = youtubeObj.streams.get_highest_resolution()
#     # Start the download
#         try:
#            # Estimate the total duration based on the file size
#             total_duration = youtubeObj.filesize / 1000000 # in MB

#         # Start the download
#             start_time = time.time()
#             youtubeObj.download()
#             end_time = time.time()

#         # Emit the progress through the signal
#             elapsed_duration = end_time - start_time
#             elapsed_percent = elapsed_duration / total_duration * 100
#             self.progress_updated.emit(elapsed_percent)
#             for i in range(0, total_duration):
#                 self.progressBar.setValue(i+1)

#         except Exception as e:
#             print("Error downloading: " + str(e))
#         return

    def download_from_youtube(self, link):
        print(f'Downloading link: {link}')
        try:
            youtubeObj = YouTube(link,on_progress_callback=self.on_download_progress)
            # self.resolution_option.setup(youtubeObj)
        except RegexMatchError:
        # Handle the error here
            print("Invalid YouTube link")
            return

        stream = youtubeObj.streams.get_highest_resolution()
        stream.download()

    def on_download_progress(self, stream, chunk, bytes_remaining):
        file_size = stream.filesize
        bytes_received = file_size - bytes_remaining
        percentage = int((bytes_received/file_size)*100)
        self.progressBar.setValue(percentage)
    
    def downloadfromFacebook(self,link):
        print(link) # Print the link to see if it's correct
        try:
            with youtube_dl.YoutubeDL({'outtmpl': '%(title)s.%(ext)s'}) as ydl:                
                def progress_hook(progress):
                    if progress['status'] == 'downloading':
                    # Get the total file size in bytes
                        total_size = int(progress['total_bytes'])
                    # Get the downloaded size in bytes
                        downloaded_size = int(progress['downloaded_bytes'])
                    # Calculate the download progress as a percentage
                        progress_percent = int(downloaded_size / total_size * 100)
                    # Emit the progress_updated signal with the progress percentage
                        self.thread.update_progress(progress_percent)
                        self.progressBar.update()

                ydl.params['progress_hooks'] = [progress_hook]
                # ydl.params['progress_hooks'] = [self.my_hook]
                ydl.download([link])
        except Exception as e:
            print("Error downloading" + str(e)) 
            return

    def choise(self):
        link = self.linkEditTxt.toPlainText()
        if self.comboBox.currentText() == "Facebook":
            self.thread = DownloadThread(self.downloadfromFacebook, link)
            self.thread.progress_updated.connect(self.progressBar.setValue)
            self.thread.start()
        elif self.comboBox.currentText() == "Youtube":
            self.download_from_youtube(link)
            # self.thread = DownloadThread(self.download_from_youtube,link)
            # self.downloader.download_video(link,'D:\Workspace\Python\MediaDownloader')
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())