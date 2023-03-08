import random
import webbrowser
import wikipedia
import datetime

def normal_conversation(command):
    if 'hello' in command:
        responses = [
            'Hello, how can I help you today?',
            'Hi there, how can I assist you today?',
            'Greetings, what can I do for you today?'
        ]
        return random.choice(responses)
    elif 'how are you' in command:
        responses = [
            'I am a computer program, I do not have feelings, but I am functioning well, thank you for asking!',
            'As a computer program, I do not have emotions, but I am functioning as expected, thanks for asking!',
            'I am just a computer program, but I am functioning properly, thank you for asking!'
        ]
        return random.choice(responses)


      #time
    elif "what is the time".lower() in command:
                    strTime =datetime.datetime.now().strftime("%H:%M:%S")
                    return(f"Sir, the time is {strTime}")
                    
    elif "what is the date".lower() in command:
                    strDay=datetime.date.today().strftime("%B %d, %Y")
                    return (f"Today is {strDay}")
                    
    elif "what day is today".lower() in command:
                    return (f"Today is {datetime.datetime.now().strftime('%A')}")
                    
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com/")
        return "Opening YouTube in your default web browser."
    
    elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            return(info)
            

    else:
        responses = [
            'I am not sure what you mean, could you please rephrase your question?',
            'I am sorry, but I am not sure what you are asking. Can you please provide more context or clarification?',
            'I am not able to understand your request, could you please rephrase or provide more information?'
        ]
        return random.choice(responses)
