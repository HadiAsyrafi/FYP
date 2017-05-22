# import the necessary packages
from cam2 import PhotoBoothApp
from imutils.video import VideoStream
import time
 
# initialize the video stream and allow the camera sensor to warmup

print("[INFO] warming up camera...")
vs = VideoStream(0).start()
time.sleep(2.0)
		 
# start the app
pba = PhotoBoothApp(vs)
pba.root.mainloop()
