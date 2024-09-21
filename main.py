from capture import capture_photo
from db_handling import writeToSQL, readSQL, initialiseTable, registerCar
l = ['“','\n', ' ', '@', '!', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', ']', '|', '\\', ':', ';', '"', "'", '<', ',', '>', '.', '?', '/', '`', '~']
def withoutSpecialCharacters(text):
    for i in l:
        try:
            text = text.replace(i, "")
        except: 
            print("Error in removing special chars:")
            print("Text: ", text)
    return text
def gateOpen():
    # Opens Gate
    print("Gate Opened")

event="all"
x1 = int(input("""
Welcome to the Vehicle Identification and Logging System. 
Select the type of event to simulate: 
        Enter 1 for Faculty only
        Enter 2 for Students only
        Enter 3 for Students AND Faculty
        Enter 4 for Students, Faculty AND Guests
        Enter 5 for Faculty AND Guests
------------------------------------------------------------
To register a new vehicle, enter 6. 
input> """
))
# Declare flag variable which will be set to True if the vehicle is found in the database
flagFound = False

arr = []
if(x1==1):
    arr =["Faculty"]
if(x1==2):
    arr = ["Student"]
if(x1==3):
    arr =["Student", "Faculty"]
if(x1==4):
    arr = ["Student", "Faculty", "Guest"]
if(x1==5):
    arr = ["Faculty", "Guest"]

if(x1==6):
    print('''Registering a new vehicle. Please enter the following details.''')
    vehicleNum = input("Enter Vehicle Number [As on the numberplate. NO SPACES.]: ")
    vehicleOwner = input("Enter Vehicle Owner Name: ")
    ownerType = input("Enter Owner Type [Student/Faculty/Guest]: ")
    registerCar(vehicleNum, vehicleOwner, ownerType)
    print("Vehicle Registered Successfully. Exiting program.")
    exit()

carNo = withoutSpecialCharacters(capture_photo()) #Working

print("Read Vehicle Number:", carNo)

initialiseTable()
saved_db = readSQL()
# print("SQL Data:", saved_db)
numberplates = []
for i in saved_db:
    numberplates.append(i['vehicleNumber'])

if(carNo in numberplates):
    print("Found in Database")
for i in saved_db:
    
    if i['vehicleNumber'] == carNo:
        flagFound = True
        if i['ownerType'] in arr:
            print(f"Entry Permitted to: {i['vehicleOwner']}, {i['ownerType']}; Vehicle Number: {i['vehicleNumber']}")
            gateOpen()
            writeToSQL(i['vehicleOwner'], i['vehicleNumber'], i['ownerType'], "True")
        else:
            print("Entry Denied - Owner Type Mismatch")
            writeToSQL(i['vehicleOwner'], i['vehicleNumber'], i['ownerType'], "False")
if not flagFound:
    print("Entry Denied - Not Found in Database")
    writeToSQL("Unknown", carNo, "Unknown", "False")