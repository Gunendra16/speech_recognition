# Real-Time Speech Recognition and Podcast Summarization

This project leverages state-of-the-art technologies to provide real-time speech recognition, sentiment analysis, and podcast summarization using OpenAI's GPT models, AssemblyAI, and Listen Notes.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [API Keys](#api-keys)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project enables real-time speech recognition and sentiment analysis, alongside providing podcast summaries. It is built using a combination of advanced AI models and APIs to ensure high accuracy and efficiency.

## Features

- **Real-Time Speech Recognition**: Converts spoken language into text using AssemblyAI's real-time transcription API.
- **Sentiment Analysis**: Analyzes the sentiment of the recognized speech using OpenAI's models.
- **Podcast Summarization**: Summarizes podcasts using Listen Notes API and displays them in a user-friendly format.
- **Integration with OpenAI**: Utilizes OpenAI's GPT models for various natural language processing tasks.

## Technologies Used

- **Python**
- **Streamlit**: For the web application interface
- **OpenAI API**: For natural language processing and sentiment analysis
- **AssemblyAI**: For real-time speech recognition
- **Listen Notes API**: For podcast summarization
- **PyAudio**: For capturing audio input

## Setup and Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/Gunendra16/Real-Time-Speech-Recognition.git
   cd Real-Time-Speech-Recognition
   ```

2. **Create a Virtual Environment**:
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Set Up API Keys**:
   - Obtain API keys from OpenAI, AssemblyAI, and Listen Notes.
   - Create a file named `api_secrets.py` and add your API keys:
     ```python
     API_KEY_ASSEMBLYAI = 'your_assemblyai_api_key'
     API_KEY_LISTENNOTES = 'your_listennotes_api_key'
     API_KEY_OPENAI = 'your_openai_api_key'
     ```

## Usage

1. **Run the Streamlit Application**:
   ```sh
   streamlit run main.py
   ```

2. **Interacting with the App**:
   - Enter the episode ID of a podcast in the sidebar to get a summary.
   - Speak into your microphone to get real-time transcription and sentiment analysis.

## API Keys

- **AssemblyAI**: [Get your API key](https://www.assemblyai.com/)
- **Listen Notes**: [Get your API key](https://www.listennotes.com/api/)
- **OpenAI**: [Get your API key](https://beta.openai.com/signup/)

## Contributing

Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are warmly welcome.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/fooBar`).
3. Commit your changes (`git commit -am 'Add some fooBar'`).
4. Push to the branch (`git push origin feature/fooBar`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
