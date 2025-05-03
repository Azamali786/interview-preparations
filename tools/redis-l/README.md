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

 


