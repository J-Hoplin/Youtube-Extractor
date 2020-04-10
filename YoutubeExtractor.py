#-*- coding: utf-8 -*-

#This code and description is written by Hoplin
#No matter to use it as non-commercial.
#if there's issue after pip install pytube, install pip install pytube3

import pytube as pt #pip install pytube3
import re
import os
import warnings
import shutil
from moviepy.video.io.VideoFileClip import VideoFileClip
warnings.filterwarnings("ignore")

#Default save directory
programa_dir = os.getcwd()
print("Youtube mp4,mp3 Extractor made by Hoplin.")
print("This program is open source and protected by MIT License.(https://github.com/J-hoplin1/Youtube-Extractor)\n\n\n")
print("Directory will be generated in : ",programa_dir)
YTURL = input("Enter Youtube URL : ")
os.system('cls')
#Check URL Link Pattern
YTURLPattern = re.compile("https\:\/\/www\.youtube\.com\/watch[A-Za-z?=.]*")
ckP = YTURLPattern.match(YTURL)

#if Patter correct
if ckP:
    pass
    YTu = pt.YouTube(YTURL)
    options = YTu.streams

    for ot in range(len(options)):
        # value like this : ['<Stream:', 'itag="18"', 'mime_type="video/mp4"', 'res="360p"', 'fps="30fps"', 'vcodec="avc1.42001E"', 'acodec="mp4a.40.2"', 'progressive="True"', 'type="video">']
        optList = str(options[ot]).split(' ')
        print(ot+1, '. ' + "MIME Type : " + optList[2].split("\"")[1] + " | " + "RES : " + optList[3].split("\"")[1] + " | " + "VCodec : " + optList[5].split("\"")[1] + " | " + "ACodec : " + optList[6].split("\"")[1] + " | " + "Type : " + optList[-1].split("\"")[1] + "\n")
    opNum = int(input("\nEnter option Number : "))
    os.system('cls')
    try:
        print("Downloading files....")
        defaultfilename = options[opNum - 1].default_filename
        os.mkdir(programa_dir+"\\" + defaultfilename.split('.mp4')[0] +"\\")
        regenerateDefaultDir = programa_dir+"\\" + defaultfilename.split('.mp4')[0]
        options[opNum - 1].download(regenerateDefaultDir)
        print("Video file(.mp4) download complete....")
        clip = VideoFileClip(regenerateDefaultDir+"\\"+defaultfilename)
        clip.audio.write_audiofile(regenerateDefaultDir+"\\"+defaultfilename.split('.mp4')[0] + ".mp3")
        print("Music file(.mp3) download complete....")
        print("Download Completed")
    except IndexError as e:
        print("Error : Wrong option number.")
        os.system('cls')
        time.sleep(1.5)
    except FileNotFoundError as w:
        print("Error : Unexpected critical error. Can't re-encode File.")
        os.system('cls')
        time.sleep(1.5)
    except FileExistsError as e:
        print("Error : Already existing directory name - ",defaultfilename.split('.mp4')[0])
#if pattern not correct
else:
    print("Wrong types of Youtube Link. Please check again.")
