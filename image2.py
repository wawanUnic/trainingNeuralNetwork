import cv2

cap = cv2.VideoCapture(2) # 2 — вторая камера в системе
if not cap.isOpened():
    raise RuntimeError("Камера не открылась")
ret, frame = cap.read()
if not ret:
    raise RuntimeError("Не удалось получить кадр")
cv2.imwrite("image2.jpg", frame)
cap.release()
print("Снимок сохранён в image2.jpg")
