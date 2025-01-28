import datetime

# Sample blood types
BLOOD_TYPES = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']

# Blood Bank data
blood_inventory = {
    'A+': 10,
    'A-': 5,
    'B+': 8,
    'B-': 3,
    'O+': 12,
    'O-': 6,
    'AB+': 4,
    'AB-': 2
}

# User and Admin data storage
users = {}  # {email: User object}
admins = {'admin@bloodbank.com': 'admin'}  # {email: password}

# User class
class User:
    def __init__(self, email, password, name, blood_type, contact):
        self.email = email
        self.password = password
        self.name = name
        self.blood_type = blood_type
        self.contact = contact

    def __str__(self):
        return f"Name: {self.name}, Blood Type: {self.blood_type}, Contact: {self.contact}"

# Login status
current_user = None

# Function to register a new user
def register_user():
    email = input("Enter your email: ")
    if email in users:
        print("Email already registered. Please log in.")
        return

    password = input("Enter your password: ")
    name = input("Enter your name: ")
    blood_type = input(f"Enter your blood type ({', '.join(BLOOD_TYPES)}): ").upper()
    if blood_type not in BLOOD_TYPES:
        print("Invalid blood type. Try again.")
        return

    contact = input("Enter your contact number: ")
    user = User(email, password, name, blood_type, contact)
    users[email] = user
    print(f"User {name} registered successfully!")

# Function to log in
def login_user():
    global current_user
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if email in users and users[email].password == password:
        current_user = users[email]
        print(f"Welcome, {current_user.name}!")
    else:
        print("Invalid email or password.")

# Function to log out
def logout_user():
    global current_user
    if current_user:
        print(f"Goodbye, {current_user.name}. You have logged out.")
        current_user = None
    else:
        print("No user logged in.")

# Function to update user profile
def update_profile():
    if not current_user:
        print("Please log in first.")
        return

    print(f"Updating profile for {current_user.name}")
    current_user.name = input("Enter your new name: ")
    current_user.blood_type = input(f"Enter your new blood type ({', '.join(BLOOD_TYPES)}): ").upper()
    if current_user.blood_type not in BLOOD_TYPES:
        print("Invalid blood type.")
        return
    current_user.contact = input("Enter your new contact number: ")
    print("Profile updated successfully.")

# Function to delete user account
def delete_account():
    global current_user
    if not current_user:
        print("Please log in first.")
        return

    confirm = input(f"Are you sure you want to delete your account, {current_user.name}? (y/n): ")
    if confirm.lower() == 'y':
        del users[current_user.email]
        print(f"Account for {current_user.name} deleted.")
        current_user = None
    else:
        print("Account deletion canceled.")

# Function to request blood
def request_blood():
    if not current_user:
        print("Please log in first.")
        return

    blood_type = input(f"Enter the blood type you need ({', '.join(BLOOD_TYPES)}): ").upper()
    if blood_type not in BLOOD_TYPES:
        print("Invalid blood type.")
        return

    if blood_inventory[blood_type] > 0:
        blood_inventory[blood_type] -= 1
        print(f"Your blood request for {blood_type} has been fulfilled.")
    else:
        print(f"Sorry, blood type {blood_type} is not available at the moment.")

# Function to search for available blood
def search_blood():
    blood_type = input(f"Enter the blood type to search for ({', '.join(BLOOD_TYPES)}): ").upper()
    if blood_type not in BLOOD_TYPES:
        print("Invalid blood type.")
        return

    print(f"Blood type {blood_type} is {'available' if blood_inventory[blood_type] > 0 else 'not available'}.")
    print(f"Available quantity: {blood_inventory[blood_type]} units.")

# Admin functions
def admin_dashboard():
    print("\n--- Admin Dashboard ---")
    print("1. Add blood to inventory")
    print("2. Edit blood donations")
    print("3. Contact registered users")
    print("4. Delete users")
    print("5. Logout")

    choice = input("Enter your choice: ")
    if choice == '1':
        add_blood()
    elif choice == '2':
        edit_blood_donations()
    elif choice == '3':
        contact_users()
    elif choice == '4':
        delete_user()
    elif choice == '5':
        print("Logging out.")
        return
    else:
        print("Invalid choice. Please try again.")

def admin_login():
    email = input("Enter admin email: ")
    password = input("Enter admin password: ")

    if email == "admin@bloodbank.com" and password == "admin":
        print("Admin login successful.")
        while True:
            admin_dashboard()
    else:
        print("Invalid admin credentials.")

def add_blood():
    blood_type = input(f"Enter blood type to add ({', '.join(BLOOD_TYPES)}): ").upper()
    quantity = int(input("Enter the quantity to add: "))
    if blood_type not in BLOOD_TYPES:
        print("Invalid blood type.")
        return
    blood_inventory[blood_type] += quantity
    print(f"Added {quantity} units of {blood_type} to the inventory.")

def edit_blood_donations():
    blood_type = input(f"Enter blood type to edit ({', '.join(BLOOD_TYPES)}): ").upper()
    if blood_type not in BLOOD_TYPES:
        print("Invalid blood type.")
        return
    new_quantity = int(input("Enter the new quantity: "))
    blood_inventory[blood_type] = new_quantity
    print(f"Updated {blood_type} to {new_quantity} units.")

def contact_users():
    email = input("Enter user email to contact: ")
    if email in users:
        print(f"Sending message to {email}...")
    else:
        print("User not found.")

def delete_user():
    email = input("Enter user email to delete: ")
    if email in users:
        del users[email]
        print(f"User {email} has been deleted.")
    else:
        print("User not found.")

# Main menu
def main_menu():
    while True:
        print("\n--- Blood Bank System ---")
        print("1. Register")
        print("2. Login")
        print("3. Logout")
        print("4. Update Profile")
        print("5. Request Blood")
        print("6. Search Blood")
        print("7. Delete Account")
        print("8. Admin Login")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            logout_user()
        elif choice == '4':
            update_profile()
        elif choice == '5':
            request_blood()
        elif choice == '6':
            search_blood()
        elif choice == '7':
            delete_account()
        elif choice == '8':
            admin_login()
        elif choice == '9':
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the system
main_menu()
