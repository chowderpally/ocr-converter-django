# ocr-converter-django
This is the basic django app that extracts text from an image into a .txt and .csv file. In simple words this is OCR web app. The text in the image is converted into text using pytesseract, tesseract-ocr.

Resources:

https://github.com/tesseract-ocr/tesseract
https://github.com/madmaze/pytesseract

#Inital Steps to run the django-project

1. Make sure you run this in new vitual environment
2. $ cd ocr-converter-django
3. $ pip install -r requirements.txt
4. $ python manage.py makemigrations
5. $ python manage.py migrate
6. $ python manage.py runserver

And it's done! Enjoy..


