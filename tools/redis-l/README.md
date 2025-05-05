# This file will contain learning resources, notes and other stack realted informations #

# We’ll cover everything from basic key-value operations to advanced features like:

    - Data structures (Strings, Lists, Sets, Hashes, Sorted Sets)
    - Pub/Sub
    - Transactions
    - Pipelines
    - Expiration & TTL
    - Caching Patterns (LRU, Write-through)
    - Redis Streams
    - Lua scripting
    - Redis with Celery
    - Redis for rate limiting
    - Redis Search
    - Redis Cluster & Sentinel
    - Redis JSON (ReJSON)
    - Security & performance tuning
    - RedisInsight for visualization

- What is redis ??
    - Redis (Remote Dictionary Server) is an in-memory data structure store.
    - Supports Strings, Hashes, Lists, Sets, Sorted Sets, Bitmaps, HyperLogLogs, Streams.
    - Use cases: Caching, real-time analytics, queues, pub/sub messaging, session store.

- Installing and starting redis server
    - sudo apt update
    - sudo apt install redis
    - redis-server

    - Install uisng docker image from dockerhub
        - docker run -d --name redis -p 6379:6379 redis
        - docker ps (will show the status)

    python Client for redis is redis
    - pip install redis
    - connect to redis
        import redis
        r = redis.Redis(host='localhost', port=6379, db=0)
        print(r.ping())  # True if connected

    - connect using redis-cli
        - docker exec -it redis(container name) redis-cli, gets connected
        - wring ping returns pong
        - set name Azam  (set key=Azam)
        - get name (get key value)


- Redis Data types ??
    - Strings (Basic key-value like "username" => "azam")
        r.set("key", "value")   // r.set("name", "azam ali")  // using python
        set key valye   // set name "azam ali"  // using redis-cli 
    
    - Lists (Ordered list, supports push/pop from left/right — queue/stack use cases.)


###################### Beginer Level Projects ########################
Cache System for Website

Use Redis to cache frequent database queries and improve website performance.

Session Store for Web Applications

Implement Redis as a session store for user login sessions (e.g., using SETEX to expire sessions).

Simple To-Do List App

Store and retrieve a list of tasks, with the ability to add, delete, and mark tasks as done.

Simple Chat Application

Use Redis Pub/Sub for real-time messaging between users in a chat room.

Counter for Visitor Tracking

Use Redis to count and track website visits, incrementing a key each time a page is visited.

Caching Weather Data

Cache weather data using Redis for fast lookups and set an expiration time to refresh the data periodically.

Leaderboards in Games

Store and update scores in a Redis sorted set, allowing you to fetch the top scores efficiently.

URL Shortener

Implement a simple URL shortener where Redis maps short URLs to original URLs.

Rate Limiting for API

Use Redis for API rate limiting, ensuring that users can't hit the API more than a certain number of times per minute.

Simple Voting System

Build a voting system where votes are stored in Redis. Use Redis to store vote counts and set expiration times for votes.



##############  Intermediate Level Projects #########################
Real-Time Notifications System

Implement a system that uses Redis Pub/Sub for broadcasting notifications to all online users in real time.

Task Queue with Redis

Create a task queue system using Redis LPUSH/BRPOP to manage background jobs and workers (e.g., simple email sender).

Event Streaming and Logs

Use Redis Streams to store and process events or logs that can be consumed in real time by consumers.

Session Expiry System

Use Redis with a TTL (Time-To-Live) to expire sessions after a specified period or activity.

Real-Time Analytics Dashboard

Use Redis to store metrics (e.g., page views, active users) and provide a dashboard that updates in real-time.

Job Scheduling System

Build a job scheduler using Redis Sorted Sets (ZADD) to schedule jobs in the future.

Chat Application with Redis (Advanced)

Create a chat app that supports multiple rooms, persistent chat history, and real-time messaging using Redis Pub/Sub.

Caching API Responses

Build a caching system for an API, where Redis caches responses and reduces the load on the main database.

Distributed Locking System

Implement a distributed locking mechanism with Redis to prevent race conditions in distributed systems.

Search Engine with Redis

Build a simple search engine where Redis is used to index keywords and phrases, with fast retrieval of search results.



##################### Advance Level Project #######################

Distributed Task Queue with Celery and Redis

Use Redis as a broker for Celery to manage and process distributed tasks asynchronously.

Real-Time Stock Market Dashboard

Use Redis Streams to ingest real-time stock data and update a live dashboard that displays stock prices.

Distributed Caching System (Microservices)

Implement Redis as a distributed cache for a microservices architecture, with multiple services accessing shared data.

Rate Limiting for APIs (Distributed)

Implement a distributed rate-limiting system using Redis to throttle API calls across multiple servers.

Event-Driven Architecture with Redis

Use Redis Streams for event-driven architectures, where different services react to events in real-time.

Global Session Management (Across Services)

Build a session management system using Redis to store user sessions across multiple services in a microservices architecture.

Recommendation System with Redis

Use Redis to store user preferences and interactions, and generate recommendations based on their activity.

Real-Time Multi-User Game with Redis

Build a multiplayer game that stores real-time game state (scores, player positions) in Redis for low-latency updates.

Multi-Tenant SaaS App with Redis

Implement a multi-tenant SaaS application where Redis is used to store and manage tenant-specific configurations and sessions.

Redis-Based Chatbot Framework

Build a scalable chatbot framework where Redis handles the state of conversations, message queues, and user sessions in real time.


###########  Additional Bonus Pointers ###########################

Redis Cluster for High Availability: Set up Redis Cluster for horizontal scaling and fault tolerance in production.

Redis Graph: Build applications that store and query graph data, such as social networks, using Redis Graph.

Redis for Machine Learning: Use Redis as a high-speed cache for machine learning model predictions or model parameters.

Redis as a Pub/Sub System in IoT Applications: Build an IoT application where Redis Pub/Sub handles communication between devices.




############### REDIS CLI COMMANDS ##################

🧵 Strings
Strings are the most basic Redis data type, representing text or binary data.

    Command	Description:
        SET key value	Set the value of a key
        GET key	Retrieve the value of a key
        APPEND key value	Append a value to an existing key
        INCR key	Increment the integer value of a key by one
        DECR key	Decrement the integer value of a key by one
        MSET key1 val1 ...	Set multiple keys to multiple values
        MGET key1 key2 ...	Get the values of multiple keys
        STRLEN key	Get the length of the value stored at key


📚 Lists
Lists are ordered collections of strings, allowing operations from both ends.

    Command	Description:
        LPUSH key val1 val2	Prepend one or multiple values to a list
        RPUSH key val1 val2	Append one or multiple values to a list
        LPOP key	Remove and get the first element in a list
        RPOP key	Remove and get the last element in a list
        LRANGE key start stop	Get a range of elements from a list
        LLEN key	Get the length of a list
        LSET key index value	Set the value of an element in a list by index


📦 Sets
Sets are unordered collections of unique strings.

    Command	Description: 
        SADD key member1 ...	Add one or more members to a set
        SMEMBERS key	Get all the members in a set
        SREM key member1 ...	Remove one or more members from a set
        SISMEMBER key member	Determine if a given value is a member of a set
        SCARD key	Get the number of members in a set
        SUNION key1 key2	Get the union of multiple sets
        SINTER key1 key2	Get the intersection of multiple sets


🧩 Hashes
Hashes are maps between string field and string values, ideal for representing objects.


    Command	Description: 
        HSET key field value	Set the string value of a hash field
        HGET key field	Get the value of a hash field
        HMSET key field1 val1 field2 val2	Set multiple hash fields to multiple values
        HGETALL key	Get all fields and values in a hash
        HDEL key field1 field2	Delete one or more hash fields
        HEXISTS key field	Determine if a hash field exists
        HINCRBY key field increment	Increment the integer value of a hash field by the given number


📊 Sorted Sets (ZSets)
Sorted Sets are similar to Sets but with an associated score for each member, allowing sorted retrieval.


    Command	Description
        ZADD key score1 member1 score2 member2	Add one or more members to a sorted set, or update its score if it already exists
        ZRANGE key start stop [WITHSCORES]	Return a range of members in a sorted set, by index
        ZREVRANGE key start stop [WITHSCORES]	Return a range of members in a sorted set, by index, with scores ordered from high to low
        ZREM key member1 member2	Remove one or more members from a sorted set
        ZINCRBY key increment member	Increment the score of a member in a sorted set
        ZRANK key member	Determine the index of a member in a sorted set
        ZCARD key	Get the number of members in a sorted set


🔁 Streams
Streams are append-only data structures, ideal for logs and real-time data.

    Command	Description:
        XADD key * field1 value1 [field2 value2 ...]	Add a new entry to a stream
        XRANGE key start end	Get a range of entries from a stream
        XREAD COUNT count STREAMS key id	Read data from one or multiple streams
        XDEL key id1 [id2 ...]	Delete one or more entries from a stream
        XLEN key	Get the length of a stream

⚙️ Generic Commands
These commands apply to various data types.

    Command	Description:
        DEL key1 key2 ...	Delete one or more keys
        EXISTS key	Determine if a key exists
        EXPIRE key seconds	Set a key's time to live in seconds
        TTL key	Get the time to live for a key
        TYPE key	Determine the type stored at key
        RENAME key newkey	Rename a key
        KEYS pattern	Find all keys matching the given pattern
        SCAN cursor [MATCH pattern] [COUNT count]	Incrementally iterate the keys space

🧪 Server & Connection Commands
Commands to manage the Redis server and client connections.

    Command	Description
        PING	Check if the server is running
        AUTH password	Authenticate to the server
        SELECT index	Change the selected database for the current connection
        FLUSHDB	Remove all keys from the current database
        FLUSHALL	Remove all keys from all databases
        INFO	Get information and statistics about the server
        CLIENT LIST	Get a list of connected clients
        MONITOR	Listen for all requests received by the server
        CONFIG GET parameter	Get the value of a configuration parameter
        CONFIG SET parameter value	Set a configuration parameter


