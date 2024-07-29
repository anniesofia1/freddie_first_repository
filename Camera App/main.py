import Camera

start = input("Enter 1 to Open Camera: ")
try:
    if int(start) == 1:
        Camera.CameraClass.OpenCamera()
except:
    print("1 not entered.")
