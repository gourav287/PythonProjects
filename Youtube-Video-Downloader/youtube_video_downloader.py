# Importing the necessary libraries
from pytube import YouTube
# from google.colab import drive

# Steps in google colab to integrate with Google Drive
# drive.mount('/content/gdrive')
# %cd 'gdrive/My Drive/Rush_Classes/C3 Batch 26'

# Accept the input and format in the right format
def accept_format_input():
    myl = []
    with open("input.txt", "r") as data:
        myl = list(data.read().split('\n'))
    return myl

# Function to start downloading the video
def startDownload(url):

    try:

        # Creating the YouTube object with given URL
        yt = YouTube(url)
        
        title = yt.title
        
        # Creating stream object for the best audio+video stream url
        stream = yt.streams.filter(progressive=True).get_highest_resolution()
        
        # Getting the location to download the video file
        download_path = ''
        
        # Measuring the size of the file to be downloaded
        file_size = stream.filesize_mb
        print('Video {} size: {} mb'.format(title, file_size))
        
        # Downloading the video at specified location
        stream.download(download_path)
        print('Video {} downloaded successfully!'.format(title))

    except Exception as e:
        
        print("We have an error:", e)

# The driver code.
if __name__ == '__main__':
    
    # Take input from the input file
    urls = accept_format_input()
    
    # Display number of videos to be downloaded from youtube
    n = len(urls)
    print('Total videos to be downloaded:', n)

    # Download the videos one-by-one
    for i in range(n):
        
      startDownload(urls[i])