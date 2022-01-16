"""
This is a Command Line Calender
"""
from time import sleep, strftime
User_Name = raw_input("What is your name please: ")
calender = {}
def welcome():
  print "Welcome, " + User_Name + "."
  print "Calender starting..."
  sleep(1)
  print "Today is: " + strftime("%A %B %d, %Y")
  print "Time is: " + strftime("%I") + ":"+ strftime("%M") + ":" + strftime("%S") 
  sleep(1)
  print "What would you like to do?"

def start_calender():
  welcome()
  start = True
  while start:
    user_choice = raw_input("Enter A to Add, U to Update, V to View, D to delete, X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calender.keys()) < 1:
        print "Calender empty."
      else:
        print calender
    elif user_choice == "U":
      date = raw_input("What date? ")
      update = raw_input("Enter the update: ")
      calender[date] = update
      print "Update Successful"
      print calender
    elif user_choice == "A":
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if (len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
        print "invalid date" 
        try_again = raw_input("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calender [date] = event
        print "Event Successfully Added"
        print calender
    elif user_choice == "D":
      if (len(calender.keys()) < 1):
        print "calender is empty"
      else:
        event = raw_input("What event? ")
        for date in calender.keys():
          if event == calender[date]:
            del calender[date]
            print "Event Successfully Deleted"
          else:
            print "Incorrect event was specified"
    elif user_choice == "X":
      start = False
    else:
      print "Invalid Entry"
      start = False

start_calender()
