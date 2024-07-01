import streamlit as st
import json
from api_communication import save_transcript

st.title('Welcome to my Podcast Summary Application!')

# Sidebar input for episode ID
episode_id = st.sidebar.text_input('Please input an episode id')
button = st.sidebar.button('Get Podcast Summary!')

def get_clean_time(start_ms):
    seconds = int((start_ms / 1000) % 60)
    minutes = int((  start_ms / (1000*60)) % 60)
    hours = int((start_ms / (1000 * 60 *60)) % 24)
    if hours > 0:
        start_t = f'{hours:02d}:{minutes:02d}:{seconds:02d}'
    else :
        start_t = f'{minutes:02d}:{seconds:02d}'

    return start_t
                
if button and episode_id:
    st.write(f"Episode ID: {episode_id}")

    # Call save_transcript() with the episode ID
    success = save_transcript(episode_id)
    if success:
        filename = episode_id + '_chapters.json'
        st.write(f"Expected filename: {filename}")

        try:
            with open(filename, 'r') as f:
                data = json.load(f)

            chapters = data.get('chapters', [])
            podcast_title = data.get('podcast_title', 'Unknown Podcast Title')
            episode_title = data.get('episode_title', 'Unknown Episode Title')
            thumbnail = data.get('episode_thumbnail', '')

            st.header(f'{podcast_title} - {episode_title}')
            if thumbnail:
                st.image(thumbnail)
            for chp in chapters:
                with st.expander(chp['gist'] + '-' + get_clean_time(chp['start'])):
                    st.write(chp['summary'])
        except FileNotFoundError:
            st.error("The transcription file was not found.")
    else:
        st.error("There was an error transcribing the episode. Please try again.")

#save_transcript('71de733737a74d4994b0d4d58ebbeafe')