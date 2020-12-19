import pytube
from tkinter import *

root=Tk()
root.geometry('600x200')
root.title('Youtube Video Downloader')

Label_1=Label(root,text="  Youtube Video Download",fg="Blue",font=("bold",20))
Label_1.place(x=120,y=20)

def yt_Download():
    a=mylink.get()
    ytVideo = YouTube(a).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    ytVideo.download('C:\sai')
    print("entrybox",a)

mylink=StringVar()

userlink=Entry(root, width=60, textvariable=mylink)
userlink.place(x=140, y=80)


b= Button(root,text="Download Video", width=20, bg='green',fg="white", command=yt_Download)
b.place(x=220, y=110)


root.mainloop()
