
import random
from datetime import datetime
def greeting():
    time = datetime.now()
    greetings = "Good Morning,"
    if 12 < time.hour < 17:
        greetings ="Good Afternoon,"
    elif 17 <= time.hour < 22:
        greetings ="Good Evening,"
    elif 22 <= time.hour < 24 or 00 <= time.hour < 0o3:
        greetings ="Hi,It's late,"
    elif 0o3 <= time.hour < 0o5:
        greetings ="Hi,It's early,"
    intro ="Welcome to ******* Hospitals.I am Alex an reception bot I am here to help you with your doctor appointments,medical needs.May I know your name?"
    print (greetings, intro)
    greets = ["Have a warm welcome.", "It's nice to meet you."]
greeting()