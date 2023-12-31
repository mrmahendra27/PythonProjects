from django.urls import path
from .views import test, text_to_speech, get_meaning_of_a_word, convert_pdf_to_speech

urlpatterns = [
    path("", test, name="test"),
    path("text-to-speech", text_to_speech, name="Text To Speech"),
    path("get-meaning-of-a-word", get_meaning_of_a_word, name="Get Meaning of a word"),
    path("convert-pdf-to-speech", convert_pdf_to_speech, name="Convert PDF to Speech"),
]
