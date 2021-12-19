from datetime import datetime

def sample_response(input_text):
    user_message = str(input_text).lower()

    # exa = input("What is your name?")
    # if exa == "Saidali":
    #     print("Welcome Boss")
    # else:
    #     print(f"Hi {exa}")

    if user_message in ("hello", "hi", "sup"):
        return "Hey! How is it going?"
    
    if user_message in ("who are you", "who are you?"):
        return "I am Saidali`s BOT"

    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d.%b.%Y, %H:%M:%S")
        return str(date_time)

    if user_message in ("thanks", "thanks!", "thank you", "thanks a lot", "thanks a bunch", "tonns of thanks"):
        return "Warm welcome"

    if user_message == "Assalomu alaykum":
        return "Va alaykum assalom"

    if user_message in ("Where are you from", "Where are you from?"):
        return "I am from Uzbekistan"

    if user_message in ("How old are you", "How old are you?"):
        return "I was born 16.12.2021 roughly at 8:50 P.M"

    if user_message in ("Where are you now", "Where are you now?"):
        return "I am on Earth Planet :)"

    if user_message in ("What is your favourite color", "What is your favourite color?"):
        return "Blue, it means loyalty!"
    
    if user_message in ("What is your name", "What is your name?"):
        return "Oops a daisy, I dunno :("
    
    if user_message in ("What is your major", "What is your major?"):
        return "My major is IT (Information Technology) and I do love English"

    if user_message in ("do you speak english", "do you speak english?"):
        return "Yes, I do!"

    if user_message in ("do you have a girlfriend", "do you have a girlfriend?"):
        return "Yes, I do while I do not intend to say about her. OK?"
    
    if user_message in ("are you idiot", "are you idiot?"):
        return "not me, probably you are"
        


    else:return "I don`t understand you."