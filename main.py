import tkinter as tk
from tkinter import Frame, Text, Label, RAISED, messagebox, ttk
import speech_recognition as sr
import pyttsx3
from googletrans import Translator

root = tk.Tk()
root.title('Language Translator')
root.geometry('590x370')

framel = Frame(root, width=590, height=370, relief=tk.RIDGE, borderwidth=5, bg='#F7DC6F')
framel.place(x=0, y=0)

Label(root, text="Language Translator", font=("Helvetica 20 bold",), fg="black", bg='#F7DC6F').pack(pady=10)

def translate():
    lang_l = text_entry1.get("1.0", "end-1c")
    cl = choose_language.get()

    if lang_l == '':
        messagebox.showerror('Language Translator', 'Enter the text to translate!')
    else:
        text_entry2.delete(1.0, 'end')
        translator = Translator()
        output = translator.translate(lang_l, dest=cl.lower() if cl.lower() != 'English' else 'en')
        translated_text = output.text
        pronunciation = output.pronunciation
        text_entry2.insert('end', f"{translated_text}\n{pronunciation}")
        # Speak the translated text
        text_to_speech()

def clear():
    text_entry1.delete('1.0', 'end')
    text_entry2.delete('1.0', 'end')

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        text_entry1.delete('1.0', 'end')
        text_entry1.insert('end', text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def text_to_speech():
    text = text_entry2.get("1.0", "end-1c")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

a = tk.StringVar()

auto_select = ttk.Combobox(framel, width=27, textvariable= a, state='randomly', font=('verdana', 10, 'bold'))
auto_select['values'] = ('Auto Select',)
auto_select.place(x=15, y=60)
auto_select.current(0)

l = tk.StringVar()
choose_language = ttk.Combobox(framel, width=27, textvariable=l, state='randomly', font=('verdana', 10, 'bold'))
choose_language['values'] = (
    'Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Azerbaijani', 'Basque', 'Belarusian', 'Bengali',
    'Bosnian', 'Bulgarian', 'Catalan', 'Cebuano', 'Chichewa', 'Chinese (Traditional)', 'Corsican', 'Croatian',
    'Czech', 'Danish', 'Dutch', 'English', 'Esperanto', 'Estonian', 'Filipino', 'Finnish', 'French', 'Frisian',
    'Galician', 'Georgian', 'German', 'Greek', 'Gujarati', 'Haitian Creole', 'Hausa', 'Hawaiian', 'Hebrew', 'Hindi',
    'Hmong', 'Hungarian', 'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kannada',
    'Kazakh', 'Khmer', 'Korean', 'Kurdish (Kurmanji)', 'Kyrgyz', 'Lao', 'Latin', 'Latvian', 'Lithuanian',
    'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Mongolian',
    'Myanmar (Burmese)', 'Nepali', 'Norwegian', 'Odia (Oriya)', 'Pashto', 'Persian', 'Polish', 'Portuguese',
    'Punjabi', 'Romanian', 'Russian', 'Samoan', 'Scots Gaelic', 'Serbian', 'Sesotho', 'Shona', 'Sindhi', 'Sinhala',
    'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese', 'Swahili', 'Swedish', 'Tajik', 'Tamil', 'Telugu',
    'Thai', 'Turkish', 'Ukrainian', 'Urdu', 'Uyghur', 'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba',
    'Zulu'
)
choose_language.place(x=305, y=60)
choose_language.current(0)

text_entry1 = Text(framel, width=20, height=7, borderwidth=5, relief=tk.RIDGE, font=('verdana', 15))
text_entry1.place(x=10, y=100)

text_entry2 = Text(framel, width=20, height=7, borderwidth=5, relief=tk.RIDGE, font=('verdana', 15))
text_entry2.place(x=300, y=100)

btn1 = tk.Button(framel, command=translate, text="Translate", relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#248aa2', fg='white', cursor="hand2")
btn1.place(x=150, y=300)

btn2 = tk.Button(framel, command=speech_to_text, text="Speak", relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#248aa2', fg='white', cursor="hand2")
btn2.place(x=250, y=300)

btn3 = tk.Button(framel, command=clear, text="Clear", relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#248aa2', fg='white', cursor="hand2")
btn3.place(x=330, y=300)

root.mainloop()
