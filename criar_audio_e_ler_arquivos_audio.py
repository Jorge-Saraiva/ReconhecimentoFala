import speech_recognition as sr

rec = sr.Recognizer()

with sr.Microphone(device_index=1) as microfone:
    rec.adjust_for_ambient_noise(microfone)
    print("Pode começar a falar")
    audio = rec.listen(microfone)

# salvar o audio
with open("audio.wav", "wb") as arquivo:
    arquivo.write(audio.get_wav_data())
# raw
# wav
# aiff
# flac

rec = sr.Recognizer()

with sr.AudioFile("audio.wav") as arquivo_audio:
    audio = rec.record(arquivo_audio)
    texto = rec.recognize_google(audio, language="en-US")
    print(texto)

arquivo = open("gravacao.txt", "a")
arquivo = open("gravacao.txt", "w")
arquivo.write(texto)
arquivo.close()


