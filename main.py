import re
import os
from pytube import Playlist
from progress.bar import IncrementalBar


class Audio:
    def __init__(self, url, condition):
        self.playlist = Playlist(url)
        self.playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
        self.PLAYLIST_STREAM = '140'

    def checkDir(self, condition):
        if condition == '3':
            # Checks wheter the directory not exists
            if not os.path.exists('My Playlist'):
                # Create directory
                os.makedirs('My Playlist')

            # Checks wheter the directory exists
            if os.path.exists('My Playlist'):
                count = len(self.playlist.video_urls)
                bar = IncrementalBar('Download', max = count)
                bar.next()
                for video in self.playlist.videos:
                    bar.next()
                    # Download in mp4 format
                    audioStream = video.streams.get_by_itag(self.PLAYLIST_STREAM)
                    audioStream.download(output_path='My Playlist')
                bar.finish()


print('''\n\n\n
       ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀▄▄▄█████▓ █    ██  ▄▄▄▄   ▓█████ 
      ▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓  ██▒ ▓▒ ██  ▓██▒▓█████▄ ▓█   ▀ 
      ▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒ ▓██░ ▒░▓██  ▒██░▒██▒ ▄██▒███   
      ░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ░ ▓██▓ ░ ▓▓█  ░██░▒██░█▀  ▒▓█  ▄ 
      ░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄  ▒██▒ ░ ▒▒█████▓ ░▓█  ▀█▓░▒████▒
       ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒  ▒ ░░   ░▒▓▒ ▒ ▒ ░▒▓███▀▒░░ ▒░ ░
       ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░    ░    ░░▒░ ░ ░ ▒░▒   ░  ░ ░  ░
       ░  ░░ ░  ░   ▒   ░        ░ ░░ ░   ░       ░░░ ░ ░  ░    ░    ░   
       ░  ░  ░      ░  ░░ ░      ░  ░               ░      ░         ░  ░
                    ░                                       ░        
''')
print('''
                             Select One Option

            [1]Video  [2]Áudio  [3]Playlist  [4]Playlist Áudio

                                  [5]Exit

''')
condition = input('>>> ')
if condition == '5':
    print('Closing...')
if condition == '3':
    print('Type Your URL:')
    url = input('>>> ')
    start = Audio(url, condition)
    start.checkDir(condition)
