from pydub import AudioSegment

sound1 = AudioSegment.from_wav("en-x-demo2_ulb_b42_mrk_c06_v01-03_t11.wav")
sound2 = AudioSegment.from_wav("en-x-demo2_ulb_b42_mrk_c06_v04-06_t08.wav")

combined_sounds = sound1 + sound2
combined_sounds.export("output.wav", format="wav")