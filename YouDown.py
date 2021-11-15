from __future__ import unicode_literals
import youtube_dl
import shutil
import os
import threading
from tkinter import *
dlthread = 0
def download(Format, vidlist):
        if Format == "mp3":
             ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }],
            'postprocessor_args': [
                '-ar', '16000'
            ],
            'prefer_ffmpeg': True,
            'keepvideo': False
            }
        else:
            ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                print(vidlist)
                ydl.download(vidlist)
            except Exception as e:
                print("Failed to download video! Error:")
                print(e)
        print("Done")

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master		
        self.init_window()
    def init_window(self):
        self.master.title("YouDown")
        self.pack(fill=BOTH, expand=1)
        runButton = Button(self, text="Mp3", command=self.mp3, fg='#282828', bg='#FF0000')
        runButton.place(x=145, y=210)
        runButton = Button(self, text="Mp4", command=self.mp4, fg='#282828', bg='#FF0000')
        runButton.place(x=205, y=210)
    def mp3(self):
        global dlthread
        try:
            os.mkdir("Videos")
        except:
            print("Folder 'Videos' Already Exists")
        if os.name == "nt":
            shutil.copy("ffmpeg.exe","Videos/ffmpeg.exe")
        os.chdir("Videos")
        vidlist = video.get().split()

        dlthread = threading.Thread(target=download, args=("mp3", vidlist,))
        dlthread.start()
    def mp4(self):
        global dlthread
        try:
            os.mkdir("Videos")
        except:
            print("Folder 'Videos' Already Exists")

        os.chdir("Videos")
        vidlist = video.get().split()
        dlthread = threading.Thread(target=download, args=("mp4", vidlist,))
        dlthread.start()

root = Tk()

video = StringVar()

mp3 = IntVar()

root.geometry("400x295")

app = Window(root)

label = Label(root, text = "YouDown by TechGuyTechTips", font=("bold", 10),fg="darkred").pack()

label1 = Label(root, text="Enter Video(s) or Playlist: ", font=("arial",12, "bold"), fg="black").place(x=100, y=20)

entry_box = Entry(root, textvariable=(video), width=50, bg="#FFFFFF").place(x=50, y=60)

root.mainloop()
dlthread.join()
