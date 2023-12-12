from pytube import Playlist, YouTube
import customtkinter as ctk
import os

mainWindow = ctk.CTk()
mainWindow.geometry("600x300")

# Get the current windows user
user = os.getlogin()


# Download the video
def downloadVideo():
    link = entryLinkVideo.get()
    yt = YouTube(link)
    video = yt.streams.get_highest_resolution()
    video.download(f"C:\\Users\\{user}\\Videos")


# Download the audio
def downloadAudio():
    link = entryLinkVideo.get()
    yt = YouTube(link)
    audio = yt.streams.get_audio_only()
    audio.download(f"C:\\Users\\{user}\\Music")


btnDescargarVideo = ctk.CTkButton(mainWindow, text="Video", command=downloadVideo)
btnDescargarAudio = ctk.CTkButton(mainWindow, text="Audio", command=downloadAudio)


def viewbtnVideo():
    btnDescargarVideo.grid(row=2, column=0, padx=5, pady=10)
    btnDescargarAudio.grid(row=3, column=0, padx=5, pady=5)


def viewbtnList():
    pass


# Link of one video
labelLinkVideo = ctk.CTkLabel(mainWindow, text="LINK-VIDEO")
labelLinkVideo.grid(row=0, column=0, padx=5, pady=5)

entryLinkVideo = ctk.CTkEntry(mainWindow, width=300)
entryLinkVideo.grid(row=0, column=1, padx=5, pady=5)

# Link of the list
labelLinkList = ctk.CTkLabel(mainWindow, text="LINK-LIST")
labelLinkList.grid(row=1, column=0, padx=5, pady=5)

entryLinkList = ctk.CTkEntry(mainWindow, width=300)
entryLinkList.grid(row=1, column=1, padx=5, pady=5)


btnVideo = ctk.CTkButton(mainWindow, text="Vídeo", command=viewbtnVideo)
btnList = ctk.CTkButton(mainWindow, text="List", command=viewbtnList)

btnVideo.grid(row=0, column=2, padx=10, pady=5)
btnList.grid(row=1, column=2, padx=10, pady=5)


mainWindow.mainloop()
