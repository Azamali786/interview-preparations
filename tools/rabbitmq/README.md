# This file will contain learning resources, notes and other stack realted informations #

- RabbitMQ is a message broker: it accepts and forwards messages. You can think about it as a post office: when you put the mail that you want 
  posting in a post box, you can be sure that the letter carrier will eventually deliver the mail to your recipient.
  In this analogy, RabbitMQ is a post box, a post office, and a letter carrier.


- It accepts, stores, and forwards binary blobs of data ‒ messages.

- Producing means nothing more than sending. A program that sends messages is a producer.

- A queue is the name for the post box in RabbitMQ.
- A queue is only bound by the host's memory & disk limits, it's essentially a large message buffer.
- using the Pika Python client for implementing RabbitMQ in python

- Producer sends messages to the "hello" queue. The consumer receives messages from that queue.
- RabbitMQ speaks multiple protocols. This tutorial uses AMQP 0-9-1, which is an open, general-purpose protocol for messaging.

# Installing Pika
- python -m pip install pika --upgrade // installing pika (rabbitmq client in python)

# Sending a message to Queue (send.py)

- Our first program send.py will send a single message to the queue. The first thing we need to do is to establish a connection with RabbitMQ server.
    #!/usr/bin/env python
    import pika

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # We're connected now, to a broker on the local machine - hence the localhost. If we wanted to connect to a broker on a different machine we'd simply specify its name or IP address here.

- Next, before sending we need to make sure the recipient queue exists. If we send a message to non-existing location, RabbitMQ will just drop the message.
    channel.queue_declare(queue='hello') // will check existance of queue

- In RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
- This exchange is special ‒ it allows us to specify exactly to which queue the message should go. The queue name needs to be 
  specified in the routing_key parameter.
- use a default exchange identified by an empty string.
    channel.basic_publish(
                        exchange='',
                        routing_key='hello',
                        body='Hello World!'
                    )
    print(" [x] Sent 'Hello World!'")

- Before exiting the program we need to make sure the network buffers were flushed and our message was actually delivered to RabbitMQ. 
  We can do it by gently closing the connection.

# Receiving meassage (receiver.py)
- Our second program receive.py will receive messages from the queue and print them on the screen.
- Again, first we need to connect to RabbitMQ server.
- channel.queue_declare(queue='hello')
- Creating a queue using queue_declare is idempotent ‒ we can run the command as many times as we like, and only one will be created.
- Receiving messages from the queue is more complex. It works by subscribing a callback function to a queue. 
- Whenever we receive a message, this callback function is called by the Pika library. In our case this function will print on the screen 
  the contents of the message.
- def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

- Next, we need to tell RabbitMQ that this particular callback function should receive messages from our hello queue:
- channel.basic_consume(
    queue='hello',
    auto_ack=True,
    on_message_callback=callback
    )
- print(' [*] Waiting for messages. To exit press CTRL+C')
  channel.start_consuming()

# Listing queues
- sudo rabbitmqctl list_queues


######################   Beginer Level ##############################
- What is RabbitMQ?
    RabbitMQ is a message broker that allows different parts of a system (called producers and consumers) 
    to communicate with each other asynchronously by sending messages via queues.

- Messaging broker: queues, exchanges, producers, consumers

    1. Producer
        Sends messages to an exchange.

    2. Queue
        A buffer that stores messages before they are consumed.

    3. Consumer
        Consumes messages from the queue.

    4. Exchange
        Receives messages from producers and routes them to queues based on rules.

    5. Routing Key
        A key used to determine where a message should go.

    6. Bindings
        A link between a queue and an exchange.

    7. ACK (Acknowledgement)
        Tells RabbitMQ that a message was processed successfully.



- Use cases: decoupling, task queues, async communication

- RabbitMQ Installation

- Install via Docker (Recommended) or native OS installation
    - docker run -d --hostname rabbitmq --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management

