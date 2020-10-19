

import random
from datetime import datetime
def greeting():
    time = datetime.now()
    greetings = "Good Morning,"
    if 12 < time.hour < 17:
        greetings ="Good Afternoon,"
    elif 17 <= time.hour < 22:
        greetings ="Good Evening,"
    elif 22 <= time.hour < 24:
        greetings ="Hi,It's late,"
    intro ="Welcome to ******* Hospitals.I am Alex an reception bot I am here to help you with your doctor appointments,medical needs.May I know your name?"
    print (greetings, intro)
    greets = ["Have a warm welcome.", "It's nice to meet you."]

def welcome(name):
    responses = ["Have a warm welcome!","It's nice to meet you","It's good to meet you"]
    print(random.choice(responses),name)

def display_options():
	n=0
	while(n!=4):
		try:
			n=int(input("How can I help you? \n Choose one of the options [1-3] \n 1. Looking a doctor appointment ?  \n 2. Booking medicine \n 3. Medical tests\n 4.End the conversation"))
			if n== 1:
				doctorAppointment()
			elif n==2:
				bookMedicine()
			elif n==3:
				medicalTest()
			elif n==4:
				break
			else:
				print("Only integers 1,2,3,4 are allowed!")
		except Exception as e:
			print("Only integers are allowed")

def main():
    greeting()
    name=input("")
    welcome(name)
    display_options()
main()
