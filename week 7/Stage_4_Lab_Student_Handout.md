Assignment 2-Case Study

Stage 4 Lab Activities

Implementing the SmartCare Domain Layer

DESIGN FIRST -> AI PAIR PROGRAMMING -> REVIEW -> VERIFY | 1hour

# A - Revisit Approved UML

Confirm responsibilities, attributes and relationships before coding.

**Patient:**

-   Responsibility: Store and maintain information about one patient
-   Attributes: patient\_id and name
-   Operations: update\_details()

**Practitioner:**

-   Responsibility: Store and maintain information about one practitioner
-   Attributes: practitioner\_id and name
-   Operations: update\_details()

**Appointment:**

-   Responsibility: Represent an appointment connecting one patient with one practitioner
-   Attributes: appointment\_id, date\_time, and status.
-   Operations: schedule() and cancel()

**Relationships:**

-   Each Appointment is associated with exactly 1 patient.
-   Each Appointment is associated with exactly 1 practitioner.
-   One Patient may be associated with many appointments.
-   One Practitioner may be associated with multiple appointments.

# B - Implement Patient: AI OFF

Implement Patient with type hints and basic validation.

class Patient:

def \_\_init\_\_(self, patient\_id: str, name: str):

if not patient\_id or not patient\_id.strip():

raise ValueError("Patient ID cannot be empty.")

if not name or not name.strip():

raise ValueError("Patient name cannot be empty.")

self.patient\_id = patient\_id

self.name = name

def update\_details(self, name: str) -> None:

if not name or not name.strip():

raise ValueError("Patient name cannot be empty.")

self.name = name

# C - Implement Practitioner: AI OFF

Implement Practitioner with identifier, name and specialty; no database logic.

class Practitioner:

def \_\_init\_\_(

self,

practitioner\_id: str,

name: str,

specialty: str

):

if not practitioner\_id or not practitioner\_id.strip():

raise ValueError("Practitioner ID cannot be empty.")

if not name or not name.strip():

raise ValueError("Practitioner name cannot be empty.")

if not specialty or not specialty.strip():

raise ValueError("Practitioner specialty cannot be empty.")

self.practitioner\_id = practitioner\_id

self.name = name

self.specialty = specialty

def update\_details(self, name: str, specialty: str) -> None:

if not name or not name.strip():

raise ValueError("Practitioner name cannot be empty.")

if not specialty or not specialty.strip():

raise ValueError("Practitioner specialty cannot be empty.")

self.name = name

self.specialty = specialty

# D - Implement Appointment: AI ON

Give AI the approved Appointment UML, business rules and explicit constraints. Ask it to implement only Appointment and agreed enum/exception.

from datetime import datetime

from enum import Enum

class AppointmentStatus(Enum):

SCHEDULED = "Scheduled"

CANCELLED = "Cancelled"

class InvalidStatusTransitionError(Exception):

"""Raised when an illegal appointment status change is attempted."""

pass

class Appointment:

def \_\_init\_\_(

self,

appointment\_id: str,

patient: Patient,

practitioner: Practitioner,

date\_time: datetime

):

if not appointment\_id or not appointment\_id.strip():

raise ValueError("Appointment ID cannot be empty.")

if not isinstance(patient, Patient):

raise TypeError("Appointment must have a valid Patient.")

if not isinstance(practitioner, Practitioner):

raise TypeError("Appointment must have a valid Practitioner.")

if not isinstance(date\_time, datetime):

raise TypeError(

"Appointment date and time must be a datetime object."

)

self.appointment\_id = appointment\_id

self.patient = patient

self.practitioner = practitioner

self.date\_time = date\_time

self.\_status = AppointmentStatus.SCHEDULED

@property

def status(self) -> AppointmentStatus:

return self.\_status

def schedule(self) -> None:

if self.\_status == AppointmentStatus.CANCELLED:

raise InvalidStatusTransitionError(

"A cancelled appointment cannot be scheduled again."

)

self.\_status = AppointmentStatus.SCHEDULED

def cancel(self) -> None:

if self.\_status != AppointmentStatus.SCHEDULED:

raise InvalidStatusTransitionError(

"Only a scheduled appointment can be cancelled."

)

self.\_status = AppointmentStatus.CANCELLED

# E - Review Generated Code

Check model consistency, unsupported features, public state mutation, unnecessary inheritance, invented dependencies and error handling.

**Model Consistency Review:**

