import cx_Oracle
import tkinter as tk
from tkinter import ttk

# Define some constant values
MAIN_WIDTH = 400
MAIN_HEIGHT = 600

LOGIN_WIDTH = 200
LOGIN_HEIGHT = 100

RESULTS_WIDTH = 500
RESULTS_HEIGHT = 300

GRID_PAD = 5

# Set up UI main window
main_window = tk.Tk()
main_window.title('Clothing Store Application')

# Position window at the center of the screen
main_window.geometry(
    f'{MAIN_WIDTH}x{MAIN_HEIGHT}+{int(main_window.winfo_screenwidth() / 2 - MAIN_WIDTH / 2)}+{int(main_window.winfo_screenheight() / 2 - MAIN_HEIGHT / 2)}')

main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1)

# region account table


def create_account_table():
    # Set up UI results window
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    values = cursor.execute("""
        CREATE TABLE ACCOUNT(
        ACCOUNT_EMAIL VARCHAR2(100) PRIMARY KEY,
        ACCOUNT_PASSWORD VARCHAR2(100) NOT NULL,
        ACCOUNT_CARD_NUMBER VARCHAR2(12),
        CUSTOMER_ID VARCHAR2(100) UNIQUE NOT NULL,
        FOREIGN KEY(CUSTOMER_ID) REFERENCES CUSTOMER(CUSTOMER_ID))""")

    ttk.Label(results_window, text='Table created').pack(
        padx=GRID_PAD, pady=GRID_PAD)


def drop_account_table():
    # Set up UI results window
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    cursor.execute("""DROP TABLE ACCOUNT""")

    ttk.Label(results_window, text='Table dropped').pack(
        padx=GRID_PAD, pady=GRID_PAD)


def populate_account_table():
    # Set up UI results window
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    cursor.execute(
        """INSERT INTO ACCOUNT(ACCOUNT_EMAIL, ACCOUNT_PASSWORD, CUSTOMER_ID) VALUES('john@ryerson.ca', 'johnpassword', 'C000')""")
    cursor.execute(
        """INSERT INTO ACCOUNT(ACCOUNT_EMAIL, ACCOUNT_PASSWORD, CUSTOMER_ID) VALUES('jane@ryerson.ca', 'janepassword', 'C001')""")
    cursor.execute(
        """INSERT INTO ACCOUNT(ACCOUNT_EMAIL, ACCOUNT_PASSWORD, CUSTOMER_ID) VALUES('alice@ryerson.ca', 'alicepassword', 'C002')""")
    cursor.execute(
        """INSERT INTO ACCOUNT(ACCOUNT_EMAIL, ACCOUNT_PASSWORD, CUSTOMER_ID) VALUES('bob@ryerson.ca', 'bobpassword', 'C003')""")
    cursor.execute(
        """INSERT INTO ACCOUNT(ACCOUNT_EMAIL, ACCOUNT_PASSWORD, CUSTOMER_ID) VALUES('jack@ryerson.ca', 'jackpassword', 'C004')""")
    cursor.execute(
        """INSERT INTO ACCOUNT(ACCOUNT_EMAIL, ACCOUNT_PASSWORD, CUSTOMER_ID) VALUES('ben@ryerson.ca', 'benpassword', 'C005')""")
    cursor.execute(
        """INSERT INTO ACCOUNT(ACCOUNT_EMAIL, ACCOUNT_PASSWORD, CUSTOMER_ID) VALUES('david@ryerson.ca', 'davidpassword', 'C006')""")
    cursor.execute(
        """INSERT INTO ACCOUNT(ACCOUNT_EMAIL, ACCOUNT_PASSWORD, CUSTOMER_ID) VALUES('ping@ryerson.ca', 'pingpassword', 'C007')""")
    cursor.execute(
        """INSERT INTO ACCOUNT(ACCOUNT_EMAIL, ACCOUNT_PASSWORD, CUSTOMER_ID) VALUES('issac@ryerson.ca', 'issacpassword', 'C008')""")
    cursor.execute(
        """INSERT INTO ACCOUNT(ACCOUNT_EMAIL, ACCOUNT_PASSWORD, CUSTOMER_ID) VALUES('zack@ryerson.ca', 'zackpassword', 'C009')""")

    ttk.Label(results_window, text='Table populated').pack(
        padx=GRID_PAD, pady=GRID_PAD)
# endregion


# region transaction table
def create_transaction_table():
    # Set up UI results window
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    cursor.execute("""
        CREATE TABLE TRANSACTION(
        TRANSACTION_ID VARCHAR2(100) PRIMARY KEY,
        TRANSACTION_DATE DATE,
        TRANSACTION_TIME TIMESTAMP,
        TRANSACTION_AMOUNT DECIMAL,
        EMPLOYEE_SIN VARCHAR(9),
        CUSTOMER_ID VARCHAR2(100) NOT NULL,
        FOREIGN KEY(CUSTOMER_ID) REFERENCES CUSTOMER(CUSTOMER_ID),
        FOREIGN KEY(EMPLOYEE_SIN) REFERENCES EMPLOYEE(EMPLOYEE_SIN))""")

    ttk.Label(results_window, text='Table created').pack(
        padx=GRID_PAD, pady=GRID_PAD)


