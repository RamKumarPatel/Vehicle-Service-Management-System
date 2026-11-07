# ==============================================================
#              VEHICLE SERVICE MANAGEMENT SYSTEM
# ==============================================================

# Student Name          : RAM KUMAR PATEL
# ERP ID                : RU-26-01758
# Course                : BCA 1B
# Programming Language  : Python 3
# Project Number        : PS No. 76
# Project Description   : Manage vehicle service records, add
#                         new services, calculate GST, update
#                         service status and delete records.

# ==============================================================


# ------------------------- CONSTANTS --------------------------

# Stores service names and their prices

services = {
    "Oil Change": 1500,
    "Wheel Alignment": 800,
    "Full Service": 4500,
    "Brake Repair": 2200
}

# Available vehicle types

vehicle_options = {
    "1": "Car",
    "2": "Bike",
    "3": "Scooter",
    "4": "Truck",
    "5": "Bus",
    "6": "Auto Rickshaw",
    "7": "Other"
}

# Available service options

service_options = {
    "1": "Oil Change",
    "2": "Wheel Alignment",
    "3": "Full Service",
    "4": "Brake Repair"
}

# Available service statuses

status_options = {
    "1": "Pending",
    "2": "In Progress",
    "3": "Completed"
}

GST_RATE = 0.18


# ------------------------- DATA STORAGE -----------------------

# Dictionary to store all service records

records = {}


# ==============================================================
#                  CLASS: SERVICE RECORD
# ==============================================================

class ServiceRecord:

    # Initialize service record details

    def __init__(self, reg_no, owner, vehicle, service):

        self.reg_no = reg_no
        self.owner = owner
        self.vehicle = vehicle
        self.service = service

        # Calculate service cost including 18% GST

        self.cost = services[service] * (1 + GST_RATE)

        # Default service status

        self.status = "Pending"

    # Display complete service record

    def display(self):

        print("\n========== SERVICE RECORD ==========")
        print("Registration No:", self.reg_no)
        print("Owner:", self.owner)
        print("Vehicle:", self.vehicle)
        print("Service:", self.service)
        print("Cost including 18% GST: Rs.", f"{self.cost:.2f}")
        print("Status:", self.status)
        print("====================================")


# ==============================================================
#                  FUNCTION 1: GET CHOICE
# ==============================================================

# Accepts both numeric choices and text inputs

def get_choice(value, options):

    value = value.strip()

    if value in options:
        return options[value]

    for item in options.values():

        if value.lower() == item.lower():
            return item

    return None


# ==============================================================
#                  FUNCTION 2: SAVE RECORDS
# ==============================================================

# Saves all records into a text file

def save_records():

    with open("services.txt", "w") as file:

        for record in records.values():

            file.write(
                record.reg_no + "|" +
                record.owner + "|" +
                record.vehicle + "|" +
                record.service + "|" +
                record.status + "\n"
            )


# ==============================================================
#                  FUNCTION 3: LOAD RECORDS
# ==============================================================

# Loads previously saved records from the text file

def load_records():

    try:

        with open("services.txt", "r") as file:

            for line in file:

                parts = line.strip().split("|")

                if len(parts) == 5:

                    reg_no, owner, vehicle, service, status = parts

                    if service in services:

                        record = ServiceRecord(
                            reg_no, owner, vehicle, service
                        )

                        record.status = status

                        records[reg_no] = record

    except FileNotFoundError:

        pass


# ==============================================================
#                  FUNCTION 4: ADD NEW RECORD
# ==============================================================

# Adds a new vehicle service record