| Review item | Finding | Decision |
| --- | --- | --- |
| Appointment class | Present and matches the UML | Accepted |
| Appointment identifier | Present as appointment_id | Accepted |
| Date and time | Present as date_time | Accepted |
| Appointment status | Present as protected _status | Accepted |
| Patient relationship | Present as a Patient reference | Accepted |
| Practitioner relationship | Present as a Practitioner reference | Accepted |
| schedule() operation | Present | Accepted with clarification |
| cancel() operation | Present | Accepted |
| AppointmentStatus enum | Required by Stage 4 | Accepted |
| Transition exception | Supports illegal-transition handling | Accepted |

**Unsupported Features Check:**

-   Database connections
-   SQL
-   File storage
-   User-interface code
-   Notifications
-   Payment processing
-   Manager classes

**Inheritance Review:**

-   The class is declared as class Appointment.
-   Appointment does not inherit from Patient, Practitioner, or another record class.

**Error Handling Review:**

The code handles:

-   Empty appointment identifiers with ValueError
-   Incorrect Patient objects with TypeError
-   Incorrect Practitioner objects with TypeError
-   Incorrect date and time values with TypeError

# F - Manual Behaviour Checks

Create valid objects, test invalid input, cancel a scheduled appointment and attempt an illegal repeated transition.

| Test | Expected result | Actual result | Result |
| --- | --- | --- | --- |
| Create valid objects | All three objects are created | Objects created successfully | Pass |
| Invalid Patient name | ValueError raised | ValueError raised | Pass |
| Invalid specialty | ValueError raised | ValueError raised | Pass |
| Cancel scheduled Appointment | Status becomes cancelled | Status became cancelled | Pass |
| Cancel again | Transition exception raised | Exception raised | Pass |
| Check status after failure | Status remains cancelled | Status remained cancelled | Pass |
| Schedule cancelled Appointment | Transition exception raised | Exception raised | Pass |

# G - Refactor

Remove unnecessary code and make implementation simpler and design-consistent.

I ensured the implementation stayed simple by limiting what each class’s domain responsibilities were. I removed/avoided databases, notifications, service and user interface features that weren’t supported. Appointment controls its own status updates, while Patient and Practitioner validate their own details.

# H - AI Engineering Log

Record prompt, generated contribution, decisions and verification evidence.

| AI contribution | Conforms? | Decision | Reason | Verification |
| --- | --- | --- | --- | --- |
| Appointment class | Yes | Accepted | Directly matches the approved UML | Created a valid Appointment |
| Patient and Practitioner references | Yes | Accepted | Implements the UML associations | Inspected the created Appointment |
| AppointmentStatus enum | Yes | Accepted | Explicitly required by Stage 4 | Checked initial and cancelled statuses |
| Initial scheduled status | Yes | Accepted | Supports the approved cancellation transition | Printed initial status |
| Protected _status | Yes | Accepted | Prevents ordinary public status assignment | Accessed status through the property |
| cancel() method | Yes | Accepted | Matches the UML operation | Cancelled a scheduled Appointment |
| Transition exception | Yes | Accepted | Rejects repeated cancellation clearly | Attempted cancellation twice |
| schedule() after cancellation | Partially | Modified | The UML contains schedule(), but rescheduling is unsupported | Cancelled Appointment could not be rescheduled |
| Extra status values | No | Rejected | No evidence supported additional statuses | Enum inspected |
| SQL or database logic | No | Rejected | Explicitly prohibited and absent from UML | Imports and methods inspected |
| Notification dependency | No | Rejected | Not supported by requirements | Imports and constructor inspected |

# Suggested AI prompt

Act as a Python pair programmer. Implement only the Appointment class from the approved SmartCare UML. Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. Do not add database, UI, notification or service classes. Protect status transitions and explain any decision not directly visible in the UML.

# Reflection

Which AI-generated part did you modify or reject? Why? How did the approved design constrain the AI?

I accepted the AppointmentStatus enum and the cancel() method used by the AI. These provided clear and testable updates/transitions from scheduled to cancelled. I also accepted the custom transition exception as it clearly identified an illegal repeated cancellation. I modified the interpretation of schedule() to ensure it didn’t reactivate a cancelled appointment. Even though the UML included schedule(), the requirements didn’t state that cancelled appointments could be restored. The approved design constrained the AI by limiting the solution to Patient, Practitioner, and Appointment. The Ai was prevented from adding database code, notification manager and unnecessary inheritance.