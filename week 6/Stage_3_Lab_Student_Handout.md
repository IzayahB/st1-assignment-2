Assignment 2- Case Study

Stage 3 Lab Activities

SmartCare Domain Modelling

AI OFF -> AI ON -> COMPARE -> VERIFY | 1 hour

# A - Requirements Review

Highlight nouns, verbs and business rules in SmartCare v0.2.

| **Nouns** | **Verbs** | **Business Rules** |
| --- | --- | --- |
| Patient, Practitioner, Appointment, Appointment status, Patient record, Practitioner record, Receptionist, Appointment history | Create, Update, Search, Schedule, Modify, Cancel, Display, Store, Validate | An appointment must link one patient and one practitioner., Duplicate appointments should not be allowed., Required information must be validated before saving., Appointments may have statuses (Scheduled, Completed, Cancelled)., Appointment history should be retained. |

# B - Candidate Classes

Record candidate concepts, supporting requirements, state and behaviour.

| **Concept** | **Supporting Requirement** | **State (Attributes)** | **Behaviour (Methods)** |
| --- | --- | --- | --- |
| Patient | Staff can create and update patient records. | patient_id, name | Update_details() |
| Practitioner | Staff can create practitioner records and search practitioner information. | Practitioner_id, name | Update_details() |
| Appointment | Staff can schedule, modify and cancel appointments. | Appointment_id, date_tine, status | Schedule(), cancel() |
| Status | Appointment status must be displayed. | Status | Set_status() |
| Clinic | Not explicitly required. | clinic_name | manage_records() |
| Database | Implementation detail, not a domain concept. | N/A | N/A |
| Cancellation | Action rather than an object. | N/A | Cancel() |

# C - CRC Cards

Create CRC cards for Patient, Practitioner and Appointment.

## Patient

| **Responsibilities** | **Collaborators** |
| --- | --- |
| Store patient information | Appointment |
| Update patient details |  |
| Provide patient information for appointments |  |

## Practitioner

| **Responsibilities** | **Collaborators** |
| --- | --- |
| Store practitioner information | Appointment |
| Update practitioner details |  |
| Participate in appointments |  |

## Appointment

| **Responsibilities** | **Collaborators** |
| --- | --- |
| Store appointment details | Patient |
| Link patient and practitioner | Practitioner |
| Store status |  |
| Cancel appointment |  |
| Update appointment status |  |
| Store appointment details |  |

# D - UML Model

Draw classes, attributes, operations, associations and multiplicities.

![](./Stage_3_Lab_Student_Handout_images/image-001.png)

# E - AI Design Review

Ask AI to suggest classes and relationships using only confirmed requirements; require supporting requirement IDs.

| **AI Suggestion** | **Supporting Requirement** |
| --- | --- |
| **Patient** | The system shall allow staff to create a patient record. The system shall allow staff to update patient information. |
| **Practitioner** | The system shall allow staff to create a practitioner record. |
| **AppointmentHistory** | The system shall store and display appointment history. |
| **ClinicController** | No supporting requirement identified. |

# F - Compare and Decide

Record at least one accepted, modified and rejected AI suggestion.

| **AI Suggestion** | **Evidence** | **Decision** | **Reason** | **Model Change** |
| --- | --- | --- | --- | --- |
| Patient | Requirement states staff can create and update patient records. | Accepted | Directly supported by requirements. | Added |
| Practitioner | Requirement states staff can create practitioner records. | Accepted | Directly supported by requirements. | Added |
| AppointmentHistory | Requirement states the system shall store and display appointment history. | Modified | History can be stored within Appointment rather than as a separate class. | No separate class created |
| ClinicController | No supporting requirement found. | Rejected | Implementation class not supported by requirements. | No change |

# G - Python Skeletons

Create simple Patient, Practitioner and Appointment class skeletons.

class Patient:

def \_\_init\_\_(self, patient\_id, name):

self.patient\_id = patient\_id

self.name = name

class Practitioner:

def \_\_init\_\_(self, practitioner\_id, name):

self.practitioner\_id = practitioner\_id

self.name = name

class Appointment:

def \_\_init\_\_(self, appointment\_id, patient, practitioner, date\_time, status):

self.appointment\_id = appointment\_id

self.patient = patient

self.practitioner = practitioner

self.date\_time = date\_time

self.status = status

# H - Consistency Check

Check model-code consistency; do not implement full behaviour yet.

| **UML Element** | **Python Class Present?** | **Consistent?** |
| --- | --- | --- |
| Patient | Yes | Yes |
| Practitioner | Yes | Yes |
| Appointment | Yes | Yes |
| patient_id | Yes | Yes |
| practitioner_id | Yes | Yes |
| status | Yes | Yes |
| Appointment association to Patient | Yes | Yes |
| Appointment association to Practitioner | Yes | Yes |

# Reflection

**What modelling decision was hardest? Where did AI over-design? What evidence supported your final choices?**

The hardest choice regarding modelling was determining whether appointment history should be a separate class entirely or just apart of the Appointment class. The requirements stated that the system should retain appointment history, but it was not clearly required as a separate AppointmentHistory object. As a result, I decided to keep appointment history as information stored within appointments rather than creating a separate class for it.

AI decided to suggest classes such as ClinicController, Patient Manager, PractitionerManager, NotificationManager, and ScheduleEngine. While these classes would be more useful in a larger system, they were not stated as requirements by SmartCare.

The final model was based on traceable requirements. Patients, Practitioner and Appointment were all mentioned explicitly in the client brief and functional requirements. By being able to link each decision in the model back to documented requirements, the design stayed simple, traceable, and stayed within the client’s stated requirements.