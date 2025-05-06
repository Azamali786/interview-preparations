

####### MongoDB Learning ###########

Table of Contents:
    1- MongoDB Fundamentals
    2- Setting Up MongoDB with Python
    3- CRUD Operations
    4- Data Modeling
    5- Indexing and Performance
    6- Aggregation Framework
    7- Transactions
    8- Security
    9- High Availability and Scaling
    10- Monitoring and Optimization
    11- Best Practices for Production

##########################################################################S

## Installing mongodb on ubuntu
    # Import the public key
    sudo apt-get install gnupg curl
    curl -fsSL https://pgp.mongodb.com/server-7.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg --dearmor

    # Add the MongoDB repository
    echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu $(lsb_release -cs)/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list

    # Update package list
    sudo apt-get update

    # Install MongoDB
    sudo apt-get install -y mongodb-org

    # Start MongoDB service
    sudo systemctl start mongod

    # Enable MongoDB to start on boot
    sudo systemctl enable mongod

    # Check MongoDB status
    sudo systemctl status mongod

## basic commands
    mongosh   # mongodb shell

    // Show databases
    show dbs

    // Use a database
    use mydb

    // Create a collection and insert a document
    db.mycollection.insertOne({ name: "John", age: 30 })

    // Find documents
    db.mycollection.find()

    // Update a document
    db.mycollection.updateOne({ name: "John" }, { $set: { age: 31 } })

    // Delete a document
    db.mycollection.deleteOne({ name: "John" })

## Securing MongoDB (Optional but Recommended)
    # Enable authentication (edit MongoDB config)
    sudo nano /etc/mongod.conf

    Add/Modify:
        security:
        authorization: enabled

    Restart MongoDB:
        sudo systemctl restart mongod

    Create an Admin User (Inside mongosh):
        use admin           // use admin database (connect to admin database)
        db.createUser({
        user: "admin",
        pwd: "yourpassword",
        roles: ["root"]
        })

    Now, authenticate when connecting:
        mongosh -u admin -p yourpassword --authenticationDatabase admin

    Summary:
        Install MongoDB using apt.
        Start the service with sudo systemctl start mongod.
        Use mongosh to interact with the database.
        Secure MongoDB by enabling authentication.

##################################################################
1. MongoDB Fundamentals
    Key Concepts: 

    - Document Database: MongoDB stores data in flexible, JSON-like documents (BSON format)
    - Collections: Group of documents (analogous to tables in relational DBs)
    - Schemaless: No fixed schema, but you can enforce schema validation
    - Horizontal Scaling: Easy to shard (partition) data across multiple servers
    - Replication: High availability through replica sets

    Comparison with SQL: 
        SQL Concept	            MongoDB Equivalent
        Table	                Collection
        Row	                    Document
        Column	                Field
        Primary Key	            _id field
        Joins	                $lookup or embedding
        Transactions	        Multi-document ACID transactions

    2. Setting Up MongoDB with Python
        Installation
        - Install MongoDB Community Server: Official Download

        - Install Python driver:
            pip install pymongo (this is py client for mongo, mongod (mongosh) is cli for mongo)

        Basic Connection:

            from pymongo import MongoClient
            # Connect to local MongoDB
            client = MongoClient('mongodb://localhost:27017/')

            # Connect to MongoDB Atlas (cloud)
            client = MongoClient('mongodb+srv://username:password@cluster-name.mongodb.net/dbname')

            # Get database
            db = client['mydatabase']

            # Get collection
            collection = db['mycollection']
            Connection Pooling
    
        For production, configure connection pooling:
            client = MongoClient(
                'mongodb://localhost:27017/',
                maxPoolSize=50,  # Maximum number of connections
                minPoolSize=10,  # Minimum number of connections
                connectTimeoutMS=30000,  # 30 seconds
                socketTimeoutMS=30000
            )
