import tkinter as tk
from tkinter import ttk
import pyttsx3


engine = pyttsx3.init()


voices = engine.getProperty('voices')


def speak():
    text = text_input.get("1.0", tk.END).strip()
    selected_voice_category = voice_combobox.get()
    rate = rate_scale.get()
    
    
    if selected_voice_category == "Male":
        engine.setProperty('voice', voices[0].id)  
    elif selected_voice_category == "Female" and len(voices) > 1:
        engine.setProperty('voice', voices[1].id) 
    
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def save_audio_pyttsx3(text, filename):
    engine = pyttsx3.init()
    engine.save_to_file(text, filename)
    engine.runAndWait()
save_audio_pyttsx3("This audio will be saved as an output file.", "output_audio.mp3")


project = tk.Tk()
project.title("Text to Speech Converter")

tk.Label(project, text="Enter Text:").pack(pady=5)
text_input = tk.Text(project, height=10, width=50)
text_input.pack(pady=5)

tk.Label(project, text="Select Voice:").pack(pady=5)
voice_combobox = ttk.Combobox(project, values=["Male", "Female"])
voice_combobox.set("Male")  
voice_combobox.pack(pady=5)

tk.Label(project, text="Select Speech Rate:").pack(pady=5)
rate_scale = tk.Scale(project, from_=50, to_=300, orient=tk.HORIZONTAL)
rate_scale.set(200)
rate_scale.pack(pady=5)

speak_button = tk.Button(project, text="Speak", command=speak)
speak_button.pack(pady=20)

project.mainloop()
