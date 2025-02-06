import speech_recognition as sr
for index, name in enumerate(sr.Microphone.list_working_microphones()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))