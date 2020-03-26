import pyttsx3
import engineio
import PyPDF2
#tere kaam ki cheej nhi h####
engineio = pyttsx3.init()
voices = engineio.getProperty('voices')
engineio.setProperty('rate', 130)
engineio.setProperty('voice',voices[1].id)
#############################
def speak(text): #Function to speak text
    engineio.say(text)
    engineio.runAndWait()

pdfFileObj = open(r'C:\Users\HP\Desktop\InterProcessComm.pdf', 'rb') #Creating file object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) #file reading object
print(pdfReader.numPages) #fetching number of pages
pageObj = pdfReader.getPage(5) #creating object per page
print(pageObj.extractText())
speak(pageObj.extractText())
