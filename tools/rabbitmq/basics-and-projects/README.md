############

This folder contains one Producer file send.py which produces messages with que_name (sms, email, pad)
Here are three consumers for sms, email and pdf queues

turn on rabbitmq server using docker (recommended)
    - docker run -d --hostname rabbitmq --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management

first start all three consumers and then stasrt sending messages using producer file (send.py)