def drop_transaction_table():
    # Set up UI results window
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    cursor.execute("""DROP TABLE TRANSACTION""")

    ttk.Label(results_window, text='Table dropped').pack(
        padx=GRID_PAD, pady=GRID_PAD)


def populate_transaction_table():
    # Set up UI results window
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    cursor.execute(
        """INSERT INTO TRANSACTION(TRANSACTION_ID, TRANSACTION_AMOUNT, CUSTOMER_ID) VALUES('T000', 25.0, 'C000')""")
    cursor.execute(
        """INSERT INTO TRANSACTION(TRANSACTION_ID, TRANSACTION_AMOUNT, CUSTOMER_ID) VALUES('T001', 50.0, 'C003')""")
    cursor.execute(
        """INSERT INTO TRANSACTION(TRANSACTION_ID, TRANSACTION_AMOUNT, CUSTOMER_ID) VALUES('T002', 10.0, 'C003')""")
    cursor.execute(
        """INSERT INTO TRANSACTION(TRANSACTION_ID, TRANSACTION_AMOUNT, CUSTOMER_ID) VALUES('T003', 45.0, 'C003')""")
    cursor.execute(
        """INSERT INTO TRANSACTION(TRANSACTION_ID, TRANSACTION_AMOUNT, CUSTOMER_ID) VALUES('T004', 65.0, 'C002')""")
    cursor.execute(
        """INSERT INTO TRANSACTION(TRANSACTION_ID, TRANSACTION_AMOUNT, CUSTOMER_ID) VALUES('T005', 60.0, 'C002')""")

    ttk.Label(results_window, text='Table populated').pack(
        padx=GRID_PAD, pady=GRID_PAD)
# endregion


# region archive table
def create_archive_table():
    # Set up UI results window
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    cursor.execute("""
        CREATE TABLE ARCHIVE(
        ARCHIVE_ID VARCHAR2(100) PRIMARY KEY,
        RETURN_DURATION INTEGER,
        FOREIGN KEY(ARCHIVE_ID) REFERENCES ITEM(ITEM_ID))""")

    ttk.Label(results_window, text='Table created').pack(
        padx=GRID_PAD, pady=GRID_PAD)


def drop_archive_table():
    # Set up UI results window
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    cursor.execute("""DROP TABLE ARCHIVE""")

    ttk.Label(results_window, text='Table dropped').pack(
        padx=GRID_PAD, pady=GRID_PAD)


def populate_archive_table():
    # Set up UI results window
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    cursor.execute("""INSERT INTO ARCHIVE VALUES('I008', 30)""")
    cursor.execute("""INSERT INTO ARCHIVE VALUES('I009', 30)""")

    ttk.Label(results_window, text='Table populated').pack(
        padx=GRID_PAD, pady=GRID_PAD)
# endregion


# region item table

def create_item_table():
    # Set up UI results window
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    cursor.execute("""
        CREATE TABLE ITEM(
        ITEM_ID VARCHAR2(100) PRIMARY KEY,
        ITEM_TYPE VARCHAR2(100),
        ITEM_BRAND VARCHAR2(100),
        ITEM_SIZE VARCHAR2(100),
        ITEM_PRICE DECIMAL,
        ITEM_DISCOUNT_PERCENTAGE INTEGER CHECK(ITEM_DISCOUNT_PERCENTAGE BETWEEN 0 AND 100),
        CUSTOMER_ID VARCHAR2(100),
        STORE_ID VARCHAR2(100),
        FOREIGN KEY(CUSTOMER_ID) REFERENCES CUSTOMER(CUSTOMER_ID),
        FOREIGN KEY(STORE_ID) REFERENCES STORE(STORE_ID))""")

    ttk.Label(results_window, text='Table created').pack(
        padx=GRID_PAD, pady=GRID_PAD)


def drop_item_table():
    # Set up UI results window
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    cursor.execute("""DROP TABLE ITEM""")

    ttk.Label(results_window, text='Table dropped').pack(
        padx=GRID_PAD, pady=GRID_PAD)


