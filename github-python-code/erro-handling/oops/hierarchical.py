# Parent Class (Common Base)
class Employee:
    def mark_attendance(self):
        print("✅ Attendance marked successfully.")

# Child Class 1 (Inherits from Employee)
class Developer(Employee):
    def write_code(self):
        print("💻 Writing Python scripts...")

# Child Class 2 (Inherits from Employee)
class Designer(Employee):
    def design_ui(self):
        print("🎨 Creating app interfaces...")

# --- Using the Child Classes ---
dev = Developer()
dev.mark_attendance()  # Inherited from Parent
dev.write_code()       # Its own method

print("---")

designer = Designer()
designer.mark_attendance() # Inherited from the SAME Parent
designer.design_ui()       # Its own method