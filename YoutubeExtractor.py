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
from pytube.exceptions import RegexMatchError
from urllib.request import HTTPError
import time
import sys
warnings.filterwarnings("ignore")
loop = True


while loop:
    loop_inner = True
    # Default save directory
    programa_dir = os.getcwd()
    print("Youtube mp4,mp3 Extractor made by Hoplin.")
    print("This program is open source and protected by MIT License.(https://github.com/J-hoplin1/Youtube-Extractor)")
    print("Enter 'exit' to exit.\n\n\n")
    print("Directory will be generated in : ", programa_dir)
    YTURL = input("Enter Youtube URL : ")
    if YTURL == 'exit':
        loop = False
    else:
        os.system('cls')
        # Check URL Link Pattern
        YTURLPattern = re.compile("https\:\/\/www\.youtube\.com\/watch[A-Za-z0-9?=.&_#$]*") # Youtube Link Regex Boolean
        ckP = YTURLPattern.match(YTURL)

        # if Patter correct
        if ckP:
            try:
                while loop_inner:
                    print("Is this URL you want to extract? : ", YTURL, "\n\n")
                    yOrn = input("Press 'n' key to re-enter. Or press 'y' key to move on to the next section. : ")
                    if yOrn == 'n' or yOrn == "N":
                        os.system('cls')
                        loop_inner = False
                    elif yOrn == 'y' or yOrn == "Y":
                        loop_inner = False
                        os.system('cls')
                        try:
                            YTu = pt.YouTube(YTURL)
                            options = YTu.streams

                            for ot in range(len(options)):
                                # value like this : ['<Stream:', 'itag="18"', 'mime_type="video/mp4"', 'res="360p"', 'fps="30fps"', 'vcodec="avc1.42001E"', 'acodec="mp4a.40.2"', 'progressive="True"', 'type="video">']
                                optList = str(options[ot]).split(' ')
                                print(ot + 1,
                                      '. ' + "MIME Type : " + optList[2].split("\"")[1] + " | " + "RES : " +
                                      optList[3].split("\"")[
                                          1] + " | " + "VCodec : " + optList[5].split("\"")[1] + " | " + "ACodec : " +
                                      optList[6].split("\"")[
                                          1] + " | " + "Type : " + optList[-1].split("\"")[1])

                            print("\nACodec False means, that option can't download Audio(mp3) files.")
                            print("VCodec False means, that option can't download Video(mp4) files\n")
                            print("Recommend to download - VCodec : avc1 , ACodec : mp4a option")
                            opNum = int(input("\nEnter option Number : "))
                            os.system('cls')
                            print("Downloading files....")
                            defaultfilename = options[opNum - 1].default_filename
                            os.mkdir(programa_dir + "\\" + defaultfilename.split('.mp4')[0] + "\\")
                            regenerateDefaultDir = programa_dir + "\\" + defaultfilename.split('.mp4')[0]
                            options[opNum - 1].download(regenerateDefaultDir)
                            print("Video file(.mp4) download complete....")
                            clip = VideoFileClip(regenerateDefaultDir + "\\" + defaultfilename)
                            clip.audio.write_audiofile(
                                regenerateDefaultDir + "\\" + defaultfilename.split('.mp4')[0] + ".mp3")
                            print("Music file(.mp3) download complete....")
                            print("Download Completed")
                            os.system('cls')
                        except IndexError as e:
                            print("Error : Wrong option number.")
                            time.sleep(2.5)
                            os.system('cls')
                        except FileNotFoundError as w:
                            print("Error : Unexpected critical error. Can't re-encode File.")
                            time.sleep(2.5)
                            os.system('cls')
                        except FileExistsError as e:
                            print("Error : Already existing directory name - ", defaultfilename.split('.mp4')[0])
                            time.sleep(2.5)
                            os.system('cls')
                        except HTTPError as e:
                            print("Error : Selected option has been blocked.")
                            time.sleep(2.5)
                            os.system('cls')
                        # Exception when ACodec = False
                        except AttributeError as e:
                            print("Download Completed")
                            time.sleep(2.5)
                            os.system('cls')
                        # Exception when download webm or ACodec
                        except KeyError as e:
                            print("Download Completed")
                            time.sleep(2.5)
                            os.system('cls')
                        except RegexMatchError as e:
                            print("Error : Unable to open URL. Check your URL again.")
                            time.sleep(2.5)
                            os.system('cls')
                        except EOFError as e:
                            print("Error : Unexpected Error....")
                            time.sleep(2.5)
                            os.system('cls')
                        except KeyboardInterrupt as e:
                            print("Error : Keyboard hit has been interrupted! Did you entered Ctrl + C?")
                            time.sleep(2.5)
                            os.system('cls')

                    else:
                        print("You entered wrong option. Please give value y or n\n\n")

            except EOFError as e:
                print("Error : Unexpected Error....")
                time.sleep(2.5)
                os.system('cls')
            except KeyboardInterrupt as e:
                print("Error : Keyboard hit has been interrupted! Did you entered Ctrl + C?")
                time.sleep(2.5)
                os.system('cls')
        # if pattern not correct
        else:
            print("Wrong types of Youtube Link. Please check again.")
            time.sleep(2.5)
            os.system('cls')
