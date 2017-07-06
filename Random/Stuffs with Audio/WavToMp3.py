from pydub import AudioSegment

inputFile = "chapter.wav"

#convert to mp3
sound = AudioSegment.from_wav(inputFile)
sound.export("chapter.mp3", format="mp3")