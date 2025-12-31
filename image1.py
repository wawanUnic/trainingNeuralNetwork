import cv2

cap = cv2.VideoCapture(0) # 0 — первая камера в системе
if not cap.isOpened():
    raise RuntimeError("Камера не открылась")
ret, frame = cap.read()
if not ret:
    raise RuntimeError("Не удалось получить кадр")
cv2.imwrite("image1.jpg", frame)
cap.release()
print("Снимок сохранён в image1.jpg")
