import wave
import contextlib

# assign the file to the audio source
audio = 'C:\Users\wyatt\Desktop\chapter.wav'

#read the file
with contextlib.closing(wave.open(audio, 'r')) as f:
    #get the number of frames in the file
    frames = f.getnframes()
    #get the frame rate
    rate = f.getframerate()
    #calculate duration
    duration = frames / float(rate)
    #seconds of length
    print duration,'seconds long'

    #calculate minutes
    minutes = duration / 60
    print float(minutes)