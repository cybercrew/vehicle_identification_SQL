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
if(x1==4):
    arr = ["faculty", "guest"]
carNo = withoutSpecialCharacters(capture_photo()) #Working
print(carNo)
#print(readJSON()) #
initialiseTable()
J = readSQL()
print("SQL Data:", J)
def gateOpen():
    #Opens Gate
    print("Gate Opened")
if(carNo in J):
    print("Found in Database")
    print(f"Name: {J[carNo]['name']}\nType: {J[carNo]['type']}")
    if(J[carNo]['type'] in arr):
        print("Entry Permitted")
        gateOpen()
        writeToSQL(readSQL()[carNo]['name'], carNo, readSQL()[carNo]['type'])
    else:
        print("Entry Denied")
else:
    print("Entry Denied")