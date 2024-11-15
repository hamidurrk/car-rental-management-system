# Fall-2024, 2nd period, CT60A0250 
# Project work - Car Rental Management System
#
# Submitted by: Md Hamidur Rahman Khan
# Student ID: 002475552

from datetime import datetime

class CarRentalManagementSystem:
    def __init__(self):
        self.APP_NAME = "Car Rental Management System"
        self.AUTHOR = "Md Hamidur Rahman Khan"
        self.APP_WIDTH = 80
        
        self.VEHICLES_FILE = "files/vehicles.txt"
        self.CUSTOMERS_FILE = "files/customers.txt"
        self.RENTED_VEHICLES_FILE = "files/rentedVehicles.txt"
        self.TRANSACTION_FILE = "files/transActions.txt"
        
        self.open_files()
        self.theme = {
            "title": "magenta",
            "info": "blue",
            "normal": "white",
            "error": "red",
            "warning": "yellow",
            "success": "green"
        }
        self.menu_options = {
                "1": "List available cars",
                "2": "Rent a car",
                "3": "Return a car",
                "4": "Count the money",
                "0": "Exit"
            }
        self.available_cars_table_header = ["Reg. No.", "Model", "Price/Day", "Features"]
        
    def __del__(self):
        self.close_files()
    
    def open_files(self):
        self.vehicle_file = open(self.VEHICLES_FILE, "r+")
        self.customer_file = open(self.CUSTOMERS_FILE, "a+")
        self.rented_vehicle_file = open(self.RENTED_VEHICLES_FILE, "a+")
        self.transaction_file = open(self.TRANSACTION_FILE, "a")
    
    def close_files(self):
        self.customer_file.close()
        self.vehicle_file.close()
        self.rented_vehicle_file.close()
        self.transaction_file.close()
    
    def truncate_file(self, file_name):
        file = open(file_name, "w")
        file.truncate(0)
        file.close()
    
    def reinitialize(self):
        self.close_files()
        self.open_files()
    
    def get_data(self, file):
        data = []
        file = file.readlines()
        for line in file:
            data.append(line.strip().split(","))
        return data
        
    def get_vehicle_data(self):
        self.reinitialize()
        return self.get_data(self.vehicle_file)
    
    def get_customer_data(self):
        self.reinitialize()
        return self.get_data(self.customer_file)
    
    def get_rented_vehicle_data(self):
        self.reinitialize()
        return self.get_data(self.rented_vehicle_file)
    
    def get_transaction_data(self):
        self.reinitialize()
        return self.get_data(self.transaction_file)
  
    def write_data(self, file, data):
        file.write(data)
    
    def write_customer_data(self, data):
        self.write_data(self.customer_file, data)
    
    def write_rented_vehicle_data(self, data):
        self.write_data(self.rented_vehicle_file, data)
        
    def write_transaction_data(self, data):
        self.write_data(self.transaction_file, data)
                
    def list_to_csv(self, data: list):
        return "".join([",".join(data)])+"\n"
    
    def search_data(self, data: list, search_value: str):
        for line in data:
            if search_value in line:
                return line
        return None
            
    def remove_data_from_rented_vehicles(self, license_plate: str):
        rented_vehicles = self.get_rented_vehicle_data()
        print(rented_vehicles)
        for i, line in enumerate(rented_vehicles):
            if license_plate in line:
                del rented_vehicles[i]
                break    
        self.truncate_file(self.RENTED_VEHICLES_FILE)
        for vehicle in rented_vehicles:
            print(self.list_to_csv(vehicle))
            self.write_rented_vehicle_data(self.list_to_csv(vehicle))
      
    def print_colored(self, text, color, end="", will_return=True):
        colors = {
            "red": "\033[91m",
            "green": "\033[92m",
            "yellow": "\033[93m",
            "blue": "\033[94m",
            "magenta": "\033[95m",
            "cyan": "\033[96m",
            "white": "\033[97m",
            "reset": "\033[0m"
        }
        
        if will_return:
            return f"{colors.get(color, colors['reset'])}{text}{colors['reset']}"
        else:
            print(f"{colors.get(color, colors['reset'])}{text}{colors['reset']}", end=end)
            
    def print_title(self, text):
        return self.print_colored(text, self.theme["title"])
        
    def print_info(self, text):
        return self.print_colored(text, self.theme["info"])
    
    def print_normal(self, text):
        return self.print_colored(text, self.theme["normal"])
    
    def print_success(self, text):
        return self.print_colored(text, self.theme["success"])
    
    def print_warning(self, text):
        return self.print_colored(text, self.theme["warning"])
    
    def print_error(self, text):
        return self.print_colored(text, self.theme["error"])
    
    def print_bar(self, char="-"):
        value = self.APP_WIDTH
        print(f"{char*value}")
        
    def println(self, message: str = "", char="|", center=False, adjust=0):
        value = self.APP_WIDTH
        if message != "":
            wrt = f"{message}"
        else:
            wrt = f" "
        if center:
            print(f"{char}{wrt.center(value+7+adjust)}{char}")
        else:
            print(f"{char} {wrt.ljust(value-4+adjust)} {char}")

    def print_section_title(self, title):
        self.print_bar("=")
        self.println(self.print_info(title), center=True)
        self.print_bar("=")
                
    def print_header(self, header:str):
        # self.println(char="\u2588")
        self.print_bar("=")
        self.println(self.print_title(header), center=True)
        self.print_bar("=")
        
    def print_footer(self):
        self.print_bar("=")
        self.println(self.print_title(f"Developed by: {self.AUTHOR}"), center=True)
        self.print_bar("=")
    
    def take_input(self, prompt):
        print(f"\033[D| {prompt}", end='')
        input_value = input()
        print(f"\033[F", end='')
        print(f"\033[{self.APP_WIDTH}G|")
        return input_value

    def print_list(self, list):
        for line in list:
            for value in line:
                print(value, end=2*"\t")
            print("")
            
    def print_table(self, data, title=None,headers=None):
        if headers:
            modified_headers = []
            for header in headers:
                header = self.print_title(header)
                modified_headers.append(header)
            data.insert(0, headers)
        max_cols = max(len(row) for row in data)
        col_widths = [0] * max_cols
        for row in data:
            for i, item in enumerate(row):
                col_widths[i] = max(col_widths[i], len(str(item)))

        if title:
            title = self.print_info(title)
            print("---".join("-" * width for width in col_widths))
            print(f"{title.center(sum(col_widths)+((len(col_widths))*2)+1)}")
            print("---".join("-" * width for width in col_widths))
            
        if headers:
            data.remove(data[0])
            print("=+=".join("=" * width for width in col_widths))
            print(" | ".join(f"{str(item).center(width)}" for item, width in zip(headers, col_widths)))
            print("=+=".join("=" * width for width in col_widths))
        else:
            print("-+-".join("-" * width for width in col_widths))
        
        for row in data:
            padded_row = row + [""] * (max_cols - len(row))
            print(" | ".join(f"{str(item).ljust(width)}" for item, width in zip(padded_row, col_widths)))
            print("-+-".join("-" * width for width in col_widths))
    
    def age(self, birthday: str):
        today = datetime.now()
        return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
                    
    def menu(self, count):
        if count == 0:
            self.print_header(header=self.APP_NAME)
        else:
            self.print_header(header="Main Menu")

        for key, value in self.menu_options.items():
            self.println(self.print_info(f"{key}) {value}"), adjust=9)
        while True:
            try:
                option_choice = int(self.take_input("Enter a choice [0-4]: "))
                option = self.menu_options[str(option_choice)]
                break
            except ValueError:
                self.println(self.print_error("Enter the selection as an integer."), adjust=9)
            except KeyError:
                self.println(self.print_error("Unknown selection, please try again."), adjust=9)
        self.print_bar("=")
        return option
    
    def list_available_cars(self, return_cars=False):
        vehicles = self.get_vehicle_data()
        rented_vehicles = self.get_rented_vehicle_data()
        available_vehicles = []
        
        for vehicle in vehicles:
            if self.search_data(rented_vehicles, vehicle[0]) == None:
                available_vehicles.append(vehicle)
        if return_cars:
            return available_vehicles
        else:
            self.print_table(available_vehicles, title="Available Cars", headers=self.available_cars_table_header)
    
    def rent_a_car(self):
        is_car_available = True
        is_valid_birthday = False
        is_new_customer = False
        new_rent_query = []
        
        self.print_section_title("Rent a Car")
        input_car_no = self.take_input("Enter registration number: ")
        if self.search_data(self.get_vehicle_data(), input_car_no) == None:
            self.println(self.print_error("Car not owned by the company."), adjust=9)
        else:
            if self.search_data(self.list_available_cars(return_cars=True), input_car_no) == None:
                self.println(self.print_error(f"Car with registration number {input_car_no} is being rented."), adjust=9)
                self.println(self.print_warning(f"Please pick another car from the available ones."), adjust=9)
            else:
                self.println(self.print_success(f"Car with registration number {input_car_no} is available."), adjust=9)
                is_car_available = True
        
        if is_car_available:
            while True:
                input_birthday = self.take_input("Please enter your birthday (DD/MM/YYYY): ")
                input_birthday_format = input_birthday.split("/")
                input_birthday_format = [len(item) for item in input_birthday_format]
                if len(input_birthday_format) != 3 or input_birthday_format[0] != 2 or input_birthday_format[1] != 2 or input_birthday_format[2] != 4:
                    self.println(self.print_error("Invalid date format."), adjust=9)
                    self.println(self.print_warning("Please enter the date in DD/MM/YYYY format."), adjust=9)
                    continue
                else:
                    try:
                        input_birthday = datetime.strptime(input_birthday, "%d/%m/%Y")
                        if input_birthday > datetime.now():
                            self.println(self.print_error("Date is in the future."), adjust=9)
                            self.println(self.print_warning("Please enter a valid date."), adjust=9)
                            continue
                        else:
                            is_valid_birthday = True
                            break
                    except ValueError:
                        self.println(self.print_error("Date is invalid."), adjust=9)
                        self.println(self.print_warning("Please enter a valid date."), adjust=9)
        
        if is_valid_birthday:
            if self.search_data(self.get_customer_data(), input_birthday.strftime("%d/%m/%Y")) == None:
                if self.age(input_birthday) < 18:
                    self.println(self.print_warning("You must be at least 18 years old to rent a car."), adjust=9)
                elif self.age(input_birthday) > 75:
                    self.println(self.print_warning("You must be younger than 75 years old to rent a car."), adjust=9)
                else:
                    self.println(self.print_success("You are eligible to rent a car."), adjust=9)
                    self.print_bar("-")
                    self.println(self.print_title("Welcome to our car rental service!"),center=True)
                    self.print_bar("-")
                    self.println(self.print_info("Please register with your information below:"), adjust=9)
                    is_new_customer = True
            else:
                customer_info = self.search_data(self.get_customer_data(), input_birthday.strftime("%d/%m/%Y"))
                new_rent_query.append(input_car_no)
                self.print_bar("-")
                self.println(f"{self.print_normal("Hi,")} {self.print_title(f"{customer_info[1]}!")} {self.print_normal("Welcome back to our service!")}", adjust=27)
                self.print_bar("-")
                new_rent_query.append(input_birthday.strftime("%d/%m/%Y")) 
                self.println(f"{self.print_normal("Car with registration number")} {self.print_success(input_car_no)} {self.print_normal("has been assigned to you.")}", adjust=27)
                new_rent_query.append(datetime.now().strftime("%d/%m/%Y %H:%M"))
                self.write_rented_vehicle_data(self.list_to_csv(new_rent_query))
                self.println(self.print_success(f"Rent for {input_car_no} started successfully!"), adjust=9)
    
    def main(self):
        iteration_count = 0
        while True:
            option = self.menu(iteration_count)
            match option:
                case "List available cars":
                    self.list_available_cars()
                case "Rent a car":
                    self.rent_a_car()
                case "Return a car":
                    pass
                case "Count the money":
                    pass
                case "Exit":
                    self.println(self.print_success("See you again!"), adjust=9)
                    break
            iteration_count += 1
        self.print_footer()
                
if __name__ == "__main__":
    system = CarRentalManagementSystem()
    # system.main()
    # system.rent_a_car()
    system.write_rented_vehicle_data(system.list_to_csv(['KOL-99', '12/12/1985', '16/11/2024 01:05']))