import calendar
from datetime import datetime, timedelta


def add_30_days():
    # Получаем текущую дату
    current_date = datetime.now()

    # Добавляем 30 дней
    future_date = current_date + timedelta(days=30)

    return future_date


today = datetime.now().strftime('%A')


class Calendar:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grid_step = 40
        self.num_columns = 7
        self.num_rows = 6
        self.number_of_current_month = datetime.now().month
        self.first_day_coordinate = self.get_first_number_of_date_of_the_month_number(self.get_first_day_month_in_str())
        self.table_coordinates = self.create_table_coordinates()

    def create_table_coordinates(self):
        coordinates = []
        for i in range(self.num_rows):
            current_x = self.x
            for j in range(self.num_columns):
                coordinates.append([current_x, self.y])
                current_x += self.grid_step
            self.y += self.grid_step
        return coordinates

    def get_first_day_month_in_str(self):
        current_date = datetime.now()
        first_day_of_month = datetime(current_date.year, current_date.month, 1)
        day_of_week = first_day_of_month.strftime("%A")
        return day_of_week

    def get_first_day_month_in_str__(self, year, month):
        first_day_of_month = datetime(year, month, 1)
        day_of_week = first_day_of_month.strftime("%A")
        return day_of_week

    def get_first_number_of_date_of_the_month_number(self, week_day_name):
        week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        key_week_number = week_days.index(week_day_name)
        return key_week_number

    def get_days_in_current_month(self):
        # Получаем текущую дату
        current_date = datetime.now()

        # Находим количество дней в текущем месяце
        days_in_month = calendar.monthrange(current_date.year, current_date.month)[1]

        return days_in_month

    def get_current_day(self):
        current_day = datetime.now().day
        return current_day

    def get_coordinates_for_current_month(self):
        first_day = self.first_day_coordinate + self.get_current_day()
        last_day = self.first_day_coordinate + self.get_days_in_current_month()
        return self.table_coordinates[first_day:last_day]

    def get_first_day_next_month(self):
        current_date = datetime.now()

        first_day_next_month = datetime(current_date.year, current_date.month % 12 + 1, 1)

        day_of_week = first_day_next_month.strftime("%A")
        return day_of_week

    def get_coordinates_for_next_month(self):
        number_of_days_in_next_month = 30 - (30 - self.get_current_day())
        first_day = self.get_first_number_of_date_of_the_month_number(self.get_first_day_next_month())
        last_day = first_day + number_of_days_in_next_month
        return self.table_coordinates[first_day:last_day]


# calendar_br = Calendar(200, 405)
# calendar_br.get_coordinates_for_next_month()

def next_day_time_steps(hours):
    current_time = datetime.now()
    next_day = current_time + timedelta(days=1)
    time_steps = []
    while current_time < next_day:
        time_steps.append([current_time.hour, current_time.minute])
        current_time += timedelta(hours=hours)

    time_steps.append(time_steps[0])
    time_steps.pop(0)

    return time_steps

hours = 4
result = next_day_time_steps(hours)
for time_step in result:
    print(time_step)
