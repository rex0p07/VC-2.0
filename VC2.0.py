import tkinter as tk
import speech_recognition as sr 
import pyttsx3
import replies
from PIL import Image, ImageTk
from tkinter.font import Font
from tkinter import ttk

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_Command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query

def get_response():
    command = take_Command().lower()
    response = replies.normal_conversation(command)
    print(f"VC: {response}")
    output_text.insert("end", "User: " + command + "\n")


  

    if response:
        talk(response)
        output_text.insert("end", "VC: " + response + "\n")
    else:
        talk("I am not sure what you mean.")
        output_text.insert("end", "VC: I am not sure what you mean.\n")





root = tk.Tk()

root.title("VC 2.0")
root.resizable(False, False)

bigfont = Font(family="RubikDirt-Regular", size=12, weight="bold", slant="italic")

input_frame = tk.Frame(root)
input_frame.pack(side="bottom")

input_button = tk.Button(input_frame, text="Get Response", command=get_response,bg = "#6767A2", fg ="white" , width=100,font=bigfont,borderwidth=2)
input_button.pack(side="right", padx=10,fill="both")

output_frame = tk.Frame(root)
output_frame.pack(side="right", fill="both", expand=True)

output_text = tk.Text(output_frame, height=10,font=bigfont,bg="#CDE0F8")

output_text.pack(side="right", fill="both", expand=True)

logo = Image.open("bird.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo,bg="#6767A2")
logo_label.image = logo
logo_label.pack(side="left", fill="both", expand=True)

root.mainloop()
