# Clear the file of any previous settings
def initWriteToFile():
    x = open("data/private.py", "w")
    x.write('')
# Write to file function, everything must be preceise
def writetofile(key,value,addbrackets):
    x = open("data/private.py", "a")
    x.write(key)
    x.write(" = ")
    if addbrackets : # So it would not be written as a string in the private file
        x.write('"')
        x.write(value)
        x.write('"\n')
    else:
        x.write(value)
        x.write('\n')
    x.close()
# Time to wait
def getTimeToWait():
    timetowait= input("how much time to wait between emails? (seconds) \n")
    if timetowait == "":timetowait = "86400"  # defaults to 24 hours if there was no input
    writetofile(key="timetowait",value=timetowait, addbrackets=False)
# APIkey
def getAPIKey():
    APIKey= input("Please input APIKey \n")
    writetofile(key="apikey", value=APIKey, addbrackets=True)
# reciever
def getRecieverAdress():
    recieveradress= input("What is the recievers address ?")
    writetofile(key="recieveradress", value=recieveradress, addbrackets=True)
def getSignUpEmail():
    signupemail= input("What is the sign up email ?")
    writetofile(key="signupemail", value=signupemail, addbrackets=True)
# Terminal Activation
def getTerminalActivation():
    TerminalActivate = str(input("Would you like The terminal to print The info? (Y/n)")).strip().lower()
    match(TerminalActivate):
        case "":
            writetofile(key="TerminalActivated", value="True", addbrackets=False)
        case "yes":
            writetofile(key="TerminalActivated", value="True", addbrackets=False)
        case "y":
            writetofile(key="TerminalActivated", value="True", addbrackets=False)
        case "no" :
            writetofile(key="TerminalActivated", value="False", addbrackets=False)
        case "n" :
            writetofile(key="TerminalActivated", value="False", addbrackets=False)
# Main function
def getInformation():
        initWriteToFile()
        getTimeToWait()
        getAPIKey()
        getSignUpEmail()
        getRecieverAdress()
        getTerminalActivation()
        #here you may add a check funtion that checks the file
        print("Settings have been saved, Please run 'run.py'")
#Init
getInformation()

