# audio file format
# .mp3 uses lossy compression tech(means loss of data)
# .flac uses loss less compression tech( means no loss of data)
# .wav use save file in uncompressed manner, loss less and large files sizes

import wave
# - Audio signal parameters
# - number of channels
# - sample width
# - framerate/sample_rate: 44,100 hz
# - number of frames
# - values of frame

obj = wave.open("pro_audio.wav" , "rb")
 # rb stands for read binary

print("number of channels", obj.getnchannels())
print("sample width" , obj.getsampwidth())
print("frame rate" , obj.getframerate())
print("number of frames" , obj.getnframes())
print("parameters" , obj.getparams())

t_audio = obj.getnframes() / obj.getframerate()
print("time of the audio :",t_audio)


frame = obj.readframes(-1)
print(type(frame), type(frame[0]))
print(len(frame)/2)

obj.close()
# saving this auido file in a new object
obj_new = wave.open("guddi_audio.wav", "wb")

# Setting the parameters of the new file
obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(16000.0)

# Writing the frames
obj_new.writeframes(frame)

obj_new.close()