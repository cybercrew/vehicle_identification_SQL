import json
import time
def writeToJSON(param1, param2, param3):
    file_path = "data.json"
    try:
        with open(file_path, 'r') as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        existing_data = []
    new_data = {
        "vehicleOwner": param1,
        "vehicleNumber": param2,
        "type": param3,
        "timeEntered": time.strftime("%H:%M", time.localtime(time.time()))
    }
    existing_data.append(new_data)
    with open(file_path, 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)
def readJSON():
    file_path = "dbe.json"
    try:
        with open(file_path, 'r') as json_file:
            dbe = json.load(json_file)
            return dbe
    except FileNotFoundError:
        return []