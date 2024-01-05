from django.shortcuts import render
from django.http import HttpResponse

import pyttsx3

from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO

from PyDictionary import PyDictionary

from PyPDF2 import PdfReader

from .forms import TextToSpeechForm, WordMeaningForm, PDFToSpeechForm, SpeechToTextForm


# Create your views here.
def test(request):
    return HttpResponse("Hello Guys, This is test Page")


def text_to_speech(request):
    if request.method == "POST":
        form = TextToSpeechForm(request.POST)
        if form.is_valid():
            # language = 'en'
            text = form.cleaned_data["text"]

            # # Using GTTS
            # tts = gTTS(text, lang=language, slow=False)
            # tts.save('converted_audio.mp3')

            # Using PYTTSX3
            engine = pyttsx3.init()

            # RATE
            rate = engine.getProperty(
                "rate"
            )  # getting details of current speaking rate
            engine.setProperty("rate", 125)  # setting up new voice rate

            # VOLUME
            volume = engine.getProperty(
                "volume"
            )  # getting to know current volume level (min=0 and max=1)
            engine.setProperty(
                "volume", 1.0
            )  # setting up volume level  between 0 and 1

            # VOICE
            voices = engine.getProperty("voices")  # getting details of current voice
            # engine.setProperty(
            #     "voice", voices[0].id
            # )  # changing index, changes voices. o for male
            engine.setProperty(
                "voice", voices[1].id
            )  # changing index, changes voices. 1 for female

            engine.say("I will speak the following text")
            engine.say(text)
            # engine.save_to_file('Generated Speech', 'test.mp3')

            engine.runAndWait()
            engine.stop()
    else:
        form = TextToSpeechForm()

    return render(request, "text-to-speech.html", {"form": form})


def get_meaning_of_a_word(request):
    if request.method == "POST":
        form = WordMeaningForm(request.POST)
        data = None
        word = None
        if form.is_valid():
            word = form.cleaned_data["word"]
            dictionary = PyDictionary()

            data = {
                "meaning": dictionary.meaning(word),
                "antonym": dictionary.antonym(word),
                "synonym": dictionary.synonym(word),
            }
    else:
        data = None
        word = None
        form = WordMeaningForm()

    return render(
        request, "word-meaning.html", {"form": form, "word": word, "data": data}
    )


def convert_pdf_to_speech(request):
    if request.method == "POST":
        form = PDFToSpeechForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.cleaned_data["pdf_file"]
            reader = PdfReader(pdf_file)

            text = ""

            for page in reader.pages:
                text += page.extract_text()

            # # Using GTTS
            tts = gTTS(text, slow=False)
            tts.save("pdf_audio.mp3")

            # # Using PYTTSX3
            # engine = pyttsx3.init()

            # # RATE
            # rate = engine.getProperty(
            #     "rate"
            # )  # getting details of current speaking rate
            # engine.setProperty("rate", 125)  # setting up new voice rate

            # # VOLUME
            # volume = engine.getProperty(
            #     "volume"
            # )  # getting to know current volume level (min=0 and max=1)
            # engine.setProperty(
            #     "volume", 1.0
            # )  # setting up volume level  between 0 and 1

            # # VOICE
            # voices = engine.getProperty("voices")  # getting details of current voice
            # # engine.setProperty(
            # #     "voice", voices[0].id
            # # )  # changing index, changes voices. o for male
            # engine.setProperty(
            #     "voice", voices[1].id
            # )  # changing index, changes voices. 1 for female

            # engine.say("I will read the following PDF")
            # engine.say(text)
            # # engine.save_to_file('Generated Speech', 'test.mp3')

            # engine.runAndWait()
            # engine.stop()
    else:
        form = PDFToSpeechForm()

    return render(request, "convert-pdf-to-speech.html", {"form": form})

def speech_to_text(request):
    form = SpeechToTextForm
    return render(request, "speech-to-text.html", {"form": form})