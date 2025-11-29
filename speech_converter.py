import speech_recognition as sr
import sys
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import os
import time

def get_audio_input_sd(filename="temp.wav", duration=7, fs=16000):
    """
    Records audio using sounddevice and saves to a file.
    """
    print(f"\nListening for {duration} seconds... (Speak now)")
    try:
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()  # Wait until recording is finished
        wav.write(filename, fs, recording)
        return filename
    except Exception as e:
        print(f"Error recording audio: {e}")
        return None

def recognize_speech_from_file(recognizer, audio_file, language_code):
    """
    Recognizes speech from an audio file.
    """
    try:
        with sr.AudioFile(audio_file) as source:
            # Use the first 0.5 seconds for noise calibration
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.record(source)
        
        print("Recognizing...")
        text = recognizer.recognize_google(audio, language=language_code)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None
    except Exception as e:
        print(f"Error processing audio file: {e}")
        return None

def main():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    print("--- Speech to Text Converter (SoundDevice) ---")
    print("1. English")
    print("2. Hindi")
    
    while True:
        choice = input("\nSelect Language (1/2) or 'q' to quit: ").strip().lower()
        
        if choice == 'q':
            print("Exiting...")
            break
        
        if choice == '1':
            language_code = 'en-IN'
            lang_name = "English"
        elif choice == '2':
            language_code = 'hi-IN'
            lang_name = "Hindi"
        else:
            print("Invalid choice. Please try again.")
            continue

        print(f"\nSelected Language: {lang_name}")
        
        while True:
            # Record audio
            audio_file = get_audio_input_sd()
            
            if audio_file:
                text = recognize_speech_from_file(recognizer, audio_file, language_code)
                if text:
                    print(f"\n> Recognized Text: {text}")
                
                # Cleanup
                if os.path.exists(audio_file):
                    os.remove(audio_file)
            
            # Ask to continue or switch language
            cont = input("\nPress Enter to continue listening, 'b' to change language, orrr 'q' to quit: ").strip().lower()
            if cont == 'q':
                sys.exit()
            elif cont == 'b':
                break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
