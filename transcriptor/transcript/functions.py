import os
import pafy
import speech_recognition as sr
import moviepy.editor as mp
from youtube_transcript_api import YouTubeTranscriptApi
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from heapq import nlargest


def convertVideoToText(url):
    """ Converts Youtube Video to Text if Transcript from Youtube is not available"""

    video = pafy.new(url)
    bestaudio = video.getbestaudio()
    path = "Audio." + bestaudio.extension
    bestaudio.download(filepath=path)
    clip = mp.AudioFileClip(path)
    os.remove(path)
    path = 'converted.wav'
    clip.write_audiofile(path)
    r = sr.Recognizer()
    audio = sr.AudioFile(path)
    os.remove(path)
    with audio as source:
        audio_file = r.record(source)
    result = r.recognize_google(audio_file)
    return result


def convertToTranscript(url):
    """ Get Transcript from Youtube URL"""

    video = pafy.new(url, ydl_opts={'nocheckcertificate': True})
    id = video.videoid
    final_transcript = ""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(id)
        for trans in transcript:
            final_transcript += trans['text']
            final_transcript += " "
    except:
        final_transcript = convertVideoToText(url)

    return final_transcript

def getSummarization(text):
    stopwords = list(STOP_WORDS)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    from string import punctuation
    punctuation = punctuation + '\n'
    word_freq = {}
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text.lower() not in word_freq.keys():
                    word_freq[word.text.lower()] = 1
                else:
                    word_freq[word.text.lower()] += 1

    max_freq = max(word_freq.values())
    for word in word_freq.keys():
        word_freq[word] = word_freq[word] / max_freq
    sentence_tokens = [sent for sent in doc.sents]
    sentence_score = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_freq.keys():
                if sent not in sentence_score.keys():
                    sentence_score[sent] = word_freq[word.text.lower()]
                else:
                    sentence_score[sent] += word_freq[word.text.lower()]

    select_length = int(len(sentence_tokens) * 0.3)
    summary = nlargest(select_length, sentence_score, key=sentence_score.get)
    finalsummary = [word.text for word in summary]
    summary = ' '.join(finalsummary)
    return summary