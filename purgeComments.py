# -*- coding: utf-8 -*-
# @Author: user
# @Date:   2022-07-18 12:41:20
# @Last Modified by:   user
# @Last Modified time: 2022-07-19 13:03:44

from getComments import *
from dateutil.parser import parse
from dateutil.tz import tzlocal
#from detoxify import Detoxify

""" def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
"""

#detoxifier = Detoxify(checkpoint="ai_ckpt/original.ckpt")

# this is a toxic spammers 𝘸𝘰𝘳𝘴𝘵 nightmare come true


def getCommentsToPurge():
    print(len(getComments(69).items))

if __name__ == '__main__':
    getCommentsToPurge()