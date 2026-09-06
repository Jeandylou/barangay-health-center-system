# Validation Matrix

## Team Members

| Name | Role |
|---|---|
| Jeandy Lou Pactul | Repo Lead |
| Jechele Ane Munez | Board Lead |
| Mary Cajenta | Scribe |
| Hanna Evangelista | Builder |
| Angelica Aninon | Builder |

---

## Patient Management

| Field | Rule | POST | PUT |
|---|---|---|---|
| firstName | Required, string, 1–50 characters | 422 | 422 |
| lastName | Required, string, 1–50 characters | 422 | 422 |
| dateOfBirth | Required, YYYY-MM-DD format | 422 | 422 |
| gender | Male, Female, or Other | 422 | 422 |
| contactNumber | 11 digits, starts with 09 | 422 | 422 |
| address | Required, string, 5–200 characters | 422 | 422 |

---

## Appointment Management

| Field | Rule | POST | PUT |
|---|---|---|---|
| patientId | Must reference an existing patient | 422 | 422 |
| appointmentDate | YYYY-MM-DD format | 422 | 422 |
| appointmentTime | HH:MM format | 422 | 422 |
| service | Required, 1–100 characters | 422 | 422 |
| status | Scheduled, Completed, or Cancelled | 422 | 422 |

---

## Medical Records

| Field | Rule | POST | PUT |
|---|---|---|---|
| patientId | Must reference an existing patient | 422 | 422 |
| diagnosis | Required, string | 422 | 422 |
| treatment | Required, string | 422 | 422 |
| recordDate | YYYY-MM-DD format | 422 | 422 |

---

## Health Services

| Field | Rule | POST | PUT |
|---|---|---|---|
| name | Required, 1–100 characters | 422 | 422 |
| description | Required, string | 422 | 422 |
| status | Active or Inactive | 422 | 422 |

---

## User Management

| Field | Rule | POST | PUT |
|---|---|---|---|
| username | Required, string | 422 | 422 |
| password | Required, minimum 8 characters | 422 | 422 |
| role | Administrator or Staff | 422 | 422 |

---

# Standard Error Response

All validation failures use HTTP 422.

```json
{
  "status": 422,
  "error": "Validation error message",
  "field": "fieldName"
}
{
  "status": 403,
  "error": "not allowed",
  "field": "authorization"
}
# Break-It Test Log

| Test | Expected Result | Actual Result |
|---|---|---|
| Missing required patient field | HTTP 422 | Passed |
| Invalid patient contact number | HTTP 422 | Passed |
| Invalid patient gender | HTTP 422 | Passed |
| Invalid appointment date | HTTP 422 | Passed |
| Invalid appointment status | HTTP 422 | Passed |
| Invalid medical record patientId | HTTP 422 | Passed |
| Invalid health service status | HTTP 422 | Passed |
| Invalid user role | HTTP 422 | Passed |
| Forbidden delete action | HTTP 403 | Passed |

## Break-It Testing Notes

- Invalid input must not create or update a record.
- Validation errors must use the standard error response.
- Validation failures must return HTTP 422.
- Forbidden actions must return HTTP 403.
- All listed Break-It tests currently pass in the automated test suite.
