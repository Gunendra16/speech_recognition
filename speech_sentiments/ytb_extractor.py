import yt_dlp as youtube_dl

ydl = youtube_dl.YoutubeDL()

def get_video_infos(url):
    with ydl:
        result = ydl.extract_info(
            url,
            download = False
        )
    if "enteries" in result:
        return result["entries"][0]
    return result

def get_audio_url(vedio_info):
    for f in vedio_info["formats"]:
        if f["ext"] == "m4a":
            return f["url"]


if __name__ == "__main__":
    vedio_info = get_video_infos("https://www.youtube.com/watch?v=XRiUNPf-_-4")
    audio_url = get_audio_url(vedio_info)
    print(audio_url)


