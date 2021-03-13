import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, image = cap.read()
    if(ret):
        cv2.imshow("My Camera", image)

    key = cv2.waitKey(30)

    if key == ord("q"):
        break
    elif key == ord("c"):
        cv2.imwrite("classroom.png", image)