##########  REDIS DATA TYPES and USES with CLI ##############
🔤 Strings

📚 Lists

📦 Sets

🧩 Hashes

📊 Sorted Sets (ZSets)

🔁 Streams

🧮 Bitmaps (under Strings)

🧠 HyperLogLog

🧱 GeoSpatial

🗃️ JSON (via RedisJSON module)

1- String
    SET user "Azam Ali"
    GET user

    SET count 10
    INCR count
    GET count

2- LPUSH fruits "banana" "apple" "cherry" "apple"   // create an ordered array (list) with given elements
    LRANGE fruits 0 -1   // display all elements of the array
    RPUSH fruits "banana"    // add banana to the right of the array
    LPUSH fruits "jackfruit"    // add element to the left of the string
    LREM fruits 1 banana     // removes the first occurance
    LREM fruits 2 "apple"    // removes the second occurance
    DEL fruits       // deletes the array

    LLEN fruits
    LINDEX mylist 1     // get item by index
    LSET fruits 1 "grape"    // sets(updates) value at specific index

    LPOP furits     // Remove and return first (leftmost) item
    RPOP fruits     // Remove and return last (rightmost) item

    LPUSHX mylist "kiwi"    // Push only if list exists
    RPUSHX mylist "mango"   

    BLPOP names 10  // Blocking left pop (wait for 10 seconds if list empty)
    BRPOP mylist 10

    LREM mylist 2 "apple"   // Removes 2 occurrences from head to tail
    LTRIM mylist 0 2    // Keeps only first 3 items ( 0 1 and 2nd indexes are safa rest trimed)

    RPOPLPUSH mylist yourlist       // Pop from end of one list and push to start of another
    BRPOPLPUSH mylist yourlist 10   // Blocking version of RPOPLPUSH

    Command	        Description
    LPUSH	        Add to left (start)
    RPUSH	        Add to right (end)
    LPUSHX/RPUSHX	Push only if list exists
    LPOP / RPOP	    Remove from left / right
    LRANGE	        Get elements in index range
    LLEN	        Get list length
    LINDEX	        Get element at index
    LSET	        Set element at index
    LREM	        Remove elements by value
    LTRIM	        Trim list to given range
    RPOPLPUSH	    Transfer element from one list to another
    BLPOP/BRPOP	    Blocking pop (waits if list is empty)
    BRPOPLPUSH	    Blocking pop + push between lists
    DEL	            Delete list

 


#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

🥇 BASICS (Foundational Topics)
    Topic	                                Description
    What is Redis?	                        Overview, Use-cases, How Redis works internally (memory-based).
    Installation & Setup	                Install Redis locally, run Redis server, basic configuration.
    Redis CLI Basics	                    Connect to Redis using CLI, basic commands.
    Data Types                              Introduction	String, List, Set, Hash, Sorted Set (ZSet) — core types.
    Simple CRUD Operations	                SET, GET, DEL, EXISTS, EXPIRE, TTL.

    ✅ Practical:
    - Build a simple Redis-powered counter.
    - Store and retrieve user profiles.

🥈 INTERMEDIATE (Core Developer Skills)
    Topic	                                    Description
    Advanced Data Structures	                Lists (LPUSH, LRANGE), Sets (SADD, SMEMBERS), Hashes (HSET, HGETALL), Sorted Sets (ZADD, ZRANGE).
    Expiration and TTLs	                        Setting expiration for keys (EXPIRE), using it for sessions/caching.
    Pub/Sub System	                            Real-time messaging using PUBLISH and SUBSCRIBE.
    Transactions	                            MULTI, EXEC, DISCARD, WATCH (optimistic locking).
    Pipelining	                                Execute multiple commands faster with fewer network round-trips.
    Scripting with Lua	                        Write custom scripts in Redis with EVAL.
    Redis Streams	                            Reliable messaging (like Kafka-lite) using XADD, XREAD, XGROUP.
    Persistence	                                RDB Snapshots, AOF (Append Only Files), Hybrid approach.
    Redis Security	Securing Redis (requirepass, renaming commands, IP whitelisting).
    Basic Performance Tuning	Configs that improve memory and speed.

    ✅ Practical:

    - Create a chat app using Pub/Sub.
    - Build a task queue with Lists.
    - Create real-time notification system.

🥇 ADVANCED (Production-Ready Concepts)
    Topic	Description
    Redis Cluster	Distributing data across multiple nodes for scaling.
    Sharding	Manual partitioning of keys across Redis instances.
    High Availability	Redis Sentinel, automatic failover setup.
    Caching Strategies	Cache Aside, Write Through, Write Behind.
    Rate Limiting	Build API rate limiter with Redis (e.g., 100 requests/min/user).
    Leaderboards & Ranking	Using Sorted Sets (ZADD, ZRANGE) for building leaderboards.
    Distributed Locks	Reliable locking using RedLock algorithm (using SETNX).
    Session Store	Storing web sessions securely and efficiently.
    HyperLogLog	Probabilistic data structures for approximate counts.
    Bitmaps and Bitfields	Space-efficient tracking (e.g., daily active users).
    Redis Bloom Filters	Fast membership tests with minimal memory usage.

    ✅ Practical:
    - Build a Leaderboard App (e.g., for gaming apps).
    - Implement distributed lock system.
    - Build a scalable real-time feed system.

🏆 BONUS (Mastery Skills)
    Topic	                                Description
    Monitoring Redis	                    Using INFO, RedisInsight, and metrics.
    Redis Backup & Restore	                Best practices.
    Eviction Policies	                    LRU, LFU, Random eviction.
    Memory Optimization	                    Compression techniques, memory efficient data types.
    Using Redis Modules	                    e.g., RediSearch (for search), RedisJSON (store JSON efficiently).
    Real-time Analytics with Redis	        Dashboard counters and trends.
    Redis in Microservices	                Redis as a central broker and cache for microservices architecture.
    Integrating with Docker & Kubernetes	Running Redis inside containers.
    Using Redis with Celery	                Task queues with Django, Flask, or FastAPI.

    ✅ Practical:
    - Build a real-time analytics dashboard.
    - Integrate Redis as broker for background workers (with Celery).

🛠 HOW TO STUDY?
    - For each topic:
    - Understand theory (concept clearly)
    - Write CLI commands manually 
    - Implement a small project for each major concept
    - Do Redis Python projects combining topics
    - Practice optimization and production deployment

🚀 Example Big Final Projects (Production-Level)
    ✅ Real-time Chat Application (Pub/Sub + Streams + WebSocket)
    ✅ Task Scheduler (Redis Queue + Worker System)
    ✅ Rate Limiting Gateway (Redis for API limits)
    ✅ Real-Time Leaderboard (Sorted Sets)
    ✅ Distributed Lock Manager (SETNX/RedLock)
    ✅ E-commerce Cart System (Hash + TTL)    
    ✅ Session Management (Web App Sessions in Redis)

🧠 Summary: Redis Learning Ladder
    Level	                Focus
    Basics	                Setup, basic types (Strings, Lists, Sets, Hashes).
    Intermediate	        Real-world apps (pub/sub, caching, persistence, security).
    Advanced	C           lustering, high availability, distributed locks, real-time analytics.
    Bonus	                Optimization, microservices, monitoring, Redis modules.



############################################################################################################
📚 Redis Major Use Cases (with Practical Examples)
    1. Caching (Most Common)
        🔹 Problem: Slow database queries or API calls.
        🔹 Solution: Use Redis as an in-memory cache to store frequently accessed data.
        🔹 Example:
            - Store API responses temporarily.
            - Cache product information on an e-commerce site.
            - Cache rendered pages or parts of a page.

        🔹 Practical:
            cache.set('product:123', product_data, ex=300)  # 5 mins expiration

    2. Real-time Chat / Messaging
        🔹 Problem: Need fast communication between users.
        🔹 Solution: Redis Pub/Sub or Streams allow sending and receiving messages instantly.
        🔹 Example:
            Chat applications.
            Real-time notifications (order updates, messages).

        🔹 Practical:
            redis.publish('chat_room', 'Hello from user123')

    3. Leaderboards / Ranking Systems
        🔹 Problem: Maintain ranked lists (high scores, best sellers).        
        🔹 Solution: Use Sorted Sets (ZADD, ZRANGE) to maintain sorted ranking.
        
        🔹 Example:        
            Online gaming leaderboards.       
            Sales competitions dashboard.
        
        🔹 Practical:
            redis.zadd('game_leaderboard', {'player1': 100, 'player2': 150})

    4. Session Management
        🔹 Problem: Store and retrieve user session data quickly.
        🔹 Solution: Use Redis to store web sessions (JWT, cookies, auth info).

        🔹 Example:
            User login sessions for websites.
            Shopping carts that persist across sessions.

        🔹 Practical:
            redis.hset('session:user123', mapping={'token': 'abc123', 'role': 'admin'})

    5. Rate Limiting
        🔹 Problem: Prevent abuse (e.g., too many login attempts).
        🔹 Solution: Redis counters with expiration.

        🔹 Example:
            Allow 100 API calls per user per minute.
            Throttle login attempts.

        🔹 Practical:
            count = redis.incr('user:123:requests')
            redis.expire('user:123:requests', 60)

    6. Task Queues / Background Jobs
        🔹 Problem: Offload heavy tasks from main server.
        🔹 Solution: Push tasks into a Redis List, then worker servers pop and process them.

        🔹 Example:
            Sending emails, SMS, image processing, video rendering.

        🔹 Practical:
            redis.lpush('task_queue', 'send_email_to_user_123')

    7. Real-Time Analytics
        🔹 Problem: Dashboard counters need fast updates.
        🔹 Solution: Use counters and bitmaps.
        
        🔹 Example:
            Counting website visits.
            Tracking which users were active today.
        
        🔹 Practical:
            redis.incr('page_views:homepage')

    8. Distributed Locking
        🔹 Problem: Multiple servers need to lock a resource safely.
        🔹 Solution: Redis SETNX (SET if Not eXists) or RedLock algorithm.

        🔹 Example:
            Prevent double booking (event tickets).
            Prevent two workers from picking same job.

        🔹 Practical:
            redis.set('lock:resource', 'locked', nx=True, ex=10)

    9. Geo-Spatial Applications
        🔹 Problem: Find nearby locations efficiently.
        🔹 Solution: Redis GEO commands (GEOADD, GEORADIUS).

        🔹 Example:
            Food delivery app: find restaurants near user.
            Ride sharing app: find nearby drivers.

        🔹 Practical:
            redis.geoadd('drivers', (longitude, latitude, 'driver1'))

    10. Stream Processing
        🔹 Problem: Process continuous streams of data reliably.
        🔹 Solution: Use Redis Streams (XADD, XREAD, XGROUP).

        🔹 Example:
            IoT sensor data ingestion.
            Real-time financial transactions.

        🔹 Practical:
            redis.xadd('mystream', {'temp': 22, 'humidity': 55})

    11. Temporary Data Storage
        🔹 Problem: Need a short-lived, fast, flexible database.
        🔹 Solution: Redis stores key-value data with optional TTL.

        🔹 Example:
            OTP codes for login.
            Temporary discount coupons.

        🔹 Practical:
            redis.set('otp:user123', '567890', ex=120)  # Expires in 2 mins

    12. Full-Text Search (with RediSearch Module)
        🔹 Problem: Need super-fast search capability.
        🔹 Solution: Use RedisSearch module for indexing and full-text search.

        🔹 Example:
            Search users by name, emails.
            Search products by title and description.

        🔹 Practical:
            (Requires module setup.)

