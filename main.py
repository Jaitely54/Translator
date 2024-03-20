import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os

def initialize_recognizer():
    # Creating Recognizer and Microphone instances
    recog = spr.Recognizer()
    mic = spr.Microphone()
    return recog, mic

def capture_voice(recog, mic, prompt_message):
    # Function to capture voice input from the user
    with mic as source:
        print(prompt_message)
        recog.adjust_for_ambient_noise(source, duration=0.2)
        audio = recog.listen(source)
    return audio

def translate_speech(audio, recog, from_lang='en', to_lang='hi'):
    # Translate speech from one language to another
    try:
        sentence = recog.recognize_google(audio)
        print(f"Phrase to be translated: {sentence}")

        translator = Translator()
        translated = translator.translate(sentence, src=from_lang, dest=to_lang)
        return translated.text
    except spr.UnknownValueError:
        print("Unable to understand the input.")
    except spr.RequestError as e:
        print(f"Unable to provide required output: {e}")

def text_to_speech(text, lang='hi'):
    # Convert text to speech in the specified language
    speech = gTTS(text=text, lang=lang, slow=False)
    speech.save("captured_voice.mp3")
    os.system("start captured_voice.mp3")

def main():
    recog, mic = initialize_recognizer()
    print("Speak 'hello' to initiate the translation!")

    # Capturing 'hello' to start the translation process
    hello_audio = capture_voice(recog, mic, "Speak 'hello' to initiate the translation!")
    if 'hello' in recog.recognize_google(hello_audio).lower():
        # If 'hello' is detected, proceed with capturing the next sentence to translate
        sentence_audio = capture_voice(recog, mic, "Speak a sentence to translate...")
        translated_text = translate_speech(sentence_audio, recog)

        if translated_text:
            # If translation is successful, convert the translated text to speech
            text_to_speech(translated_text)

if __name__ == "__main__":
    main()
