# HBnB Project: Phase 2 - Implementation

This phase marks the transition from design to functional development. The project follows a **Layered Architecture** to ensure a strict separation of concerns between the user interface (API), the domain rules (Business Logic), and the data management (Persistence).

##  Project Structure

The codebase is organized into a modular package structure to facilitate scalability and maintainability:

```text
hbnb/
├── app/
│   ├── __init__.py          # App factory and Flask initialization
│   ├── api/                 # Presentation Layer: RESTful API endpoints
│   │   ├── __init__.py
│   │   └── v1/              # Versioned API routes
│   ├── models/              # Business Logic Layer: Entity definitions
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   └── amenity.py
│   ├── services/            # Facade Layer: Orchestrates logic between layers
│   │   ├── __init__.py
│   │   └── facade.py
│   └── persistence/         # Persistence Layer: In-memory storage
│       ├── __init__.py
│       └── repository.py
├── config.py                # Environment and app configurations
├── run.py                   # Application entry point
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

##  Architecture Overview

The application utilizes the **Facade Design Pattern**. The `HBnBFacade` class acts as a single point of entry for the API layer to interact with the models and repository.



* **Presentation Layer**: Built with `Flask-RESTx`. It handles HTTP requests, validates input data, and returns JSON responses.
* **Business Logic Layer**: Defines the core entities (User, Place, etc.) and ensures they follow business rules.
* **Persistence Layer**: Currently implements an `InMemoryRepository` for rapid development. This layer will be swapped for an SQL database in Part 3 without altering the Business Logic.

##  Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/holbertonschool-hbnb.git
    cd part2
    ```

2.  **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    python run.py
    ```
    *The API will be available at `http://127.0.0.1:5000/api/v1/` with full Swagger documentation.*
