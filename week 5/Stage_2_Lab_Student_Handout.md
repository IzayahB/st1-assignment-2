Assignment 2 – Case Study Lab

Stage 2 Lab Activities

SmartCare Requirements Engineering

AI OFF -> AI ON -> VERIFY | 1 hour

# Learning objectives

-   Analyse the SmartCare client brief.
-   Identify stakeholders and scope.
-   Write functional and non-functional requirements.
-   Develop user stories and Given-When-Then acceptance criteria.
-   Use AI to critique requirements without allowing it to invent stakeholder needs.
-   Produce SmartCare Requirements Specification v1.0.

# Part A - Client Brief: AI OFF

SmartCare uses spreadsheets and paper records. Staff report duplicate bookings, difficulty finding patient information, inconsistent appointment status and limited appointment history. Management wants a small, maintainable patient, practitioner and appointment system.

# Part B - Stakeholders and Scope: AI OFF

Identify at least four stakeholders. Create In Scope and Out of Scope lists. Label uncertain features as provisional rather than confirmed.

**Stakeholders**

**Receptionists:**

-   Create appointments
-   Update appointment details
-   Search patient information

**Patients:**

-   Have appointments booked and managed
-   Need accurate appointment records

**Practitioners (Doctors/Nurses)**

-   View appointment schedules
-   Access patient information relevant to appointments

**Clinic Management:**

-   Monitor clinic operations
-   Review appointment history and records

**Administrative Staff:**

-   Maintain patient and practitioner records

**Scope**

**In Scope:**

-   Store patient records
-   Store practitioner records
-   Create appointments
-   Edit appointments
-   Cancel appointments
-   Search patient information
-   View practitioner information
-   View appointment status
-   View appointment history
-   Prevent duplicate bookings

**Out of Scope:**

-   Online patient self-booking
-   Payment processing
-   Billing and invoicing
-   Electronic prescriptions
-   Medical diagnosis support
-   SMS or email notifications

**Provisional Features:**

-   Different user access levels
-   Automated appointment reminders

# Part C - Functional Requirements: AI OFF

Write 8-12 numbered functional requirements using FR-01, FR-02 and so on. Each should describe one observable capability.

| **Functional Requirement** | **Description** |
| --- | --- |
| FR-01 | The system shall allow staff to create a patient record. |
| FR-02 | The system shall allow staff to update patient information. |
| FR-03 | The system shall allow staff to create a practitioner record. |
| FR-04 | The system shall allow staff to schedule an appointment between a patient and practitioner. |
| FR-05 | The system shall prevent appointments from being booked in an occupied time slot. |
| FR-06 | The system shall allow staff to modify an existing appointment. |
| FR-07 | The system shall allow staff to cancel an appointment. |
| FR-08 | The system shall allow staff to search for a patient record. |
| FR-09 | The system shall display the status of an appointment (Scheduled, Completed, Cancelled). |
| FR-10 | The system shall validate required fields before saving records. |

# Part D - Non-Functional Requirements: AI OFF

Write 4-6 numbered non-functional requirements covering appropriate qualities such as reliability, maintainability, usability, data integrity or testability.

| **Non-Functional Requirement** | **Description** |
| --- | --- |
| NFR-01 Reliability | The system shall save appointment data without loss during normal operation. |
| NFR-02 Usability | The system shall allow reception staff to perform common tasks with minimal training. |
| NFR-03 Maintainability | The system shall use a simple structure that can be updated and maintained by future developers. |
| NFR-04 Data Integrity | The system shall prevent duplicate appointment records from being stored. |
| NFR-05 Testability | All functional requirements shall be verifiable through testing. |
| NFR-06 Performance | Patient and appointment searches shall return results within 3 seconds under normal use. |

# Part E - User Stories and Acceptance Criteria: AI OFF

Write 4-6 user stories. For at least three, create Given-When-Then acceptance criteria including one negative or failure scenario.

**User Story 1**

As a receptionist, I want to create appointments so that patients can meet with practitioners.

**Acceptance Criteria:**

-   Given a patient and practitioner exist in the system
-   When the receptionist enters a valid appointment time
-   Then the appointment is saved successfully.

**Negative Scenario:**

-   Given an appointment already exists for that practitioner at the same time
-   When the receptionist attempts to create another appointment
-   Then the system rejects the booking and displays an error message.

**User Story 2**

As a receptionist, I want to search for patient records so that I can quickly locate patient information.

**Acceptance Criteria:**

-   Given a patient record exists
-   When the receptionist enters the patient's name into the search function
-   Then matching patient records are displayed.

**Negative Scenario:**

-   Given no matching patient exists
-   When the receptionist performs a search
-   Then the system displays "No records found."

**User Story 3**

As a receptionist, I want to update appointment information so that schedules remain accurate.

**Acceptance Criteria:**

