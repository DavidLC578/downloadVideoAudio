from pytube import Playlist, YouTube
import customtkinter as ctk


mainWindow = ctk.CTk()
mainWindow.geometry("600x300")


def descargarVideo():
    pass


def descargarAudio():
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


btnDescargarVideo = ctk.CTkButton(mainWindow, text="Vídeo", command=descargarVideo)
btnDescargarAudio = ctk.CTkButton(mainWindow, text="Audio", command=descargarAudio)

btnDescargarVideo.grid(row=0, column=2, padx=10, pady=5)
btnDescargarAudio.grid(row=1, column=2, padx=10, pady=5)


mainWindow.mainloop()
