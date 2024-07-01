# this project have 4 steps:
# uploading a file on the assemblyAi
# then perform transcrpition
# keep polling the AssemblyAi Api untill the transcription is done
# then save the transcript

import sys
from api_communication import *

# Ensure that the script receives an argument
if len(sys.argv) < 2:
    print("Usage: python main.py <path_to_audio_file>")
    sys.exit(1)

filename = sys.argv[1]

audio_url = upload(filename)
save_transcript(audio_url, filename)




# now we want this data to display on a text file





