from pydub import AudioSegment
import os

# Update this to the correct path where ffmpeg.exe is located
ffmpeg_path = r"C:\path\to\ffmpeg\bin\ffmpeg.exe"

# Check if ffmpeg is accessible
if not os.path.isfile(ffmpeg_path):
    raise FileNotFoundError(f"ffmpeg not found at {ffmpeg_path}")

AudioSegment.converter = ffmpeg_path

# Load the WAV file
input_file = "guddi_audio.wav"
output_file = "mp3_audio.mp3"

try:
    audio = AudioSegment.from_wav(input_file)
except FileNotFoundError:
    raise FileNotFoundError(f"Input file '{input_file}' not found.")
except CouldntDecodeError:
    raise CouldntDecodeError(f"Could not decode '{input_file}'. Ensure it's a valid WAV file.")

# Manipulate the audio
audio = audio + 6  # Increase the volume by 6 dB
audio = audio * 2  # Repeat the audio twice
audio = audio.fade_in(2000)  # Fade in over 2 seconds

# Export the manipulated audio as an MP3 file
try:
    audio.export(output_file, format="mp3")
except Exception as e:
    raise IOError(f"Failed to export the audio file: {e}")

# Load the exported MP3 file
try:
    audio2 = AudioSegment.from_mp3(output_file)
    print("All set")
except FileNotFoundError:
    raise FileNotFoundError(f"Exported file '{output_file}' not found.")
except CouldntDecodeError:
    raise CouldntDecodeError(f"Could not decode '{output_file}'. Ensure it's a valid MP3 file.")
