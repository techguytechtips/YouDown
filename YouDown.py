from __future__ import unicode_literals
import youtube_dl
from tkinter import *

class Window(Frame):                   
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master		
        self.init_window()
		#fm = Frame(master, width=400, height=296, bg="#2C2F33")
		#fm.pack(side=TOP, expand=NO, fill=NONE)
    def init_window(self):
        self.master.title("YouDown")
        self.pack(fill=BOTH, expand=1)
        runButton = Button(self, text="Start", command=self.download, fg='#282828', bg='#FF0000')
        runButton.place(x=180, y=210)

    def download(self):
        vidlist = list = video.get().split()
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(vidlist)

root = Tk()

video = StringVar()

root.geometry("400x295")

app = Window(root)

label = Label(root, text = "YouDown by TechGuyTechTips", font=("bold", 10),fg="darkred").pack()

label1 = Label(root, text="Enter Video(s) or Playlist: ", font=("arial",12, "bold"), fg="black").place(x=100, y=20)

entry_box = Entry(root, textvariable=(video), width=25, bg="#FFFFFF").place(x=120, y=50)

root.mainloop()