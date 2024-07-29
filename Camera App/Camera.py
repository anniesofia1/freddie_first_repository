import cv2

class CameraClass():
    def OpenCamera():
        cv2.namedWindow("Camera Preview")
        vc = cv2.VideoCapture(0)
    
        if vc.isOpened(): # try to get the first frame
            rval, frame = vc.read()
        else:
            rval = False
    
        while rval:
            cv2.imshow("Camera Preview", frame)
            cv2.setWindowProperty("Camera Preview", cv2.WND_PROP_TOPMOST, 1)
            rval, frame = vc.read()
            key = cv2.waitKey(20)
            if key == 27: # exit on ESC
                break
            
        vc.release()
        cv2.destroyWindow("Camera Preview")