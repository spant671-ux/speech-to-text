# Speech-to-Text Converter (English & Hindi)

A Python script that converts spoken English and Hindi into text using Google's Web Speech API.

## 📚 Libraries Used

This project relies on the following powerful Python libraries:

1.  **[SpeechRecognition](https://pypi.org/project/SpeechRecognition/)**: The core library used to send audio data to Google's Web Speech API and receive the text transcript.
2.  **[sounddevice](https://pypi.org/project/sounddevice/)**: Used for recording audio from the microphone. It was chosen over `PyAudio` for better compatibility with newer Python versions.
3.  **[numpy](https://pypi.org/project/numpy/)**: Used by `sounddevice` to handle audio data arrays efficiently.
4.  **[scipy](https://pypi.org/project/scipy/)**: Used to save the recorded numpy arrays as `.wav` files that `SpeechRecognition` can process.

## 🛠️ Installation

To run this project, you need to install the dependencies:

```bash
pip install SpeechRecognition sounddevice numpy scipy
```

## 🚀 Usage -->

1.  Run the script:
    ```bash
    python speech_converter.py
    ```
2.  Select your language:
    - Enter `1` for **English**.
    - Enter `2` for **Hindi**.
3.  Speak clearly into your microphone. The script will record for **7 seconds**.
4.  Wait a moment for the text to appear on the screen!

## 📝 How It Works

1.  **Recording**: The script uses `sounddevice` to record audio at **16kHz** (optimized for speech) for 7 seconds.
2.  **Saving**: The audio is temporarily saved as a `temp.wav` file using `scipy`.
3.  **Recognition**: `SpeechRecognition` reads the file, adjusts for ambient noise, and sends it to Google's API.
4.  **Output**: The recognized text is printed to the console.