def populate_item_table():
    # Set up UI results window
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    cursor.execute(
        """INSERT INTO ITEM VALUES('I000', 'Shirt', 'Levi', 'M', 10.0, 0, NULL, 'S000')""")
    cursor.execute(
        """INSERT INTO ITEM VALUES('I001', 'Shirt', 'Channel', 'S', 15.0, 0, NULL, 'S000')""")
    cursor.execute(
        """INSERT INTO ITEM VALUES('I002', 'Jeans', 'Levi', 'S', 20.0, 0, NULL, 'S001')""")
    cursor.execute(
        """INSERT INTO ITEM VALUES('I003', 'Jeans', 'H and M', 'XXL', 40.0, 20, NULL, 'S000')""")
    cursor.execute(
        """INSERT INTO ITEM VALUES('I004', 'Pants', 'H and M', 'XL', 25.0, 20, NULL, 'S001')""")
    cursor.execute(
        """INSERT INTO ITEM VALUES('I005', 'Pants', 'Gucci', 'L', 60.0, 0, NULL, 'S001')""")
    cursor.execute(
        """INSERT INTO ITEM VALUES('I006', 'Sneakers', 'Nike', 'L', 80.0, 0, NULL, 'S000')""")
    cursor.execute(
        """INSERT INTO ITEM VALUES('I007', 'Sneakers', 'Adidas', 'M', 99.0, 0, NULL, 'S001')""")
    cursor.execute(
        """INSERT INTO ITEM VALUES('I008', 'T-shirt', 'Uniqlo', 'XS', 8.0, 0, 'C000', 'S000')""")
    cursor.execute(
        """INSERT INTO ITEM VALUES('I009', 'Pants', 'Uniqlo', 'XL', 40.0, 0, 'C003', 'S001')""")
    cursor.execute(
        """INSERT INTO ITEM VALUES('I010', 'Hoodie', 'Supreme', 'L', 400.0, 0, 'C003', 'S001')""")

    ttk.Label(results_window, text='Table populated').pack(
        padx=GRID_PAD, pady=GRID_PAD)
# endregion


# region customer table
def create_customer_table():
    # Set up UI results window
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    cursor.execute("""
        CREATE TABLE CUSTOMER(
        CUSTOMER_ID VARCHAR2(100) PRIMARY KEY,
        CUSTOMER_NAME_FIRST VARCHAR2(100),
        CUSTOMER_NAME_LAST VARCHAR2(100),
        CUSTOMER_ADDRESS_STREET VARCHAR2(100),
        CUSTOMER_ADDRESS_CITY VARCHAR2(100),
        CUSTOMER_ADDRESS_STATE VARCHAR2(2),
        CUSTOMER_ADDRESS_ZIP VARCHAR2(6),
        CUSTOMER_PHONE_NUMBER VARCHAR2(10))""")

    ttk.Label(results_window, text='Table created').pack(
        padx=GRID_PAD, pady=GRID_PAD)


def drop_customer_table():
    # Set up UI results window
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    cursor.execute("""DROP TABLE CUSTOMER""")

    ttk.Label(results_window, text='Table dropped').pack(
        padx=GRID_PAD, pady=GRID_PAD)


def populate_customer_table():
    # Set up UI results window
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    cursor.execute(
        """INSERT INTO CUSTOMER(CUSTOMER_ID, CUSTOMER_NAME_FIRST, CUSTOMER_PHONE_NUMBER) VALUES('C000', 'John','1234567890')""")
    cursor.execute(
        """INSERT INTO CUSTOMER(CUSTOMER_ID, CUSTOMER_NAME_FIRST, CUSTOMER_PHONE_NUMBER) VALUES('C001', 'Jane','1234567890')""")
    cursor.execute(
        """INSERT INTO CUSTOMER(CUSTOMER_ID, CUSTOMER_NAME_FIRST, CUSTOMER_PHONE_NUMBER) VALUES('C002', 'Alice','1234567890')""")
    cursor.execute(
        """INSERT INTO CUSTOMER(CUSTOMER_ID, CUSTOMER_NAME_FIRST, CUSTOMER_PHONE_NUMBER) VALUES('C003', 'Bob','1234567890')""")
    cursor.execute(
        """INSERT INTO CUSTOMER(CUSTOMER_ID, CUSTOMER_NAME_FIRST, CUSTOMER_PHONE_NUMBER) VALUES('C004', 'Jack','1234567890')""")
    cursor.execute(
        """INSERT INTO CUSTOMER(CUSTOMER_ID, CUSTOMER_NAME_FIRST, CUSTOMER_PHONE_NUMBER) VALUES('C005', 'Ben','1234567890')""")
    cursor.execute(
        """INSERT INTO CUSTOMER(CUSTOMER_ID, CUSTOMER_NAME_FIRST, CUSTOMER_PHONE_NUMBER) VALUES('C006', 'David','1234567890')""")
    cursor.execute(
        """INSERT INTO CUSTOMER(CUSTOMER_ID, CUSTOMER_NAME_FIRST, CUSTOMER_PHONE_NUMBER) VALUES('C007', 'Ping','1234567890')""")
    cursor.execute(
        """INSERT INTO CUSTOMER(CUSTOMER_ID, CUSTOMER_NAME_FIRST, CUSTOMER_PHONE_NUMBER) VALUES('C008', 'Issac','1234567890')""")
    cursor.execute(
        """INSERT INTO CUSTOMER(CUSTOMER_ID, CUSTOMER_NAME_FIRST, CUSTOMER_PHONE_NUMBER) VALUES('C009', 'Zack','1234567890')""")

    ttk.Label(results_window, text='Table populated').pack(
        padx=GRID_PAD, pady=GRID_PAD)
# endregion


