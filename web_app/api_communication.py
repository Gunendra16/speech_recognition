import requests
from api_secrets import API_KEY_ASSEMBLYAI,API_KEY_LISTENNOTES
import time
import json
import pprint

assemblyai_headers = {'authorization': API_KEY_ASSEMBLYAI}
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
 
listennotes_episode_endpoint = "https://listen-api.listennotes.com/api/v2/episodes"
listennotes_header = {'X-ListenAPI-key': API_KEY_LISTENNOTES}

def get_episode_audio_url(episode_id):
    url = listennotes_episode_endpoint + '/' + episode_id
    response = requests.request('GET' , url , headers = listennotes_header)
    data = response.json()
    #pprint.pprint(data)

    audio_url = data['audio']
    episode_thumbnail = data['thumbnail']
    podcast_title = data['podcast']['title']
    episode_title = data['title']

    return audio_url , episode_thumbnail , podcast_title , episode_title
#transcription

def transcribe(audio_url , auto_chapters):
    transcript_request = { "audio_url" :audio_url ,
                          "auto_chapters" :auto_chapters }
    transcribe_response = requests.post(transcript_endpoint , json = transcript_request , headers = assemblyai_headers)
    job_id = transcribe_response.json()['id']
    return job_id


#polling (this will keep polling the assemblyAI that if our transcription is ready or not)

def poll(transcript_id):
    polling_endpoint = transcript_endpoint + '/' + transcript_id
    polling_response =   requests.get(polling_endpoint ,  headers = assemblyai_headers)
    return polling_response.json()
    
def get_transcription_result_url(audio_url,auto_chapters ):
    transcript_id = transcribe(audio_url, auto_chapters)
    while True:
        data = poll(transcript_id)
        if data['status'] == 'completed':
            return data , None
        elif data['status'] == 'error':
            return data, data['error']
        
        print('waiting 60 seconds.... ')
        time.sleep(60)


def save_transcript(episode_id):
    audio_url , episode_thumbnail , podcast_title , episode_title  = get_episode_audio_url(episode_id)
    data, error = get_transcription_result_url(audio_url, auto_chapters = True)

    pprint.pprint(data)
    if data:
      
        
        # Write the transcript text to the file
        filename = episode_id + ".txt"
        with open(filename, 'w') as f:
            f.write(data['text'])
        
        chapters_filename = episode_id + '_chapters.json'
        with open(chapters_filename, 'w') as f:
            chapters = data['chapters']

            episode_data = {'chapters': chapters}
            episode_data['episode_thumbnail'] =  episode_thumbnail
            episode_data['podcast_title'] = podcast_title
            episode_data['episode_title'] = episode_title

            json.dump(episode_data , f)
            print('transcript saved')
            return True

    
    elif error:
        print("Oops! Error:", error)
        return False