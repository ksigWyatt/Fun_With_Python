import mad


# how to find the length of an audio file
mf = mad.MadFile("\Uploads\79862bbc-5aa2-11e7-907b-a6006ad3dba0\chapter.wav")
track_length_in_milliseconds = mf.total_time()