# region employee table
def create_employee_table():
    # Set up UI results window
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    cursor.execute("""
        CREATE TABLE EMPLOYEE(
        EMPLOYEE_SIN VARCHAR2(9) PRIMARY KEY,
        EMPLOYEE_NAME_FIRST VARCHAR2(100),
        EMPLOYEE_NAME_LAST VARCHAR2(100),
        EMPLOYEE_ADDRESS_STREET VARCHAR2(100),
        EMPLOYEE_ADDRESS_CITY VARCHAR2(100),
        EMPLOYEE_ADDRESS_STATE VARCHAR2(2),
        EMPLOYEE_ADDRESS_ZIP VARCHAR2(6),
        EMPLOYEE_PHONE_NUMBER VARCHAR2(10),
        EMPLOYEE_SHIFT_DAY_OF_WEEK VARCHAR2(50),
        EMPLOYEE_SHIFT_START_TIME VARCHAR2(50),
        EMPLOYEE_SHIFT_END_TIME VARCHAR2(50),
        EMPLOYEE_WORK_STORE_ID VARCHAR2(100) NOT NULL,
        EMPLOYEE_MANAGE_STORE_ID VARCHAR2(100) UNIQUE,
        FOREIGN KEY(EMPLOYEE_WORK_STORE_ID) REFERENCES STORE(STORE_ID),
        FOREIGN KEY(EMPLOYEE_MANAGE_STORE_ID) REFERENCES STORE(STORE_ID))""")

    ttk.Label(results_window, text='Table created').pack(
        padx=GRID_PAD, pady=GRID_PAD)


def drop_employee_table():
    # Set up UI results window
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    cursor.execute("""DROP TABLE EMPLOYEE""")

    ttk.Label(results_window, text='Table dropped').pack(
        padx=GRID_PAD, pady=GRID_PAD)


def populate_employee_table():
    # Set up UI results window
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    cursor.execute("""INSERT INTO EMPLOYEE(EMPLOYEE_SIN, EMPLOYEE_NAME_FIRST, EMPLOYEE_ADDRESS_CITY, EMPLOYEE_WORK_STORE_ID, EMPLOYEE_MANAGE_STORE_ID) VALUES('000111222', 'Chris', 'Toronto', 'S001', 'S001')""")
    cursor.execute("""INSERT INTO EMPLOYEE(EMPLOYEE_SIN, EMPLOYEE_NAME_FIRST, EMPLOYEE_ADDRESS_CITY, EMPLOYEE_WORK_STORE_ID, EMPLOYEE_MANAGE_STORE_ID) VALUES('333444555', 'Dave', 'Toronto', 'S000', NULL)""")
    cursor.execute("""INSERT INTO EMPLOYEE(EMPLOYEE_SIN, EMPLOYEE_NAME_FIRST, EMPLOYEE_ADDRESS_CITY, EMPLOYEE_WORK_STORE_ID, EMPLOYEE_MANAGE_STORE_ID) VALUES('666777888', 'Emily', 'Brampton', 'S000', 'S000')""")

    ttk.Label(results_window, text='Table populated').pack(
        padx=GRID_PAD, pady=GRID_PAD)
# endregion


# region store table
def create_store_table():
    # Set up UI results window
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    cursor.execute("""
        CREATE TABLE STORE(
        STORE_ID VARCHAR2(50) PRIMARY KEY,
        STORE_ADDRESS_STREET VARCHAR2(100),
        STORE_ADDRESS_CITY VARCHAR2(100),
        STORE_ADDRESS_STATE VARCHAR2(2),
        STORE_ADDRESS_ZIP VARCHAR2(6),
        STORE_PHONE_NUMBER VARCHAR2(10))""")

    ttk.Label(results_window, text='Table created').pack(
        padx=GRID_PAD, pady=GRID_PAD)


def drop_store_table():
    # Set up UI results window
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    cursor.execute("""DROP TABLE STORE""")

    ttk.Label(results_window, text='Table dropped').pack(
        padx=GRID_PAD, pady=GRID_PAD)


def populate_store_table():
    # Set up UI results window
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    cursor.execute(
        """INSERT INTO STORE(STORE_ID, STORE_PHONE_NUMBER) VALUES('S000', '0001112222')""")
    cursor.execute(
        """INSERT INTO STORE(STORE_ID, STORE_PHONE_NUMBER) VALUES('S001', '3334445555')""")

    ttk.Label(results_window, text='Table populated').pack(
        padx=GRID_PAD, pady=GRID_PAD)
# endregion


