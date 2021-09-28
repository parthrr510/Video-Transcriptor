import pafy
from youtube_transcript_api import YouTubeTranscriptApi


def convertToTranscript(url):
    """ Get Transcript from Youtube URL"""
    video = pafy.new(url,ydl_opts={'nocheckcertificate': True})
    id = video.videoid
    transcript = YouTubeTranscriptApi.get_transcript(id)
    return transcript