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
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Couldn't access the camera")
        return None
    
    ret, frame = camera.read() 
    if ret:
        t = time.time()
        fname = f"./temp/{t}_u.jpg"
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(fname, gray)
        print(f"Photo captured and saved as '{fname}'")

        img = cv2.imread(fname)
        if img is None:
            print(f"Error: Couldn't read the image file '{fname}'")
            return None

        resized_img = cv2.resize(img, (640, 480))
        fnamer = f"./temp/{t}.jpg"
        cv2.imwrite(fnamer, resized_img)
        print(f"Resized photo saved as '{fnamer}'")
        # Display the image 
        cv2.namedWindow('Captured Image', cv2.WINDOW_NORMAL)
    # Set the window to be always on top
        cv2.setWindowProperty('Captured Image', cv2.WND_PROP_TOPMOST, 1)
        cv2.imshow('Captured Image', resized_img)
        cv2.waitKey(2000)  # Wait for specified time
        cv2.destroyAllWindows()
        extracted_text = extract_text_from_image(fname)
        return extracted_text
    else:
        print("Error: Couldn't capture photo")
        return None