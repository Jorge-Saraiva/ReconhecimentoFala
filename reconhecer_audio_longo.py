import speech_recognition as sr
import time

def tratar_audio(rec, audio):
    global acabou
    # tratar o meu audio
    try:
        texto = rec.recognize_google(audio, language="en-US")
        if 'encerrar gravação' in texto:
            print(texto[:-17])
        else:
            print(texto)
        arquivo = open("gravacao_longa.txt", "a")
        arquivo = open("gravacao_longa.txt", "w")
        if 'encerrar gravação' in texto:
            posicao = texto.find('encerrar gravação')
            texto = texto[:posicao]
        else:
            pass
        if "encerrar gravação" in texto:
            acabou = True
        arquivo.write(texto)
        arquivo.close()
        acabou = True
    except:
        print("Não entendi o que você falou")

acabou = False

rec = sr.Recognizer()

with sr.Microphone(device_index=1) as microfone:
    rec.adjust_for_ambient_noise(microfone)
    rec.pause_threshold = 0.8
    # rec.dynamic_energy_adjustment_ratio = 4
    print("Pode começar a falar: \n(para encerrar diga: '\033[31mENCERRAR GRAVAÇÃO\033[m')")


# thread 1
parar_ouvir = rec.listen_in_background(microfone, tratar_audio)

# thread 2
while True:
    time.sleep(0.1)
    if acabou == True:  # vou falar pra ele encerrar a gravação
        break

# thread 1
parar_ouvir(wait_for_stop=False)
