import pyttsx3, PyPDF2



# reader = PyPDF2.PdfReader(open("The-Choice-by-Edith-Eger.pdf", "rb"))
# text = " ".join(page.extract_text() for page in reader.pages)
text = "Hello, this is a text to speech test."
pyttsx3.init().say(text)