def create_all_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('All')

    cursor.execute("""
        CREATE TABLE CUSTOMER(
        CUSTOMER_ID VARCHAR2(100) PRIMARY KEY,
        CUSTOMER_NAME_FIRST VARCHAR2(100),
        CUSTOMER_NAME_LAST VARCHAR2(100),
        CUSTOMER_ADDRESS_STREET VARCHAR2(100),
        CUSTOMER_ADDRESS_CITY VARCHAR2(100),
        CUSTOMER_ADDRESS_STATE VARCHAR2(2),
        CUSTOMER_ADDRESS_ZIP VARCHAR2(6),
        CUSTOMER_PHONE_NUMBER VARCHAR2(10))""")


    cursor.execute("""
        CREATE TABLE ACCOUNT(
        ACCOUNT_EMAIL VARCHAR2(100) PRIMARY KEY,
        ACCOUNT_PASSWORD VARCHAR2(100) NOT NULL,
        ACCOUNT_CARD_NUMBER VARCHAR2(12),
        CUSTOMER_ID VARCHAR2(100) UNIQUE NOT NULL,
        FOREIGN KEY(CUSTOMER_ID) REFERENCES CUSTOMER(CUSTOMER_ID))""")

    cursor.execute("""
        CREATE TABLE STORE(
        STORE_ID VARCHAR2(50) PRIMARY KEY,
        STORE_ADDRESS_STREET VARCHAR2(100),
        STORE_ADDRESS_CITY VARCHAR2(100),
        STORE_ADDRESS_STATE VARCHAR2(2),
        STORE_ADDRESS_ZIP VARCHAR2(6),
        STORE_PHONE_NUMBER VARCHAR2(10))""")

    cursor.execute("""
        CREATE TABLE EMPLOYEE(
        EMPLOYEE_SIN VARCHAR2(9) PRIMARY KEY,
        EMPLOYEE_NAME_FIRST VARCHAR2(100),
        EMPLOYEE_NAME_LAST VARCHAR2(100),
        EMPLOYEE_ADDRESS_STREET VARCHAR2(100),
        EMPLOYEE_ADDRESS_CITY VARCHAR2(100),
        EMPLOYEE_ADDRESS_STATE VARCHAR2(2),
        EMPLOYEE_ADDRESS_ZIP VARCHAR2(6),
        EMPLOYEE_PHONE_NUMBER VARCHAR2(10),
        EMPLOYEE_SHIFT_DAY_OF_WEEK VARCHAR2(50),
        EMPLOYEE_SHIFT_START_TIME VARCHAR2(50),
        EMPLOYEE_SHIFT_END_TIME VARCHAR2(50),
        EMPLOYEE_WORK_STORE_ID VARCHAR2(100) NOT NULL,
        EMPLOYEE_MANAGE_STORE_ID VARCHAR2(100) UNIQUE,
        FOREIGN KEY(EMPLOYEE_WORK_STORE_ID) REFERENCES STORE(STORE_ID),
        FOREIGN KEY(EMPLOYEE_MANAGE_STORE_ID) REFERENCES STORE(STORE_ID))""")

    cursor.execute("""
        CREATE TABLE TRANSACTION(
        TRANSACTION_ID VARCHAR2(100) PRIMARY KEY,
        TRANSACTION_DATE DATE,
        TRANSACTION_TIME TIMESTAMP,
        TRANSACTION_AMOUNT DECIMAL,
        EMPLOYEE_SIN VARCHAR(9),
        CUSTOMER_ID VARCHAR2(100) NOT NULL,
        FOREIGN KEY(CUSTOMER_ID) REFERENCES CUSTOMER(CUSTOMER_ID),
        FOREIGN KEY(EMPLOYEE_SIN) REFERENCES EMPLOYEE(EMPLOYEE_SIN))""")

    cursor.execute("""
        CREATE TABLE ITEM(
        ITEM_ID VARCHAR2(100) PRIMARY KEY,
        ITEM_TYPE VARCHAR2(100),
        ITEM_BRAND VARCHAR2(100),
        ITEM_SIZE VARCHAR2(100),
        ITEM_PRICE DECIMAL,
        ITEM_DISCOUNT_PERCENTAGE INTEGER CHECK(ITEM_DISCOUNT_PERCENTAGE BETWEEN 0 AND 100),
        CUSTOMER_ID VARCHAR2(100),
        STORE_ID VARCHAR2(100),
        FOREIGN KEY(CUSTOMER_ID) REFERENCES CUSTOMER(CUSTOMER_ID),
        FOREIGN KEY(STORE_ID) REFERENCES STORE(STORE_ID))""")


    cursor.execute("""
        CREATE TABLE ARCHIVE(
        ARCHIVE_ID VARCHAR2(100) PRIMARY KEY,
        RETURN_DURATION INTEGER,
        FOREIGN KEY(ARCHIVE_ID) REFERENCES ITEM(ITEM_ID))""")   
    
   
    ttk.Label(results_window, text='Tables created').pack(
        padx=GRID_PAD, pady=GRID_PAD)


def drop_all_table():
    # Set up UI results window
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    cursor.execute("""DROP TABLE ACCOUNT""")
    cursor.execute("""DROP TABLE TRANSACTION""")
    cursor.execute("""DROP TABLE ARCHIVE""")
    cursor.execute("""DROP TABLE ITEM""")
    cursor.execute("""DROP TABLE CUSTOMER""")
    cursor.execute("""DROP TABLE EMPLOYEE""")
    cursor.execute("""DROP TABLE STORE""")

    ttk.Label(results_window, text='Tables dropped').pack(
        padx=GRID_PAD, pady=GRID_PAD)


