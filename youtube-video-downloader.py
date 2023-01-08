import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import filedialog, messagebox


# creating widgets
def createWidgets():

    link_label = Label(root, text="Youtube URL: ", bg="#f5f5f5")
    link_label.grid(row=1, column=0, pady=5, padx=5)

    root.link_text = Entry(root, width=60, textvariable=video_link)
    root.link_text.grid(row=1, column=1, pady=5, padx=5)

    destination_label = Label(root, text="Destination: ", bg="#f5f5f5")
    destination_label.grid(row=2, column=0, pady=5, padx=5)

    root.destination_text = Entry(root, width=45, textvariable=download_path)
    root.destination_text.grid(row=2, column=1, pady=3, padx=3)

    browse_but = Button(root, text="Browse", command=browse,
                        width=10, bg="#505050")
    browse_but.grid(row=2, column=2, pady=1, padx=1)

    download_but = Button(root, text="Download Video",
                          command=download, width=25, bg="#505050")
    download_but.grid(row=3, column=1, pady=3, padx=3)


# creating a function of browse(where the downloaded files will be stored)
def browse():

    download_dir = filedialog.askdirectory(initialdir="Your Directory Path")

    download_path.set(download_dir)


# create a function of downloading youtube video
def download():

    url = video_link.get()
    folder = download_path.get()

    get_video = YouTube(url)
    get_stream = get_video.streams.get_highest_resolution()
    get_stream.download(folder)

    messagebox.showinfo('R0wh4n-Youtube Video Downloader',
                        "Sucessfully Downloaded! The video is in the " + folder)
    messagebox.grid(row=5, column=1, pady=5, padx=5)


# create display window
root = tk.Tk()
root.geometry = ('100x800')
root.title("R0wh4n-Youtube Video Downloader")
root.config(background="#49A")


# setting video link and download path to a string variable
video_link = StringVar()
download_path = StringVar()
createWidgets()


root.mainloop()
