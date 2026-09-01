# Flask SQLAlchemy Workout Application Backend

## Project Description

This project is a backend API for a Workout Application built using **Flask** and **Flask-SQLAlchemy**.

The application allows users to manage workout-related information through RESTful API endpoints. It demonstrates database modeling, relationships between entities, serialization, validations, table constraints, and organized project structure.

The project was developed as part of the **Summative Lab: Flask SQLAlchemy Workout Application Backend**.

---

## Technologies Used

* Python 3
* Flask
* Flask-SQLAlchemy
* SQLAlchemy
* Flask-Migrate
* SQLite
* Flask RESTful API
* Git & GitHub

---

## Project Features

The application includes:

* RESTful API endpoints
* SQLAlchemy database models
* Relationships between database models
* Model serialization
* Schema validations
* Model validations
* Database table constraints
* Seed data for testing
* CRUD operations
* Error handling
* Modular project structure

---

## Project Structure

```text
workout-app/
│
├── server/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── ...
│   ├── routes/
│   │   └── ...
│   └── schemas/
│       └── ...
     ── migrations/
│
     __seed.py
├    ── run.py
│
├
├── requirements.txt
├── README.md
└── .gitignore
```


## API Endpoints

The backend provides endpoints for managing workout application data.

Typical RESTful operations include:

| Method | Endpoint    | Description                |
| ------ | ----------- | -------------------------- |
| GET    | `/...`      | Retrieve all records       |
| GET    | `/.../<id>` | Retrieve a specific record |
| POST   | `/...`      | Create a new record        |
| PATCH  | `/.../<id>` | Update a record            |
| DELETE | `/.../<id>` | Delete a record            |

The exact endpoints depend on the models and requirements implemented in the project.

---

## Validations

The application includes validations to ensure that invalid data cannot be stored in the database.

Examples include:

* Required fields cannot be empty.
* Numeric values must contain valid numbers.
* Values must meet required ranges.
* Duplicate values are prevented where necessary.
* Related records must reference valid database objects.

---

## Database Relationships

The SQLAlchemy models use relationships to connect related entities.

Relationships allow the application to efficiently access associated records and maintain referential integrity within the database.

---

## Table Constraints

The database uses constraints to maintain data integrity.

Examples include:

* `NOT NULL`
* `UNIQUE`
* `FOREIGN KEY`
* `CHECK`

These constraints help prevent invalid or inconsistent records from being stored.

---

## Testing the API

The API can be tested using tools such as:

* Postman
* Insomnia
* cURL
* Browser developer tools

Example:

```bash
curl http://127.0.0.1:5000/
```

For POST, PATCH, and DELETE requests, Postman or Insomnia can be used to send JSON request bodies.

---

## Git Workflow

Git was used to manage the development process.

The project follows a feature-based workflow where changes can be developed on separate branches and merged into the main branch.

Example:

```bash
git checkout -b feature/workout-endpoints
```

After making changes:

```bash
git add .
git commit -m "Add workout API endpoints"
git push origin feature/workout-endpoints
```

Branches can then be merged into the main branch after the feature has been completed and tested.

---

## Environment Variables

If environment variables are required, create a `.env` file and add the required configuration.

Example:

```text
DATABASE_URL=sqlite:///app.db
```

Do not commit sensitive information such as passwords, secret keys, or API credentials to GitHub.

---

## Future Improvements

Possible future improvements include:

* User authentication
* JWT authorization
* Workout progress tracking
* Exercise categories
* Advanced workout statistics
* Pagination
* Search and filtering
* Automated API testing
* Deployment to a cloud platform

---

## Author

**Elvis Chege**

Flask SQLAlchemy WorkoutExercise Application Backend

---

## License

This project was created for educational purposes as part of a summative backend development lab.
