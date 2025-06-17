## THIS FILE WILL CONTAIN FASTAPI RESOURCES ##

## module based structure of a fastapi project
fastapi-project
├── alembic/
├── src
│   ├── auth
│   │   ├── router.py         # auth main router with all the endpoints
│   │   ├── schemas.py        # pydantic models
│   │   ├── models.py         # database models
│   │   ├── dependencies.py   # router dependencies
│   │   ├── config.py         # local configs
│   │   ├── constants.py      # module-specific constants
│   │   ├── exceptions.py     # module-specific errors
│   │   ├── service.py        # module-specific business logic
│   │   └── utils.py          # any other non-business logic functions
│   ├── aws
│   │   ├── client.py  # client model for external service communication
│   │   ├── schemas.py
│   │   ├── config.py
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   └── utils.py
│   └── posts
│   │   ├── router.py
│   │   ├── schemas.py
│   │   ├── models.py
│   │   ├── dependencies.py
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── service.py
│   │   └── utils.py
│   ├── config.py      # global configs
│   ├── models.py      # global database models
│   ├── exceptions.py  # global exceptions
│   ├── pagination.py  # global module e.g. pagination
│   ├── database.py    # db connection related stuff
│   └── main.py
├── tests/
│   ├── auth
│   ├── aws
│   └── posts
├── templates/
│   └── index.html
├── requirements
│   ├── base.txt
│   ├── dev.txt
│   └── prod.txt
├── .env
├── .gitignore
├── logging.ini
└── alembic.ini

