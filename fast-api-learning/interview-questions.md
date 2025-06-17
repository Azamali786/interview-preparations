## will include all levels interview questions with answers ##

📚 On Which Pattern Does FastAPI Work?

FastAPI does NOT force any strict architecture like Django’s MVT (Model-View-Template).
It is a minimalist framework — you are free to design your application however you want.

BUT —
in good production-level FastAPI applications, developers usually follow a clean architecture based on:

✅ APIRouter / Controller Layer
✅ Service Layer
✅ Repository Layer (for database)
✅ Models/Schemas Layer

This is often called a "Layered Architecture" or a "Clean Architecture" in FastAPI apps.

🛠 In Simple Terms:
| Layer                    | Responsibility                                       | Example                                 |
| :----------------------- | :--------------------------------------------------- | :-------------------------------------- |
| **API / Router Layer**   | Handle incoming HTTP requests and responses.         | `/users/`, `/items/`                    |
| **Service Layer**        | Business logic (e.g., processing, rules, workflows). | "Register a user", "Calculate discount" |
| **Repository Layer**     | Database operations (CRUD).                          | `UserRepository`, `ItemRepository`      |
| **Models/Schemas Layer** | Data structures (Pydantic models for validation).    | `UserCreate`, `UserOut`                 |

🧩 Quick Diagram:
Client (Frontend) 
    ⬇️ 
FastAPI (Router/Controller) 
    ⬇️ 
Service Layer (Business Logic)
    ⬇️ 
Repository Layer (DB Interaction)
    ⬇️ 
Database


