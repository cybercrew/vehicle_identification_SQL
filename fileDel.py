import os
import schedule

def delete_file():
    try:
        os.remove("data.json")
        print("File deleted")
    except FileNotFoundError:
        print("File not found.")

schedule.every().day.at("00:00").do(delete_file)

def deleteAtMidnight():
    while True:
        schedule.run_pending()