# PDF-To-Speech
This Python script converts text from a PDF file into speech and saves it as an MP3 file. It utilizes the `pdftotext` library to extract text from the PDF and the `gTTS` (Google Text-to-Speech) library for text-to-speech conversion.

## Prerequisites

Before running the script, make sure you have the following libraries installed:

- `pdftotext`: Used to extract text from PDF files.
- `gTTS` (Google Text-to-Speech): Used for text-to-speech conversion.
- `nltk` (Natural Language Toolkit): Used for sentence tokenization.

You can install these libraries using pip:

~~~
pip install pdftotext gtts nltk
~~~

## Usage

1. Replace "your-file-name.pdf" in the pdf_file_path variable with the path to the PDF file you want to convert.
2. Run the script:

~~~
pdftospeech.py
~~~

The script will extract text from the PDF, convert it to speech, and save the audio as "output.mp3" in the current directory.

## Customization

You can customize the script by modifying the following parameters:

• pdf_file_path: Replace with the path to your PDF file.  
• lang: Change the language for text-to-speech conversion (e.g., 'en' for English, 'ru' for Russian).  
• tld: Modify the Top-Level Domain for voice selection based on the desired region (e.g., 'ru' for Russian voices).  

## Contributing

If you would like to contribute to this program, feel free to submit a pull request. Please include a detailed description of the changes made and the reasons for the changes.

## License

Feel free to use and modify the code as per your requirements.