def populate_all_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    
    # Customer
    cursor.execute(
        """INSERT INTO CUSTOMER(CUSTOMER_ID, CUSTOMER_NAME_FIRST, CUSTOMER_PHONE_NUMBER) VALUES('C000', 'John','1234567890')""")
    cursor.execute(
        """INSERT INTO CUSTOMER(CUSTOMER_ID, CUSTOMER_NAME_FIRST, CUSTOMER_PHONE_NUMBER) VALUES('C001', 'Jane','1234567890')""")
    cursor.execute(
        """INSERT INTO CUSTOMER(CUSTOMER_ID, CUSTOMER_NAME_FIRST, CUSTOMER_PHONE_NUMBER) VALUES('C002', 'Alice','1234567890')""")
    cursor.execute(
        """INSERT INTO CUSTOMER(CUSTOMER_ID, CUSTOMER_NAME_FIRST, CUSTOMER_PHONE_NUMBER) VALUES('C003', 'Bob','1234567890')""")
    cursor.execute(
        """INSERT INTO CUSTOMER(CUSTOMER_ID, CUSTOMER_NAME_FIRST, CUSTOMER_PHONE_NUMBER) VALUES('C004', 'Jack','1234567890')""")
    cursor.execute(
        """INSERT INTO CUSTOMER(CUSTOMER_ID, CUSTOMER_NAME_FIRST, CUSTOMER_PHONE_NUMBER) VALUES('C005', 'Ben','1234567890')""")
    cursor.execute(
        """INSERT INTO CUSTOMER(CUSTOMER_ID, CUSTOMER_NAME_FIRST, CUSTOMER_PHONE_NUMBER) VALUES('C006', 'David','1234567890')""")
    cursor.execute(
        """INSERT INTO CUSTOMER(CUSTOMER_ID, CUSTOMER_NAME_FIRST, CUSTOMER_PHONE_NUMBER) VALUES('C007', 'Ping','1234567890')""")
    cursor.execute(
        """INSERT INTO CUSTOMER(CUSTOMER_ID, CUSTOMER_NAME_FIRST, CUSTOMER_PHONE_NUMBER) VALUES('C008', 'Issac','1234567890')""")
    cursor.execute(
        """INSERT INTO CUSTOMER(CUSTOMER_ID, CUSTOMER_NAME_FIRST, CUSTOMER_PHONE_NUMBER) VALUES('C009', 'Zack','1234567890')""")

    # Account
    cursor.execute(
        """INSERT INTO ACCOUNT(ACCOUNT_EMAIL, ACCOUNT_PASSWORD, CUSTOMER_ID) VALUES('john@ryerson.ca', 'johnpassword', 'C000')""")
    cursor.execute(
        """INSERT INTO ACCOUNT(ACCOUNT_EMAIL, ACCOUNT_PASSWORD, CUSTOMER_ID) VALUES('jane@ryerson.ca', 'janepassword', 'C001')""")
    cursor.execute(
        """INSERT INTO ACCOUNT(ACCOUNT_EMAIL, ACCOUNT_PASSWORD, CUSTOMER_ID) VALUES('alice@ryerson.ca', 'alicepassword', 'C002')""")
    cursor.execute(
        """INSERT INTO ACCOUNT(ACCOUNT_EMAIL, ACCOUNT_PASSWORD, CUSTOMER_ID) VALUES('bob@ryerson.ca', 'bobpassword', 'C003')""")
    cursor.execute(
        """INSERT INTO ACCOUNT(ACCOUNT_EMAIL, ACCOUNT_PASSWORD, CUSTOMER_ID) VALUES('jack@ryerson.ca', 'jackpassword', 'C004')""")
    cursor.execute(
        """INSERT INTO ACCOUNT(ACCOUNT_EMAIL, ACCOUNT_PASSWORD, CUSTOMER_ID) VALUES('ben@ryerson.ca', 'benpassword', 'C005')""")
    cursor.execute(
        """INSERT INTO ACCOUNT(ACCOUNT_EMAIL, ACCOUNT_PASSWORD, CUSTOMER_ID) VALUES('david@ryerson.ca', 'davidpassword', 'C006')""")
    cursor.execute(
        """INSERT INTO ACCOUNT(ACCOUNT_EMAIL, ACCOUNT_PASSWORD, CUSTOMER_ID) VALUES('ping@ryerson.ca', 'pingpassword', 'C007')""")
    cursor.execute(
        """INSERT INTO ACCOUNT(ACCOUNT_EMAIL, ACCOUNT_PASSWORD, CUSTOMER_ID) VALUES('issac@ryerson.ca', 'issacpassword', 'C008')""")
    cursor.execute(
        """INSERT INTO ACCOUNT(ACCOUNT_EMAIL, ACCOUNT_PASSWORD, CUSTOMER_ID) VALUES('zack@ryerson.ca', 'zackpassword', 'C009')""")

    # Transaction
    cursor.execute(
        """INSERT INTO TRANSACTION(TRANSACTION_ID, TRANSACTION_AMOUNT, CUSTOMER_ID) VALUES('T000', 25.0, 'C000')""")
    cursor.execute(
        """INSERT INTO TRANSACTION(TRANSACTION_ID, TRANSACTION_AMOUNT, CUSTOMER_ID) VALUES('T001', 50.0, 'C003')""")
    cursor.execute(
        """INSERT INTO TRANSACTION(TRANSACTION_ID, TRANSACTION_AMOUNT, CUSTOMER_ID) VALUES('T002', 10.0, 'C003')""")
    cursor.execute(
        """INSERT INTO TRANSACTION(TRANSACTION_ID, TRANSACTION_AMOUNT, CUSTOMER_ID) VALUES('T003', 45.0, 'C003')""")
    cursor.execute(
        """INSERT INTO TRANSACTION(TRANSACTION_ID, TRANSACTION_AMOUNT, CUSTOMER_ID) VALUES('T004', 65.0, 'C002')""")
    cursor.execute(
        """INSERT INTO TRANSACTION(TRANSACTION_ID, TRANSACTION_AMOUNT, CUSTOMER_ID) VALUES('T005', 60.0, 'C002')""")

    # Store
    cursor.execute(
        """INSERT INTO STORE(STORE_ID, STORE_PHONE_NUMBER) VALUES('S000', '0001112222')""")
    cursor.execute(
        """INSERT INTO STORE(STORE_ID, STORE_PHONE_NUMBER) VALUES('S001', '3334445555')""")

    # Item
    cursor.execute(
        """INSERT INTO ITEM VALUES('I000', 'Shirt', 'Levi', 'M', 10.0, 0, NULL, 'S000')""")
    cursor.execute(
        """INSERT INTO ITEM VALUES('I001', 'Shirt', 'Channel', 'S', 15.0, 0, NULL, 'S000')""")
    cursor.execute(
        """INSERT INTO ITEM VALUES('I002', 'Jeans', 'Levi', 'S', 20.0, 0, NULL, 'S001')""")
    cursor.execute(
        """INSERT INTO ITEM VALUES('I003', 'Jeans', 'H and M', 'XXL', 40.0, 20, NULL, 'S000')""")
    cursor.execute(
        """INSERT INTO ITEM VALUES('I004', 'Pants', 'H and M', 'XL', 25.0, 20, NULL, 'S001')""")
    cursor.execute(
        """INSERT INTO ITEM VALUES('I005', 'Pants', 'Gucci', 'L', 60.0, 0, NULL, 'S001')""")
    cursor.execute(
        """INSERT INTO ITEM VALUES('I006', 'Sneakers', 'Nike', 'L', 80.0, 0, NULL, 'S000')""")
    cursor.execute(
        """INSERT INTO ITEM VALUES('I007', 'Sneakers', 'Adidas', 'M', 99.0, 0, NULL, 'S001')""")
    cursor.execute(
        """INSERT INTO ITEM VALUES('I008', 'T-shirt', 'Uniqlo', 'XS', 8.0, 0, 'C000', 'S000')""")
    cursor.execute(
        """INSERT INTO ITEM VALUES('I009', 'Pants', 'Uniqlo', 'XL', 40.0, 0, 'C003', 'S001')""")
    cursor.execute(
        """INSERT INTO ITEM VALUES('I010', 'Hoodie', 'Supreme', 'L', 400.0, 0, 'C003', 'S001')""")
    
    # Archive
    cursor.execute("""INSERT INTO ARCHIVE VALUES('I008', 30)""")
    cursor.execute("""INSERT INTO ARCHIVE VALUES('I009', 30)""")

    # Employee
    cursor.execute("""INSERT INTO EMPLOYEE(EMPLOYEE_SIN, EMPLOYEE_NAME_FIRST, EMPLOYEE_ADDRESS_CITY, EMPLOYEE_WORK_STORE_ID, EMPLOYEE_MANAGE_STORE_ID) VALUES('000111222', 'Chris', 'Toronto', 'S001', 'S001')""")
    cursor.execute("""INSERT INTO EMPLOYEE(EMPLOYEE_SIN, EMPLOYEE_NAME_FIRST, EMPLOYEE_ADDRESS_CITY, EMPLOYEE_WORK_STORE_ID, EMPLOYEE_MANAGE_STORE_ID) VALUES('333444555', 'Dave', 'Toronto', 'S000', NULL)""")
    cursor.execute("""INSERT INTO EMPLOYEE(EMPLOYEE_SIN, EMPLOYEE_NAME_FIRST, EMPLOYEE_ADDRESS_CITY, EMPLOYEE_WORK_STORE_ID, EMPLOYEE_MANAGE_STORE_ID) VALUES('666777888', 'Emily', 'Brampton', 'S000', 'S000')""")

   



    ttk.Label(results_window, text='Tables populated').pack(
        padx=GRID_PAD, pady=GRID_PAD)


