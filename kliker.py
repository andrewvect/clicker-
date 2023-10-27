from datetime import datetime, timedelta
import pyautogui
import time
from service import Calendar

import pyperclip

screenWidth, screenHeight = pyautogui.size()
time.sleep(1)


class Clicks:

    def __init__(self, message, hours):
        self.message = message
        self.send_big_blue_button_coordinate = None
        self.message_input_box_coordinate = None
        self.date_window_box_coordinate = None
        self.button_with_paper_plane_coordinate = None
        self.button_with_schedule_menu = None
        self.button_with_time_set_menu = None
        self.button_with_time_minuets_menu = None
        self.button_with_time_seconds_menu = None
        self.next_month_button = None
        self.time_wait = 2
        self.days = None
        self.minuets = None
        self.list_time_intervals = self.next_day_time_steps(hours)

    def next_day_time_steps(self, hours):
        current_time = datetime.now()
        next_day = current_time + timedelta(days=1)
        time_steps = []
        while current_time < next_day:
            hours2 = ''
            minuets = ''

            if len(str(current_time.hour)) == 1:
                hours2 = '0' + str(current_time.hour)
            else:
                hours2 = str(current_time.hour)
            if len(str(current_time.minute)) == 1:
                minuets = '0' + str(current_time.minute)
            else:
                minuets = str(current_time.minute)

            time_steps.append([hours2, minuets])

            current_time += timedelta(hours=hours)

        time_steps.append(time_steps[0])
        time_steps.pop(0)

        return time_steps

    def click_to_input_message(self, x, y):
        pyautogui.click(x, y)
        time.sleep(0.5)

    def paste_message(self):
        pyperclip.copy(self.message)
        time.sleep(0.25)
        pyautogui.hotkey('command', 'v')

    def push_enter_keyboard(self):
        pyautogui.press('enter')

    def push_right_click(self, x, y):
        pyautogui.rightClick(x, y)
        time.sleep(0.25)

    def push_schedule_button_menu(self, x, y):
        pyautogui.rightClick(x, y)
        time.sleep(0.25)

    def set_time_to_schedule(self, hours, minuets):
        pyautogui.click(self.button_with_time_set_menu[0], self.button_with_time_set_menu[1])
        time.sleep(0.25)
        pyautogui.write(str(hours))
        time.sleep(0.25)
        pyautogui.click(self.button_with_time_minuets_menu[0], self.button_with_time_minuets_menu[1])
        time.sleep(0.25)
        pyautogui.write(str(minuets))
        time.sleep(0.25)
        pyautogui.click(self.button_with_time_seconds_menu[0], self.button_with_time_seconds_menu[1])
        time.sleep(0.25)
        pyautogui.write('00')

    def set_date_to_schedule(self, x, y):
        pyautogui.click(x, y)
        time.sleep(0.5)

    def push_button_send_schedule(self, x, y):
        pyautogui.click(x, y)

    def push_to_calendar_button(self):
        calendar = Calendar(200, 405)
        buttons = calendar.get_coordinates_for_current_month()
        buttons2 = calendar.get_coordinates_for_next_month()

        for i in range(len(buttons)):

            for time_interval in self.list_time_intervals:
                self.click_to_input_message(71.71, 625.16)
                time.sleep(self.time_wait)

                self.paste_message()
                time.sleep(self.time_wait)
                self.push_enter_keyboard()
                time.sleep(self.time_wait)

                pyautogui.click(230, 340)
                time.sleep(self.time_wait)
                pyautogui.click(buttons[i][0], buttons[i][1])

                time.sleep(self.time_wait)
                self.set_time_to_schedule(time_interval[0], time_interval[1])

                pyautogui.click(315, 400)
                time.sleep(self.time_wait)

        for i in range(len(buttons2)):

            for time_interval in self.list_time_intervals:
                self.click_to_input_message(71.71, 625.16)
                time.sleep(self.time_wait)

                self.paste_message()
                time.sleep(self.time_wait)
                self.push_enter_keyboard()
                time.sleep(self.time_wait)

                pyautogui.click(230, 340)
                time.sleep(self.time_wait)
                pyautogui.click(self.next_month_button[0], self.next_month_button[1])
                time.sleep(self.time_wait)
                pyautogui.click(buttons2[i][0], buttons2[i][1])

                time.sleep(self.time_wait)
                self.set_time_to_schedule(time_interval[0], time_interval[1])

                pyautogui.click(315, 400)
                time.sleep(self.time_wait)

    def first_message_start(self):

        pyautogui.click(self.message_input_box_coordinate[0], self.message_input_box_coordinate[1])
        time.sleep(self.time_wait)
        self.paste_message()
        time.sleep(self.time_wait)

        pyautogui.rightClick(self.button_with_paper_plane_coordinate[0], self.button_with_paper_plane_coordinate[1])
        time.sleep(self.time_wait)
        pyautogui.rightClick(self.button_with_schedule_menu[0], self.button_with_schedule_menu[1])
        time.sleep(self.time_wait)

        self.set_time_to_schedule( self.list_time_intervals[0][0], self.list_time_intervals[0][1])
        time.sleep(self.time_wait)
        pyautogui.click(self.send_big_blue_button_coordinate[0], self.send_big_blue_button_coordinate[1])
        time.sleep(self.time_wait)

        self.push_to_calendar_button()


try:
    clicker = Clicks('привет', 4)
    clicker.send_big_blue_button_coordinate = (300, 400)
    clicker.message_input_box_coordinate = (100, 620)
    clicker.date_window_box_coordinate = (230, 335)
    clicker.button_with_paper_plane_coordinate = (590, 625)
    clicker.button_with_schedule_menu = (643, 668)
    clicker.button_with_time_set_menu = (363, 339)
    clicker.button_with_time_minuets_menu = (397, 333)
    clicker.button_with_time_seconds_menu = (424, 335)
    clicker.time_wait = 1
    clicker.next_month_button = (451, 361)
    clicker.first_message_start()
except Exception as e:
    print(e)


