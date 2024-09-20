# Sarvam Voice Agent

This project implements an interactive voice agent using the Sarvam AI API. The agent can understand and respond in multiple languages, including English, Hindi, and Odia. It supports text input and generates both text and audio responses.

## Features

- Multi-language support (English, Hindi, Odia)
- Text-to-Speech conversion
- Language translation
- Interactive command-line interface
- Audio response generation

## Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/deepak-lenka/sarvam_voice_agent.git
   cd sarvam_voice_agent
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install requests
   ```

## Usage

1. Ensure you have a valid Sarvam API key. The API key is currently set in the `API_KEY` variable in the `voice_agent.py` script. For security reasons, consider using environment variables to store your API key in a production environment.

2. Run the script:
   ```
   python voice_agent.py
   ```

3. Follow the on-screen prompts:
   - Select a language by typing 'en' for English, 'hi' for Hindi, or 'od' for Odia.
   - Type your message when prompted.
   - The agent will respond with text and generate an audio file.
   - To hear the audio response, play the generated WAV file (e.g., `response_en.wav`).

4. Type 'quit' at any prompt to exit the program.

## File Structure

- `voice_agent.py`: The main script containing the voice agent implementation.
- `response_*.wav`: Audio files generated for each response (e.g., `response_en.wav` for English responses).

## Functions

- `translate_text(text, source_lang, target_lang)`: Translates text between languages.
- `text_to_speech(text, language_code)`: Converts text to speech.
- `process_input(input_text, language_code)`: Processes user input and generates responses.
- `save_audio(audio_data, filename)`: Saves audio data as a WAV file.

## Supported Languages

- English (en-IN)
- Hindi (hi-IN)
- Odia (od-IN)

## Error Handling

The script includes basic error handling for API requests. If an error occurs during translation or text-to-speech conversion, an error message will be displayed.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Disclaimer

This project uses the Sarvam AI API. Make sure you comply with Sarvam's terms of service and data usage policies when using this script.