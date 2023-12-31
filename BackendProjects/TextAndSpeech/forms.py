from django import forms
from django.core.validators import FileExtensionValidator


class TextToSpeechForm(forms.Form):
    # language = forms.ChoiceField(
    #     label="Select a language",
    #     choices=[
    #         ("hi", "Hindi"),
    #         ("en", "English"),
    #         ("af", "Afrikaans"),
    #         ("sq", "Albanian"),
    #         ("am", "Amharic"),
    #         ("ar", "Arabic"),
    #         ("hy", "Armenian"),
    #         ("az", "Azerbaijani"),
    #     ],
    #     required=True,
    #     widget=forms.Select(attrs={'class': 'form-control'}),
    # )
    text = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control"}),
        label="Enter Text to generate speech",
        # max_length=10,
        min_length=2,
    )


class WordMeaningForm(forms.Form):
    word = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Enter Word to Get it's Meaning/Antonym/Synonym",
        min_length=2,
    )


class PDFToSpeechForm(forms.Form):
    pdf_file = forms.FileField(
        widget=forms.FileInput(attrs={"class": "form-control"}),
        label="Select File",
        required=True,
        help_text="File must be in PDF format.",
        validators=[
            FileExtensionValidator(allowed_extensions=["pdf"]),
        ],
    )
