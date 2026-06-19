# Reminder Management System API

## Project Overview

Reminder Management System ek REST API based project hai jo Django REST Framework (DRF) ka use karke develop kiya gaya hai. Is project ka purpose users ko reminders create, view, update aur delete karne ki facility provide karna hai.

Project me JWT Authentication implement ki gayi hai jisse har user sirf apne reminders access kar sakta hai.

---

# Technologies Used

* Python
* Django
* Django REST Framework (DRF)
* SQLite3 Database
* JWT Authentication (Simple JWT)

---

# Features Implemented

## 1. Create Reminder

User new reminder create kar sakta hai.

Fields:

* Date
* Time
* Message
* Status
* Priority

---

## 2. View Reminders

User apne reminders dekh sakta hai.

Endpoint:

```http
GET /api/reminder/
```

---

## 3. Update Reminder

Existing reminder update kiya ja sakta hai.

Endpoint:

```http
PUT /api/reminder/update/<id>/
```

---

## 4. Delete Reminder

Reminder delete kiya ja sakta hai.

Endpoint:

```http
DELETE /api/reminder/delete/<id>/
```

---

# Reminder Model

```python
class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    status = models.CharField(max_length=20, default="Pending")
    priority = models.CharField(max_length=20, default="Medium")
```

---

# Status Feature

Reminder status maintain kiya gaya hai.

Examples:

* Pending
* Completed

Filtering:

```http
GET /api/reminder/?status=Pending
```

```http
GET /api/reminder/?status=Completed
```

---

# Priority Feature

Reminder priority maintain ki gayi hai.

Examples:

* High
* Medium
* Low

Filtering:

```http
GET /api/reminder/?priority=High
```

```http
GET /api/reminder/?priority=Medium
```

```http
GET /api/reminder/?priority=Low
```

---

# Message Search

Message ke basis par search implement ki gayi hai.

Example:

```http
GET /api/reminder/?message=testing
```

Implementation:

```python
queryset = queryset.filter(message__icontains=message)
```

---

# Date Filter

Date ke basis par reminder filter kiya ja sakta hai.

Example:

```http
GET /api/reminder/?date=2025-05-16
```

---

# Multiple Filter Support

Ek hi request me multiple filters use kiye ja sakte hain.

Example:

```http
GET /api/reminder/?status=Completed&priority=Medium
```

---

# User Registration API

New users registration ke liye API create ki gayi.

Endpoint:

```http
POST /api/reminder/register/
```

Request:

```json
{
  "username": "testuser",
  "password": "test12345"
}
```

Response:

```json
{
  "username": "testuser"
}
```

---

# JWT Authentication

Project me JWT Authentication implement ki gayi hai.

Package Used:

```bash
pip install djangorestframework-simplejwt
```

Settings Configuration:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
```

---

# Login API

User login karke access token aur refresh token generate kar sakta hai.

Endpoint:

```http
POST /api/token/
```

Request:

```json
{
  "username": "testuser",
  "password": "test12345"
}
```

Response:

```json
{
  "refresh": "token",
  "access": "token"
}
```

---

# Protected APIs

Reminder APIs ko secure kiya gaya hai.

```python
authentication_classes = [JWTAuthentication]
permission_classes = [IsAuthenticated]
```

Unauthorized Request:

```json
{
  "detail": "Authentication credentials were not provided."
}
```

---

# User-wise Reminder Security

Har reminder specific user ke saath linked hai.

```python
user = models.ForeignKey(User, on_delete=models.CASCADE)
```

Reminder Create:

```python
def perform_create(self, serializer):
    serializer.save(user=self.request.user)
```

---

# User-wise Data Access

User sirf apne reminders dekh sakta hai.

```python
def get_queryset(self):
    return Reminder.objects.filter(user=self.request.user)
```

---

# User-wise Update Security

User kisi dusre user ka reminder update nahi kar sakta.

```python
class ReminderUpdateView(generics.UpdateAPIView):

    def get_queryset(self):
        return Reminder.objects.filter(user=self.request.user)
```

---

# User-wise Delete Security

User kisi dusre user ka reminder delete nahi kar sakta.

```python
class ReminderDeleteView(generics.DestroyAPIView):

    def get_queryset(self):
        return Reminder.objects.filter(user=self.request.user)
```

---

# APIs Summary

## Registration

```http
POST /api/reminder/register/
```

## Login

```http
POST /api/token/
```

## Refresh Token

```http
POST /api/token/refresh/
```

## List Reminders

```http
GET /api/reminder/
```

## Create Reminder

```http
POST /api/reminder/
```

## Update Reminder

```http
PUT /api/reminder/update/<id>/
```

## Delete Reminder

```http
DELETE /api/reminder/delete/<id>/
```

---

# Project Outcome

Successfully implemented:

* CRUD Operations
* Status Management
* Priority Management
* Message Search
* Date Filtering
* Multiple Query Filters
* User Registration
* JWT Authentication
* Protected APIs
* User-wise Reminder Access
* User-wise Update Security
* User-wise Delete Security

This project demonstrates practical implementation of Django REST Framework, Authentication, Authorization, API Security, Filtering, and User-specific Data Management.