3. CRUD Operations
    Create (Insert): 

        # Insert one document
        result = collection.insert_one({
            "name": "John Doe",
            "age": 30,
            "email": "john@example.com",
            "address": {
                "street": "123 Main St",
                "city": "New York"
            },
            "interests": ["coding", "reading", "hiking"]
        })
        print(f"Inserted ID: {result.inserted_id}")

        # Insert many documents
            users = [
                {"name": "Alice", "age": 25},
                {"name": "Bob", "age": 35},
                {"name": "Charlie", "age": 40}
            ]
            result = collection.insert_many(users)
            print(f"Inserted IDs: {result.inserted_ids}")

    Read (Query): 

        # Find one document
            user = collection.find_one({"name": "John Doe"})
            print(user)

        # Find multiple documents
            for user in collection.find({"age": {"$gt": 30}}):
                print(user)

        # Projection (select fields)
            for user in collection.find(
                {"age": {"$gt": 30}},
                {"name": 1, "email": 1, "_id": 0}  # 1=include, 0=exclude
            ):
                print(user)

        # Complex queries
            results = collection.find({
                "$and": [
                    {"age": {"$gte": 25, "$lte": 35}},
                    {"interests": "coding"}
                ]
            }).sort("age", -1).limit(5)

    Update : 
        # Update one
            result = collection.update_one(
                {"name": "John Doe"},
                {"$set": {"age": 31, "status": "active"}}
            )
        print(f"Matched: {result.matched_count}, Modified: {result.modified_count}")

        # Update many
            result = collection.update_many(
                {"age": {"$gt": 30}},
                {"$inc": {"age": 1}}  # Increment age by 1
            )

        # Upsert (insert if not exists)
            result = collection.update_one(
                {"email": "new@example.com"},
                {"$setOnInsert": {"name": "New User", "age": 20}},
                upsert=True
            )

    Delete: 

        # Delete one
            result = collection.delete_one({"name": "John Doe"})

        # Delete many
            result = collection.delete_many({"status": "inactive"})

4. Data Modeling
    Embedding vs Referencing
    Embedding (Denormalization):
        Best for one-to-few relationships
        Data is read together frequently
        Example: Comments in a blog post
        {
            "_id": "post1",
            "title": "MongoDB Guide",
            "comments": [
                {"text": "Great post!", "user": "Alice"},
                {"text": "Very helpful", "user": "Bob"}
            ]
        }
    
    Referencing (Normalization):
        Best for one-to-many or many-to-many
        Data changes frequently
        Example: Author of a book
        # books collection
        {
            "_id": "book1",
            "title": "MongoDB: The Definitive Guide",
            "author_id": "author1"
        }

        # authors collection
        {
            "_id": "author1",
            "name": "Kristina Chodorow"
        }

    Schema Design Patterns: 
        1- Polymorphic Pattern: Different document types in same collection
            # products collection
            {
                "_id": 1,
                "type": "book",
                "title": "MongoDB Guide",
                "author": "John Doe",
                "pages": 300
            }
            {
                "_id": 2,
                "type": "movie",
                "title": "Inception",
                "director": "Christopher Nolan",
                "duration": 148
            }

        2- Bucket Pattern: Group similar data into buckets (good for time-series)
            {
                "_id": "sensor1-2023-01",
                "sensor_id": "sensor1",
                "month": "2023-01",
                "readings": [
                    {"timestamp": ISODate("2023-01-01T00:00:00Z"), "value": 25.3},
                    {"timestamp": ISODate("2023-01-01T00:01:00Z"), "value": 25.4}
                ]
            }

        3- Attribute Pattern: For fields with similar characteristics
            {
                "_id": "product1",
                "attributes": [
                    {"name": "color", "value": "red"},
                    {"name": "size", "value": "XL"}
                ]
            }

5. Indexing and Performance
    Index Types:
        # Create single field index
        collection.create_index("email", unique=True)

        # Compound index
        collection.create_index([("name", 1), ("age", -1)])

        # Text index for full-text search
        collection.create_index([("description", "text")])

        # Geospatial index
        collection.create_index([("location", "2dsphere")])

        # TTL index (auto-delete after time)
        collection.create_index("createdAt", expireAfterSeconds=3600)

    Query Optimization:
        # Explain query execution
        explanation = collection.find({"age": {"$gt": 30}}).explain()
        print(explanation["executionStats"])

        # Covered queries (use index only)
        result = collection.find(
            {"age": {"$gt": 30}},
            {"_id": 0, "name": 1, "age": 1}
        ).hint([("age", 1), ("name", 1)])