-   Given an existing appointment
-   When the receptionist edits the appointment details and saves changes
-   Then the updated appointment information is stored.

**Negative Scenario:**

-   Given required information is missing
-   When the receptionist attempts to save changes
-   Then the system displays a validation error and does not save the record.

**User Story 4**

As a practitioner, I want to view my scheduled appointments so that I know which patients I am seeing.

**User Story 5**

As a clinic manager, I want to view appointment history so that clinic activity can be reviewed when required.

# Part F - AI Requirements Review: AI ON

Prompt: Act as a software requirements reviewer. Review the SmartCare requirements for ambiguity, inconsistency, missing clarification questions and testability. Do NOT invent new client requirements. For every suggestion, state whether it is based on evidence or is only a question/assumption requiring validation.

| **Suggestion** | **Finding** | **Type** | **Reason** |
| --- | --- | --- | --- |
| Appointment Status Definition | If requirements mention appointment status, the allowed status values may not be defined. | Evidence-based | The client brief states there is "inconsistent appointment status". Requirements should clearly define status values to ensure consistent system behavior. |
| Duplicate Booking Rules | The system may need clarification on what constitutes a duplicate booking. | Validation Question | The brief mentions duplicate bookings, but does not specify whether duplicates involve the same patient, practitioner, time slot, or a combination of these. |
| Patient Information Scope | Requirements should clearly identify which patient details are stored. | Validation Question | The brief mentions difficulty finding patient information but does not specify the minimum set of data required. |
| Appointment History Retention | The meaning of "appointment history" should be clarified. | Validation Question | The brief states limited appointment history but does not define how much historical data must be retained. |
| Practitioner Records Consistency | Functional requirements should consistently use the same terminology for practitioner records. | Evidence-based | Testability improves when a single term is used throughout the specification. |
| Search Function Testability | Search-related requirements should contain measurable success criteria. | Evidence-based | Requirements such as "find patient records" are difficult to test unless expected outcomes are specified. |
| Error Handling | Requirements should state how invalid or incomplete data is handled. | Evidence-based | Data integrity is a stated problem area and validation behavior should be testable. |
| User Roles | Clarification may be required regarding who can create, edit, or view records. | Validation Question | The brief identifies staff and management but does not define permissions. |

# Part G - VERIFY the AI Review

Classify each significant AI suggestion as Accepted, Modified, Rejected, or Unverified. Explain the evidence used.

| **AI Suggestion** | **Classification** | **Evidence Used** |
| --- | --- | --- |
| Define appointment status values | Accepted | Client brief explicitly mentions inconsistent appointment status. |
| Clarify duplicate booking rules | Accepted | Client brief identifies duplicate bookings but does not define duplicate criteria. |
| Specify patient information fields | Accepted | Client brief refers to patient information but not required fields. |
| Clarify appointment history retention period | Unverified | Brief mentions appointment history but no retention requirements are provided. |
| Use consistent practitioner terminology | Accepted | Improves consistency and testability throughout the specification. |
| Add measurable search outcomes | Accepted | Requirements should be testable and observable. |
| Define handling of invalid data | Accepted | Supports data integrity and system reliability. |
| Define user permissions | Unverified | User access levels are not described in the client brief. |

# Part H - Finalise SmartCare v0.2

Submit stakeholder analysis, scope, 8-12 FRs, 4-6 NFRs, 4-6 user stories, acceptance criteria, assumptions/open questions and selected AI review evidence.

**Assumptions:**

-   Staff members will create and manage appointments.
-   Practitioners will have individual records stored in the system.
-   Patient records can be searched by staff.
-   Appointment history will be retained for future viewing.

**Open Questions:**

-   What rules determine a duplicate booking?
-   What patient details must be stored?
-   How much appointment history should be retained?
-   Are different user permission levels required?

# Reflection

In 150-250 words: What did AI notice that you missed? What did AI invent or overreach on? Which requirement changed after review? Why must requirements have evidence?

While writing the requirements, I had not considered many areas that the AI had reviewed and identified. The most important being that appointment status values and duplicate bookings had not been clearly defined. Although the client brief mentions inconsistent appointment statuses and duplicate bookings, my original requirements didn’t explain how these would be fully handled. The AI also highlighted the importance of making the requirements measurable and testable, particularly for data validation and search functionality.

AI also generated suggestions that were outside of the evidence available within the client brief. One example being user permissions being implemented within the system, yet no direct evidence showed that SmartCare required such role-based access controls. Another example, similarly, suggests that appointment history retention time could not be confirmed from the brief. These suggestions, among others, were classified as unverified rather than being accepted.

After the review, I updated the requirements to further define appointment statues and the validation rules for appointment data. These changes helped improve the clarity and testability of requirements. It is important that requirements are supported by evidence as assumptions may lead to software features/implementations that do not meet the client’s needs. Evidence helps ensure that requirements are accurate and align with the problems identified in the client brief.