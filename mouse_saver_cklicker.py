from pynput import mouse

# Имя файла для записи координат
filename = "mouse_clicks.txt"


# Функция для записи координат в файл
def on_click(x, y, button, pressed):
    if pressed:
        print(f'X:{x}, Y:{y}')
        # with open(filename, "a") as f:
        #     f.write(f"X: {x}, Y: {y}\n")

# Слушаем события кликов
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