6. Aggregation Framework
    Basic Pipeline:
            pipeline = [
            {"$match": {"status": "active"}},
            {"$group": {
                "_id": "$department",
                "averageSalary": {"$avg": "$salary"},
                "count": {"$sum": 1}
            }},
            {"$sort": {"averageSalary": -1}},
            {"$limit": 5}
        ]

        results = collection.aggregate(pipeline)

    Advanced Stages: 
        # $lookup (similar to SQL join)
        pipeline = [
            {
                "$lookup": {
                    "from": "departments",
                    "localField": "dept_id",
                    "foreignField": "_id",
                    "as": "department"
                }
            },
            {"$unwind": "$department"},
            {"$project": {
                "name": 1,
                "department_name": "$department.name"
            }}
        ]

        # $facet (multiple aggregations in one pass)
        pipeline = [
            {
                "$facet": {
                    "age_stats": [
                        {"$group": {
                            "_id": None,
                            "average": {"$avg": "$age"},
                            "min": {"$min": "$age"},
                            "max": {"$max": "$age"}
                        }}
                    ],
                    "department_counts": [
                        {"$group": {
                            "_id": "$department",
                            "count": {"$sum": 1}
                        }}
                    ]
                }
            }
        ]

7. Transactions

    from pymongo import MongoClient, WriteConcern, ReadConcern

    client = MongoClient('mongodb://localhost:27017/')
    db = client['banking']

    # Start a session
    with client.start_session() as session:
        try:
            # Start transaction
            with session.start_transaction(
                read_concern=ReadConcern('snapshot'),
                write_concern=WriteConcern('majority')
            ):
                # Transfer $100 from account A to B
                db.accounts.update_one(
                    {"_id": "A", "balance": {"$gte": 100}},
                    {"$inc": {"balance": -100}},
                    session=session
                )
                db.accounts.update_one(
                    {"_id": "B"},
                    {"$inc": {"balance": 100}},
                    session=session
                )
            # Transaction will commit if no exceptions
        except Exception as e:
            print(f"Transaction aborted: {e}")
            # Transaction will automatically abort on exception

8. Security
    Authentication and Authorization:
        # Connect with authentication
        client = MongoClient(
            'mongodb://username:password@localhost:27017/admin',
            authSource='admin'
        )

        # Create user with roles
        db.command(
            "createUser",
            "appuser",
            pwd="securepassword",
            roles=[
                {"role": "readWrite", "db": "mydatabase"},
                {"role": "read", "db": "reporting"}
            ]
        )
    Encryption: 
        1-At Rest Encryption: Configure in mongod.conf
            security:
                enableEncryption: true
                encryptionKeyFile: /path/to/keyfile

        2-TLS/SSL:
            client = MongoClient(
                'mongodb://localhost:27017/',
                tls=True,
                tlsCAFile='/path/to/ca.pem',
                tlsCertificateKeyFile='/path/to/client.pem'
            )

9. High Availability and Scaling

    Replica Set:
        # Connect to replica set
        client = MongoClient(
            'mongodb://host1:27017,host2:27017,host3:27017/?replicaSet=myReplicaSet',
            readPreference='secondaryPreferred'
        )
    Sharding: 
        # Connect to mongos router
        client = MongoClient('mongodb://mongos1:27017,mongos2:27017/')

        # Enable sharding
        admin_db = client.admin
        admin_db.command("enableSharding", "mydatabase")

        # Shard a collection
        admin_db.command(
            "shardCollection",
            "mydatabase.mycollection",
            key={"customer_id": "hashed"}  # or {"region": 1, "customer_id": 1}
        )


