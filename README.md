# SpeechTranscription - Streamlit Application
Healthcare Translation Web App with Generative AI

## Overview
The **SpeechTranscription** project is a Streamlit-based web application that converts speech into text using state-of-the-art speech recognition models. The application allows users to upload audio files, record live speech, and transcribe it into text in real time.

## Features
- **Playback Audio Files**: Playback common audio format (.mp3) after transcription.
- **Live Speech Recording**: Record audio directly through the web interface.
- **Automatic Speech Recognition (ASR)**: Uses a robust speech-to-text model for transcription.
- **Multilingual Support**: Recognizes speech in multiple languages.
- **User-friendly UI**: Built with Streamlit for easy interaction.

## Installation
To set up and run the application, follow these steps:

### Prerequisites
Ensure you have the following installed:
- Python 3.8 or later
- pip (Python package manager)
- Virtual environment (optional but recommended)

### Clone the Repository
```bash
git clone https://github.com/PrabuddhaBanerjee/SpeechTranscription.git
cd SpeechTranscription
```

### Create and Activate Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
### Running the Application
```bash
streamlit run app.py
```

### Application Interface
1. **Speakers Language**: Select the choice of language of Speaker
2. **Translated Language**: Select the choice of language for Transcription
3. **Start Listening**: Click the 'Start Listening' button to capture speech and transcribe.
4. **Stop Listening**: Click the 'Stop Listening' button to stop capturing speech, to save the last transcribe and to play the last trancribe.
5. **Playback**: To save the transcribed audio as a file and play it back.
6. **View Transcription**: The text output appears on the screen after processing.

## Configuration
- Modify the `config.py` file (if present) to set parameters like language preference, model selection, and output format.

## Dependencies
The `requirements.txt` file includes necessary libraries such as:
```txt
streamlit
websockets
asyncio
googletrans
speech_recognition
gtts
pipwin
assemblyai
```

## Deployment
The application has been deployed on platform render.com for utilization.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes and push to GitHub.
4. Create a Pull Request (PR).

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Contact
For queries, reach out to [Prabuddha Banerjee](https://github.com/PrabuddhaBanerjee).


