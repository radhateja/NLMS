# import required libraries
from pydub import AudioSegment
from pydub.playback import play
import numpy as np

#wav_file_1 = AudioSegment.from_file("noice.wav")
wav_file_2 = AudioSegment.from_file("speech.wav")
wav_file_2 = np.random.normal(0,1,len(speech.wav))
# Combine the two audio files
wav_file_3 = wav_file_1 + wav_file_2

# play the sound
play(wav_file_3)

