from capture import capture_photo
from db_handling import writeToSQL, readSQL, initialiseTable
l = ['\n', ' ', '@', '!', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', ']', '|', '\\', ':', ';', '"', "'", '<', ',', '>', '.', '?', '/', '`', '~']
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
"""))
arr = []
if(x1==1):
    arr =["faculty"]
if(x1==2):
    arr = ["student"]
if(x1==3):
    arr =["student", "faculty"]
if(x1==4):
    arr = ["student", "faculty", "guest"]
if(x1==5):
    arr = ["faculty", "guest"]
carNo = withoutSpecialCharacters(capture_photo()) #Working
print(carNo)

initialiseTable()
saved_db = readSQL()
print("SQL Data:", saved_db)
numberplates = []
for i in saved_db:
    numberplates.append(i['vehicleNumber'])

if(carNo in numberplates):
    print("Found in Database")
    print(f"Name: {saved_db[carNo]['name']}\nType: {saved_db[carNo]['type']}")
for i in saved_db:
    global flagFound 
    flagFound = False
    if i['vehicleNumber'] == carNo:
        flagFound = True
        if i['ownerType'] in arr:
            print("Entry Permitted")
            gateOpen()
            writeToSQL(i['vehicleOwner'], i['vehicleNumber'], i['ownerType'], "True")
        else:
            print("Entry Denied - Owner Type Mismatch")
            writeToSQL(i['vehicleOwner'], i['vehicleNumber'], i['ownerType'], "False")
if not flagFound:
    print("Entry Denied - Not Found in Database")
    writeToSQL("Unkown", carNo, "Unknown", "False")