🎯 Quick Recap Table
    Use Case	                    Redis Feature	                    Example
    Caching	                        TTL, SET/GET	                    Cache database queries
    Chat App	                    Pub/Sub, Streams	                Messaging between users
    Leaderboard	                    Sorted Sets	                        Rank players
    Sessions	                    Hashes, TTL	                        User authentication
    Rate Limiting	                Counters + Expiry	                API throttling
    Task Queue	                    Lists	                            Background jobs
    Analytics	                    Counters, Bitmaps	                Real-time dashboards
    Distributed Locks	            SETNX, RedLock	                    Lock critical resources
    Geo Search	                    GEO commands	                    Find nearest locations
    Streams	                        XADD, XREAD	                        Real-time logs


#####################################################################################################
    - Data structures (Strings, Lists, Sets, Hashes, Sorted Sets)
    - Pub/Sub
    - Transactions
    - Pipelines
    - Expiration & TTL
    - Caching Patterns (LRU, Write-through)
    - Redis Streams
    - Lua scripting
    - Redis with Celery
    - Redis for rate limiting
    - Redis Search
    - Redis Cluster & Sentinel
    - Redis JSON (ReJSON)
    - Security & performance tuning
    - RedisInsight for visualization

## Data Structure ##
    📚 All Redis Data Structures (with Simple Explanation)

        Data Structure	                        Description	                                        Real-world Usage

        Strings	                                Basic key-value pair (text, numbers, binary)	    Caching, counters, session tokens
        Lists	                                Ordered collection of strings	                    Queues, recent activities
        Sets	                                Unordered collection of unique strings	            Unique users, tags, lottery systems
        Sorted Sets (ZSets)	                    Sets ordered by score	                            Leaderboards, rankings, time-series events
        Hashes	                                Map of fields and values (like a dictionary)	    User profiles, settings
        Streams	                                Append-only log data (like Kafka)	                Event sourcing, chat messages
        Bitmaps	                                Operate at the bit level inside a string	        User activity tracking, feature flags
        HyperLogLog	                            Approximate counting of unique items	            Counting unique visitors with small memory
        Geospatial Indexes	                    Store and query locations	                        Nearby stores, location-based services
        Bloom Filters (via RedisBloom Module)	Probabilistic data structure for membership tests	Fast "maybe" tests (e.g., did I already see this email?)

    📦 Full List
        Type	                    Name	                    Purpose
        Primitive	                Strings	                    Store any type of basic data (text, binary, integers)
        Collection	                Lists	                    Ordered collection of values
        Collection	                Sets	                    Unordered, unique values
        Collection	                Sorted Sets	                Values ordered by a score
        Collection	                Hashes	                    Key-value inside a key
        Stream	                    Streams	                    Append-only logs for real-time systems
        Bitwise	                    Bitmaps	                    Efficient bit-level storage and operation
        Probabilistic	            HyperLogLog	                Approximate distinct count
        Spatial	                    Geospatial	                Store and query latitude/longitude points
        Probabilistic	            Bloom Filters (Module)	    Space-efficient membership test

    ## Strings ##
        (Simple key-value pairs.)
        Most basic.
        Value can be: Text, JSON, binary, or integers.

        Command	                            Use	                            Example
        SET key value	                    Set a key to a value	        SET name "azam"
        GET key	                            Get value of a key	            GET name
        INCR key	                        Increment integer value	        INCR counter
        DECR key	                        Decrement integer value	        DECR counter
        INCRBY key number	                Increment by specific amount	INCRBY counter 5
        APPEND key value	                Append data to string	        APPEND name " ali"
        MSET key1 val1 key2 val2 ...	    Set multiple keys at once	    MSET a 1 b 2
        MGET key1 key2	                    Get multiple keys	            MGET a b
        STRLEN key	                        Length of string value	        STRLEN name
        SETEX key seconds value	            Set with expiry	                SETEX otp 120 "1234"
        GETSET key new_value	            Get old value, set new value	GETSET name "azam ali"

        ALL CLI commands :

        | Command                          | Meaning                      | Example                    | Use Case            |
        | :------------------------------- | :--------------------------- | :------------------------- | :------------------ |
        | `SET key value`                  | Set a string                 | `SET name "Azam"`          | Store simple values |
        | `GET key`                        | Get the value                | `GET name`                 | Retrieve data       |
        | `DEL key`                        | Delete the key               | `DEL name`                 | Remove data         |
        | `SETEX key seconds value`        | Set value with expiry        | `SETEX temp 60 "hot"`      | Temporary data      |
        | `SETNX key value`                | Set if not exists            | `SETNX first_visit "true"` | Atomic set          |
        | `MSET key value [key value ...]` | Set multiple keys            | `MSET name Azam age 25`    | Insert batch        |
        | `MGET key [key ...]`             | Get multiple keys            | `MGET name age`            | Fetch batch         |
        | `INCR key`                       | Increment numeric value by 1 | `INCR counter`             | Page views, likes   |
        | `INCRBY key amount`              | Increment by value           | `INCRBY counter 10`        | Add scores          |
        | `DECR key`                       | Decrement by 1               | `DECR stock`               | Countdown timers    |
        | `DECRBY key amount`              | Decrement by value           | `DECRBY stock 5`           | Reduce stock        |
        | `APPEND key value`               | Append value to string       | `APPEND log "new event"`   | Logs, tracking      |
        | `GETSET key value`               | Set new value, return old    | `GETSET name "Ali"`        | Update tracking     |
        | `STRLEN key`                     | Get length of value          | `STRLEN name`              | String size check   |

        Advance Concepts : 
            - SET key value [EX seconds] - expire after seconds
            - SET key value [PX milliseconds] - expire after ms
            - SET key value [NX|XX]
            - NX: Set if Not Exists
            - XX: Set if key already Exists
            examples:
            SET session:user123 "token" EX 3600 NX   => Store a session token for 1 hour, only if it doesn't exist already.

        Python Implementations : 
        pip install redis
        Also start a local Redis server running (redis-server) before running these.

        import redis

        # Connect to local Redis server
        r = redis.Redis(host='localhost', port=6379, db=0)
        r.set('name', 'Azam')       # SET key value

        value = r.get('name')
        print(value.decode())  # Output: Azam   # GET key

        r.delete('name')    // DEL key

        r.setex('temp_key', 10, 'This will expire in 10 sec')   # SETEX key seconds value
        r.setnx('first_login', 'true')     # SETNX key value (Set only if Not Exists)

        r.mset({                        # MSET key value [key value ...] (Multiple Set)
            'city': 'Mumbai',
            'country': 'India',
            'language': 'Hindi'
        })

        values = r.mget('city', 'country', 'language')          # MGET key [key ...] (Multiple Get)
        print([v.decode() for v in values])
        # Output: ['Mumbai', 'India', 'Hindi']

        r.set('counter', 0)             # INCR key
        r.incr('counter')
        print(r.get('counter').decode())  # Output: '1'

        r.incrby('counter', 10)             # INCRBY key amount
        print(r.get('counter').decode())  # Output: '11'

        r.decr('counter')                   # DECR key
        print(r.get('counter').decode())  # Output: '10'

        r.decrby('counter', 5)              # DECRBY key amount
        print(r.get('counter').decode())  # Output: '5'

        r.set('log', 'start:')              # APPEND key value
        r.append('log', ' user_logged_in')
        print(r.get('log').decode())  # Output: 'start: user_logged_in'

        old_value = r.getset('name', 'Ali')         # GETSET key value (Set New Value, Return Old)
        if old_value:
            print(old_value.decode())  # Output: previous value of 'name'
        print(r.get('name').decode())  # Output: 'Ali'

        length = r.strlen('name')               # STRLEN key
        print(length)  # Output: length of the string 'Ali' -> 3

        Adcance Concepts :
        ✅ EX (expire seconds)
        ✅ PX (expire milliseconds)
        ✅ NX (Only if key doesn't exist)
        ✅ XX (Only if key exists)

        # Set a key with expiration 30 seconds, only if key does NOT exist
        r.set('token', 'abc123', ex=30, nx=True)

        # Set a key with expiration 5000 milliseconds (5 sec), only if EXISTS
        r.set('token', 'newtoken456', px=5000, xx=True)
        
        Real-World Use Cases: 
        
        Use Case	                    Example
        Session storage	                Store login tokens
        Caching	                        Cache API responses
        Counters	                    Track page views, likes
        Temporary data	                OTP codes, temp auth
        Feature flags	                Set ON/OFF switches easily

        Production Level Tips:

        Tip                                             	Reason
        Always use EX (expiry) for sessions/temp data	    Avoid stale data
        Use SETNX to prevent overwriting critical values	Atomic operations
        Use pipelining (pipeline) for batch operations	    Speed up multiple queries
        Monitor string size	                                512MB is huge, but be careful

        Example of pipelining (batch set):
            pipe = r.pipeline()
            pipe.set('k1', 'v1')
            pipe.set('k2', 'v2')
            pipe.execute()

        Common Interview Questions :                        
        | Question                                             | Tip to Answer                 |
        | :--------------------------------------------------- | :---------------------------- |
        | How is Redis String different from normal DB string? | Binary-safe, can be counters  |
        | Can Redis Strings hold JSON objects?                 | Yes, serialize before storing |
        | What's the maximum size of a String in Redis?        | 512MB                         |
        | How do you expire a String key after 10 minutes?     | `SET key value EX 600`        |
        
        Practical Example: 
        Imagine you want to save an OTP code that expires after 5 minutes:

        otp_code = '987654'
        r.setex('otp:user123', 300, otp_code)

        # Later, retrieve it
        retrieved_otp = r.get('otp:user123')
        if retrieved_otp:
            print(retrieved_otp.decode())
        else:
            print('OTP expired!')

        Summary : 

        Command	            Python Method

        SET	                r.set(key, value)
        GET	                r.get(key)
        DEL	                r.delete(key)
        SETEX	            r.setex(key, seconds, value)
        SETNX	            r.setnx(key, value)
        MSET	            r.mset({key: value, ...})
        MGET	            r.mget(key1, key2, ...)
        INCR	            r.incr(key)
        INCRBY	            r.incrby(key, amount)
        DECR	            r.decr(key)
        DECRBY	            r.decrby(key, amount)
        APPEND	            r.append(key, value)
        GETSET	            r.getset(key, value)
        STRLEN	            r.strlen(key)


    ##  Lists ##
    Like an array.
    You can push/pull from left/right.
    Useful for Queues, Stacks.
    Redis Lists are ordered collections of strings.
    You can use them like:
    Queues (FIFO → First In First Out)
    Stacks (LIFO → Last In First Out)

    Commands: 

        Command	                    Description	                                    Example
        LPUSH	                    Insert value(s) at the head (left)	            LPUSH mylist "world"
        RPUSH	                    Insert value(s) at the tail (right)	            RPUSH mylist "hello"
        LPOP	                    Remove and get element from the head	        LPOP mylist
        RPOP	                    Remove and get element from the tail	        RPOP mylist
        LRANGE	                    Get elements by range (start to end)	        LRANGE mylist 0 -1
        LLEN	                    Get the length of list	                        LLEN mylist
        LINDEX	                    Get element by index	                        LINDEX mylist 0
        LSET	                    Set value at a specific index	                LSET mylist 0 "updated"
        LREM	                    Remove elements equal to value	                LREM mylist count value
        LTRIM	                    Trim list to specified range	                LTRIM mylist 0 2
        BLPOP	                    Blocking LPOP from multiple lists	            BLPOP mylist 0
        BRPOP	                    Blocking RPOP from multiple lists	            BRPOP mylist 0
        RPOPLPUSH	                Pop from right and push to another list's left	RPOPLPUSH list1 list2
        BRPOPLPUSH	                Blocking RPOPLPUSH	                            BRPOPLPUSH list1 list2 0
        LPOS	                    Find the position of a value	                LPOS mylist "hello"

    Redis in Python:
        pip install redis

        import redis

        # Connect to local Redis server
        r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

        # Key we'll work on
        list_key = "mylist"

        r.lpush(list_key, "world")      # LPUSH (Insert at left/head)
        r.lpush(list_key, "hello")

        r.rpush(list_key, "redis")      # RPUSH (Insert at right/tail)

        element = r.lpop(list_key)      # LPOP (Remove from left/head)
        print("Popped:", element)

        element = r.rpop(list_key)      # RPOP (Remove from right/tail)
        print("Popped:", element)

        elements = r.lrange(list_key, 0, -1)    # LRANGE (Get list items)
        print(elements)

        length = r.llen(list_key)       # LLEN (Get length of list)
        print("Length:", length)

        element = r.lindex(list_key, 0)     # LINDEX (Get item at index)
        print("First element:", element)

        r.lset(list_key, 0, "new_value")    # LSET (Set value at index)

        r.lrem(list_key, 2, "world")  # Remove up to 2 occurrences  # LREM (Remove elements by value)

        r.ltrim(list_key, 0, 1)     # LTRIM (Trim list to range)

        element = r.blpop([list_key], timeout=5)    # BLPOP (Blocking LPOP)
        print("Blocking pop left:", element)

        element = r.brpop([list_key], timeout=5)     # BRPOP (Blocking RPOP)
        print("Blocking pop right:", element)

        r.rpoplpush("list1", "list2")       # RPOPLPUSH (Move last of list1 to start of list2)

        r.brpoplpush("list1", "list2", timeout=5)       # BRPOPLPUSH (Blocking move between lists)

        pos = r.lpos(list_key, "new_value")     # LPOS (Find position of a value)
        print("Position:", pos)

        ✅ Practical Example Scenario
            Queue system where you:
            - Add tasks (LPUSH)
            - Workers pop tasks (RPOP)
            - If no tasks → workers wait (BRPOP)

        🚀 Uses of Lists in Real World
            Use Case	                            Explanation
            Task Queues	                            LPUSH tasks, workers RPOP
            Chat Messages	                        Store latest chat messages
            Notifications	                        Stack of recent alerts
            Order Queue	                            E-commerce order management
            Logs	                                Temporarily store logs in queue
            Workflow Pipelines	                    Steps processed in order

        📋 Summary Table
            Command	            Main Use
            LPUSH	            Insert left (stack)
            RPUSH	            Insert right (queue)
            LPOP	            Remove left (FIFO)
            RPOP	            Remove right (LIFO)
            LRANGE	            View elements
            LLEN	            Length
            LINDEX	            Get item
            LSET	            Update item
            LREM	            Delete matching item(s)
            LTRIM	            Cut list to sublist
            BLPOP/BRPOP	        Wait until item exists
            RPOPLPUSH	        Move item atomically
            LPOS	            Find index of item


    ##  Sets ##

        Like a List but NO duplicates.
        Useful for tagging, unique user IDs, random selection.
        Set = Unordered collection of unique elements.

        No duplicate elements allowed.
        Very fast operations like add, remove, membership checking.
        Great for things like: tags, followers, active users, etc.
        Redis Set ≈ Python set (very similar!)

        Unique values only (automatic duplicate removal)

        No order guaranteed
        Fast insert, delete, check exists (O(1) time)
        Supports set operations like Union, Intersection, Difference

        🔥 All Redis Set Commands (FULL LIST)
            Command	                    Description
            SADD	                    Add one or more members to a set
            SMEMBERS	                Get all members in a set
            SISMEMBER	                Check if a member exists
            SREM	                    Remove one or more members
            SCARD	                    Get number of elements
            SPOP	                    Remove and return random element
            SRANDMEMBER	                Get random elements without removing
            SUNION	                    Union of multiple sets
            SINTER	                    Intersection of multiple sets
            SDIFF	                    Difference of multiple sets
            SMOVE	                    Move a member from one set to another 

        Sets in python : 
            import redis
            r = redis.Redis(host='localhost', port=6379, db=0)


            Add member(s) to a set
            r.sadd('fruits', 'apple', 'banana', 'mango')                #  SADD key member [member ...]
            r.sadd('fruits', 'banana')  # Duplicate, will be ignored
            ✅ Adds apple, banana, mango to fruits set.
            
            Get all members
            fruits = r.smembers('fruits')               #  SMEMBERS key
            print([item.decode() for item in fruits])
            # Output: ['apple', 'banana', 'mango']

            Check if an item exists
            is_present = r.sismember('fruits', 'apple')     #  SISMEMBER key member
            print(is_present)  # Output: True

            Remove one or more members
            r.srem('fruits', 'banana')      # SREM key member [member ...]
            ✅ Now banana is removed.

            Count number of members
            count = r.scard('fruits')       # SCARD key
            print(count)  # Output: 2

            Remove and return random member
            item = r.spop('fruits')             # SPOP key
            print(item.decode())  # Random item like 'apple' or 'mango'
            ✅ Useful when you want to consume elements randomly

            Get random member(s) without removing
            r.sadd('colors', 'red', 'blue', 'green')        # SRANDMEMBER key [count]
            # Get single random element             
            print(r.srandmember('colors').decode())
            # Get multiple random elements
            print([item.decode() for item in r.srandmember('colors', 2)])

            Union of sets (all unique elements)
            r.sadd('set1', 'a', 'b', 'c')           #  SUNION key [key ...]
            r.sadd('set2', 'c', 'd', 'e')
            union = r.sunion('set1', 'set2')
            print([item.decode() for item in union])
            # Output: ['a', 'b', 'c', 'd', 'e']

            Intersection (common elements)
            intersection = r.sinter('set1', 'set2')         # SINTER key [key ...]
            print([item.decode() for item in intersection])
            # Output: ['c']

            Difference (elements in first not in others)
            diff = r.sdiff('set1', 'set2')              # SDIFF key [key ...]
            print([item.decode() for item in diff])
            # Output: ['a', 'b']

            Move a member from one set to another
            r.sadd('set3', 'x', 'y', 'z')       # SMOVE source destination member
            r.sadd('set4', 'p', 'q')
            r.smove('set3', 'set4', 'x')
            ✅ Now x moves from set3 ➔ set4.

            ✅ Summary Table
            Command	            Python Method
            SADD	            r.sadd(key, member1, member2, ...)
            SMEMBERS	        r.smembers(key)
            SISMEMBER	        r.sismember(key, member)
            SREM	            r.srem(key, member)
            SCARD	            r.scard(key)
            SPOP	            r.spop(key)
            SRANDMEMBER	        r.srandmember(key, count)
            SUNION	            r.sunion(key1, key2, ...)
            SINTER	            r.sinter(key1, key2, ...)
            SDIFF	            r.sdiff(key1, key2, ...)
            SMOVE	            r.smove(source, destination, member)


    ## Sorted Sets ##
        Each value has a score.
        Always sorted automatically.
        Good for Top 10 Players, News Feed sorting.
        Sorted Sets are similar to Sets, but each element has a score.

        Elements are ordered by their score (lowest to highest by default).
        Score is a floating-point number.
        You can:
            Add elements with scores
            Update scores
            Fetch elements ordered by scores
            Do range queries (by score or rank)
        Each element is unique, but scores can repeat.

        🔥 Real-world use cases
            - Leaderboards (Top players)
            - Task queues (by priority)
            - Event scheduling
            - Recommender systems
            - Ranking articles, movies, products

        Command	                Purpose	                                                Example CLI
        ZADD	                Add one/more members with score to a sorted set.	    ZADD games 300 "Chess" 500 "Football"
        ZRANGE	                Get elements by rank (ascending).	                    ZRANGE games 0 -1 WITHSCORES
        ZREVRANGE	            Get elements by rank (descending).	                    ZREVRANGE games 0 1 WITHSCORES
        ZRANGEBYSCORE	        Get elements by score range (min to max).	            ZRANGEBYSCORE games 100 400 WITHSCORES
        ZREVRANGEBYSCORE	    Get elements by score range (max to min).	            ZREVRANGEBYSCORE games 500 100 WITHSCORES
        ZRANK	                Get rank (position) of a member (ascending).	        ZRANK games "Chess"
        ZREVRANK	            Get reverse rank (position) of a member (descending).	ZREVRANK games "Chess"
        ZSCORE	                Get the score of a member.	                            ZSCORE games "Football"
        ZINCRBY	                Increment the score of a member.	                    ZINCRBY games 100 "Chess"
        ZREM	                Remove member(s) from sorted set.	                    ZREM games "Football"
        ZCARD	                Count total members in sorted set.	                    ZCARD games
        ZCOUNT	                Count members within a score range.	                    ZCOUNT games 100 400
        ZPOPMIN	                Pop (remove+return) member with lowest score.	        ZPOPMIN games
        ZPOPMAX	                Pop (remove+return) member with highest score.	        ZPOPMAX games
        ZREMRANGEBYRANK	        Remove members by rank range.	                        ZREMRANGEBYRANK games 0 1
        ZREMRANGEBYSCORE	    Remove members by score range.	                        ZREMRANGEBYSCORE games 200 300
        ZSCAN	                Iterate elements in sorted set (useful for large sets).	ZSCAN games 0 MATCH Chess*

        📋 Notes
            WITHSCORES → if you want to fetch scores along with members.
            NX, XX, CH, INCR → Options you can apply with ZADD depending on your needs.
            start, stop → 0-indexed positions in ZRANGE/ZREVRANGE.
            min, max → Score limits for ZRANGEBYSCORE/ZREVRANGEBYSCORE.
            cursor → Used in ZSCAN to iterate without blocking server.

        | **Python Command**                                    | **Use**                                                   |
        | :---------------------------------------------------- | :-------------------------------------------------------- |
        | `r.zadd('myzset', {'member1': 1.0, 'member2': 2.0})`  | Add members with scores to a sorted set.                  |
        | `r.zrange('myzset', 0, -1, withscores=True)`          | Get members ordered by score (ascending).                 |
        | `r.zrevrange('myzset', 0, -1, withscores=True)`       | Get members ordered by score (descending).                |
        | `r.zrangebyscore('myzset', 1, 2, withscores=True)`    | Get members with scores between 1 and 2.                  |
        | `r.zrevrangebyscore('myzset', 2, 1, withscores=True)` | Get members with scores between 2 and 1, descending.      |
        | `r.zrank('myzset', 'member1')`                        | Get the rank (index) of a member (lowest score = rank 0). |
        | `r.zrevrank('myzset', 'member1')`                     | Get reverse rank (highest score = rank 0).                |
        | `r.zscore('myzset', 'member1')`                       | Get the score of a specific member.                       |
        | `r.zincrby('myzset', 1, 'member1')`                   | Increment the score of a member by 1.                     |
        | `r.zrem('myzset', 'member2')`                         | Remove a member from the sorted set.                      |
        | `r.zcard('myzset')`                                   | Get the total number of elements in the sorted set.       |
        | `r.zcount('myzset', 1, 3)`                            | Count members with scores between 1 and 3.                |
        | `r.zpopmin('myzset')`                                 | Pop and return the member with the lowest score.          |
        | `r.zpopmax('myzset')`                                 | Pop and return the member with the highest score.         |
        | `r.zremrangebyrank('myzset', 0, 1)`                   | Remove members within a specified rank range.             |
        | `r.zremrangebyscore('myzset', 1, 2)`                  | Remove members with scores between 1 and 2.               |
        | `r.zscan('myzset', cursor=0, match='member*')`        | Incrementally iterate members matching a pattern.         |


    ## Hashes ##
        Like a List but NO duplicates.
        Useful for tagging, unique user IDs, random selection.
        A Hash in Redis is a collection of key-value pairs.
        Think of it like a Python dictionary or JSON object.
        Hashes are perfect when you want to store and retrieve multiple related fields (attributes) for an object (like a User or Product).

        🔹 Example:
            A user's profile can be saved like:
                Field	Value
                name	John
                age	30
                city	New York
        🎯 Why Use Hashes?
            Efficient memory usage for related small data sets.
            Quick access to individual fields without fetching the whole object.
            Easy to update or delete a single field.
            Perfect for storing objects, caching database rows, or session data.

        📚 CLI Commands for Hashes (Quick Overview)
            Command	                Purpose
            HSET	                Set field in hash
            HGET	                Get field value
            HMSET (Deprecated)	    Set multiple fields (use HSET with multiple fields instead)
            HMGET	                Get multiple fields
            HGETALL	                Get all fields and values
            HDEL	                Delete one or more fields
            HEXISTS	                Check if a field exists
            HLEN	                Get number of fields
            HKEYS	                Get all field names
            HVALS	                Get all field values
            HINCRBY	                Increment integer field
            HINCRBYFLOAT	        Increment float field
            HSTRLEN	                Get length of field value string
            HSCAN	                Iterate fields in hash
                                                                                                                                                                                   
            r.hset('user:1', 'name', 'John')	                                Set a field (name) in a hash.
            r.hset('user:1', mapping={'age': 30, 'city': 'New York'})	        Set multiple fields in a hash.
            r.hget('user:1', 'name')	                                        Get value of a field.
            r.hmget('user:1', 'name', 'city')	                                Get multiple field values.
            r.hgetall('user:1')	                                                Get all fields and values in a hash.
            r.hdel('user:1', 'age')	                                            Delete a field from the hash.
            r.hexists('user:1', 'city')	                                        Check if field city exists.
            r.hlen('user:1')	                                                Get number of fields in hash.
            r.hkeys('user:1')	                                                Get all field names.
            r.hvals('user:1')	                                                Get all field values.
            r.hincrby('user:1', 'logins', 1)	                                Increment a field by an integer (for counters).
            r.hincrbyfloat('user:1', 'balance', 12.50)	                        Increment a field by a float.
            r.hstrlen('user:1', 'name')	                                        Get the string length of a field's value.
            r.hscan('user:1', cursor=0, match='*')	                            Iterate over fields matching pattern.

        🏆 Important Tips
            hset is smart: if field exists → overwrites value.
            Redis keys are binary safe: you can store any strings (even emojis).
            Always check output types — Redis returns bytes, you may want to .decode('utf-8') in Python.
            hscan is useful for large hashes (use it for pagination).

    ## Streams ##
        Message Queue system built-in.
        You can create producers and consumers natively in Redis.
        Redis Streams are a log data structure.
        They are append-only — new records are always added at the end.
        Very similar to Kafka topics or logs.
        Useful for real-time messaging, event sourcing, job queues, analytics, etc.
        You can add, read, consume, and group messages efficiently.
        Each entry has:
            ID (timestamp + sequence number)
            Field-Value pairs (like a mini dictionary)
            example: 
            ID: 1687456789012-0
            Field1: "order_id"  Value1: "1234"
            Field2: "status"    Value2: "pending"

        🎯 Why Use Streams?
            Real-time data ingestion (chat messages, payments, logs, etc.).
            Reliable and persistent message queues.
            Consumer groups allow horizontal scaling.
            In-order message delivery (preserved sequence).

        📚 Full List of Redis Stream CLI Commands
            Command	                    Purpose
            XADD	                    Add new entries to a stream
            XRANGE	                    Read entries between IDs
            XREVRANGE	                Read entries in reverse order
            XREAD	                    Read new data as it arrives
            XREADGROUP	                Read using Consumer Groups
            XGROUP CREATE	            Create a consumer group
            XGROUP DESTROY	            Delete a consumer group
            XGROUP DELCONSUMER	        Delete a consumer from a group
            XGROUP SETID	            Change last delivered ID
            XACK	                    Acknowledge messages
            XDEL	                    Delete entries
            XTRIM	                    Trim (delete) old stream entries
            XPENDING	                List pending messages for consumers
            XINFO STREAM	            Show information about a stream
            XINFO GROUPS	            Info about groups
            XINFO CONSUMERS	            Info about consumers in a group

        ✍️ Basic Commands
            Purpose	                Python Code
            Add an entry	        r.xadd('mystream', {'name': 'John', 'action': 'login'})
            Read entries	        r.xrange('mystream', min='-', max='+')
            Read entries reverse	r.xrevrange('mystream', max='+', min='-')
            Read new entries	    r.xread({'mystream': '0-0'}, count=10, block=0)
            Delete an entry	        r.xdel('mystream', '1687456789012-0')
            Trim a stream	        r.xtrim('mystream', maxlen=1000)
            Create a group	        r.xgroup_create('mystream', 'mygroup', id='0-0', mkstream=True)
            Read from group	        r.xreadgroup('mygroup', 'consumer-1', {'mystream': '>'}, count=1)
            Acknowledge message	    r.xack('mystream', 'mygroup', '1687456789012-0')
            Delete group	        r.xgroup_destroy('mystream', 'mygroup')
            Remove a consumer	    r.xgroup_delconsumer('mystream', 'mygroup', 'consumer-1')
            See pending messages	r.xpending('mystream', 'mygroup')

        🔥 Full Example: Add, Read, and Acknowledge

            # Add some entries
            r.xadd('orders', {'order_id': '001', 'status': 'created'})
            r.xadd('orders', {'order_id': '002', 'status': 'pending'})

            # Create a consumer group
            try:
                r.xgroup_create('orders', 'order_group', id='0-0', mkstream=True)
            except redis.exceptions.ResponseError:
                print("Group already exists!")

            # Consumer reading messages
            messages = r.xreadgroup('order_group', 'consumer1', {'orders': '>'}, count=10)

            for stream, msgs in messages:
                for msg_id, fields in msgs:
                    print(f"Message ID: {msg_id}")
                    print(f"Fields: {fields}")

                    # Acknowledge the message
                    r.xack('orders', 'order_group', msg_id)

        ⚡ Advanced Features in Streams
            Blocking Reads (block=0 in xread) — wait until new data arrives!
            Auto-Claim Messages (XAUTOCLAIM) — reassign stuck pending messages.
            Stream Trimming (XTRIM) — keep your streams memory efficient.
            Consumer scaling — multiple consumers inside a group read independently.

        🏆 Streams Best Practices
            Use consumer groups for scalable workers.
            Always acknowledge messages you processed (using XACK).
            For high volume streams, trim old entries to save memory.
            If order matters, process sequentially.

    ## Bitmaps ##
        Set/get bits at certain positions.
        Used for fast analytics (e.g., track if users were active each day).
        A bitmap in Redis is a way to store binary (0 or 1) information compactly inside a string.
        Internally, Redis uses a String data type (not a new type) and treats it bit-by-bit.
        You can think of a bitmap as a very memory-efficient array of flags (true/false, yes/no, etc.).
        Each bit represents a small piece of information.
        You set, get, or count bits at specific offsets.

        📚 When are Bitmaps used?
            ✅ Track if a user was online today
            ✅ Track daily active users (1 billion users tracking in 100 MB memory!)
            ✅ Feature flags (is feature enabled?)
            ✅ Simple voting systems
            ✅ Presence checks (like login/logout)
            ✅ Counting and analytics
            ✅ Tracking visited/unvisited pages/items

        🎯 Important Properties
            Zero memory overhead: 1 bit = 1/8 byte
            Super fast (bit-level operations are extremely fast)
            Atomic operations (no race conditions)

        📚 Main Redis CLI Commands for Bitmaps
            Command	Purpose
            SETBIT key offset value	Set the bit at an offset (0 or 1)
            GETBIT key offset	Get the bit value at an offset
            BITCOUNT key [start end]	Count number of set bits (1s)
            BITOP operation destkey key1 [key2 ...]	Perform bitwise operations (AND, OR, XOR, NOT)
            BITPOS key bit [start end]	Find first bit of value (0 or 1)

            Operation	                Purpose	Python Implementation
            SETBIT	                    Set the value of a bit at a given offset	r.setbit('key', offset, value)
            GETBIT	                    Get the bit value at a given offset	r.getbit('key', offset)
            BITCOUNT	                Count the number of bits set to 1	r.bitcount('key', start=optional, end=optional)
            BITOP (AND, OR, XOR, NOT)	Perform bitwise operation between keys	r.bitop('operation', 'destkey', 'key1', 'key2', ...)
            BITPOS	                    Find the position of the first 0 or 1 bit	r.bitpos('key', bit, start=optional, end=optional)


            📢 Key Notes:
            setbit(key, offset, value) → value = 0 or 1
            getbit(key, offset) → returns 0 or 1
            bitcount(key) → counts how many bits are set to 1
            bitop('operation', destination, source1, source2, ...) → combines bitmaps
            bitpos(key, bit) → finds first bit of 0 or 1


    ## Hyperlog ##
        Super memory-efficient counting (e.g., millions of users with ~12 KB memory).
        HyperLogLog is a probabilistic data structure in Redis, used to count unique elements (like users, IP addresses, events) approximately — using very little memory (~12 KB only) even for millions of records!

        ✅ Approximate counting (with ~0.81% error rate)
        ✅ Extremely memory efficient
        ✅ Useful when exact counts are not necessary (e.g., analytics)

        ⚡ Real-World Use Cases
            Use Case	                Example
            Unique website visitors	    Track unique IPs daily
            Unique app downloads	    Count how many different devices installed your app
            Unique searches	            Count distinct search queries without storing all data
            Unique event participation	Count number of unique users in a campaign


        🧠 Key HyperLogLog Commands (CLI)
            Command	Purpose
            PFADD key element [element ...]	Adds elements to the HyperLogLog
            PFCOUNT key [key ...]	Returns the approximate number of unique elements
            PFMERGE destkey sourcekey [sourcekey ...]	Merges multiple HyperLogLogs into one

        Command	            Python Implementation	                            Usage Example
        PFADD	            r.pfadd('key', 'element1', 'element2')	            r.pfadd('visitors', 'user1', 'user2')
        PFCOUNT	            r.pfcount('key')	                                count = r.pfcount('visitors')
        PFMERGE	            r.pfmerge('destination', 'source1', 'source2')	    r.pfmerge('all_visitors', 'visitors1', 'visitors2')

        🎯 Full Working Python Example

            import redis

            r = redis.Redis(host='localhost', port=6379, db=0)

            # Add elements to a HyperLogLog
            r.pfadd('unique_visitors', 'user1', 'user2', 'user3')

            # Add more elements
            r.pfadd('unique_visitors', 'user4', 'user5', 'user1')  # user1 duplicate won't affect much

            # Count unique elements approximately
            count = r.pfcount('unique_visitors')
            print(f"Approximate Unique Visitors: {count}")  # Output: around 4-5

            # Merge two HyperLogLogs
            r.pfadd('day1_visitors', 'user1', 'user2')
            r.pfadd('day2_visitors', 'user2', 'user3')

            r.pfmerge('total_visitors', 'day1_visitors', 'day2_visitors')

            total_count = r.pfcount('total_visitors')
            print(f"Total Approximate Visitors after merge: {total_count}")
        🧩 Important Things to Remember
            Topic	                Details
            Accuracy	            ~0.81% error
            Memory Used	            ~12 KB per HyperLogLog, no matter how many elements you add
            Duplicate elements	    Are automatically ignored
            Merge	                You can combine multiple HyperLogLogs into one
            Not for exact counts	If you need exact counting, use Sets, but they use more memory

        🚀 Quick Use Case: Track Daily Unique Users
            def track_user(user_id):
                r.pfadd('daily:users', user_id)

            def get_daily_unique_user_count():
                return r.pfcount('daily:users')

            # Example
            track_user('user_123')
            track_user('user_456')

            print("Today's unique users:", get_daily_unique_user_count())

        📋 HyperLogLog vs Set Comparison
            | | HyperLogLog | Set |
            |:---|:---|
            | Accuracy | Approximate | Exact |
            | Memory Usage | Fixed (~12 KB) | Grows with number of elements |
            | Speed | Very fast | Slower with very large sets |
            | Best Use | Unique counts where precision isn't critical | Exact unique data tracking |


    ## Geospatical Indexes ##
        Redis can calculate distances, find locations within radius.
        Redis Geospatial features allow you to store, query, and analyze locations (longitude, latitude, and member name) — efficiently.

        ✅ Save locations (longitude, latitude, name)
        ✅ Find distance between locations
        ✅ Query nearby locations (radius queries)
        ✅ Sort results by distance

        👉 Useful when building: maps, delivery apps, location-based search, ride-sharing apps (like Uber), etc.
        ⚡ Real-World Use Cases
            Use Case	            Example
            Food Delivery	        Find nearby restaurants for a user
            Ride-Sharing	        Match users with closest drivers
            Retail	                Find nearest stores to a customer
            Travel Apps	            Show hotels near tourist locations

        🛠️ Core Geospatial Commands (Redis CLI)
            Command	                                        Purpose
            GEOADD	                                        Add longitude, latitude, and member to a key
            GEOPOS	                                        Get the position (lon, lat) of member(s)
            GEODIST	                                        Get the distance between two members
            GEORADIUS (deprecated, use GEOSEARCH)	        Find members within radius (center point)
            GEORADIUSBYMEMBER (deprecated, use GEOSEARCH)	Same as above but center is a member
            GEOSEARCH	                                    Search within a radius or box
            GEOSEARCHSTORE	                                Search and store results into a new key
            GEOHASH	                                        Get GeoHash string representation of locations

        🧠 Updated Best Practice (Redis 6.2+)
            Use GEOSEARCH and GEOSEARCHSTORE instead of deprecated GEORADIUS, GEORADIUSBYMEMBER.

        Operation	                        Python Code                     	                        Example
        Add a location	                    r.geoadd('places', (longitude, latitude, 'member_name'))	r.geoadd('restaurants', (77.5946, 12.9716, 'PizzaHut'))
        Get position	                    r.geopos('places', 'member_name')	                        r.geopos('restaurants', 'PizzaHut')
        Distance between two	            r.geodist('places', 'member1', 'member2', unit='km')	    r.geodist('restaurants', 'PizzaHut', 'BurgerKing', unit='km')
        Find nearby locations	            r.geosearch('places', longitude=77.59, latitude=12.97, radius=5, unit='km')	
        Find nearby from a member	        r.geosearch('places', member='PizzaHut', radius=5, unit='km')	
        Get GeoHash	                        r.geohash('places', 'PizzaHut')

        📋 Full Working Python Example
            import redis

            r = redis.Redis(host='localhost', port=6379, db=0)

            # Adding some locations
            r.geoadd('restaurants', (77.5946, 12.9716, 'PizzaHut'))
            r.geoadd('restaurants', (77.6100, 12.9500, 'Dominos'))
            r.geoadd('restaurants', (77.6200, 12.9300, 'BurgerKing'))

            # Get position of a location
            print(r.geopos('restaurants', 'PizzaHut'))

            # Distance between two locations
            print("Distance:", r.geodist('restaurants', 'PizzaHut', 'Dominos', unit='km'), "km")

            # Find nearby restaurants within 5 km of PizzaHut
            nearby = r.geosearch('restaurants', member='PizzaHut', radius=5, unit='km')
            print("Nearby restaurants:", nearby)

            # GeoHash of PizzaHut
            print("GeoHash:", r.geohash('restaurants', 'PizzaHut'))

        🎯 Important Points
            Topic	                Details
            Units	                m, km, mi, ft (meters, kilometers, miles, feet)
            Accuracy	            High (uses ZSETs internally)
            Internal Storage	    Redis uses Sorted Sets behind the scenes
            Performance	            Very fast even with millions of geo points
            Index	                You cannot manually create secondary indexes (automatic with ZSET)

        🧪 Advanced Usage: GEOSEARCHSTORE
        Example: Store results of a nearby search into another key
            r.geosearchstore('nearby_restaurants', 'restaurants',
                member='PizzaHut', radius=5, unit='km')

            print(r.zrange('nearby_restaurants', 0, -1))  # View stored nearby places

            🔥 Full Table: Commands vs Python
                CLI Command	                            Purpose	Python                         Implementation
                GEOADD	                                Add location	                       r.geoadd('key', (longitude, latitude, member))
                GEOPOS	                                Get lat, lon	                       r.geopos('key', member)
                GEODIST	                                Distance between two	               r.geodist('key', member1, member2, unit='km')
                GEOSEARCH	                            Search nearby	                       r.geosearch('key', member='start', radius=5, unit='km')
                GEOSEARCHSTORE	                        Search and store	                   r.geosearchstore('dest', 'src', member='start', radius=5, unit='km')
                GEOHASH	                                GeoHash	                               r.geohash('key', member)
                                                                            |
    |:-------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------- |
    |`GEOADD restaurants 77.5946 12.9716 PizzaHut`                                     | `r.geoadd('restaurants', (77.5946, 12.9716, 'PizzaHut'))`                                       |
    |`GEOPOS restaurants PizzaHut`                                                     | `r.geopos('restaurants', 'PizzaHut')`                                                           |
    |`GEODIST restaurants PizzaHut Dominos km`                                         | `r.geodist('restaurants', 'PizzaHut', 'Dominos', unit='km')`                                    |
    |`GEOSEARCH restaurants FROMMEMBER PizzaHut BYRADIUS 5 km`                         | `r.geosearch('restaurants', member='PizzaHut', radius=5, unit='km')`                            |
    |`GEOSEARCHSTORE nearby_restaurants restaurants FROMMEMBER PizzaHut BYRADIUS 5 km` | `r.geosearchstore('nearby_restaurants', 'restaurants', member='PizzaHut', radius=5, unit='km')` |
    |`GEOHASH restaurants PizzaHut`                                                    | `r.geohash('restaurants', 'PizzaHut')`                                                          |
    |`GEORADIUS restaurants 77.5946 12.9716 5 km`                                      | `r.georadius('restaurants', 77.5946, 12.9716, 5, unit='km')`                                    |
    |`GEORADIUSBYMEMBER restaurants PizzaHut 5 km`                                     | `r.georadiusbymember('restaurant')`

        🎯 Important Points:
            Prefer GEOSEARCH instead of old GEORADIUS.
            Redis internally uses Sorted Sets to manage geospatial data.
            All operations are highly optimized for speed and scaling.
            Units matter (km, mi, m, ft).
        

    ## Bloom Filters ##
        A "maybe-set" with very tiny memory.
        Used for checking existence quickly but with small false positives.

        🌟 What is a Bloom Filter?
            A Bloom Filter is a space-efficient probabilistic data structure.
            It tells you if an element is:
            Definitely not present ✅
            May be present (false positives possible) ⚠️
            It never gives false negatives, but can give false positives.

        🌟 Why use Bloom Filters?
            Ultra-fast membership checking
            Memory efficient (useful for millions/billions of entries)
            Good for cache checking, fraud detection, database filtering, etc.

        🚀 Setting Up
            ✅ You must have RedisBloom Module installed!
            You can install RedisBloom using Docker easily:
            docker run -p 6379:6379 --name redis-bloom redislabs/rebloom:latest

            Command	            Purpose	                    CLI Example	                            Python Example
            BF.RESERVE	        Create bloom filter	        BF.RESERVE mybloom 0.01 1000	        r.bfCreate('mybloom', errorRate=0.01, capacity=1000)
            BF.ADD	            Add item	                BF.ADD mybloom apple	                r.bfAdd('mybloom', 'apple')
            BF.MADD	            Add multiple items	        BF.MADD mybloom banana orange mango	    r.bfMAdd('mybloom', 'banana', 'orange', 'mango')
            BF.EXISTS	        Check if item exists	    BF.EXISTS mybloom apple	                r.bfExists('mybloom', 'apple')
            BF.MEXISTS	        Check multiple items	    BF.MEXISTS mybloom apple mango grapes	r.bfMExists('mybloom', 'apple', 'mango', 'grapes')

## Pub/Sub ##
    🌟 What is Redis Pub/Sub?
        Pub/Sub = Publish/Subscribe messaging system
        Producers (Publishers) send messages
        Consumers (Subscribers) receive messages instantly when published
        Redis acts like a broker: it passes published messages to all subscribers of a channel

    🧠 Basic Concepts
        Term	            Meaning
        Publisher	        Sends messages to channels
        Subscriber	        Listens to specific channels
        Channel	            A named queue where messages are sent
        Pattern	            Wildcard-based subscription (subscribe to multiple channels)

    ⚙️ How Pub/Sub Works
        Publisher ---> [Redis Channel] ---> Subscribers
        ✅ No storage: Redis does not persist messages.
        ✅ Real-time communication: Messages are immediately delivered to active subscribers.


        | Command                       | Purpose                                | Example                         |
        | :---------------------------- | :------------------------------------- | :------------------------------ |
        | `PUBLISH <channel> <message>` | Send message to a channel              | `PUBLISH news "Breaking news!"` |
        | `SUBSCRIBE <channel>`         | Subscribe to channel                   | `SUBSCRIBE news`                |
        | `UNSUBSCRIBE <channel>`       | Unsubscribe from channel               | `UNSUBSCRIBE news`              |
        | `PSUBSCRIBE <pattern>`        | Subscribe to channels matching pattern | `PSUBSCRIBE news.*`             |
        | `PUNSUBSCRIBE <pattern>`      | Unsubscribe from pattern               | `PUNSUBSCRIBE news.*`           |
        

        🎯 CLI Example (Basic)
            Open 2 terminals:
            Terminal 1: (Subscriber)
            redis-cli
            SUBSCRIBE news

            Terminal 2: (Publisher)
            redis-cli
            PUBLISH news "Hello World!"

            Output (Terminal 1):
                1) "message"
                2) "news"
                3) "Hello World!"
            💬 The message gets delivered in real-time!

            🐍 Full Python Implementation of Pub/Sub
            1. Publisher
                import redis
                r = redis.Redis(host='localhost', port=6379, db=0)
                channel = 'news'
                message = 'Breaking news from ChatGPT!'
                r.publish(channel, message)
                print(f"Published message: {message} to channel: {channel}")

            2. Subscriber
                import redis
                r = redis.Redis(host='localhost', port=6379, db=0)
                pubsub = r.pubsub()
                pubsub.subscribe('news')
                print("Subscribed to 'news' channel...")
                for message in pubsub.listen():
                    if message['type'] == 'message':
                        print(f"Received message: {message['data'].decode()} on channel: {message['channel'].decode()}")

            🎯 Python Pattern Subscriptions (Advanced)
            Subscribe to multiple channels using wildcards.

                pubsub = r.pubsub()
                pubsub.psubscribe('news.*')

                print("Subscribed to all 'news.*' channels...")

                for message in pubsub.listen():
                    if message['type'] == 'pmessage':
                        print(f"[{message['channel'].decode()}] {message['data'].decode()}")

            🛠 Production Best Practices for Redis Pub/Sub
                ✅ Use dedicated Redis connections for Pub/Sub
                ✅ Don't use the same connection for Pub/Sub and normal commands — it can cause blocking
                ✅ Implement retries / reconnects in case of dropped connections
                ✅ No message history — if subscriber was offline, messages are lost
                ✅ Pub/Sub ≠ Durable Queues — if you want persistent messaging, use Redis Streams, Kafka, RabbitMQ instead
                ✅ Monitor subscriber health (especially for dropped TCP connections)

            ⚡ Real-World Use Cases
                Use Case	                    Description
                Chat applications	            Send real-time chat messages
                Live notifications	            Push alerts, stock updates, news
                Gaming apps	                    Multiplayer game moves, scores
                Real-time analytics	            Tracking events instantly
                Microservices communication	    Broadcast events between services

            📋 Full Summary Table
                Command	                            CLI Example	            Python Code	                    Purpose
                SUBSCRIBE <channel>	                SUBSCRIBE news	        pubsub.subscribe('news')	    Subscribe to a single channel
                PUBLISH <channel> <message>	        PUBLISH news "Hello"	r.publish('news', 'Hello')	    Publish message
                PSUBSCRIBE <pattern>	            PSUBSCRIBE news.*	    pubsub.psubscribe('news.*')	    Pattern-based subscription
                UNSUBSCRIBE <channel>	            UNSUBSCRIBE news	    pubsub.unsubscribe('news')	    Unsubscribe from channel
                PUNSUBSCRIBE <pattern>	            PUNSUBSCRIBE news.*	    pubsub.punsubscribe('news.*')   Unsubscribe from pattern

            🧠 Important Limitations
                Point	                    Description
                ❗ No persistence	       If subscriber is offline, message is lost
                ❗ No queueing	           No "pending" message queue
                ❗ Not reliable for financial transactions, guaranteed delivery required