def add_record():

    print("\n---------- ADD NEW RECORD ----------")

    reg_no = input("Enter Registration No: ").strip().upper()

    if not reg_no or "|" in reg_no:

        print("Invalid registration number!")
        return

    if reg_no in records:

        print("Record already exists!")
        return

    owner = input("Enter Owner Name: ").strip()

    if not owner or "|" in owner:

        print("Invalid owner name!")
        return

    # Select vehicle type

    print("\nSelect Vehicle Type:")

    for key, value in vehicle_options.items():

        print(key + ". " + value)

    vehicle_input = input("Enter Vehicle Type: ")

    vehicle = get_choice(vehicle_input, vehicle_options)

    if vehicle is None:

        print("Invalid vehicle choice!")
        return

    # Select service type

    print("\nAvailable Services:")

    for key, value in service_options.items():

        print(
            key + ". " + value +
            " - Rs. " + str(services[value])
        )

    service_input = input("Enter Service: ")

    service = get_choice(service_input, service_options)

    if service is None:

        print(
            "Invalid service type. Choose from: "
            "Oil Change, Wheel Alignment, Full Service, Brake Repair."
        )
        return

    # Create and store new service record

    record = ServiceRecord(
        reg_no, owner, vehicle, service
    )

    records[reg_no] = record

    save_records()

    # Display confirmation message

    print(
        f"Record added. {reg_no} | {service} | "
        f"Cost incl. 18% GST: Rs. {record.cost:.2f} | "
        f"Status: {record.status}"
    )


# ==============================================================
#                  FUNCTION 5: VIEW RECORD
# ==============================================================

# Searches and displays a particular service record

def view_record():

    reg_no = input("Enter Registration No: ").strip().upper()

    if reg_no in records:

        records[reg_no].display()

    else:

        print(f"No record found for {reg_no}.")


# ==============================================================
#                  FUNCTION 6: UPDATE STATUS
# ==============================================================

# Updates the status of an existing service record

def update_status():

    reg_no = input("Enter Registration No: ").strip().upper()

    if reg_no not in records:

        print(f"No record found for {reg_no}.")
        return

    # Display available statuses

    print("\nSelect New Status:")
    print("1. Pending")
    print("2. In Progress")
    print("3. Completed")

    status_input = input("Enter New Status: ")

    new_status = get_choice(status_input, status_options)

    if new_status is None:

        print("Invalid choice!")
        return

    # Update old status with new status

    old_status = records[reg_no].status

    records[reg_no].status = new_status

    save_records()

    print(f"Status updated: {old_status} -> {new_status}")


# ==============================================================
#                  FUNCTION 7: DELETE RECORD
# ==============================================================

# Deletes an existing service record

def delete_record():

    reg_no = input("Enter Registration No: ").strip().upper()

    if reg_no in records:

        del records[reg_no]

        save_records()

        print(f"Record for {reg_no} deleted.")

    else:

        print(f"No record found for {reg_no}.")


# ==============================================================
#                  FUNCTION 8: VIEW ALL RECORDS
# ==============================================================

# Displays all available service records

def view_all_records():

    if not records:

        print("No service records available!")
        return

    print("\n========== ALL SERVICE RECORDS ==========")

    for record in records.values():

        record.display()

    print("\nTotal Records:", len(records))


# ==============================================================
#                  MAIN FUNCTION
# ==============================================================

# Controls the complete Vehicle Service Management System

def main():

    # Load previously saved records

    load_records()

    # Display main menu

    print("\nVEHICLE SERVICE MANAGEMENT")
    print("1. Add Record")
    print("2. View Record")
    print("3. Update Service Status")
    print("4. Delete Record")
    print("5. View All Records")
    print("6. Exit")

    # Execute menu options

    while True:

        try:

            choice = input("\nEnter your choice: ").strip()

            if choice == "1":

                add_record()

            elif choice == "2":

                view_record()

            elif choice == "3":

                update_status()

            elif choice == "4":

                delete_record()

            elif choice == "5":

                view_all_records()

            elif choice == "6":

                print("Thank you for using Vehicle Service Management!")
                break

            else:

                print("Invalid choice! Please select 1 to 6.")

        except (KeyboardInterrupt, EOFError):

            print("\nProgram closed.")
            break


# ==============================================================
#                  PROGRAM EXECUTION
# ==============================================================

if __name__ == "__main__":

    main()

# ======================== END OF PROJECT ======================
