'''
DOWNLOAD YOUR PLAYLIST
														 
Created by Kizner
How to use?
 1 - Type in the terminal to download all dependencies:

	For Linux: pip3 -r install requeriments.txt
	For Windows: pip -r install requeriments.txt

2- Now, run the 'main.py' file and enter the url, example:
	Enter playlist url: https://www.youtube.com/playlist?list=PLZTplHNMbAgbT6UhDKmz-LB3KoazwcRcG

'''
import re
import os
from pytube import Playlist


def reciveVideo(url, condition):
	playlist = Playlist(url)
	playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
	YOUTUBE_STREAM_AUDIO = '140'

	if condition == 'y':

		# Checks whether the directory not exists
		if not os.path.exists('Youtube Playlist'): 
			# Create directory
			os.makedirs('Youtube Playlist')

		# Checks whether the directory exists
		if os.path.exists('Youtube Playlist'):
			count = len(playlist.video_urls)
			count = str(count)
			print('\n' + count + ' Videos in this playlist\n')
			# Number of the video
			num = 0
			for video in playlist.videos:
				num += 1
				num2 = str(num)
				print('Download ' + num2 + ' of ' + count)
				print('Title: ' + video.title)
				print('Author: ' + video.author + '\n')

				try:
					# Video Download
					audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
					audioStream.download(output_path='Youtube Playlist')
					# Convert for .mp3 format
					name = video.title + '.mp4'
					path = 'Youtube Playlist/' + name
					convert = os.path.splitext(name)[0]
					# Rename file extension .mp4 for .mp3
					os.rename(path, path + convert + '.mp3')


				except KeyError:
					print('Sorry! Something unexpected happened, aborting...')

	if condition == 'n':
		print('\nOk! Aborting...')


url = input('Enter playlist URL: ')
condition = input('Continue y/n? ')

reciveVideo(url, condition)
