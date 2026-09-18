Assignment 2-Case Study

Stage 3 Tutorial Activities

From Requirements to Domain Models

Week 6 | 60 minutes

# Candidate Concepts

| Candidate | Class? | Reason |
| --- | --- | --- |
| Patient |  |  |
| Practitioner |  |  |
| Appointment |  |  |
| Name |  |  |
| Clinic |  |  |
| Database |  |  |
| Cancellation |  |  |
| Status |  |  |

# CRC Cards

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

# Relationship Reasoning

**Patient to Appointment: which relationship and why?**

Patient to Appointment

Relationship: Association

Reason: A patient can have many appointments.

**Practitioner to Appointment: what multiplicity?**

Practitioner 1 --- 0..\* Appointment

**Should Appointment inherit from Patient?**

No, an appointment is not a patient, therefore inheritance is false.

**Does Clinic need to own every object?**

No, the requirements only confirm Patient, Practitioner and Appointment. Adding Clinic may be outside the design.

# AI Model Critique

Critique AI proposals: PatientManager, PractitionerManager, AppointmentManager, ClinicController, NotificationManager, ScheduleEngine.

| **AI Proposal** | **Critique** |
| --- | --- |
| **PatientManager** | Not included. The requirements mention patients, but not a separate manager class. Patient information can be managed by the Patient class at this stage. |
| **PractitionerManager** | Not included. No requirement specifies a manager class for practitioners. This appears to be an implementation detail. |
| **AppointmentManager** | Not included. Appointment scheduling and cancellation can be represented through the Appointment class. A separate manager class is not supported by the requirements. |
| **ClinicController** | Rejected. No requirement mentions a controller class. This is a software architecture concept rather than a domain concept. |
| **NotificationManager** | Rejected. The requirements do not mention SMS, email reminders, or notifications. |
| **ScheduleEngine** | Rejected. The requirements mention creating and managing appointments, but not automated scheduling logic. |