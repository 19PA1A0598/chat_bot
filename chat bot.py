

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

def timing():
    j = 0
    while (j != 4):
        try:
            j = int (input ("Which time do you prefer your appointment to be? \n Choose one of the options [1-4] \n 1. 7:00 am to 12:00 pm  \n 2. 1:00 pm to 5:00 pm \n 3. 6:00 pm to 10:00pm \n 4.End the conversation\n"))
            if j == 1:
                print("Your appointment has been recorded after verification you will be contacted.Thank you for using our services.Have a nice day :).")
                print(" ")
                print("Do you need my assistance with anything else.If no please end the conversation")
                break
            elif j == 2:
                print ("Your appointment has been recorded after verification you will be contacted.Thank you for using our services.Have a nice day :).")
                print("")
                print ("Do you need my assistance with anything else.If no please end the conversation")
                break
            elif j == 3:
                print ("Your appointment has been recorded after verification you will be contacted.Thank you for using our services.Have a nice day :).")
                print(" ")
                print ("Do you need my assistance with anything else.If no please end the conversation")
                break
            elif j == 4:
                break
            else:
                print ("Only integers 1,2,3,4 are allowed!")
        except Exception as e:
            print ("Only integers are allowed")

def doctorAppointment():
    print("May I know the patient's detail's")
    N=input("name of the patient:")
    a=int(input("age of the patient:"))
    numb=int(input("May I have your contact number:"))
    m = 0
    while (m != 5):
        try:
            m = int (input ("What kind of illness are facing? \n Choose one of the options [1-5] \n 1. Heart related problem  \n 2. Eye related problem \n 3. Diabetes related problem\n 4.Skin related problem \n 5.End the conversation\n"))
            if m == 1:
                timing ()
                break
            elif m == 2:
                timing ()
                break
            elif m == 3:
                timing ()
                break
            elif m == 4:
                timing ()
                break
            elif m == 5:
                break
            else:
                print ("Only integers 1,2,3,4,5 are allowed!")
        except Exception as e:
            print ("Only integers are allowed")

def display_options():
	n=0
	while(n!=4):
		try:
			n=int(input("How can I help you? \n Choose one of the options [1-4] \n 1. Looking a doctor appointment ?  \n 2. Booking medicine \n 3. Medical tests\n 4.End the conversation\n"))
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
