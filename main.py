##################
#Imports
##################
from time import sleep
import os
import pyfiglet

##################
#Variables
##################
ascii_banner = pyfiglet.figlet_format("TRASH - SHELL")
user = "guest"
usr_input = ""

##################
#Welcome
##################
print("Loading Trash-Shell...")
sleep(2)
print("Welcome...")
sleep(2)

print("")
print("")
print("")
print("")
print(ascii_banner)
print("")
print("Trash-Shell")
print("Type !help for all comands")



########################
#Functions
########################
def help():
    print("")
    print("All Comands:")
    print("!whoami     outputs the user status")



def cmd(usr_i):
    if(usr_i == "!help"):
        help()
    elif(usr_i == "!whoami"):
        print("your status: " + user)


########################
#Loop
########################
while True:
    usr_input = input(">>>")
    cmd(usr_input)


