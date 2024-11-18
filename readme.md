# Car Rental Management System

## Description
A Python-based system to manage car rentals, including listing available cars, renting a car, returning a car, and calculating total revenue. The system features a custom terminal interface for an enhanced user experience.

## Features
1. **List Available Cars**:
The system can list all available cars that are not currently rented. It reads data from the vehicles.txt and rentedVehicles.txt files to determine which cars are available.

2. **Rent a Car**:
Customers can rent a car by providing their details and the registration number of the car they wish to rent. The system checks the availability of the car and validates customer information, including age and email. New customers are registered in the system, and rental details are recorded in the rentedVehicles.txt file.

3. **Return a Car**:
Customers can return a rented car by providing the car's registration number. The system calculates the total rent based on the rental period and updates the transaction details in the transActions.txt file. The car is then marked as available again.

4. **Count the Money**:
The system calculates the total revenue generated from all completed transactions. It reads data from the transActions.txt file and sums up the rental amounts.

## Custom Terminal Interface
The project includes a custom terminal interface with the following features:
- **Colored Text**: Different colors for titles, information, warnings, errors, and success messages.
- **Formatted Tables**: Displays data in well-formatted tables with headers.
- **Section Titles and Bars**: Clear section titles and bars to separate different parts of the interface.
- **Centered and Adjusted Text**: Options to center text and adjust its position for better readability.

## Data Files
`vehicles.txt`: Contains information about all vehicles owned by the company.
`customers.txt`: Contains information about all registered customers.
`rentedVehicles.txt`: Contains information about currently rented vehicles.
`transActions.txt`: Contains information about completed rental transactions.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/hamidurrk/car-rental-management-system.git
    ```
2. Navigate to the project directory:
    ```bash
    cd car-rental-management-system
    ```
3. Start the application:
    ```bash
    python src/project.py
    ```

## Usage
1. Start the application on your terminal.
2. Use the interface to manage cars, customers, and rentals.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Add feature"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-name
    ```
5. Create a pull request.

## Code Structure
- `CarRentalManagementSystem`: Main class implementing the system functionalities.
  - `list_available_cars()`: Lists all available cars.
  - `rent_a_car()`: Handles the process of renting a car.
  - `return_a_car()`: Handles the process of returning a rented car.
  - `count_the_money()`: Calculates and displays the total revenue.
  - `get_vehicle_data()`: Reads vehicle data from the file.
  - `get_customer_data()`: Reads customer data from the file.
  - `get_rented_vehicle_data()`: Reads rented vehicle data from the file.
  - `get_transaction_data()`: Reads transaction data from the file.
  - `write_data()`: Writes data to a file.
  - `write_customer_data()`: Writes customer data to the file.
  - `write_rented_vehicle_data()`: Writes rented vehicle data to the file.
  - `write_transaction_data()`: Writes transaction data to the file.
  - `list_to_csv()`: Converts a list to a CSV format.
  - `search_data()`: Searches for specific data in a list.
  - `remove_data_from_rented_vehicles()`: Removes data from rented vehicles.
  - `date_obj()`: Converts a date string to a datetime object.
  - `print_colored()`: Prints colored text.
  - `print_title()`: Prints a title.
  - `print_info()`: Prints information.
  - `print_normal()`: Prints normal text.
  - `print_success()`: Prints a success message.
  - `print_warning()`: Prints a warning message.
  - `print_error()`: Prints an error message.
  - `print_bar()`: Prints a bar.
  - `println()`: Prints a line with optional formatting.
  - `print_section_title()`: Prints a section title.
  - `print_header()`: Prints a header.
  - `print_footer()`: Prints a footer.
  - `take_input()`: Takes input from the user.
  - `print_list()`: Prints a list.
  - `print_table_cell_line()`: Prints a table cell line.
  - `custom_join()`: Joins strings with a custom separator.
  - `print_table()`: Prints a table.
  - `age()`: Calculates age.
  - `check_name()`: Checks if a name is valid.
  - `check_email()`: Checks if an email is valid.
  - `calculate_and_parse_rent_details()`: Calculates and parses rent details.
  - `check_rent_calculation()`: Checks rent calculation.