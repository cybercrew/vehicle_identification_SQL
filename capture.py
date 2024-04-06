import cv2
import time
from PIL import Image
import pytesseract

fName = ""
def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        
        text = pytesseract.image_to_string(img)
        
        return text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
def capture_photo():
    #camera = cv2.VideoCapture(0)

    #if not camera.isOpened():
        #print("Error: Couldn't access the camera")
       # return
    
   #ret, frame = camera.read() #if ret:
    i = cv2.imread("sample.png")
    cv2.imshow('Captured Photo', i)
    time.sleep(0.5)
    gray = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
    t = time.time()
    cv2.imwrite(f'./temp/{t}_u.jpg', gray)
    fname = f"./temp/{t}_u.jpg"
    img = cv2.imread(fname)
    """
    resized_img = cv2.resize(img, (640, 480))
    fnamer = f"./temp/{t}.jpg"
    cv2.imwrite(fnamer, resized_img)
    """
    print(f"Photo captured and saved as '{t}_u.jpg'")
    extracted_text = extract_text_from_image(fname)
    #cv2.destroyAllWindows()
    return extracted_text
   # else:
  #      print("Error: Couldn't capture photo")

    #camera.release()