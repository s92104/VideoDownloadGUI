import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from UI import Ui_Form

from pytube import YouTube

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        
        # init
        self.ui.link.setFocus()
        # DownloadClick
        self.ui.downloadBtn.clicked.connect(self.downloadBtn_Click)
        self.show()  
    # 下載按鈕
    def downloadBtn_Click(self):    
        link=self.ui.link.text()
        yt=YouTube(link)
        # 可下載
        videoStream=yt.streams.filter(progressive=True)
        video=videoStream.all()
        if len(video)==0:
            print("無法下載")
        # MP4
        mp4VideoStream=videoStream.filter(subtype="mp4")
        mp4Video=mp4VideoStream.all()
        if len(mp4Video)==0:
            print("無MP4")
            downloadVideoStream=videoStream
        else:      
            downloadVideoStream=mp4VideoStream
        downloadVideo=downloadVideoStream.order_by('resolution').desc().first()
        # Thread
        self.downloadThread=DownloadThread(downloadVideo)
        yt.register_on_complete_callback(self.downloadThread.complete)
        yt.register_on_progress_callback(self.downloadThread.progress)
        self.downloadThread.completeSignal.connect(self.complete)
        self.downloadThread.progressSignal.connect(self.progress)
        self.downloadThread.start()
    # 下載完成
    def complete(self,title):
        # 標題
        self.ui.title.setText(title)
        # 訊息框
        messageBox=QMessageBox.information(self,"訊息","下載完成",QMessageBox.Ok)
        print("下載完成:"+title)
    # 下載進度
    def progress(self,percent):   
        self.ui.progressBar.setValue(int(percent))
        print(percent)
        
# 下載Thread
class DownloadThread(QThread):    
    completeSignal = pyqtSignal(str)
    progressSignal=pyqtSignal(int)
    def __init__(self,downloadVideo):
        super().__init__()
        self.downloadVideo=downloadVideo    
    def run(self):
        self.downloadVideo.download()
    # 下載完成
    def complete(self,stream,file_handle):
        self.completeSignal.emit(stream.default_filename)
    # 下載進度
    def progress(self,stream, chunk, file_handle, bytes_remaining):  
        file_size=stream.filesize
        percent = (100*(file_size-bytes_remaining))/file_size
        self.progressSignal.emit(percent)

app=QApplication(sys.argv)
w=AppWindow()
w.show()
sys.exit(app.exec_())