##  Transactions  ##
    🌟 What is a Redis Transaction?
        A transaction in Redis is a way to execute a group of commands sequentially without any interruption.
        ✅ All commands are queued first
        ✅ Then executed atomically (i.e., all-or-nothing)
        Note: Redis transactions are not fully ACID-compliant like a database.
        They queue commands and then execute them together, but no rollback happens on error unless you explicitly use WATCH.

    🧠 Core Transaction Commands
        Command	                        Purpose
        MULTI	                        Start a transaction block
        EXEC	                        Execute all queued commands
        DISCARD	                        Cancel the transaction
        WATCH <key>	                    Watch a key for changes (optimistic locking)
        UNWATCH	                        Unwatch all watched keys

    🔥 How Redis Transactions Work (Steps)
        Client sends MULTI
        Client sends commands — they get queued
        Client sends EXEC
        Redis runs all commands sequentially and atomically
        ✅ Either all commands run or none (if a watched key changed)

    🚀 CLI Usage Example
        127.0.0.1:6379> MULTI
        OK
        127.0.0.1:6379> SET foo bar
        QUEUED
        127.0.0.1:6379> INCR counter
        QUEUED
        127.0.0.1:6379> EXEC
        1) OK
        2) (integer) 1

        MULTI starts the transaction

            - Commands are QUEUED
            - EXEC runs them together
        
        🚨 Important Behavior
            Syntax errors (like wrong command format) fail immediately.
            Runtime errors (like wrong data type) occur during EXEC but don't stop other commands.
            If you WATCH a key and it gets modified before EXEC, then EXEC aborts.

        🛠 Python Implementation using redis-py
        1. Basic Transaction
            import redis
            r = redis.Redis(host='localhost', port=6379, db=0)
            with r.pipeline() as pipe:
                pipe.multi()  # start transaction
                pipe.set('foo', 'bar')
                pipe.incr('counter')
                responses = pipe.execute()  # execute all
                print(responses)

            pipeline in redis-py automatically uses transactions (MULTI/EXEC).

        2. Handling Errors in Python
            try:
                with r.pipeline() as pipe:
                    pipe.multi()
                    pipe.set('foo', 'bar')
                    pipe.lpush('counter', 'value')  # Wrong type operation! (counter is int)
                    responses = pipe.execute()
            except redis.exceptions.ResponseError as e:
                print(f"Transaction error: {e}")

            ✅ You can catch ResponseError if an invalid operation happens inside the transaction.

        🔥 Optimistic Locking with WATCH
            WATCH lets you monitor keys.
            If any watched key changes before EXEC, then transaction will abort safely.

            ✅ Used for race condition protection
            ✅ Useful in concurrent environments

        CLI Example with WATCH
        Terminal 1:
            MULTI
            WATCH balance
            DECR balance
            EXEC
        If someone modifies balance between WATCH and EXEC, then EXEC will fail.

        Python Example with WATCH: 
            import redis
            r = redis.Redis(host='localhost', port=6379, db=0)
            key = 'balance'
            while True:
                try:
                    with r.pipeline() as pipe:
                        pipe.watch(key)  # watch key
                        balance = int(pipe.get(key) or 0)

                        if balance < 10:
                            print("Insufficient balance")
                            pipe.unwatch()
                            break

                        pipe.multi()
                        pipe.decr(key, amount=10)
                        pipe.execute()
                        print("Balance deducted by 10")
                        break
                except redis.exceptions.WatchError:
                    print("Balance changed by another process. Retrying...")
            💬 Note: If someone changes balance, it retries automatically.

        📋 Summary Table
            Command	                Purpose	                CLI Example	                Python Equivalent
            MULTI	                Start transaction	    MULTI	                    pipe.multi()
            EXEC	                Execute                 queued commands	EXEC	    pipe.execute()
            DISCARD	                Cancel transaction	    DISCARD	                    pipe.reset()
            WATCH <key>	            Watch key changes	    WATCH balance	            pipe.watch('balance')
            UNWATCH	                Unwatch keys	        UNWATCH	                    pipe.unwatch()

        🎯 When to Use Redis Transactions?
            Use Case	                    Why?
            Bank account operations	        Ensure balance doesn't overdraft
            Atomic updates	                Update multiple keys together safely
            Optimistic concurrency	        Prevent race conditions
            Grouped writes	                Batch multiple writes at once

        ⚡ Production Tips
            ✅ Keep transaction blocks small and fast
            ✅ WATCH carefully — avoid watching too many keys
            ✅ Always handle WatchError and retries in code
            ✅ Prefer Redis Streams if you need more powerful queuing
            ✅ Remember no rollback — only prevention using WATCH

    

