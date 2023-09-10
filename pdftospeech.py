import pdftotext
from gtts import gTTS
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize


def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_text = pdftotext.PDF(file)
        text = "\n".join(pdf_text)
        return text


def convert_text_to_speech(text):
    sentences = sent_tokenize(text)
    engine = gTTS(text=text, lang='en')

    # Save the audio to a file
    engine.save("output.mp3")


def pdf_to_speech(file_path):
    text = extract_text_from_pdf(file_path)
    convert_text_to_speech(text)


# Provide the path to the PDF file you want to convert
pdf_file_path = "your-file-name.pdf"
pdf_to_speech(pdf_file_path)
