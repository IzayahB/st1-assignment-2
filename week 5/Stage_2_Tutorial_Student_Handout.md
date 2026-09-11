Assignment 2 Case Study

Stage 2 Tutorial From Problems to Requirements

Week 5 | 60 minutes

# Learning goals

-   Analyse stakeholders.
-   Distinguish functional and non-functional requirements.
-   Recognise ambiguity and unsupported requirements.
-   Define scope.
-   Develop user stories and acceptance criteria.
-   Critique AI-generated requirements.

# Activity 1 - Stakeholder Map

| Stakeholder | Need | Potential conflict |
| --- | --- | --- |
| Receptionists | Quickly create and manage appointments.. | May want faster booking while management wants more validation checks. |
| Patients | Accurate appointments and records. | May want privacy while staff need access to information. |
| Practitioners | View schedules and patient appointments. | Schedule changes may conflict with patient preferences. |
| Clinic Management | Efficient clinic operations and reliable records. | May want detailed reporting that increases staff workload. |
| IT Support / System Maintainer | A system that is easy to maintain and update. | Management may want new features that increase system complexity. |

# Activity 2 - Functional or Non-Functional?

□ Functional □ Non-functional The system shall allow staff to cancel an appointment.

□ Functional □ Non-functional The system should remain responsive for the course-scale dataset.

□ Functional □ Non-functional The system shall retain cancelled appointments.

□ Functional □ Non-functional Core business logic should be independently testable.

□ Functional □ Non-functional The system shall search for a patient by ID.

# Activity 3 - Repair Ambiguous Requirements

The system should be easy to use.

Problem: "Easy to use" is subjective and not measurable. Clarification question: How much training should staff require before they can use the system effectively?

Patient search should be fast.

Problem: "Fast" is vague and cannot be tested. Clarification question: What is the maximum acceptable search response time?

The system should securely manage data.

Problem: "Securely" is not defined. Clarification question: What security measures or access controls are required?

Appointments should normally be easy to cancel.

Problem: "Normally" and "easy" are vague and cannot be tested. Clarification question: What steps should a user take to cancel an appointment?

Activity 4 - AI Requirements Audit

Classify each suggestion: Confirmed / Assumption requiring validation / Unsupported / Out of scope.

| AI suggestion | Classification | Evidence / reason |
| --- | --- | --- |
| Patients receive SMS reminders. | Assumption requiring validation | The client brief does not mention reminders. |
| Facial recognition login. | Unsupported | No evidence in the brief supports this feature. |
| Receptionists create appointments. | Confirmed | Staff manage appointments, and receptionists are a reasonably identified stakeholder. |
| Online payment. | Out of scope | The brief focuses on patient, practitioner and appointment management only. |
| Practitioners view schedules. | Assumption requiring validation | Practitioners are stakeholders but viewing schedules are not explicitly stated. |
| AI recommends treatments. | Unsupported | The brief does not mention diagnosis or treatment support. |
| Cancelled appointments remain in history. | Confirmed | The brief identifies limited appointment history as a problem, so retaining historical records supports this need. |

# Exit question

Why is 'AI suggested it' not sufficient evidence for a requirement?

AI suggestions should not be viewed as sufficient as evidence for a requirement as it may create assumptions not stated in the client brief. If requirements are added without any evidence of the client needing it, then the finalised system may include unwanted features that increase the complexity of the system, cost and lead to scope creep.