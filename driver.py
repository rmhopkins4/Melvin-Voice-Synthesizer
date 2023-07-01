import os
import simpleaudio as sa
import wave
from pathlib import Path

# Define the mapping between characters and audio files
audio_mapping = {
        # vowels
        'i': 'sounds/vowels/close_front_unrounded.wav',
        'y': 'sounds/vowels/close_front_rounded.wav',
        'ɨ': 'sounds/vowels/close_central_unrounded.wav',
        'ʉ': 'sounds/vowels/close_central_rounded.wav',
        'ɯ': 'sounds/vowels/close_back_unrounded.wav',
        'u': 'sounds/vowels/close_back_rounded.wav',
        'ɪ': 'sounds/vowels/near-close_front_unrounded.wav',
        'ʏ': 'sounds/vowels/near-close_front_rounded.wav',
        'ʊ': 'sounds/vowels/near-close_near-back_rounded.wav',
        'e': 'sounds/vowels/close-mid_front_unrounded.wav',
        'ø': 'sounds/vowels/close-mid_front_rounded.wav',
        'ɘ': 'sounds/vowels/close-mid_central_unrounded.wav',
        'ɵ': 'sounds/vowels/close-mid_central_rounded.wav',
        'ɤ': 'sounds/vowels/close-mid_back_unrounded.wav',
        'o': 'sounds/vowels/close-mid_back_rounded.wav',
        'e̞': 'sounds/vowels/mid_front_unrounded.wav',
        'ø̞': 'sounds/vowels/mid_front_rounded.wav',
        'ə': 'sounds/vowels/mid_central.wav',
        'ɤ̞': 'sounds/vowels/mid_back_unrounded.wav',
        'o̞': 'sounds/vowels/mid_back_rounded.wav',
        'ɛ': 'sounds/vowels/open-mid_front_unrounded.wav',
        'œ': 'sounds/vowels/open-mid_front_rounded.wav',
        'ɜ': 'sounds/vowels/open-mid_central_unrounded.wav',
        'ɞ': 'sounds/vowels/open-mid_central_rounded.wav',
        'ʌ': 'sounds/vowels/open-mid_back_unrounded.wav',
        'ɔ': 'sounds/vowels/open-mid_back_rounded.wav',
        'æ': 'sounds/vowels/near-open_front_unrounded.wav',
        'ɐ': 'sounds/vowels/near-open_central.wav',
        'a': 'sounds/vowels/open_front_unrounded.wav',
        'ɶ': 'sounds/vowels/open_front_rounded.wav',
        'ä': 'sounds/vowels/open_central_unrounded.wav',
        'ɑ': 'sounds/vowels/open_back_unrounded.wav',
        'ɒ': 'sounds/vowels/open_back_rounded.wav',
        'ɚ': 'sounds/vowels/r-colored.wav',
        # consonants
            # pulmonic
        'm': 'sounds/consonants/voiced_bilabial_nasal.wav',
        'ɱ': 'sounds/consonants/voiced_labiodental_nasal.wav',
        'n̼': '',
        'n': 'sounds/consonants/voiced_alveolar_nasal.wav',
        'ɳ': '',
        'ɲ': '',
        'ŋ': 'sounds/consonants/voiced_velar_nasal.wav',
        'ɴ': '',
        'p': 'sounds/consonants/voiceless_bilabial_plosive.wav',
        'b': 'sounds/consonants/voiced_bilabial_plosive.wav',
        't̼': '',
        'd̼': '',
        't̪': '',
        'd̪': '',
        't': 'sounds/consonants/voiceless_alveolar_plosive.wav',
        'd': 'sounds/consonants/voiced_alveolar_plosive.wav',
        'ʈ': '',
        'ɖ': '',
        'c': '',
        'ɟ': '',
        'k': 'sounds/consonants/voiceless_velar_plosive.wav',
        'g': 'sounds/consonants/voiced_velar_plosive.wav',
        'q': '',
        'ɢ': '',
        'ʡ': '',
        'ʔ': '',
        't̪s̪': '',
        'd̪z̪': '',
        'ts': '',
        'dz': '',
        'tʃ': 'sounds/consonants/voiceless_postalveolar_affricate.wav',
        'dʒ': 'sounds/consonants/voiced_postalveolar_affricate.wav',
        'tʂ': '',
        'dʐ': '',
        'tɕ': '',
        'dʑ': '',
        'pɸ': '',
        'bβ': '',
        'p̪f': '',
        'b̪v': '',
        't̪θ': '',
        'd̪ð': '',
        'tɹ̝̊': '',
        'dɹ̝': '',
        't̠ɹ̠̊˔': '',
        'd̠ɹ̠˔': '',
        'cç': '',
        'ɟʝ': '',
        'kx': '',
        'ɡɣ': '',
        'qχ': '',
        'ɢʁ': '',
        'ʡʜ': '',
        'ʡʢ': '',
        'ʔh': '',
        's': 'sounds/consonants/voiceless_alveolar_fricative.wav',
        'z': 'sounds/consonants/voiced_alveolar_fricative.wav',
        'ʃ': 'sounds/consonants/voiceless_postalveolar_fricative.wav',
        'ʒ': 'sounds/consonants/voiced_postalveolar_fricative.wav',
        'ʂ': '',
        'ʐ': '',
        'ɕ': '',
        'ʑ': '',
        'ɸ': '',
        'β': '',
        'f': 'sounds/consonants/voiceless_labiodental_fricative.wav',
        'v': 'sounds/consonants/voiced_labiodental_fricative.wav',
        'θ̼': '',
        'ð̼': '',
        'θ': 'sounds/consonants/voiceless_dental_fricative.wav',
        'ð': 'sounds/consonants/voiced_dental_fricative.wav',
        'θ̠': '',
        'ð̠': '',
        'ɹ̠̊˔': '',
        'ɹ̠˔': '',
        'ç': '',
        'ʝ': '',
        'x': '',
        'ɣ': '',
        'χ': '',
        'ʁ': '',
        'ħ': '',
        'ʕ': '',
        'h': 'sounds/consonants/voiceless_glottal_fricative.wav',
        'ɦ': '',
        'β̞': '',
        'ʋ': '',
        'ð̞': '',
        'ɹ': 'sounds/consonants/voiced_alveolar_approximant.wav',
        'ɹ̠': '',
        'ɻ': '',
        'j': 'sounds/consonants/voiced_palatal_approximant.wav',
        'ɰ': '',
        'ʁ̞': '',
        'ⱱ': '',
        'ɾ': '',
        'ɽ': '',
        'ʡ̆': '',
        'ʙ̥': '',
        'ʙ': '',
        'r̥': '',
        'r': '',
        'r̠': '',
        'ɽr': '',
        'ʀ̥': '',
        'ʀ': '',
        'ʜ': '',
        'ʢ': '',
        'tɬ': '',
        'dɮ': '',
        'c𝼆': '',
        'k𝼄': '',
        'ɡʟ̝': '',
        'ɬ': '',
        'ɮ': '',
        'ꞎ': '',
        '𝼄': '',
        'ʟ̝': '',
        'l̪': '',
        'l': 'sounds/consonants/voiced_alveolar_lateral_approximant.wav',
        'l̠': '',
        'ɭ': '',
        'ʎ': '',
        'ʟ': '',
        'ʟ̠': '',
                # co-articulated
            # non-pulmonic
        
    }


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