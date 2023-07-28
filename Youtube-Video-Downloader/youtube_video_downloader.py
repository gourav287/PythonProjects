# Importing the necessary libraries
from pytube import YouTube
from google.colab import drive

# Steps in google colab to integrate with Google Drive
drive.mount('/content/gdrive')
%cd 'gdrive/My Drive/Rush_Classes/C3 Batch 26'

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
        # stream.download(download_path)
        print('Video {} downloaded successfully!'.format(title))

    except Exception as e:
        
        print("We have an error:", e)

# The driver code.
if __name__ == '__main__':
    
    # urls = ['https://youtu.be/anqsgNzCJPM', 'https://youtu.be/IHOSIgqQOIg', 'https://youtu.be/IrJeyYA-LVQ', 'https://youtu.be/mKXgf9Py0SA', 'https://youtu.be/IWBCVzvLiuk', 'https://youtu.be/ZIJsjAhV1Cc', 'https://youtu.be/em40jhBG8a8', 'https://youtu.be/pvOYqSZmvBI', 'https://youtu.be/U8eNks6Wkvs', 'https://youtu.be/lz6CN0r3KK8', 'https://youtu.be/2nYcaaKYL6k', 'https://youtu.be/ur9w_axUP2w', 'https://youtu.be/9JHGZWsxdCA', 'https://youtu.be/s1EwUZB3XuI', 'https://youtu.be/WD0LGV1afak', 'https://youtu.be/OgMxRniPmgE', 'https://youtu.be/rmfWSu9b3Qs', 'https://youtu.be/g1oHqw891qY', 'https://youtu.be/wyqnu9wZwkY', 'https://youtu.be/o50E_m_WSj0', 'https://youtu.be/oVLkXOOJEjo', 'https://youtu.be/XuvY_anz8OI', 'https://youtu.be/5iMGGk1Psh0', 'https://youtu.be/Y4-e1Aie6xA', 'https://youtu.be/lCdtCnM03Hs', 'https://youtu.be/pmVtpEHCbyg', 'https://youtu.be/Y7iCSUsqLQg', 'https://youtu.be/EA6R5qDNBP0', 'https://youtu.be/l-_1To9OWIY', 'https://youtu.be/GoL5MEdiChs', 'https://youtu.be/JoZZTzQugfM', 'https://youtu.be/6AKWoKppHog', 'https://youtu.be/yumYq912zh0', 'https://youtu.be/7raaMBo7_7Y']
    urls = ['https://youtu.be/anqsgNzCJPM']
    
    n = len(urls)

    for i in range(n):

      startDownload(urls[i])