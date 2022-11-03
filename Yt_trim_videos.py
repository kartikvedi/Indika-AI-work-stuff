# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:00:59 2022

@author: Mudit
"""

# importing necessary liabraries
from pytube import YouTube
import os
import pandas as pd
import moviepy.editor as mp
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import datetime

# reading the datafile into a dataframe
df = pd.read_csv("C:\\Users\\Mudit\\Desktop\\Indika AI\\Rephrase Submission -Final - 133-Trim.csv")
df.head()

# converting the Start Time and End Time into datetime objects
df['Start Time'] = df['Start Time'].str.replace('.',':')
df['End Time'] = df['End Time'].str.replace('.',':')

# downloading the full length videos using pytube
path = "C:\\Users\\Mudit\\Desktop\\Indika AI\\Good_videos"
for i in range (0, df.shape[0]):
    yt = YouTube(df['YouTube Video Link'][i])
    name = str(i) + '.mp4'
    yt.streams.filter(progressive=True).order_by('resolution').desc().first().download(path, filename = name)
    
# creating a function to convert the timestamps into seconds
def conv_to_sec(time):
    date_time = datetime.datetime.strptime(time, "%H:%M:%S")
    a_timedelta = date_time - datetime.datetime(1900, 1, 1)
    seconds = a_timedelta.total_seconds()
    return(seconds)

# cropping the videos based on timestamp
for i in range(0,df.shape[0]):
    initial = "C:\\Users\\Mudit\\Desktop\\Indika AI\\Good_videos\\" + str(i) + ".mp4"
    st = conv_to_sec(df['Start Time'][i])
    et = conv_to_sec(df['End Time'][i])
    final = "C:\\Users\\Mudit\\Desktop\\Indika AI\\Good_videos_final\\" + str(i) + ".mp4"
    ffmpeg_extract_subclip(initial, st, et, targetname = final)