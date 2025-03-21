# Speech2Text - Streamlit Application
Healthcare Translation Web App with Generative AI

## Overview
The **Speech2Text** project is a Streamlit-based web application that converts speech into text using state-of-the-art speech recognition models. The application allows users to upload audio files, record live speech, and transcribe it into text in real time.

## Features
- **Upload Audio Files**: Supports common audio formats (.wav, .mp3, .flac, etc.).
- **Live Speech Recording**: Record audio directly through the web interface.
- **Automatic Speech Recognition (ASR)**: Uses a robust speech-to-text model for transcription.
- **Multilingual Support**: Recognizes speech in multiple languages (if supported by the ASR model).
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
git clone https://github.com/PrabuddhaBanerjee/speech2Text.git
cd speech2Text
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
1. **Upload Audio File**: Select an audio file for transcription.
2. **Live Recording**: Click the 'Record' button to capture speech and transcribe.
3. **View Transcription**: The text output appears on the screen after processing.
4. **Download Transcription**: Save the transcribed text as a file.

## Configuration
- Modify the `config.py` file (if present) to set parameters like language preference, model selection, and output format.

## Dependencies
The `requirements.txt` file includes necessary libraries such as:
```txt
streamlit
speechrecognition
pydub
openai-whisper (if used for ASR)
```

## Deployment
You can deploy the application on platforms like Streamlit Cloud, Heroku, or AWS. For deployment on Streamlit Cloud:
1. Push your changes to GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Connect your repository and deploy.

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


