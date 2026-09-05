Part C:

1. What the Code Does
This program stores and displays clinic appointments.

Step 1: Create a list
appointments = []
An empty list called appointments is created to store appointment records.

Step 2: Book an appointment
def book_appointment(patient_name, practitioner_name, appointment_time):
This function adds a new appointment.

It first checks whether a patient name was entered:
if not patient_name:
raise ValueError("Patient name cannot be empty")
If the patient name is empty, a ValueError is raised.

Next, it creates a dictionary containing the appointment details:
appointment = {
"patient": patient_name,
"practitioner": practitioner_name,
"time": appointment_time
}

The dictionary is then added to the appointments list:
appointments.append(appointment)

Step 3: Display appointments
def display_appointments():
This function prints all stored appointments.

If the list is empty:
if not appointments:
it displays:
No appointments recorded.

Otherwise, it loops through every appointment and prints the details:
for appointment in appointments:

Step 4: Run the program
The program:
Prints a welcome message.
Creates two appointments.
Displays all appointments.

Output would look similar to:
Welcome to SmartCare: The Clinical Appointment Booking System!
Patient: Alice Smith | Practitioner: Dr. John Doe | Time: 2024-07-20 10:00 AM
Patient: Bob Johnson | Practitioner: Dr. Jane Roe | Time: 2024-07-20 11:30 AM

2. Three Limitations

1. Only the patient name is validated
The program checks that patient_name is not empty, but it does not validate:
practitioner name
appointment time
For example:
book_appointment("Alice", "", "") would still be accepted.

2. No check for conflicting appointments
The system allows multiple appointments at the same time.
Example:
book_appointment("Alice", "Dr. Smith", "10:00 AM")
book_appointment("Bob", "Dr. Smith", "10:00 AM")
A doctor cannot attend both appointments, but the program allows it.

3. Data is not saved permanently
Appointments exist only while the program is running.
When the program closes:
appointments = [] is recreated and all appointment data is lost.

3. Suggested Improvements

Improvement 1: Validate all inputs
Check that:
patient name is not empty
practitioner name is not empty
appointment time has a valid format
This helps prevent incorrect data being stored.

Improvement 2: Detect scheduling conflicts
Before adding an appointment, check whether the practitioner already has an appointment booked at that time.
This would make the booking system more realistic.

Improvement 3: Save data to a file
Store appointments in a text file, CSV file, or database so records remain available after the program closes.
This improves reliability and usability.

Additional Improvements
Allow appointment cancellation.
Allow appointment updates/rescheduling.
Sort appointments by date and time.
Give each appointment a unique ID.
Add a menu so users can enter appointments interactively.

4. Understanding Check
Try answering these yourself:

Question 1:
Why does the program use: appointments.append(appointment)
instead of: appointments = appointment
ANSWER: This allows for multiple appointments to be added to a list without removing any previous ones, as appointments = appointment would override any previously existing ones.

Question 2:
 What would happen if the line below was removed?
if not patient_name:
raise ValueError("Patient name cannot be empty")
ANSWER: Appointment bookings are now able to be entered without any patient name, resulting in scheduling issues.