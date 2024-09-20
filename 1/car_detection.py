import cv2

# захват видео
cap = cv2.VideoCapture('cars.mp4')

# используем вычитание фона
fgbg = cv2.createBackgroundSubtractorMOG2()

# переменная для хранения центроидов предыдущего кадра
previous_centroids = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # применение вычитания фона для выделения движущихся объектов
    fgmask = fgbg.apply(frame)

    # устанавливаем глобальный порог для удаления теней
    retval, mask_thresh = cv2.threshold(fgmask, 80, 200, cv2.THRESH_BINARY)

    # морфологическая обработка для устранения шумов
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    fgmask = cv2.erode(fgmask, kernel, iterations=2)
    fgmask = cv2.dilate(fgmask, None, iterations=5)

    # поиск контуров на маске fgmask
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # ропределяем размер контуров
    contours = [cnt for cnt in contours if 15000 > cv2.contourArea(cnt) > 1000]

    frame_out = frame.copy()

    current_centroids = []

    for contour in contours:
        # определяем прямоугольник вокруг объекта
        (x, y, w, h) = cv2.boundingRect(contour)

        centroid_x = int(x + w / 2)
        centroid_y = int(y + h / 2)
        current_centroids.append((centroid_x, centroid_y))

        # рисуем прямоугольник
        frame_out = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # отслеживаем перемещение центроидов
    if previous_centroids:
        for prev, curr in zip(previous_centroids, current_centroids):
            delta_x = curr[0] - prev[0]
            delta_y = curr[1] - prev[1]

            direction = ''
            if delta_x > 0:
                direction += 'Right '
            elif delta_x < 0:
                direction += 'Left '

            if delta_y > 0:
                direction += 'Down'
            elif delta_y < 0:
                direction += 'Up'

            if direction:
                print(f"Car detected, x: {curr[0]}, y: {curr[1]}, moving {direction.strip()}")

    # обновляем предыдущие центроиды для следующего кадра
    previous_centroids = current_centroids

    # показываем изображение с обнаружением
    cv2.imshow('Frame', frame_out)
    cv2.imshow('Foreground Mask', fgmask)

    # выход по нажатию ESC
    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