10. Monitoring and Optimization
    Monitoring Tools
        - MongoDB Atlas: Built-in monitoring for cloud
        - mongostat/mongotop: Command-line tools
        - Database Profiler:
            db.setProfilingLevel(1, 100)  # Log slow queries (>100ms)

    Performance Tips:
        - Use explain() to analyze query plans
        - Create appropriate indexes
        - Use projection to limit returned fields
        - Batch operations when possible
        - Monitor connection pool usage


11. Best Practices for Production

    Schema Design:
        Design for your application's access patterns
        Consider read/write ratio
        Pre-allocate space when possible

    Indexing:
        Follow ESR rule (Equality, Sort, Range)
        Avoid unnecessary indexes (each index adds write overhead)
        Use partial indexes for filtered queries

    Operations:
        Use connection pooling
        Implement retry logic for transient errors
        Set appropriate write concerns
        Regularly compact collections if lots of updates/deletes

    Backup and Recovery:
        Regular backups (mongodump or filesystem snapshots)
        Test restore procedures
        Consider point-in-time recovery with oplog

    Python Specific:
        Use PyMongo's built-in connection pooling
        Handle BSON types properly (ObjectId, ISODate, etc.)
        Consider using Motor for async applications
        Use bson.json_util for proper JSON serialization

    Example Production-Ready Application:

        from pymongo import MongoClient, ASCENDING, DESCENDING
        from pymongo.errors import ConnectionFailure, OperationFailure
        from datetime import datetime
        import os
        from typing import Optional

        class MongoDBManager:
            def __init__(self):
                self.client = None
                self.db = None

            def connect(self):
                """Connect to MongoDB with production-ready settings"""
                try:
                    self.client = MongoClient(
                        os.getenv('MONGO_URI', 'mongodb://localhost:27017/'),
                        maxPoolSize=50,
                        minPoolSize=10,
                        connectTimeoutMS=30000,
                        socketTimeoutMS=30000,
                        retryWrites=True,
                        retryReads=True,
                        readPreference='secondaryPreferred',
                        appname='MyProductionApp'
                    )

                    # Verify connection
                    self.client.admin.command('ping')
                    self.db = self.client[os.getenv('MONGO_DB', 'production_db')]

                    # Ensure indexes
                    self._ensure_indexes()

                except ConnectionFailure as e:
                    print(f"Failed to connect to MongoDB: {e}")
                    raise

            def _ensure_indexes(self):
                """Create necessary indexes"""
                try:
                    # Example indexes
                    self.db.users.create_index([("email", ASCENDING)], unique=True)
                    self.db.orders.create_index([("customer_id", ASCENDING), ("created_at", DESCENDING)])
                    self.db.products.create_index([("name", "text"), ("description", "text")])

                except OperationFailure as e:
                    print(f"Failed to create indexes: {e}")
                    raise

            def get_user(self, user_id: str) -> Optional[dict]:
                """Get user by ID with proper error handling"""
                try:
                    return self.db.users.find_one(
                        {"_id": user_id},
                        projection={"password": 0}  # Exclude sensitive fields
                    )
                except OperationFailure as e:
                    print(f"Failed to get user: {e}")
                    return None

            def create_order(self, order_data: dict) -> str:
                """Create a new order with transaction"""
                with self.client.start_session() as session:
                    try:
                        with session.start_transaction():
                            # Insert order
                            result = self.db.orders.insert_one(order_data, session=session)

                            # Update user's order count
                            self.db.users.update_one(
                                {"_id": order_data["customer_id"]},
                                {"$inc": {"order_count": 1}},
                                session=session
                            )

                            return str(result.inserted_id)

                    except Exception as e:
                        print(f"Order creation failed: {e}")
                        raise

        # Usage example
        if __name__ == "__main__":
            db_manager = MongoDBManager()
            db_manager.connect()

            user = db_manager.get_user("some_user_id")
            print(user)


############# Mongosh CLI (mongod) commands ##################

1. Basic Commands
show dbs
// Shows all databases on the server

