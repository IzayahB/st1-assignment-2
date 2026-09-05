#PART B:

#task1
print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

# First Appointment
patient1_name = 'Alice Smith'
practitioner1_name = 'Dr. John Doe'
appointment1_time = '2024-07-20 10:00 AM'
print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time: {appointment1_time}")

# Second Appointment
patient2_name = 'Bob Johnson'
practitioner2_name = 'Dr. Jane Roe'
appointment2_time = '2024-07-20 11:30 AM'
print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time: {appointment2_time}")

#task1enhanced
appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)

def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return
    for appointment in appointments:
        print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")

print("Welcome to SmartCare: The Clinical Appointment Booking System!")
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')
display_appointments()

# # #Limitations for both programs:
# # #1. No user input for booking appointments, all data is hardcoded.
# # #2. Data is not saved to any sort of file or database, so it is lost when the program ends.
# # #3. The same practitioner can be booked for multiple patients at the same time, leading to scheduling conflicts.
# # #4. No login or authentication system to ensure only authorized users can book appointments or view them.
# # #5. The program does not handle errors or exceptions gracefully, which could lead to crashes or unexpected behavior.
# # #6. There is no search function, so users cannot easily find specific appointments, dates, patients or practitioners.
# # #7. Appointments are not uniquely identified, making it difficlt to modify or cancel specific appointments.
# # #8. Incorrect formats for date and time are not validated, which can led to scheduling confusion.
# # #9. The system does not record the status of appointments, whether they are cancelled, completed, reschedules or booked.

#Part D: Ai Generated code

appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    appointment = {
        "patient_name": patient_name,
        "practitioner_name": practitioner_name,
        "appointment_time": appointment_time
    }

    appointments.append(appointment)
    return appointment

# Example usage
book_appointment("Alice Smith", "Dr Brown", "10:00 AM")
book_appointment("John Davis", "Dr Lee", "2:30 PM")

print(appointments)

#Part F: Testing AI-Generated code:

appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):

    appointment = {
        "patient_name": patient_name,
        "practitioner_name": practitioner_name,
        "appointment_time": appointment_time
    }

    appointments.append(appointment)
    return appointment

# Example usage
book_appointment("John Davis", "Dr Brown", "10:00 AM")
book_appointment("", "Dr Brown", "10:00 AM")

print(appointments)

#Part G:Improvement to AI-generated code:

appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):

    if not patient_name:
        raise ValueError("Patient name cannot be empty")

    appointment = {
        "patient_name": patient_name,
        "practitioner_name": practitioner_name,
        "appointment_time": appointment_time
    }

    appointments.append(appointment)
    return appointment

# Example usage
book_appointment("John Davis", "Dr Brown", "10:00 AM")
book_appointment("", "Dr Brown", "10:00 AM")

print(appointments)
