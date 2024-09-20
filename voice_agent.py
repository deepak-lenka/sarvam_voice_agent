import requests
import json
import base64
import wave
import os

# Replace with your actual Sarvam API key
API_KEY = "YOUR_API_KEY_HERE"

def translate_text(text, source_lang, target_lang):
    print(f"Translating from {source_lang} to {target_lang}")
    url = "https://api.sarvam.ai/translate"
    headers = {
        "Content-Type": "application/json",
        "API-Subscription-Key": API_KEY
    }
    payload = {
        "input": text,
        "source_language_code": source_lang,
        "target_language_code": target_lang,
        "speaker_gender": "Female",
        "mode": "formal",
        "model": "mayura:v1",
        "enable_preprocessing": True
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()
        return result["translated_text"]
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during translation: {e}")
        return None

def text_to_speech(text, language_code):
    print("Converting text to speech")
    url = "https://api.sarvam.ai/text-to-speech"
    headers = {
        "Content-Type": "application/json",
        "API-Subscription-Key": API_KEY
    }
    payload = {
        "inputs": [text],
        "target_language_code": language_code,
        "speaker": "meera",
        "pitch": 1,
        "pace": 1.65,
        "loudness": 1.5,
        "speech_sample_rate": 8000,
        "enable_preprocessing": True,
        "model": "bulbul:v1"
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        json_response = response.json()
        audio_data = base64.b64decode(json_response["audios"][0])
        return audio_data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during text-to-speech: {e}")
        return None

def process_input(input_text, language_code):
    # Generate response based on input and language
    if "hello" in input_text.lower() or "namaste" in input_text.lower() or "namaskar" in input_text.lower():
        if language_code == "en-IN":
            return "Hello! How can I assist you today?"
        elif language_code == "hi-IN":
            return translate_text("Hello! How can I assist you today?", "en-IN", "hi-IN")
        elif language_code == "od-IN":
            return translate_text("Hello! How can I assist you today?", "en-IN", "od-IN")
    elif "goodbye" in input_text.lower():
        if language_code == "en-IN":
            return "Thank you for using our service. Goodbye!"
        elif language_code == "hi-IN":
            return translate_text("Thank you for using our service. Goodbye!", "en-IN", "hi-IN")
        elif language_code == "od-IN":
            return translate_text("Thank you for using our service. Goodbye!", "en-IN", "od-IN")
    else:
        response = f"You said: '{input_text}'. How can I help you with that?"
        if language_code == "en-IN":
            return response
        elif language_code == "hi-IN":
            return translate_text(response, "en-IN", "hi-IN")
        elif language_code == "od-IN":
            return translate_text(response, "en-IN", "od-IN")

def save_audio(audio_data, filename):
    with wave.open(filename, "wb") as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(8000)  # Sample rate as per API
        wav_file.writeframes(audio_data)
    print(f"Audio response saved as '{filename}'")

def main():
    print("Welcome to the Interactive Sarvam Voice Agent for Odia, Hindi, and English!")
    print("Please type your messages. Use 'en' for English, 'hi' for Hindi, or 'od' for Odia.")
    print("Type 'quit' to exit.")
    
    while True:
        language_input = input("Select language (en/hi/od): ").lower()
        if language_input == 'quit':
            print("Thank you for using the Sarvam Voice Agent. Goodbye!")
            break
        
        if language_input == 'en':
            language_code = 'en-IN'
        elif language_input == 'hi':
            language_code = 'hi-IN'
        elif language_input == 'od':
            language_code = 'od-IN'
        else:
            print("Invalid language selection. Please choose 'en', 'hi', or 'od'.")
            continue
        
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Thank you for using the Sarvam Voice Agent. Goodbye!")
            break
        
        response_text = process_input(user_input, language_code)
        print(f"Agent: {response_text}")
        
        audio_response = text_to_speech(response_text, language_code)
        if audio_response:
            filename = f"response_{language_input}.wav"
            save_audio(audio_response, filename)
            print(f"To hear the response, play the '{filename}' file.")
        else:
            print("Failed to generate audio response.")

if __name__ == "__main__":
    main()