- Access management UI (usually at http://localhost:15672)

- Core Concepts

    - Producer, Consumer

    - Queues, Exchanges (Direct, Fanout, Topic)
        1. Direct Exchange

            Routes messages to queues with exact routing key match.
            Useful when you want to send a message to a specific queue.

            Example:
            channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
            channel.queue_bind(exchange='direct_logs', queue='info_queue', routing_key='info')

        2. Fanout Exchange

            Broadcasts all messages to all queues bound to the exchange.
            Does not use routing keys.
            Useful for broadcasting events (e.g., notifications).

            Example:
            channel.exchange_declare(exchange='logs', exchange_type='fanout')
            channel.queue_bind(exchange='logs', queue='queue1')
            channel.queue_bind(exchange='logs', queue='queue2')

        3. Topic Exchange

            Routes messages to queues based on pattern matching of routing keys.
            Wildcards:
            - (* (star) = matches one word) 
            - (# (hash) = matches zero or more words)
            Useful for complex routing scenarios like logs filtering.

            Example:
            channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
            channel.queue_bind(exchange='topic_logs', queue='queue1', routing_key='*.info')
            channel.queue_bind(exchange='topic_logs', queue='queue2', routing_key='kern.*') 



# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
- pika.ConnectionParameters('localhost'): This sets up the connection parameters for RabbitMQ.
- BlockingConnection: Creates a synchronous (blocking) connection to the RabbitMQ server.
- The result is a connection object that you can use to communicate with RabbitMQ


# channel = connection.channel()
- Creates a channel on the open connection.
- Channels are virtual connections inside a connection. They're used to send and receive messages.
- You can think of it like opening a tab in a browser session (the connection is the browser, the tab is the channel).

# channel.queue_declare(queue='hello')
- Declares (creates) a queue named 'hello'
- If the queue already exists, it does nothing.
- If it doesn’t exist, RabbitMQ creates it.
- This ensures the queue is available before you try to send a message to it.

# channel.basic_publish(exchange='', routing_key='hello', body='Hello, RabbitMQ!')
- This is the line that sends (publishes) the message.
    - exchange='':
        This means you're using the default exchange.
        The default exchange routes messages directly to a queue with the same name as the routing_key
    - routing_key='hello':
        This is the name of the queue where the message should go.
        Since we’re using the default exchange, RabbitMQ uses this key to find the queue called 'hello'
    - body='Hello, RabbitMQ!':
        This is the actual message being sent.
        It must be a string or byte object (under the hood it's converted to bytes).
    - connection.close()
        Closes the connection to RabbitMQ.
        It's a good practice to cleanly shut down your connection after you're done sending messages.


- Producer Setup :
    import pika

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='', routing_key='hello', body='Hello, RabbitMQ!')
    print(" [x] Sent 'Hello, RabbitMQ!'")
    connection.close()

- Consumer Setup : 
    import pika

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

- Beginner Projects:
    - Build a simple task queue that processes jobs in the background.
    - A logging service that collects logs from multiple sources.



########################## Inter Mediate Level  ############################

- Exchange Types
    - Direct
    - Fanout
    - Topic

- Headers (less common)

- Message Durability

- Durable Queues

- Persistent Messages

- Acknowledgments & Fair Dispatch

- Manual ack, auto_ack=False

- prefetch_count for load balancing

- Dead Letter Exchanges (DLX)

- RPC (Remote Procedure Call) pattern

- Producer 
    channel.exchange_declare(exchange='logs_topic', exchange_type='topic')
    channel.basic_publish(exchange='logs_topic', routing_key='user.info', body='User info log')

- Consumer 
    channel.exchange_declare(exchange='logs_topic', exchange_type='topic')
    result = channel.queue_declare('', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='logs_topic', queue=queue_name, routing_key='user.*')

- Task Que with mannual Ack
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', on_message_callback=callback, auto_ack=False)

- Intermediate projects : 
    -Implement a multi-service log aggregator using Topic exchange.
    -Create a PDF generation microservice triggered by messages.
    -Build a notification service (email/SMS) with retry and DLX support.


######################  Advance Level ######################

- Advanced Patterns

- Work queues

- Pub/Sub

- Delayed Messaging

- Priority Queues

- Security

- Authentication & Authorization

- SSL/TLS setup

- Clustering & High Availability

- RabbitMQ clustering

- Mirrored queues

- Shovel & Federation plugins

- Monitoring & Management

- RabbitMQ Management Plugin

- Metrics, Alerts, and Prometheus/Grafana integration

- Scaling RabbitMQ

- Performance tuning

- Load balancing

- RabbitMQ in Kubernetes (optional advanced deployment)

- Integrating with Async Libraries

- aio-pika (async Python RabbitMQ client)

- kombu (used by Celery)

- Advance Projects 
    - A complete event-driven microservices architecture

    - A real-time chat app backend using RabbitMQ Pub/Sub

    - Rate limiter or delayed retry mechanism

    - A dashboard showing live system metrics via RabbitMQ




######################### Begginer Projects ###############################

🟢 1. Simple Email Queue System
Use Case: Send email confirmations asynchronously after user registration.

user-service: Accepts registration

email-service: Listens to user.registered and sends an email

✅ Skills: Basic producer-consumer flow, JSON messages, FastAPI + Pika

🟢 2. Contact Form Handler
Use Case: Submit a contact form, then process it via a background service.

frontend: Posts form data

form-service: Pushes message to queue

processor-service: Consumes and stores in DB or sends email

✅ Skills: Message schema, async form processing, FastAPI endpoint handling

🟢 3. Logging Microservice
Use Case: Centralized logging for different services.

app1, app2: Emit log messages

log-service: Writes logs to a file or DB

✅ Skills: Fanout exchange, log level filtering, RabbitMQ basics

🟢 4. ToDo List Notification System
Use Case: Notify user via email/SMS when a task is due soon.

todo-service: Adds task with deadline

reminder-service: Checks deadlines and sends reminders

✅ Skills: Delayed tasks, time-based logic, notification systems

🟢 5. Basic Chat Message Logger
Use Case: Save every chat message for future analysis.

chat-service: Sends message

logger-service: Stores message logs

✅ Skills: String messages, persistent queues

🟢 6. Simple Blog Post Publisher
Use Case: Admin creates post → subscribers get notified

admin-service: Posts blog

notifier-service: Listens and emails subscribers

✅ Skills: Pub-sub pattern, topic exchange (optional)

🟢 7. Image Upload Tracker
Use Case: User uploads image → log the upload → notify moderator

upload-service: Accepts image

moderation-service: Logs and flags if needed

✅ Skills: Lightweight media workflows

🟢 8. URL Shortener Tracker
Use Case: Create short links and log access counts via MQ.

shortener-service: Creates + resolves links

tracker-service: Logs each access

✅ Skills: FastAPI routing, RabbitMQ logging use

🟢 9. Currency Converter Queue
Use Case: User submits conversion request → result processed and returned

client-service: Sends conversion job

converter-service: Consumes, fetches rate from API, returns result

✅ Skills: External API integration, RabbitMQ RPC-style flow

🟢 10. Simple Notification Broadcaster
Use Case: Push a message → multiple services listen and act (email, SMS, logs)

event-source-service: Sends notifications

email-service, sms-service, log-service: Listen and react

✅ Skills: Fanout exchange, parallel consumers



########################### Intermediate Projects ###############################

1. User Registration with Email & SMS Notifications
Services:

user-service: Handles user registration

email-service: Sends confirmation email

sms-service: Sends OTP via SMS

Use RabbitMQ to send events like user.created

✅ Concepts: Fanout exchange, JSON payloads, multi-consumer setup.

2. Order & Inventory Management System
Services:

order-service: Places orders

inventory-service: Decrements stock

RabbitMQ connects the two, and inventory service listens to order.created

✅ Concepts: Direct exchange, retry logic, inventory sync.

3. PDF Invoice Generator
Services:

billing-service: Calculates bill and emits event

pdf-service: Listens and generates PDF invoice (using pdfkit, etc.)

Sends invoice via email or stores it to S3 (optional)

✅ Concepts: Message persistence, error handling in consumers.

4. File Upload + Virus Scanner
Services:

upload-service: Receives files

scanner-service: Asynchronously scans files

Scan results returned using callback queues or update DB

✅ Concepts: RPC-style messaging, large file path handling.

5. Real-Time Stock Price Tracker
Services:

price-fetcher: Periodically fetches stock data from API

price-analyzer: Analyzes & stores trends

Events like stock.price.updated are sent via RabbitMQ

✅ Concepts: Scheduling (with Celery), pub-sub style messaging.

6. Image Processing Pipeline
Services:

upload-service: Accepts images

resize-service, filter-service: Apply transformations

Use topic exchange for selective processing (e.g., image.resize, image.filter.blur)

✅ Concepts: Topic exchange, multi-queue routing.

7. IoT Device Monitor
Services:

device-service: Simulates data from sensors (temp, humidity)

monitor-service: Validates threshold violations and alerts

Optionally connect with a dashboard via WebSocket

✅ Concepts: JSON messages, alert triggers, async consumers.

8. E-commerce Cart & Checkout System
Services:

cart-service: Manages cart items

payment-service: Handles payment

order-service: Finalizes order post-payment

Use RabbitMQ to coordinate between these microservices

✅ Concepts: Chained messaging, transactional flows, queue timeouts.

9. Audit Logging System
Every service (auth, billing, profile, etc.) sends events to a common log-service

log-service writes structured logs to a database (or even Elasticsearch)

✅ Concepts: Central logging, fanout exchange, message durability.

10. Ride Booking App (Uber Clone Lite)
Services:

rider-service: Books rides

driver-service: Accepts ride offers

matchmaking-service: Pairs riders and drivers

RabbitMQ events like ride.requested, ride.accepted, ride.started

✅ Concepts: Complex message flows, state transitions via messages.



################## Advance level Projects ################################

🔥 1. Distributed Task Processing System (Like Celery Alternative)
Build your own custom task queue using RabbitMQ and FastAPI.

task-scheduler: Accepts tasks and queues them.

worker-nodes: Multiple services pull and execute tasks from queues.

monitor-service: Shows task progress & status.

✅ Concepts: Load balancing, consumer groups, task tracking, retries, dead-letter queues.

🔥 2. Real-Time Fraud Detection System (Banking)
Microservices process transactions, detect anomalies, and alert fraud team.

transaction-service: Sends transaction data

fraud-service: Analyzes in real-time

alert-service: Triggers Slack/email/phone alerts

✅ Concepts: Stream processing, TTL queues, rule engine, anomaly detection patterns.

🔥 3. Live Video Streaming with Event Logs
video-ingest-service: Handles video stream metadata

log-service: Logs events like pause/play/stop via RabbitMQ

analytics-service: Generates real-time usage stats

✅ Concepts: High throughput queues, backpressure handling, event logs.

🔥 4. Booking Platform with Eventual Consistency (Flight/Hotel/Train)
booking-service: Accepts booking requests

flight-service, hotel-service, train-service: Reserve resources

coordinator-service: Manages saga-like flow (with compensation)

✅ Concepts: Sagas pattern, distributed transactions, outbox pattern, rollback via events.

🔥 5. Search Engine Indexer (Like Google/Bing)
web-crawler: Fetches web content

indexer-service: Tokenizes & indexes it

search-api: Lets users search indexed data

✅ Concepts: Queue batching, parallel processing, inverted index.

🔥 6. Social Network Feed System (Like Facebook Timeline)
post-service: Handles new posts

feed-builder: Pushes post IDs to follower timelines using RabbitMQ

notification-service: Sends push notifications

✅ Concepts: Fan-out, sharding queues, data duplication via messaging.

🔥 7. Advanced Chat System with Read Receipts
chat-service: Handles messages

read-receipt-service: Tracks reads/deliveries

notification-service: Pushes events to clients

✅ Concepts: Event ordering, queue persistence, pub/sub to multiple services.

🔥 8. Multi-Stage Data Pipeline for Machine Learning
data-ingest: Accepts data from users/APIs

data-cleaner: Validates and formats

feature-engineer: Transforms into ML features

model-service: Trains or predicts

✅ Concepts: Chained messaging, multiple queues, delay queues.

🔥 9. Stock Trading System (Robinhood-like)
order-entry-service: Accepts buy/sell orders

match-engine-service: Matches orders in real-time

portfolio-service: Updates user portfolio

notification-service: Notifies price/confirmation

✅ Concepts: High frequency queues, prioritization, transactional updates.

🔥 10. Distributed Web Scraping System
url-fetcher: Accepts URL jobs

scraper-nodes: Multiple nodes scrape data

data-aggregator: Consolidates & cleans data

monitor-service: Tracks scraping progress/errors

✅ Concepts: Dynamic scaling of consumers, task dispatching strategies.


🛠 Common Advanced Concepts in These Projects:

Concept	Description
Message TTL	Expire messages after a period
Dead Letter Queue (DLQ)	Capture failed messages for retry/debug
Sagas Pattern	Long-running transactions with rollback steps
Retry/Backoff Strategy	Automatically retry failed jobs with exponential backoff
RPC via RabbitMQ	Bi-directional service communication with correlation IDs
Queue Sharding	Distribute load using multiple queues and consumers
Rate Limiting via MQ	Throttle consumers based on token bucket or leaky bucket algorithm



#################################   Projects aiming SDE2 backend roles  ###########################

Here's a curated list of 50 real-world backend projects combining Redis, Celery, Docker, Kubernetes, RabbitMQ, and more, aimed at preparing you for an SDE2 backend developer role. These projects are categorized by themes to cover breadth and depth.

🟩 Distributed Systems & Microservices

Distributed Task Queue using Celery + Redis

Notification System (Email, SMS) using RabbitMQ + Celery

API Gateway + Microservices with FastAPI + RabbitMQ

URL Shortener Microservices with Docker Compose

Sagas-based E-commerce Checkout System

Inventory System using Event Sourcing (Kafka/RabbitMQ)

Job Scheduler Microservice (like cron-as-a-service)

Payment Processor with Retry Queues (Celery, DLQ)

Real-Time Chat App with WebSocket + Redis PubSub

Workflow Orchestrator with Celery Chains & Chords

🟦 Data Pipelines & ETL

ETL Pipeline with Celery + PostgreSQL + Redis

Real-time Log Aggregator with Redis Streams

Image Processing Pipeline using RabbitMQ

Scraper + Cleaner + Saver (3-stage RabbitMQ pipeline)

Audio Transcription Pipeline (Queue + Worker)

Real-time Analytics Ingestor with Redis TimeSeries

Database Migration Manager using Celery

Data Validation Microservice

Alert System for Sensor Data (IoT-style)

Log-based Metrics Generator using Fluentbit + Redis

🟨 DevOps + Infra Projects

Dockerized Microservice Architecture

Kubernetes Helm Chart for Microservice Deployment

Zero-Downtime Deployment with Kubernetes + Rolling Updates

Auto-scaling Microservices with HPA + Redis Metrics

Centralized Logging with ELK + RabbitMQ

Config Service using Consul + Redis

Rate Limiter Service with Redis

Service Discovery in Kubernetes using DNS

Distributed Locking System with Redis

Secrets Manager with Docker Swarm Secrets

🟥 Performance & Optimization

CDN Cache Layer using Redis

Query Result Cache with Redis

Leaderboard System using Redis Sorted Sets

Product Recommendation Engine (Background Processing)

Caching Proxy with Redis + FastAPI

Auto-expiring Sessions using Redis TTL

Image Thumbnailing via Celery + RabbitMQ

Auto Index Builder (for full-text search)

File Compression as a background job

Predictive Preload System with Queueing

🟪 Security & Auth Systems

Two-Factor Auth System using Redis + Celery

Brute-force Prevention with Redis Counters

Background Identity Verification System

Secure File Upload Pipeline

Audit Trail Service with Queue

🟫 Real-time + Streaming Projects

Real-time Sports Score Feed using Redis Streams

Real-time Crypto Price Notifier using WebSocket + Redis

Live Polling Platform using Redis PubSub

Distributed Timer Service (like setTimeout across nodes)

Activity Feed Aggregator



