import os
import simpleaudio as sa
import wave
from pathlib import Path
import json


# Load the mapping from a JSON file
with open('audio_mapping.json', 'r', encoding='utf-8') as file:
    audio_mapping = json.loads(file.read())

def build_file(string):
    input_files = []
    
    # build input files
    for i in range(len(string)):
        if i < len(string) - 1 and string[i:i+2] in audio_mapping:
            input_files.append(audio_mapping[string[i:i+2]])
        elif string[i] in audio_mapping:
            input_files.append(audio_mapping[string[i]])
            
    combine_wav_files(input_files=input_files, output_file=Path(__file__).resolve().parent / 'output.wav') # save in the script's directory 
            
def combine_wav_files(input_files, output_file):
    # open the first input file to get audio parameters
    with wave.open(input_files[0], 'rb') as first_file:
        params = first_file.getparams()
        
    # create a new WAV file for the combined audio
    with wave.open(str(output_file), 'wb') as output:
        output.setparams(params)
    
        for file_name in input_files:
            with wave.open(file_name, 'rb') as input_file:
                output.writeframes(input_file.readframes(input_file.getnframes()))
    
    print("WAV files combined successfully.")

# Example usage
ipa_input = input("Input IPA transcription: ")
build_file(ipa_input)
