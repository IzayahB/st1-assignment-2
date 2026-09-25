Assignment 2 – Case Study

Stage 4 Tutorial Activities

Object-Oriented Design Decisions

Week 7 | 60 minutes

# Activity 1 - Encapsulation Review

| Class | Protected state / invariant | Public operations |
| --- | --- | --- |
| Patient | Identifier and name cannot be blank, name updates must be validated | Constructor and update_details() |
| Practitioner | Identifier, name, and specialty cannot be blank, updates must be validated | Constructor and update_details() |
| Appointment | Must reference one Patient and Practitioner; status starts as scheduled, only scheduled appointments can be cancelled | Constructor, schedule(), cancel(), and read-only status access |

# Activity 2 - Composition or Inheritance?

Appointment and Patient -> **□ Composition/association** □ Inheritance Reason: An appointment references or contains a Patient, it is not a type of patient.

Appointment and Practitioner -> □ **Composition/association** □ Inheritance Reason: An Appointment references one Practitioner, it is not a type of Practitioner.

Doctor and Practitioner (hypothetical) -> □ Composition/association □ **Inheritance Reason**: Doctor could be described as a type of specialized practitioner.

Clinic and Appointment -> □ **Composition/association** □ Inheritance Reason: A clinic contains/manages appointment but an appointment is not a clinic. Clinic is also not apart from the approved SmartCare UML.

# Activity 3 - Responsibility Allocation

**Who decides whether SCHEDULED can become CANCELLED?**

The Appointment class decides whether scheduled can become cancelled.

**Who validates a patient name?**

The Patient class validates patient name.

**Should Appointment execute SQL? Why?**

Appointment should not execute SQL. While the class says not to add database logic, Adding SQL to Appointment would give the class too many responsibilities and would make it too difficult to test independently once connected to a database.

**Should the UI decide whether a status transition is legal?**

No. The UI can request a cancellation, but Appointment should enforce the rules within the business. If transition rules were controlled within the UI, another UI could potentially bypass them. Keeping it within Appointments ensures consistency.

# Activity 4 - AI Code Critique

**AI generates an Appointment class with public status mutation, SQL inside cancel(), a NotificationManager dependency and inheritance from PatientRecord. Identify at least five design problems and corrections.**

1.  Appointment manages domain state, database operations and notifications, giving it too many responsibilities and become difficult to test and maintains. Restrict Appointment to appointment info, associations, validations and transition of status.
2.  The AI may allow for an already cancelled Appointment to be cancelled again. Check that the status is scheduled before changing it, raising InvalidStatusTransitionError when otherwise illegal.
3.  Appointment inherits from PatientRecord when Appointment is not a type of PatientRecord. Appointment should reference a Patient using association.
4.  Appointment depends on NotificationManager when the UML does not support notifications or within the requirements. Remove the Notification Manager dependency from Appointments
5.  Public mutations could allow for unsupported strings which are not apart of the confirmed Appointment statuses. Use an AppointmentStatus enum containing only confirmed values.

# Exit question

**Why can code be object-oriented syntactically but still have poor object-oriented design?**

Poor design can occur when state is not protected, inheritance is used incorrectly, unrelated responsibilities are given to one class, or classes become intertwined to databases or services. These can be present even if code is object orientated syntactically.