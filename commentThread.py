# -*- coding: utf-8 -*-
# @Author: user
# @Date:   2022-07-19 12:30:07
# @Last Modified by:   user
# @Last Modified time: 2022-07-19 13:13:38


# this is an abstraction for the CommentThread resource, see: https://developers.google.com/youtube/v3/docs/commentThreads
class CommentThread:
	def __init__(self, commentThread: dict):
		self.topLevelComment = commentThread["snippet"]["topLevelComment"]
		self.totalReplyCount = commentThread["snippet"]["totalReplyCount"]
		self.replies = commentThread["replies"]["comments"]
		self.publishedAt = commentThread["snippet"]["topLevelComment"]["publishedAt"]

# this is an abstraction for a list of CommentThreads, see: https://developers.google.com/youtube/v3/docs/commentThreads/list
class CommentThreadList:
	def __init__(self, commentThreadList: dict):
		self.nextPageToken = commentThreadList["nextPageToken"]
		self.results = commentThread["pageInfo"]["totalResults"]
		self.items = [CommentThread(item) for item in commentThreadList["items"]]