#######################################################################################################


    - Transactions
    - Pipelines
    - Expiration & TTL
    - Caching Patterns (LRU, Write-through)
    - Redis Streams
    - Lua scripting
    - Redis with Celery
    - Redis for rate limiting
    - Redis Search
    - Redis Cluster & Sentinel
    - Redis JSON (ReJSON)
    - Security & performance tuning
    - RedisInsight for visualization

2. Hashes
(Like a dictionary: key → { field: value, field: value })

Command	Use	Example
HSET key field value	Set field in hash	HSET user:1 name "azam"
HGET key field	Get field value	HGET user:1 name
HMSET key field1 value1 field2 value2	Set multiple fields	HMSET user:1 name "azam" age 25
HMGET key field1 field2	Get multiple fields	HMGET user:1 name age
HGETALL key	Get all fields/values	HGETALL user:1
HDEL key field	Delete a field	HDEL user:1 name
HLEN key	Count fields in hash	HLEN user:1
HEXISTS key field	Check if field exists	HEXISTS user:1 age
HINCRBY key field number	Increment field by number	HINCRBY user:1 points 10

3. Lists
(Ordered collection like a queue or stack.)

Command	Use	Example
LPUSH key value	Push to left	LPUSH tasks "task1"
RPUSH key value	Push to right	RPUSH tasks "task2"
LPOP key	Pop from left	LPOP tasks
RPOP key	Pop from right	RPOP tasks
LRANGE key start stop	Get range of list	LRANGE tasks 0 -1
LLEN key	Length of list	LLEN tasks
LREM key count value	Remove N occurrences	LREM tasks 1 "task1"
LINDEX key index	Get element at index	LINDEX tasks 0
LSET key index value	Set element at index	LSET tasks 0 "urgent_task"