use myDatabase
// Switches to 'myDatabase' (creates it if it doesn't exist)

show collections
// Lists all collections in the current database

show dbs
// Shows all databases on the server


2. CRUD Operations

// Insert single document
db.users.insertOne({
  name: "John Doe",
  age: 30,
  email: "john@example.com",
  status: "active"
})

// Insert multiple documents
db.users.insertMany([
  {name: "Alice", age: 25, status: "active"},
  {name: "Bob", age: 35, status: "inactive"},
  {name: "Charlie", age: 40, status: "active"}
])

// Find all documents
db.users.find()

// Find with filter
db.users.find({status: "active"})

// Find with projection (only return name and age)
db.users.find(
  {status: "active"},
  {name: 1, age: 1, _id: 0}
)

// Find one document
db.users.findOne({name: "John Doe"})

// Count documents
db.users.countDocuments({status: "active"})

// Distinct values
db.users.distinct("status")


// Update one document
db.users.updateOne(
  {name: "John Doe"},
  {$set: {age: 31, lastModified: new Date()}}
)

// Update many documents
db.users.updateMany(
  {status: "active"},
  {$inc: {age: 1}} // Increment age by 1
)

// Replace entire document
db.users.replaceOne(
  {name: "John Doe"},
  {name: "John Doe", age: 32, email: "john.doe@example.com"}
)


// Delete one document
db.users.deleteOne({name: "John Doe"})

// Delete many documents
db.users.deleteMany({status: "inactive"})



3. Index Operations

craete indexes:

// Single field index
db.users.createIndex({email: 1}) // 1 for ascending, -1 for descending

// Compound index
db.users.createIndex({name: 1, age: -1})

// Unique index
db.users.createIndex({email: 1}, {unique: true})

// TTL index (auto-delete after 3600 seconds)
db.logs.createIndex({createdAt: 1}, {expireAfterSeconds: 3600})

// Text index for full-text search
db.articles.createIndex({content: "text"})

// Geospatial index
db.places.createIndex({location: "2dsphere"})

List Indexes;
db.users.getIndexes()

Drop Index

db.users.dropIndex("email_1")
// or
db.users.dropIndex({email: 1})

4. Aggregation Framework

Basic Aggregation:

db.orders.aggregate([
  {$match: {status: "completed"}},
  {$group: {
    _id: "$customerId",
    totalAmount: {$sum: "$amount"},
    averageAmount: {$avg: "$amount"},
    count: {$sum: 1}
  }},
  {$sort: {totalAmount: -1}},
  {$limit: 10}
])

Common Stages:

// $lookup (join)
db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      localField: "customerId",
      foreignField: "_id",
      as: "customer"
    }
  },
  {$unwind: "$customer"},
  {$project: {
    orderId: 1,
    amount: 1,
    customerName: "$customer.name"
  }}
])

// $facet (multiple aggregations)
db.products.aggregate([
  {
    $facet: {
      "priceStats": [
        {$group: {
          _id: null,
          averagePrice: {$avg: "$price"},
          maxPrice: {$max: "$price"},
          minPrice: {$min: "$price"}
        }}
      ],
      "categoryCounts": [
        {$group: {
          _id: "$category",
          count: {$sum: 1}
        }}
      ]
    }
  }
])

5. Administration Commands

Database Operations:

// Create collection with options
db.createCollection("logs", {
  capped: true,
  size: 1000000, // 1MB
  max: 1000 // max documents
})

// Drop collection
db.users.drop()

// Drop database
db.dropDatabase()

Server Status:

// Server status
db.serverStatus()

// Current operations
db.currentOp()

// Kill operation
db.killOp(opid)

User Management:

// Create user
db.createUser({
  user: "admin",
  pwd: "securepassword",
  roles: ["root"]
})

// Create application user
db.createUser({
  user: "appuser",
  pwd: "apppassword",
  roles: [
    {role: "readWrite", db: "myapp"},
    {role: "read", db: "reporting"}
  ]
})

// List users
db.getUsers()

