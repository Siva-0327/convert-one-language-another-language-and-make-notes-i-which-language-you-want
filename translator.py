import speech_recognition as sr
import pyttsx3
from googletrans import Translator
'''1.Enlish = 'en'
2.Telugu = 'te'
3.Hindi = 'hi'
4.Spanish = 'spa'
5.Tamil = 'tam'
6.Malayalam = 'mal'
7.urdu = 'urd'
8.French = 'fra' (Note: "fre" is also valid)
9.German ='deu' (Note: "ger" is also valid)
10.Ita1ian = 'ita'
11.Chinese = 'zho'
12.Japanese = 'jpn'
13.Russian ='rus'
14.Arabic = 'ara'    '''


word = sr.Recognizer()

def speech():
    with sr.Microphone() as source:
        print("Listening....")
        audio = word.listen(source)
    return audio

def speech_to_text(audio, choose):
    try:
        text = word.recognize_google(audio)

        if choose == 'Telugu':
            translator = Translator()
            translation = translator.translate(text,dest='te')
            converter = translation.text
            print(converter)
        elif choose == 'English':
            translator = Translator()
            translation = translator.translate(text,dest='en')
            converter = translation.text
            print(converter)            
        elif choose == 'Hindi':
            translator = Translator()
            translation = translator.translate(text,dest='hi')
            converter = translation.text
            print(converter)
        elif choose == 'Malayalam':
            translator = Translator()
            translation = translator.translate(text,dest='ml')
            converter = translation.text
            print(converter)
        elif choose == 'Tamil':
            translator = Translator()
            translation = translator.translate(text,dest='ta')
            converter = translation.text
            print(converter)
        elif choose == 'Russian':
            translator = Translator()
            translation = translator.translate(text,dest='ru')
            converter = translation.text
            print(converter)
        elif choose == 'Japanese':
            translator = Translator()
            translation = translator.translate(text,dest='ja')
            converter = translation.text
            print(converter)
        elif choose == 'Chinese':
            translator = Translator()
            translation = translator.translate(text,dest='zh-CN')
            print(translation.text)
        elif choose == 'urdu':
            translator = Translator()
            translation = translator.translate(text,dest='ur')
            print(translation.text)
        elif choose == 'French':
            translator = Translator()
            translation = translator.translate(text,dest='fr')
            print(translation.text)
        elif choose == 'Italian':
            translator = Translator()
            translation = translator.translate(text,dest='it')
            converter = translation.text
            print(converter)
        elif choose == 'German':
            translator = Translator()
            translation = translator.translate(text,dest='de')
            print(translation.text)
        elif choose == 'Spanish':
            translator = Translator()
            translation = translator.translate(text,dest='es')
            converter = translation.text
            print(converter)
        elif choose == 'Arabic':
            translator = Translator()
            translation = translator.translate(text,dest='ar')
            converter = translation.text
            print(converter)
        else:
            print("the language is not avalible sorry as soon as possible we will add this language")   

        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 160)
        engine.setProperty('volume', 100)
        engine.say(text)
        engine.runAndWait()
        return text,converter

    except sr.UnknownValueError:
        print("Sorry, I can't understand.")
    except Exception as e:
        print(f"Something went wrong: {str(e)}")

def save_to_file(converter, filename):
    try:
        text, converted_text = converter
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(converted_text)
            #file.write(text)
        print(f"Text saved to {filename}")
    except Exception as e:
        print(f"Error saving to file: {str(e)}")

def main():
    choose = input("Choose the language of the notes you want (Telugu/English/Malayalam/Hindi/Tamil/French/Italian/Chinese/German/Japanese/Arabic/Russian/urdu): ")
    audio = speech()
    converter = speech_to_text(audio, choose)
    if converter:
        save_to_file(converter, 'saved.txt')

main()
