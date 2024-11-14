# User Expense Test Project

## Project Description

This project implements a system for managing user expenses, storing information about expenses including categories, dates, amounts, and other details. The project uses Django and Django REST Framework to create an API that allows CRUD operations on expenses, filtering by category and date, as well as obtaining expense summaries by category.

## Setup Instructions

1. **Clone the Repository:**

   First, clone the repository:

   ```bash
   git clone https://github.com/your-username/User_Expense_Test.git
   ```
   ```bash
   cd User_Expense_Test
2. **Set Up Virtual Environment: Create a virtual environment (if you haven't done so already):**
   ```bash
   python -m venv env
   
   source env/bin/activate  # For Mac/Linux
   env\Scripts\activate     # For Windows
3. **Install Dependencies: Install all dependencies from the requirements.txt file:**
    ```bash
   pip install -r requirements.txt
   
4. **Run Database Migrations: Apply the migrations to create the necessary tables in the database:**
   ```bash
   python manage.py migrate
   
5. **Run the Server: To start the server, use the following command:**
    ```bash
   python manage.py runserver
   ```
    The server will be accessible at http://127.0.0.1:8000/.
6. **Then you can use http://127.0.0.1:8000/docs to view endpoints**

## Endpoints
1. **Expense**

In this section you can view all expenses, create new expenses for a specific user (by specifying their id).

Also, for the specified user, in a certain date range, you can get all expenses for this period

The total amount of expenses is calculated for the specified category, for the specified user, for the specified month and years

Also, by a certain cost id, you can get all the information about it, change a certain parameter, delete it
2. **User**

In this section, you can create a user. By a specific id, you can get a user, update their data, or delete them