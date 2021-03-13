import cv2
import dlib

cap = cv2.VideoCapture(2)
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

while True:
    ret, image = cap.read()
    if(ret):
        detector = dlib.get_frontal_face_detector()
        dets = detector(image, 1)
        for d in dets:
            shape = predictor(image, d)
            points = shape.parts()
            if (points[66].y - points[62].y) > 15:
                print("Open")
            else:
                print("close")
            # for point in points:
            #     image = cv2.circle(image, (point.x, point.y), 3, (255, 0, 0), 2)

        cv2.imshow("My Camera", image)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break
    elif key == ord("c"):
        cv2.imwrite("classroom.png", image)