def query():
    # Set up UI results window
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    values = cursor.execute(query_entry.get())
    for i, value in enumerate(values):
        for j, field in enumerate(value):
            ttk.Label(results_window, text=f'{field}').grid(
                row=i, column=j, padx=GRID_PAD, pady=GRID_PAD)


ttk.Label(main_window, text='Customer Table').grid(
    row=0, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Create Table', command=create_customer_table).grid(
    row=1, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Drop Table', command=drop_customer_table).grid(
    row=1, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Populate Table', command=populate_customer_table).grid(
    row=1, column=2, padx=GRID_PAD, pady=GRID_PAD)

ttk.Label(main_window, text='Account Table').grid(
    row=2, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Create Table', command=create_account_table).grid(
    row=3, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Drop Table', command=drop_account_table).grid(
    row=3, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Populate Table', command=populate_account_table).grid(
    row=3, column=2, padx=GRID_PAD, pady=GRID_PAD)

ttk.Label(main_window, text='Store Table').grid(
    row=4, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Create Table', command=create_store_table).grid(
    row=5, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Drop Table', command=drop_store_table).grid(
    row=5, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Populate Table', command=populate_store_table).grid(
    row=5, column=2, padx=GRID_PAD, pady=GRID_PAD)

ttk.Label(main_window, text='Employee Table').grid(
    row=6, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Create Table', command=create_employee_table).grid(
    row=7, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Drop Table', command=drop_employee_table).grid(
    row=7, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Populate Table', command=populate_employee_table).grid(
    row=7, column=2, padx=GRID_PAD, pady=GRID_PAD)

