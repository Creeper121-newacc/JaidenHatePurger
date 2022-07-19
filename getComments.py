# -*- coding: utf-8 -*-
# @Author: user
# @Date:   2022-07-18 12:57:21
# @Last Modified by:   user
# @Last Modified time: 2022-07-19 13:12:59

from googleapiclient.discovery import build
from pathlib import Path
from sys import executable
from commentThread import *

# this code is pyInstaller boilerplate can ignore
#api_token = '/'.join([str(Path(executable).parent), "api_token.txt"])
api_token = "./api_token.txt"

# get api token from file ./api_token.txt
with open(api_token, "r") as file:
	api_token = file.readline()

# initalizes youtube api
youtube_api = build('youtube', 'v3', developerKey=api_token)


# gets a variable number of comments
# items is the number of comments
def getComments(items):
	if items <= 100:
		video_response = CommentThreadList(youtube_api.commentThreads().list(
			part='id,snippet,replies',
  			videoId="36QMyiRAv-Y",
  			maxResults=items
		).execute())
		return video_response
	nextPageToken = ""

	if items > 100:
		result = []
		iterations = items // 100
		remaining = items % 100
		for iteration in range(0, iterations - 1):
			if iteration > 1:
				video_response = CommentThreadList(youtube_api.commentThreads().list(
					part='id,snippet,replies',
	  				videoId="36QMyiRAv-Y",
	  				maxResults=100
				).execute())
			else:
				video_response = CommentThreadList(youtube_api.commentThreads().list(
					part='id,snippet,replies',
	  				videoId="36QMyiRAv-Y",
	  				maxResults=100,
	  				pageToken=nextPageToken
				).execute())
			nextPageToken = video_response.nextPageToken
			result.append(video_response)

		video_response = CommentThreadList(youtube_api.commentThreads().list(
			part='id,snippet,replies',
  			videoId="36QMyiRAv-Y",
  			maxResults=remaining
		).execute())
		result.append(video_response)
		return result
