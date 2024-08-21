class VaccinationSystem:
    def __init__(self):
        self.users = {}  # {username: password}
        self.child_profiles = {}  # {username: [{child_name: {dob: ..., vaccinations: [...], appointments: [...]}}]}
        self.logged_in_user = None

    def get_input(self, prompt, options=None):
        while True:
            user_input = input(prompt)
            if options and user_input not in options:
                print("Invalid input. Please choose from the available options.")
            else:
                return user_input

    def register_user(self):
        print("Register a new user")
        username = self.get_input("Enter username: ")
        if username in self.users:
            print("Username already exists!")
            return
        password = self.get_input("Enter password: ")
        self.users[username] = password
        self.child_profiles[username] = []
        print("Registration successful!")

    def login(self):
        print("User login")
        username = self.get_input("Enter username: ")
        password = self.get_input("Enter password: ")
        if username in self.users and self.users[username] == password:
            self.logged_in_user = username
            print(f"Welcome, {username}!")
        else:
            print("Invalid username or password!")

    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Manage Child Profile")
            print("2. View Vaccination Schedule")
            print("3. Book Appointment")
            print("4. View Reminders")
            print("5. Logout")
            choice = self.get_input("Select an option: ", options=['1', '2', '3', '4', '5'])
            if choice == '1':
                self.manage_child_profile()
            elif choice == '2':
                self.view_vaccination_schedule()
            elif choice == '3':
                self.book_appointment()
            elif choice == '4':
                self.view_reminders()
            elif choice == '5':
                self.logout()
                break

    def manage_child_profile(self):
        print("\nManage Child Profile")
        print("1. Add Child Profile")
        print("2. Edit Child Profile")
        print("3. View Child Profile")
        choice = self.get_input("Select an option: ", options=['1', '2', '3'])
        if choice == '1':
            self.add_child_profile()
        elif choice == '2':
            self.edit_child_profile()
        elif choice == '3':
            self.view_child_profile()

    def add_child_profile(self):
        print("\nAdd Child Profile")
        child_name = self.get_input("Enter child's name: ")
        dob = self.get_input("Enter child's date of birth (YYYY-MM-DD): ")
        self.child_profiles[self.logged_in_user].append({
            child_name: {'dob': dob, 'vaccinations': [], 'appointments': []}
        })
        print("Child profile added successfully!")

    def edit_child_profile(self):
        # Logic for editing a child profile
        pass

    def view_child_profile(self):
        print("\nView Child Profile")
        if not self.child_profiles[self.logged_in_user]:
            print("No child profiles available.")
            return
        for i, child in enumerate(self.child_profiles[self.logged_in_user]):
            child_name = list(child.keys())[0]
            dob = child[child_name]['dob']
            print(f"{i+1}. {child_name} (DOB: {dob})")

    def view_vaccination_schedule(self):
        print("\nView Vaccination Schedule")
        if not self.child_profiles[self.logged_in_user]:
            print("No child profiles available.")
            return
        for child in self.child_profiles[self.logged_in_user]:
            child_name = list(child.keys())[0]
            dob = child[child_name]['dob']
            print(f"\nVaccination Schedule for {child_name} (DOB: {dob}):")
            print("1. BCG Vaccine - Due Date: 2021-06-20")
            print("2. Hepatitis B Vaccine - Due Date: 2021-07-20")
            print("3. DTP Vaccine - Due Date: 2021-08-20")

    def book_appointment(self):
        print("\nBook Appointment")
        if not self.child_profiles[self.logged_in_user]:
            print("No child profiles available.")
            return
        print("Select a child:")
        for i, child in enumerate(self.child_profiles[self.logged_in_user]):
            print(f"{i+1}. {list(child.keys())[0]}")
        choice = int(self.get_input("Enter your choice: ")) - 1
        if 0 <= choice < len(self.child_profiles[self.logged_in_user]):
            child_name = list(self.child_profiles[self.logged_in_user][choice].keys())[0]
            print(f"Booking appointment for {child_name}")
            print("Available Vaccinations:")
            print("1. BCG Vaccine")
            print("2. Hepatitis B Vaccine")
            print("3. DTP Vaccine")
            vaccine_choice = self.get_input("Select a vaccine: ")
            appointment_date = self.get_input("Enter appointment date (YYYY-MM-DD): ")
            self.child_profiles[self.logged_in_user][choice][child_name]['appointments'].append({
                'vaccine': vaccine_choice,
                'date': appointment_date
            })
            print(f"Appointment for {vaccine_choice} on {appointment_date} booked successfully!")
        else:
            print("Invalid choice!")

    def view_reminders(self):
        print("\nView Reminders")
        if not self.child_profiles[self.logged_in_user]:
            print("No child profiles available.")
            return
        for child in self.child_profiles[self.logged_in_user]:
            child_name = list(child.keys())[0]
            appointments = child[child_name]['appointments']
            if appointments:
                print(f"\nReminders for {child_name}:")
                for appointment in appointments:
                    print(f"- {appointment['vaccine']} appointment on {appointment['date']}")
            else:
                print(f"No reminders for {child_name}.")

    def logout(self):
        print(f"Goodbye, {self.logged_in_user}!")
        self.logged_in_user = None

    def run(self):
        while True:
            print("\nWelcome to the Child Vaccination Management System")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = self.get_input("Select an option: ", options=['1', '2', '3'])
            if choice == '1':
                self.register_user()
            elif choice == '2':
                self.login()
                if self.logged_in_user:
                    self.main_menu()
            elif choice == '3':
                print("Exiting the system. Goodbye!")
                break

if __name__ == "__main__":
    system = VaccinationSystem()
    system.run()
