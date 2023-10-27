import numpy as np
import cv2
import pyautogui

# Получите разрешение экрана
screen = pyautogui.size()
screen_width, screen_height = screen.width, screen.height

# Создайте изображение-холст
canvas = np.zeros((screen_height, screen_width, 3), dtype=np.uint8)

# Задайте параметры прямоугольника, который вы хотите выделить
x, y, w, h = 100, 100, 300, 200

# Выделите область красным цветом
cv2.rectangle(canvas, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Покажите изображение с выделенной областью
cv2.imshow("Window", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
