# remidme>readme.md

# Remind-me-later

**Remind-me-later** is a simple Django REST API project that allows users to create reminders by specifying a date, time, and message. The application currently supports reminders through SMS and Email, with plans to extend support for additional notification methods in the future. Note that this project only handles storing reminder data; the actual message delivery functionality is not implemented here.

---

## Features

- Create reminders by specifying date, time, and message.
- RESTful API endpoints to create and retrieve reminders.
- Designed with scalability in mind to support multiple reminder delivery methods in the future.

---

## Technologies Used

- Python 3.x
- Django Web Framework
- Django REST Framework
- SQLite (default database)

---

## Installation and Setup Instructions

Follow these steps to set up the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/TriveniPaswan/remindme.git

## ## 🚀 Project Setup Instructions

Follow the steps below to run this project locally on your system.

### Prerequisites

- Python 3.8 or above
- Git installed
- Virtual Environment module (comes with Python by default)



'''
 📦 Installation & Setup

```bash
git clone https://github.com/TriveniPaswan/remindme.git
cd remindme
python -m venv env && env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

'''

   