4. Sets
(Unordered collection of unique items.)

Command	Use	Example
SADD key value	Add member to set	SADD online_users "azam"
SREM key value	Remove member	SREM online_users "azam"
SMEMBERS key	Get all members	SMEMBERS online_users
SISMEMBER key value	Check membership	SISMEMBER online_users "azam"
SCARD key	Count members	SCARD online_users
SDIFF key1 key2	Difference between sets	SDIFF set1 set2
SINTER key1 key2	Intersection	SINTER set1 set2
SUNION key1 key2	Union	SUNION set1 set2
SRANDMEMBER key [count]	Random member(s)	SRANDMEMBER online_users 2

5. Sorted Sets (ZSET)
(Like sets but each element has a score → sorted by score.)

Command	Use	Example
ZADD key score member	Add to sorted set	ZADD leaderboard 100 "azam"
ZRANGE key start stop [WITHSCORES]	Range ascending	ZRANGE leaderboard 0 -1 WITHSCORES
ZREVRANGE key start stop [WITHSCORES]	Range descending	ZREVRANGE leaderboard 0 -1 WITHSCORES
ZRANK key member	Rank of member	ZRANK leaderboard "azam"
ZREVRANK key member	Reverse rank	ZREVRANK leaderboard "azam"
ZSCORE key member	Get score	ZSCORE leaderboard "azam"
ZREM key member	Remove member	ZREM leaderboard "azam"
ZINCRBY key increment member	Increment score	ZINCRBY leaderboard 10 "azam"

