import os
import re
import math
import PyPDF2
import textract
import speech_recognition as sr
import docx2txt as d2t
import tempfile
import cv2
import numpy as np
from pptx import Presentation
from langdetect import detect_langs
from summarizer import Summarizer
from punctuator import Punctuator
from os import path
from pydub import AudioSegment
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
from pdf2image import convert_from_path, convert_from_bytes


try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


# img = cv2.imread("C:\\Users\\lm44\\Documents\\Uni Work\\Investment analysis\\p7.jpg") 


def ocr_core(filename):

    im = Image.open(filename)
    img = im.point(lambda p: p > 75 and p + 100)
    text = pytesseract.image_to_string(img)
    lang = str(detect_langs(text)[0])[:2]
    confidence = float(str(detect_langs(text)[0])[3:])
    if lang == 'en':
        while confidence < 0.99:
            im = im.rotate(-90)
            text = pytesseract.image_to_string(im)
            confidence = float(str(detect_langs(text)[0])[3:])
            print('Processing ...')
    else:
        print('No English Detected')
        
    return text


print(ocr_core("C:\\Users\\lm44\\Documents\\Uni Work\\Investment analysis\\p7.jpg"))