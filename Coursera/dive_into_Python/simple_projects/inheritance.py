import os
import csv

PATH = os.getcwd()+"\\car_list.csv"


class CarBase:
    def __init__(self, photo_file_name, brand, carrying):
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying

    def get_photo_file_ext(self):
        # os.path.splitext
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, photo_file_name, brand, carrying, passenger_seats_count):
        super().__init__(photo_file_name, brand, carrying)
        self.car_type = "car"
        self.seats = passenger_seats_count


class Truck(CarBase):
    def __init__(self, photo_file_name, brand, carrying, body_whl):
        # The specification for size of body
        # They are split by the "x" char
        # The specs should be assigned as integer
        # If one of the spec is not valid - to assign 0 value to all specs
        super().__init__(photo_file_name, brand, carrying)
        self.car_type = "Truck"
        try:
            self.body_l = float(body_whl.split("x")[0])
            self.body_w = float(body_whl.split("x")[1])
            self.body_h = float(body_whl.split("x")[2])
        except ValueError:
            self.body_l = 0
            self.body_w = 0
            self.body_h = 0

    def get_body_volume(self):
        return self.body_h*self.body_l*self.body_w


class SpecMachine(CarBase):
    def __init__(self, photo_file_name,
                 brand, carrying, extra):
        super().__init__(photo_file_name, brand, carrying)
        self.car_type = "SpecMachine"
        self.extra = extra


@timer
def get_car_list(csv_filename):
    print("Twice or once")
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        counter = 0
        for count, row in enumerate(reader):
            try:
                if row[3] and row[1] and row[5]:
                    if row[0] == "car":
                        count = Car(row[3], row[1], row[5], row[2])
                        car_list.append(count)
                    elif row[0] == "truck":
                        count = Truck(row[3], row[1], row[5], row[4])
                        car_list.append(count)
                    elif row[0] == "spec_machine":
                        count = SpecMachine(row[3], row[1], row[5], row[6])
                        car_list.append(count)
                    else:
                        continue
            except IndexError:
                continue
    return car_list


truck = Truck('nissan.jpeg', 'Nissan', '1.5', '3.92x2.09x1.87')
# print(truck.car_type, truck.brand, truck.photo_file_name, truck.body_l, truck.body_w, truck.body_h, sep='\n')
spec_machine = SpecMachine('d355.jpg', 'Komatsu-D355', '93', 'pipelayer specs')
# print(spec_machine.car_type, spec_machine.brand, spec_machine.carrying, spec_machine.photo_file_name, spec_machine.extra, sep='\n')
# print(spec_machine.get_photo_file_ext())
cars = get_car_list(PATH)
print(cars[0].seats)
print(cars[1].get_body_volume())
