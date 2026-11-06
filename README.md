# Vehicle Service Management System

A menu-driven Python application for managing vehicle service records.
The system allows users to add, view, update, and delete service
records, calculate service cost including 18% GST, and save records in a
text file.

## Project Details

  Field                  Details
  ---------------------- -----------------
  Student Name           RAM KUMAR PATEL
  ERP ID                 RU-26-01758
  Course                 BCA 1B
  Programming Language   Python 3
  Project Number         PS No. 76

## Features

1.  **Add Record** -- Enter a vehicle registration number, owner name,
    vehicle type, and service type.
2.  **View Record** -- Search for and display a record using its
    registration number.
3.  **Update Service Status** -- Change a service status to Pending, In
    Progress, or Completed.
4.  **Delete Record** -- Remove an existing service record.
5.  **View All Records** -- Display all saved service records.
6.  **GST Calculation** -- Calculate the service cost including 18% GST.
7.  **File Storage** -- Save records in `services.txt` and load them
    when the program starts.

## Available Vehicle Types

-   Car
-   Bike
-   Scooter
-   Truck
-   Bus
-   Auto Rickshaw
-   Other

## Available Services

  Service             Base Price
  ----------------- ------------
  Oil Change           Rs. 1,500
  Wheel Alignment        Rs. 800
  Full Service         Rs. 4,500
  Brake Repair         Rs. 2,200

An additional 18% GST is included in the displayed service cost.

## Requirements

-   Python 3
-   No external Python packages are required.

## How to Run

1.  Download or clone this repository.
2.  Open a terminal in the project folder.
3.  Run the following command:

``` bash
python one.py
```

If your system uses the `python3` command, run:

``` bash
python3 one.py
```

## Data File

The program uses `services.txt` to store service records. The file is
created or updated automatically when records are saved. Keep this file
in the same folder as `one.py` when using the project.

## Main Menu

1.  Add Record
2.  View Record
3.  Update Service Status
4.  Delete Record
5.  View All Records
6.  Exit
