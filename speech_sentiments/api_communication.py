import requests
from api_secrets import API_KEY_ASSEMBLYAI
import time
import json


headers = {'authorization': API_KEY_ASSEMBLYAI}

upload_endpoint = "https://api.assemblyai.com/v2/upload"
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"


def upload(filename):
    def read_file(filename, chunk_size=5242880):  # 5MB chunk size
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    upload_response = requests.post(upload_endpoint, 
                            headers=headers,
                            data=read_file(filename))

    audio_url = upload_response.json()['upload_url']
    return audio_url
#transcription

def transcribe(audio_url , sentiment_analysis):
    transcript_request = { "audio_url" :audio_url ,
                          "sentiment_analysis" :sentiment_analysis }
    transcribe_response = requests.post(transcript_endpoint , json = transcript_request , headers = headers)
    job_id = transcribe_response.json()['id']
    return job_id


#polling (this will keep polling the assemblyAI that if our transcription is ready or not)

def poll(transcript_id):
    polling_endpoint = transcript_endpoint + '/' + transcript_id
    polling_response =   requests.get(polling_endpoint ,  headers = headers)
    return polling_response.json()
    
def get_transcription_result_url(audio_url,sentiment_analysis ):
    transcript_id = transcribe(audio_url, sentiment_analysis)
    while True:
        data = poll(transcript_id)
        if data['status'] == 'completed':
            return data , None
        elif data['status'] == 'error':
            return data, data['error']
        
        print('waiting 30 seconds.... ')
        time.sleep(30)


def save_transcript(audio_url, title, sentiment_analysis=False):
    data, error = get_transcription_result_url(audio_url, sentiment_analysis)
    if data:
      
        
        # Write the transcript text to the file
        filename = title + ".txt"
        with open(filename, 'w') as f:
            f.write(data['text'])
        
        # Write the sentiment analysis results to a separate file, if applicable
        if sentiment_analysis:
            filename = title + "_sentiments.json"
            with open(filename, 'w') as f:
                sentiments = data["sentiment_analysis_results"]
                json.dump(sentiments, f, indent=4)
        
        print('Transcription saved!!')
        return True
    elif error:
        print("Oops! Error:", error)
        return False