import pyttsx3, PyPDF2



reader = PyPDF2.PdfReader(open("The-Choice-by-Edith-Eger.pdf", "rb"))
text = " ".join(page.extract_text() for page in reader.pages)

# Розбиваємо текст на рядки
lines = text.splitlines()

# Беремо перші 20 рядків
first_lines = lines[:20]
# З'єднуємо рядки назад у текст
text = " ".join(first_lines)
print("Перші 20 рядків:")
print(text[:200] + "..." if len(text) > 200 else text)

# Створюємо TTS engine
engine = pyttsx3.init()

# Налаштовуємо швидкість мовлення (необов'язково)
engine.setProperty('rate', 150)

# Промовляємо текст
engine.say(text)

# ВАЖЛИВО: без цього виклику текст не буде промовлено!
engine.runAndWait()