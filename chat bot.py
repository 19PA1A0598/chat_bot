""" this is the code for a chat bot used for hospitals.
 this chatbot has two services namely doctor appointment booking and medical tests services at home.
 this chatbot greets the user according to the time of usage.
 It also welcomes the user with their name.
 Then it displays the services it can provide and asks the user to select one of them.
 It collects the data required from the user.
 It thanks the user for using its service. """
import random
from datetime import datetime
def greeting():
    """This method greets the user according to the time."""
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
    """ This method welcomes the user with their name."""
    responses = ["Have a warm welcome!","It's nice to meet you","It's good to meet you"]
    print(random.choice(responses),name)

def doctorAppointment():
    """ collects all the details of the patient which are needed for the doctor appointment."""
    print("May I know the patient's details")
    N=input("Name of the patient:")
    rightAge=False
    while(not(rightAge)):
    	try:
    		a=int(input("Age of the patient:"))
    		if(not(0<=a<=100)):
    			print("Invalid age")
    		else:
    			rightAge=True
    	except:
    		print("Invalid information given")
    complaint=input("What is your health problem?\n")
    rightNumb=False
    while(not(rightNumb)):
    	try:
    		numb=int(input("Enter your contact number:"))
    		rightNumb=True
    	except:
    		print("Invalid information given")
    rightTime=False
    while(not(rightTime)):
    	try:
    		time = int(input("Select your time slot for the appointment: [1-3]\n 1. 9:00 am to 12:00 pm \n 2. 1:00 pm to 5:00 pm\n 3. 6:00 pm to 10:00 pm\n"))
    		if(1<=time<=3):
    			rightTime=True
    		else:
    			print("Only options 1,2,3 are available")
    	except:
    		print("Only given options should be selected")
    print("Your appointment has been recorded after verification you will be contacted.Thank you for using our services.Have a nice day :).")
    print("Do you need my assistance with anything else ?")


def medicalTest():
	try:
		n=int(input("We provide the following tests [1-4]: \n 1. Blood Test \n 2. Diabetes Test\n 3. Thyroid Test\n 4. Corona test\n Which test do you need?\n"))
		if(1<=n<=4):
			pName =input("Enter the name of patient: ")
			address=input("Please Enter the address to get your test samples: \n")
			rightNumb=False
			while(not(rightNumb)):
			 				try:
			 					numb=int(input("Enter your contact number:"))
			 					rightNumb=True
			 				except:
			 					print("Invalid information given")
			 					print("You will receive a call from us soon.We will reach you as soon as possible.\nThank you for using our service")
		else:
			print("Select one from given tests.Sorry, if we couldn't provide the test you needed")
	except:
		print("Please select from given tests.Sorry, if we couldn't provide the test you needed")
def display_options():
	n=0
	while(n!=3):
		try:
			n=int(input("How can I help you? \n Choose one of the options [1-3] \n 1. Looking a doctor appointment ?  \n 2. Medical tests\n 3.End the conversation\n"))
			if n== 1:
				doctorAppointment()
			elif n==2:
				medicalTest()
			elif n==3:
				print("Thank you for using our services.Have a pleasent day.")
				break
			else:
				print("Only integers 1,2,3 are allowed!")
		except Exception as e:
			print("Only integers are allowed")

def main():
    greeting()
    name=input("")
    welcome(name)
    display_options()
main()
