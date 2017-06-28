# import wave, contextlib
from tinytag import TinyTag


# assign the file to the audio source
#audio = 'C:/Users/wyatt/Downloads/chapter.mp3'
audio = 'C:/Users/wyatt/Downloads/chapter.mp3'


tag = TinyTag.get(audio)
print (float(tag.filesize) / 1000000), "MB"
print ""
print tag
print ""
print 'It is %f seconds long.' % tag.duration
print ""

# # read the file
# with contextlib.closing(wave.open(audio, 'r')) as f:
#     #get the number of frames in the file
#     frames = f.getnframes()
#     #get the frame rate
#     rate = f.getframerate()
#     #calculate duration
#     duration = frames / float(rate)
#     #seconds of length
#     print duration,'Seconds long'
#
#     #calculate minutes
#     minutes = duration / 60
#     print float(minutes), "Minutes long"
#     print ""
#     print f.tell()
#     f.close()



# wavFile = wave.open(audio)
# length = wavFile.getnframes()

# for i in range(0, length):
#     waveData = wavFile.readframes(1)
#     data = struct.unpack("<h", waveData)
    # print int(data[0])
