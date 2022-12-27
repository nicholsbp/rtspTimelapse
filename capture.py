import cv2
import time
import datetime

# RTSP stream URL
rtsp_url = 'rtsp://yourRTSPsource.lan/stream_1080'


while True:
    # OpenCV video capture object
    cap = cv2.VideoCapture(rtsp_url)

    # Capture frame
    ret, frame = cap.read()

    now = datetime.datetime.now()

    # Format date and time for use in filename
    filename = f"image_{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}_{now.second}.jpg"

    # Save frame as JPEG image
    cv2.imwrite(filename, frame)
    
    cap.release()
    
    # Wait 
    time.sleep(3600)