// Update user
db.updateUser("appuser", {
  roles: [
    {role: "readWrite", db: "myapp"},
    {role: "read", db: "analytics"}
  ]
})

// Delete user
db.dropUser("olduser")

6. Performance and Diagnostics

Explain Queries

// Explain query execution
db.users.find({age: {$gt: 30}}).explain("executionStats")

// Explain aggregation
db.users.aggregate([
  {$match: {age: {$gt: 30}}},
  {$group: {_id: "$status", count: {$sum: 1}}}
]).explain()


Profiling:

// Set profiling level
db.setProfilingLevel(1, 50) // Log queries slower than 50ms

// Get profiling level
db.getProfilingStatus()

// View profile data
db.system.profile.find().limit(10).sort({ts: -1}).pretty()

7. Replication Commands

Replica Set Status:

// Check replica set status
rs.status()

// Check configuration
rs.conf()

// Add member
rs.add("mongod1.example.net:27017")

// Remove member
rs.remove("mongod1.example.net:27017")

// Step down primary
rs.stepDown(60) // 60 seconds before eligible for reelection

8. Sharding Commands

// Enable sharding for database
sh.enableSharding("myDatabase")

// Shard a collection
sh.shardCollection("myDatabase.myCollection", {userId: "hashed"})

// Check sharding status
sh.status()

// Add shard
sh.addShard("rs1/mongod1.example.net:27017")

// Check balancer status
sh.isBalancerRunning()

9. Utility Commands

Data Import/Export:

// Export collection to JSON (run in system shell, not mongosh)
mongodump --db myDatabase --collection users --out /backup/

// Import from JSON (run in system shell, not mongosh)
mongorestore --db myDatabase --collection users /backup/myDatabase/users.bson

// Export to CSV (run in system shell)
mongoexport --db myDatabase --collection users --type=csv --fields name,age,email --out users.csv

JavaScript in mongosh:

// Write JavaScript functions
function findActiveUsers(minAge) {
  return db.users.find({
    status: "active",
    age: {$gte: minAge}
  }).toArray()
}

// Call the function
findActiveUsers(30)

// Batch operations
for (let i = 0; i < 10; i++) {
  db.test.insertOne({x: i, y: Math.random()})
}

10. Advanced Features
Transactions:

// Start a session
const session = db.getMongo().startSession()

try {
  // Start transaction
  session.startTransaction({
    readConcern: {level: "snapshot"},
    writeConcern: {w: "majority"}
  })

  const users = session.getDatabase("myDatabase").users
  const orders = session.getDatabase("myDatabase").orders

  // Operations in transaction
  users.updateOne(
    {_id: "user123", balance: {$gte: 100}},
    {$inc: {balance: -100}},
    {session}
  )
  
  orders.insertOne(
    {userId: "user123", amount: 100, date: new Date()},
    {session}
  )

  // Commit transaction
  session.commitTransaction()
} catch (error) {
  // Abort transaction on error
  session.abortTransaction()
  print("Transaction aborted:", error)
} finally {
  session.endSession()
}

Change Streams:

// Watch for changes in a collection
const changeStream = db.orders.watch()

// Iterate over the change stream
while (!changeStream.isExhausted()) {
  if (changeStream.hasNext()) {
    const change = changeStream.next()
    printjson(change)
  }
}

// Watch with pipeline
const pipeline = [
  {$match: {"operationType": "insert"}},
  {$project: {"fullDocument": 1}}
]
db.orders.watch(pipeline)

# Best Practices for mongosh #

    1- Use Tab Completion: mongosh supports tab completion for commands and collection names
    2- Pretty Print: Append .pretty() to make JSON output more readable
    3- Help System: Use help command to see available commands
    4- History: Use up/down arrows to navigate command history
    5- Scripting: Write complex operations in JavaScript files and load them with load("script.js")
    6- Connect with Options: Use connection strings with options for better control
        bash
            mongosh "mongodb://localhost:27017/myDatabase?readPreference=secondaryPreferred"
    7- Batch Inserts: For large data imports, use insertMany() or dedicated tools like mongoimport