6. Pub/Sub
(Real-time message broadcasting.)

Command	Use	Example
PUBLISH channel message	Send message	PUBLISH notifications "new order"
SUBSCRIBE channel	Listen to channel	SUBSCRIBE notifications
UNSUBSCRIBE channel	Stop listening	UNSUBSCRIBE notifications

7. Streams
(Advanced log-like data structure for message queues.)

Command	Use	Example
XADD stream_name * field value [field value ...]	Add entry to stream	XADD mystream * sensor_id 123 temp 25
XREAD COUNT n STREAMS stream_name ID	Read from stream	XREAD COUNT 1 STREAMS mystream 0
XGROUP CREATE mystream groupname $ MKSTREAM	Create group	XGROUP CREATE mystream mygroup $ MKSTREAM
XREADGROUP GROUP groupname consumername STREAMS mystream >	Read by group	XREADGROUP GROUP mygroup consumer1 STREAMS mystream >
XACK stream_name groupname ID	Acknowledge message	XACK mystream mygroup 12345-0

8. Geo Commands
(Geospatial indexing.)

Command	Use	Example
GEOADD key longitude latitude member	Add geo item	GEOADD locations 13.361389 38.115556 "Palermo"
`GEORADIUS key longitude latitude radius m	km	ft
GEODIST key member1 member2	Distance between two members	GEODIST locations Palermo Catania km
GEOPOS key member	Get position	GEOPOS locations Palermo

9. HyperLogLog (Cardinality Estimation)
(Fast approximate count of unique items.)

Command	Use	Example
PFADD key element	Add element	PFADD visitors user1
PFCOUNT key	Approximate unique count	PFCOUNT visitors
PFMERGE destkey sourcekey1 sourcekey2	Merge HyperLogLogs	PFMERGE all_visitors visitors1 visitors2

10. Bitmaps
(Bitwise operations.)

Command	Use	Example
SETBIT key offset value	Set bit at offset	SETBIT userflags 7 1
GETBIT key offset	Get bit at offset	GETBIT userflags 7
BITCOUNT key	Count bits set to 1	BITCOUNT userflags

