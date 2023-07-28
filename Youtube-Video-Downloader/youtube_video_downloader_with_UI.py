# Importing the necessary libraries
from pytube import YouTube
import tkinter as tk
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from threading import *

# Function to start downloading the video
def startDownload():
    
    try:
        
        # Getting the url of the video
        url = getlink.get()
        
        # Changing the button text and status to be disabled
        save.config(text = 'Please Wait', state='disabled')
        
        # Creating the YouTube object with given URL
        yt = YouTube(url)
        
        title = yt.title
        
        # Creating stream object for the best audio+video stream url
        stream = yt.streams.filter(progressive=True).first()
        
        # Getting the location to download the video file
        download_path = askdirectory()
        
        # Measuring the size of the file to be downloaded
        file_size = stream.filesize
        
        # Downloading the video at specified location
        stream.download(download_path)
        
        # Changing the button text and status back to normal
        save.config(text = 'Download', state = 'normal')
        
        # Alert box to inform about successful download
        showinfo("Download Finished", "The video is downloaded successfully")
        
        # Empty the input textbox on the window
        getlink.delete(0, 'end')
    
    except :
        
        # Displaying the error message window
        showinfo("Invalid URL", "Please enter a valid URL")
        
        # Normalizing the download button to allow retrying the download with new url
        save.config(text = 'Download', state = 'normal')

# Function to use different thread for GUI and downloading process
# Increases the speed
def startDownloadThread():
    
    # Initializing the function inside a thread
    thread = Thread(target = startDownload)
    
    # Invoking the thread
    thread.start()

# The driver code. Create a GUI to help the user download any video just by inputting its URL.
if __name__ == '__main__':
    
    # Exception handling
    try:

        # Creating the tkinter GUI window
        root = tk.Tk()

        # Setting minsize, title and logo of the window
        root.minsize(400, 400)
        root.title('YouTube Downloader')
        root.iconbitmap('logo.ico')
        
        # Displaying the download logo
        imgfile = ImageTk.PhotoImage(Image.open('logo_.png').resize((150, 150)))
        label = tk.Label(root, image = imgfile)
        label.pack(side='top', pady = 10)

        # Creating a text label
        txt = tk.Label(root, 
                 text='Video Link: ', 
                 font=('calibre',10,'bold')) 

        txt.pack(side = 'top', pady = 10)

        # Creating a text input Entry inside first frame and gridding its position
        getlink = tk.Entry(root)
        getlink.pack(side='top', fill = X, padx = 20)
        
        # Defining a frame to put download and cancel button in it.
        bottomframe = tk.Frame(root)
        bottomframe.pack(side = 'bottom', pady = 20)

        # Creating a button to ensure intake of the input
        save = tk.Button(bottomframe,
                         text = 'Download',
                         width = 15,
                         height = 2,
                         fg = 'yellow',
                         bg = 'black',
                         #highlightthickness=14,
                         borderwidth = 2,
                         relief = 'ridge',
                         command = startDownloadThread)
        save.pack(side = 'left', padx = 4)

        # Creating another button to cancel the input
        cancel = tk.Button(bottomframe,
                           text = 'Cancel',
                           width = 15,
                           height = 2,
                           fg = 'yellow',
                           bg = 'black',
                           borderwidth = 2,
                           relief = 'ridge',
                           command = root.destroy)
        cancel.pack(side = 'left', padx = 4)

        # Running the root
        root.mainloop()

    # Print the exception if any and terminate the program
    except Exception as e:

        # Printing the error message
        #print(e)
        
        # Displaying the error prompt
        showinfo("Error Prompt", "Unexpected error. Terminating the program")
        
        # Terminating the program
        root.destroy()