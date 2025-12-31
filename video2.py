import cv2
import time

cap = cv2.VideoCapture(2) # 2 — вторая камера
if not cap.isOpened():
    raise RuntimeError("Камера не открылась")
fps = 30
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("video2.mp4", fourcc, fps, (width, height))
duration = 20
end_time = time.time() + duration
while time.time() < end_time:
    ret, frame = cap.read()
    if not ret:
        print("Кадр не получен, пропускаю…")
        continue
    out.write(frame)
cap.release()
out.release()
print("Видео сохранено в video2.mp4")