# FAST-API ROADMAP #

    ## Beginner Level (Fundamentals) ##

        - Introduction to FastAPI
            - What is FastAPI?
                ✅ FastAPI is a modern, high-performance, web framework for building APIs with Python 3.7+ based on standard Python type hints.
                It was created by Sebastián Ramírez in 2018.
                👉 It is used to create APIs quickly, that are:
                    - Fast to code (very little boilerplate)
                    - Fast to run (thanks to ASGI and async support)
                    - Automatic API documentation (Swagger UI, ReDoc)
                    - Validation built-in using Pydantic
                    - Async-first but allows sync code too
                    - In simple words: FastAPI = Flask simplicity + Django power + async speed 🚀

            - Why use FastAPI? (ASGI vs WSGI, async support, speed)

                a) Speed
                    - FastAPI is one of the fastest Python frameworks (only behind Starlette and Uvicorn because they are lower-level libraries).
                    - Thanks to asyncio and Starlette underneath, it achieves ultra-high performance.
                    - It is comparable to Node.js and Go in speed.
                    📈 Benchmark (requests/second):
                        Framework	Requests/sec
                        FastAPI 	~30,000
                        Flask	    ~3,000

                b) ASGI vs WSGI
                    Feature	WSGI (Flask/Django)	ASGI(FastAPI/Starlette)
                    Protocol	    HTTP only	    HTTP, WebSocket, SSE
                    Concurrency	    Blocking	    Non-blocking (async)
                    Speed	        Slower	        Much faster
                    Real-time apps	  ❌	            ✅ (chat apps, live dashboards)

                    WSGI: Old standard (good for traditional websites).
                    ASGI: New standard (good for real-time, async systems).
                    🔔 Result: FastAPI is future-ready for modern applications — WebSocket, Streaming, Async tasks.

                c) Built-in Async Support
                    - Asynchronous programming allows FastAPI to handle multiple requests at the same time without waiting (I/O operations like DB queries, API calls, etc).
                    - In traditional frameworks, a DB call would block the server.
                    - In FastAPI, using async def lets your app free up the thread and serve other requests.
              
            - Installing FastAPI and Uvicorn (server)
                
                pip install fastapi     // Install FastAPI
                pip install uvicorn     //  Install Uvicorn

                pip install fastapi[all]  // Installs Uvicorn, Pydantic, and Starlette too

                Basic FastAPI App (hello.py)

                from fastapi import FastAPI

                app = FastAPI()
                @app.get("/")
                async def read_root():
                    return {"message": "Hello, World!"}

                Run app with asgi server (uvicorn)

                    - uvicorn hello:app --reload  // 

                    here:
                        hello = filename
                        app = FastAPI instance
                        --reload = Auto-reload on code change (for development)

        - First FastAPI Application
            - Creating a basic "Hello World" API

                from fastapi import FastAPI
                app = FastAPI()     // create app instance of fastapi 

                @app.get("/")   // path operation: Create a route (called a "path operation" in FastAPI)
                async def read_root():
                    return {"message": "hellow world"}      // FastAPI automatically converts the Python dictionary into a JSON response!

            - Running FastAPI app with Uvicorn
            - Interactive API docs: Swagger UI and ReDoc
                http://127.0.0.1:8000/docs	Swagger UI	Interactive, clickable documentation for your API.
                http://127.0.0.1:8000/redoc	ReDoc	Another style of auto-generated docs, more for reading.

                FastAPI uses OpenAPI specification under the hood:
                FastAPI automatically creates OpenAPI JSON schema based on your routes, models, request types, etc.
                Swagger UI and ReDoc read that OpenAPI spec and build the UI dynamically.
                You can even customize the docs later (title, description, version).

                Customizing:
                    app = FastAPI(
                        title="My First FastAPI Application",
                        description="This is a simple API built with FastAPI",
                        version="1.0.0",
                    )

            - Path Operations (Endpoints)
                Path operations are the core functions in FastAPI:
                They define which HTTP method (GET, POST, etc.) will trigger which logic for which URL path.
                You define them using decorators like @app.get(), @app.post(), etc.
                Because path operations are evaluated in order, you need to make sure that the path for /users/me is declared before the one for /users/{user_id}

            - GET, POST, PUT, DELETE

                Each HTTP method has a specific purpose:

                Method	        Purpose	                Example
                GET	        Retrieve data	        GET /users/ - List all users
                POST	    Create new data	        POST /users/ - Create a new user
                PUT	        Update existing data	PUT /users/{id} - Update user by ID
                DELETE	    Delete data	            DELETE /users/{id} - Delete user by ID

                Examples :

                    from fastapi import FastAPI

                    app = FastAPI()

                    # GET
                    @app.get("/users")
                    def list_users():
                        return {"message": "List of users"}

                    # POST
                    @app.post("/users")
                    def create_user():
                        return {"message": "User created"}

                    # PUT
                    @app.put("/users/{user_id}")
                    def update_user(user_id: int):
                        return {"message": f"User {user_id} updated"}

                    # DELETE
                    @app.delete("/users/{user_id}")
                    def delete_user(user_id: int):
                        return {"message": f"User {user_id} deleted"}

            - Path parameters
                👉 Path parameters are values captured directly from the URL path.

                @app.get("/users/{user_id}")    // used in both 
                def get_user(user_id: int):
                    return {"user_id": user_id}

                - {user_id} in the URL becomes a function argument.
                - FastAPI automatically validates and converts it (e.g., ensures user_id is an integer).
                - You can add validations too!

                from fastapi import Path

                @app.get("/items/{item_id}")
                def read_item(item_id: int = Path(..., gt=0, description="Item ID must be positive")):
                    return {"item_id": item_id}
                - gt=0 means item_id must be greater than 0.

                Path(..., gt=0, description="Item ID must be positive")
                - Path(...) =>	This says "this parameter must come from the URL path".
                - ... (ellipsis) =>	This means "required" — the client must provide this path parameter.
                - gt=0	 => This means "greater than 0" — so item_id must be a positive number, not 0 or negative.
                - description="..."	=> This adds a human-friendly description in the OpenAPI docs (Swagger UI and ReDoc).

                summary
                Syntax	        Meaning
                ...	            Required field
                gt=0	        Must be greater than 0
                lt=10	        Must be less than 10
                ge=1	        Must be greater than or equal to 1
                le=100	        Must be less than or equal to 100
                description="..."	Add text for docs (Swagger UI)
                
                Full use example of Path(), Body(), Query()

                    from fastapi import FastAPI, Path, Query, Body
                    from pydantic import BaseModel, Field

                    app = FastAPI()

                    # Define the data model for the request body
                    class Item(BaseModel):
                        name: str = Field(..., min_length=3, max_length=50, description="Name of the item")
                        price: float = Field(..., gt=0, description="Price must be positive")
                        description: str | None = Field(None, max_length=300, description="Optional description")
                        in_stock: bool = Field(default=True, description="Item availability")

                    @app.put("/items/{item_id}")
                    def update_item(
                        item_id: int = Path(..., gt=0, description="The ID of the item, must be a positive integer"),  # Path param
                        confirm: bool = Query(..., description="Confirm update by passing true or false"),             # Query param
                        item: Item = Body(...),                                                                       # JSON Body
                    ):
                        """
                        Update an item with the given item_id. Requires confirmation.
                        """
                        if not confirm:
                            return {"error": "Update not confirmed. Pass confirm=true in query parameter."}

                        return {
                            "message": f"Item {item_id} updated successfully!",
                            "updated_data": item
                        }

                    Part	                            What it does
                    item_id: int = Path(..., gt=0)	    Requires a positive integer from the path.
                    confirm: bool = Query(...)	        Requires a query parameter confirm=true or false.
                    item: Item = Body(...)	            Requires a JSON request body matching the Item Pydantic model.

            - Query parameters
                👉 Query parameters are passed after a ? in the URL.
                GET /search/?q=fastapi&limit=10

                @app.get("/search/")
                def search_items(q: str, limit: int = 10):
                    return {"query": q, "limit": limit}

                If the client doesn't send limit, it defaults to 10.
                Query parameters are optional by default (unless you make them mandatory).

                Mendatory QueryParams

                    from fastapi import Query

                    @app.get("/search/")
                    def search_items(q: str = Query(..., min_length=3)):
                        return {"query": q}
                
            - Request body (JSON)
                Request body is used when the client sends structured data (like JSON) in the request body (POST/PUT).
                You use Pydantic models to define the structure.

                from pydantic import BaseModel

                class User(BaseModel):
                    name: str
                    email: str
                    age: int

                @app.post("/users/")
                def create_user(user: User):
                    return {"user": user}

                FastAPI will automatically validate and parse incoming JSON into a Python object.
                If validation fails, FastAPI automatically returns 422 error with details.

            - Request forms (Form)

                👉 Sometimes data is sent via HTML forms (application/x-www-form-urlencoded or multipart/form-data).    
                Use Form to receive form fields:

                from fastapi import Form

                @app.post("/login/")
                def login(username: str = Form(...), password: str = Form(...)):
                    return {"username": username}
                
                Form(...) tells FastAPI to expect form fields, not JSON.

            - Request files (File)

                to upload files, you use File

                from fastapi import File, UploadFile

                @app.post("/upload/")
                def upload_file(file: UploadFile = File(...)):
                    return {
                        "filename": file.filename,
                        "content_type": file.content_type,
                        "content": file.read()
                    }
                UploadFile gives you:
                    - filename
                    - content_type
                    - file (an actual file object)
                    - You can read the contents with await file.read()
                
                ✅ For multiple files upload:

                from typing import List

                @app.post("/upload-multiple/")
                def upload_files(files: List[UploadFile] = File(...)):
                    return {"filenames": [file.filename for file in files]}
                
            Summary:
                    Topic	                    Purpose	                            How to Use
            GET, POST, PUT, DELETE	        Define HTTP methods	                @app.get("/path")
            Path Parameters	                Capture part of URL	                @app.get("/users/{user_id}")
            Query Parameters	            Capture ?param=value	            def func(param: str)
            Request Body (JSON)	            Receive structured JSON	            Pydantic Models
            Request Forms	                Receive form-data	                Form(...)
            Request Files	                Upload files	                    UploadFile = File(...)
            
        - Pydantic Models
            - Request validation using Pydantic
                In FastAPI, when a client sends data (like JSON) in a request, you define a Pydantic BaseModel class to validate that incoming data automatically.
                ✅ If the data is invalid, FastAPI automatically rejects the request and returns a 422 error with useful messages.

                from fastapi import FastAPI
                from pydantic import BaseModel

                app = FastAPI()

                class User(BaseModel):
                    name: str
                    email: str
                    age: int

                @app.post("/users/")
                def create_user(user: User):  # 'user' will be auto-validated
                    return {"message": "User created", "user": user}

                Client Sends: 
                {
                    "name": "Alice",
                    "email": "alice@example.com",
                    "age": 25
                }

            - Response models
                You can control what data is returned to the client by using a response model
                ✅ Good for security (hide sensitive data)
                ✅ Good for documentation (OpenAPI Schema)

                from fastapi import FastAPI
                from pydantic import BaseModel

                app = FastAPI()

                class UserIn(BaseModel):
                    name: str
                    email: str
                    password: str

                class UserOut(BaseModel):
                    name: str
                    email: str

                @app.post("/users/", response_model=UserOut)  // response_model will go in path operation (URL)
                def create_user(user: UserIn):
                    # pretend saving user
                    return user

                - Client sends password too in the request body ✅
                - But response will only include name and email — password will not leak!

            - Data serialization and parsing
                Serialization = Convert Python object ➔ JSON (response) (converting to string)
                Parsing = Convert JSON ➔ Python object (request)        (converting to python object)

                ✅ Pydantic handles both automatically!
                You can even parse raw data into models manually.

                from pydantic import BaseModel
                class Item(BaseModel):
                    name: str
                    price: float

                # Parsing JSON (string) to object
                data = {"name": "Pen", "price": 20}
                item = Item(**data)

                print(item.name)  # Pen
                print(item.price) # 20.0

                # Serialization back to JSON
                item_json = item.json()
                print(item_json)  # '{"name": "Pen", "price": 20.0}'

            - Using BaseModel, Field, validator
                - BaseModel
                    You always inherit your data model classes from BaseModel.

                    from pydentic import BaseModel
                    class User(BaseModel):
                        name: str
                        age: int
                - Field
                    Use Field to add extra validation like min_length, gt, default, description, etc.

                    from pydantic import BaseModel, Field

                    class Product(BaseModel):
                        name: str = Field(..., min_length=3, max_length=100, description="Name must be 3-100 characters")
                        price: float = Field(..., gt=0, description="Price must be greater than zero")

                    All these validations will show in Swagger UI automatically too!

                - validator
                    Use @validator to create custom validation logic.

                    from pydantic import BaseModel, validator

                    class User(BaseModel):
                        username: str
                        password: str

                        @validator("password")
                        def password_must_be_strong(cls, value):
                            if len(value) < 8:
                                raise ValueError("Password must be at least 8 characters long")
                            return value

                    ✅ Now if the user sends a password shorter than 8 characters, they get a 422 error automatically!

            summary:

                Feature	                    Purpose
                BaseModel	                Base class for all Pydantic models
                Field(...)	                Add validations, metadata
                validator	                Add custom Python logic for validation
                .dict(), .json()	        Serialize models
                response_model=...	        Control what is sent back to client

        - Dependency Injection (Basics)
            - What are dependencies?
                Dependencies in FastAPI are reusable pieces of logic you can inject into one or multiple path operations, without repeating the same code everywhere.
                🔵 Think of:
                    - Authentication
                    - Authorization
                    - Database session handling
                    - Common configuration
                    - Validating headers, tokens, etc.

                ✅ They help you keep your API modular, clean, and DRY (Don't Repeat Yourself).
                A dependency is just a function (or class) that FastAPI calls before your endpoint function and passes the result into your endpoint automatically.

            - Depends function
                The core magic happens using Depends from fastapi
                from fastapi import Depends
                ✅ It tells FastAPI:
                    - "Hey, before calling this API route handler, call this dependency function first."

            - Simple examples of dependencies (e.g., authentication, database session)
                a- simple dependency example
                    from fastapi import FastAPI, Depends

                    app = FastAPI()

                    def get_token():
                        return "FAKE-TOKEN"

                    @app.get("/items/")
                    def read_items(token: str = Depends(get_token)):    // DI used here
                        return {"token": token}

                    ✅ What happens here:

                        - FastAPI calls get_token() first
                        - Takes its return value (FAKE-TOKEN)
                        - Passes it to read_items(token="FAKE-TOKEN")
                        - You don't have to manually call it inside.

                b- Authentication Dependency Example
                    from fastapi import FastAPI, Depends, HTTPException, status

                    app = FastAPI()

                    def authenticate_user(token: str):
                        if token != "supersecrettoken":
                            raise HTTPException(
                                status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Invalid token",
                            )
                        return True

                    def get_current_user(token: str = "supersecrettoken"):
                        # Normally you would extract token from headers
                        authenticate_user(token)
                        return {"username": "JohnDoe"}

                    @app.get("/profile/")
                    def read_profile(user: dict = Depends(get_current_user)):
                        return {"user": user}

                    - Before hitting /profile, FastAPI first calls get_current_user()
                    - If token is bad, it raises 401 error
                    - Otherwise passes the user info.

                c- Database Session Dependency Example
                    In real production apps (like with SQLAlchemy), you use dependencies to get a DB session.
                    from fastapi import Depends

                    # Imagine this is your db.py
                    def get_db():
                        db = "fake database session"
                        try:
                            yield db
                        finally:
                            print("Closing DB session")

                    # Then inside your routes
                    @app.get("/users/")
                    def read_users(db=Depends(get_db)):
                        return {"db_session": db}

                    - yield lets FastAPI treat this like an open-close operation.
                    - After request handling, FastAPI auto-closes the session.
                

    ## Intermediate Level  ##

        - Asynchronous Programming
            - async and await in FastAPI
                First, understand:
                    async def → Defines an asynchronous function.
                    await → Waits for an asynchronous task to finish without blocking the rest of the server.

                    Async def :
                    from fastapi import FastAPI
                    import asyncio

                    app = FastAPI()

                    @app.get("/async")
                    async def read_async():
                        await asyncio.sleep(5)  # Non-blocking!
                        return {"message": "Completed after 5 seconds"}

            - When to use async vs sync
        - Advanced Request Handling
            - Headers, Cookies
            - Background tasks
            - Middleware
            - Event handlers (startup, shutdown)
        - Security & Authentication
            - OAuth2 and JWT Authentication
            - API Key authentication
            - Password hashing (passlib)
            - User login and registration system
        - Database Integration
            - Using SQLAlchemy with FastAPI
            - Using Tortoise ORM (optional)
            - Database session management
            - Alembic migrations
        - CRUD Operations
            - Full CRUD API with database
            - Best practices (repository pattern)
        - Error Handling
            - Custom exception handlers
            - HTTPException
            - Validation errors
        - File Uploads and Downloads
            - Uploading images, vide
            - Returning files for download
        - Environment Variables and Settings
            - Using Pydantic Settings (BaseSettings)
            - Loading .env files securely

    ## Advanced Level  ##

        - Background Jobs
            - BackgroundTasks
            - Using Celery with FastAPI
            - Redis as a message broker

        - WebSockets
            - Real-time communication with WebSockets
            - Building a simple chat app

        - Advanced Dependency Injection
            - Dependency classes
            - Sub-dependencies
            - Scopes (request, session, etc.)

        - Testing FastAPI Applications
            - Unit testing with pytest
            - TestClient
            - Mocking database / services
        - Caching
            - Redis caching with FastAPI
            - Cache GET responses
        - Rate Limiting
            - Implementing rate limiting (example: slowapi)
        - Logging and Monitoring
            - Adding structured logs
            - Integrating with tools like Sentry, Prometheus
        - Security Best Practices
            - CORS settings
            - Secure headers
            - Protecting sensitive endpoints
        - Handling Large Applications (Modularization)
            - Routers (APIRouter)
            - Service layer, repository layer
            - Managing large codebases
        - Dockerizing FastAPI Applications
            - Creating Dockerfile
            - Running FastAPI inside Docker
            - Best practices for Docker + Uvicorn + Gunicorn

        - Deployment
            - Deploying on AWS EC2 / Elastic Beanstalk
            - Deploying on Azure / GCP
            - Nginx + Uvicorn + Gunicorn production setup