ttk.Label(main_window, text='Transaction Table').grid(
    row=8, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Create Table', command=create_transaction_table).grid(
    row=9, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Drop Table', command=drop_transaction_table).grid(
    row=9, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Populate Table', command=populate_transaction_table).grid(
    row=9, column=2, padx=GRID_PAD, pady=GRID_PAD)

ttk.Label(main_window, text='Item Table').grid(
    row=10, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Create Table', command=create_item_table).grid(
    row=11, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Drop Table', command=drop_item_table).grid(
    row=11, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Populate Table', command=populate_item_table).grid(
    row=11, column=2, padx=GRID_PAD, pady=GRID_PAD)

ttk.Label(main_window, text='Archive Table').grid(
    row=12, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Create Table', command=create_archive_table).grid(
    row=13, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Drop Table', command=drop_archive_table).grid(
    row=13, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Populate Table', command=populate_archive_table).grid(
    row=13, column=2, padx=GRID_PAD, pady=GRID_PAD)

ttk.Label(main_window, text='All Tables').grid(
    row=14, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Create all Tables', command=create_all_table).grid(
    row=15, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Drop all Tables', command=drop_all_table).grid(
    row=15, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Populate all Tables', command=populate_all_table).grid(
    row=15, column=2, padx=GRID_PAD, pady=GRID_PAD)

query_entry = ttk.Entry(main_window)
query_entry.grid(row=16, column=0, columnspan=2,
                 sticky=tk.EW, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Query', command=query).grid(
    row=16, column=2, padx=GRID_PAD, pady=GRID_PAD)


# Set up UI login window
login_window = tk.Toplevel(main_window)
login_window.title('Login')

# Position window at the center of the screen
login_window.geometry(
    f'{LOGIN_WIDTH}x{LOGIN_HEIGHT}+{int(main_window.winfo_screenwidth() / 2 - LOGIN_WIDTH / 2)}+{int(main_window.winfo_screenheight() / 2 - LOGIN_HEIGHT / 2)}')

login_window.wm_protocol('WM_DELETE_WINDOW', lambda: main_window.destroy())

login_window.columnconfigure(0, weight=1)
login_window.columnconfigure(1, weight=3)

ttk.Label(login_window, text='Username:').grid(
    row=0, column=0, sticky=tk.W, padx=GRID_PAD, pady=GRID_PAD)
username_entry = ttk.Entry(login_window)
username_entry.grid(row=0, column=1, sticky=tk.EW,
                    padx=GRID_PAD, pady=GRID_PAD)

ttk.Label(login_window, text='Password:').grid(
    row=1, column=0, sticky=tk.W, padx=GRID_PAD, pady=GRID_PAD)
password_entry = ttk.Entry(login_window, show='*')
password_entry.grid(row=1, column=1, sticky=tk.EW,
                    padx=GRID_PAD, pady=GRID_PAD)


def login():  # Handle login logic
    username = username_entry.get()
    password = password_entry.get()

    if len(username) == 0 or len(password) == 0:
        print('Please enter username and password')
        return

    global connection, cursor

    # Ryerson database connection
    try:
        connection = cx_Oracle.connect(
            user=username, password=password, dsn=cx_Oracle.makedsn('oracle.scs.ryerson.ca', 1521, sid='orcl'))
        cursor = connection.cursor()
    except:
        print('Error while logging in')
        main_window.destroy()
        return

    main_window.wm_deiconify()
    login_window.destroy()


ttk.Button(login_window, text='Login', command=login).grid(
    column=1, row=2, sticky=tk.E, padx=GRID_PAD, pady=GRID_PAD)

# Run the app
if __name__ == '__main__':
    main_window.withdraw()
    login_window.mainloop()

