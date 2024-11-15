# Fall-2024, 2nd period, CT60A0250 
# Project work - Car Rental Management System
#
# Submitted by: Md Hamidur Rahman Khan
# Student ID: 002475552


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
        
    def __del__(self):
        self.close_files()
    
    def open_files(self):
        self.vehicle_file = open(self.VEHICLES_FILE, "r+")
        self.customer_file = open(self.CUSTOMERS_FILE, "a")
        self.rented_vehicle_file = open(self.RENTED_VEHICLES_FILE, "r+")
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
        
    def print_header(self):
        # self.println(char="\u2588")
        self.print_bar("=")
        self.println(self.print_title(self.APP_NAME), center=True)
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
    
    def menu(self):
        self.println("What do you want to do:")
        for key, value in self.menu_options.items():
            self.println(self.print_info(f"{key}) {value}"), adjust=9)
        while True:
            try:
                option_choice = int(self.take_input("Your choice: "))
                option = self.menu_options[str(option_choice)]
                break
            except ValueError:
                self.println(self.print_error("Enter the selection as an integer."), adjust=9)
            except KeyError:
                self.println(self.print_error("Unknown selection, please try again."), adjust=9)
        self.print_bar("=")
        return option
    
    def main(self):
        self.print_header()
        while True:
            option = self.menu()
            match option:
                case "List available cars":
                    pass
                case "Rent a car":
                    pass
                case "Return a car":
                    pass
                case "Count the money":
                    pass
                case "Exit":
                    self.println(self.print_success("See you again!"), adjust=9)
                    break
        self.print_footer()
                
if __name__ == "__main__":
    system = CarRentalManagementSystem()
    system.main()