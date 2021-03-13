import requests

out = requests.get("https://raw.githubusercontent.com/italojs/facial-landmarks-recognition/master/shape_predictor_68_face_landmarks.dat")

with open("shape_predictor_68_face_landmarks.dat", "wb") as f:
  f.write(out.content)