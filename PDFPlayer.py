import pyttsx3
import engineio
import PyPDF2

engineio = pyttsx3.init()
voices = engineio.getProperty('voices')
engineio.setProperty('rate', 130)
engineio.setProperty('voice',voices[0].id)

def speak(text):
    engineio.say(text)
    engineio.runAndWait()

pdfFileObj = open(r'C:\Users\HP\Desktop\InterProcessComm.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(5)
print(pageObj.extractText())
speak(pageObj.extractText())
