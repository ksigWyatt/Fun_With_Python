# import wave, contextlib
import os
from tinytag import TinyTag


# assign the file to the audio source
audio = 'chapter.wav' # hash = 2569318  2454630 2614374
# audio = 'C:/Users/wyatt/Desktop/text.wav'


file = TinyTag.get(audio)
print (float(file.filesize) / 1000000), "MB"
print ""
print file.artist
print ""
print 'It is %f seconds long.' % file.duration
print "The hash value is", file.__hash__()

print ""

wav = 'chapter.mp3' #output.wav hash = 2569339
filez = TinyTag.get(wav)
print (float(filez.filesize) / 1000000), "MB"
print ""
print filez.artist
print ""
print 'It is %f seconds long.' % filez.duration
print "The hash value is", filez.__hash__()


os.remove("output.wav")
print("File Removed!")