from capture import capture_photo
from db_handling import writeToSQL, readSQL, initialiseTable
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
    #Opens Gate
    print("Gate Opened")
event="all"
x1 = int(input("""Enter type of event
1 = Faculty only
2 = Students only
3 = Students and Faculty
4 = All allowed
5 = Guest and Faculty
"""
))
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
    writeToSQL("Unkown", carNo, "Unknown", "False")