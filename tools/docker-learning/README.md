# This file will contain learning resources, notes and other stack realted informations #


"""

attach      Attach local standard input, output, and error streams to a running container
commit      Create a new image from a container's changes
cp          Copy files/folders between a container and the local filesystem
create      Create a new container
diff        Inspect changes to files or directories on a container's filesystem
exec        Execute a command in a running container
export      Export a container's filesystem as a tar archive
inspect     Display detailed information on one or more containers
kill        Kill one or more running containers
logs        Fetch the logs of a container
ls          List containers
pause       Pause all processes within one or more containers
port        List port mappings or a specific mapping for the container
prune       Remove all stopped containers
rename      Rename a container
restart     Restart one or more containers
rm          Remove one or more containers 
run         Create and run a new container from an image
start       Start one or more stopped containers
stats       Display a live stream of container(s) resource usage statistics
stop        Stop one or more running containers
top         Display the running processes of a container
unpause     Unpause all processes within one or more containers
update      Update configuration of one or more containers
wait        Block until one or more containers stop, then print their exit codes"


# docker commands list with exampls
docker ps      # list all running containers
docker ps -a    # list all containers (running and exited)
docker ps -a -q # list all containers (running and exited) ids
docker ps --filter "status=running"     # list only running containers
docker ps --filter "status=exited"      # list only exited containers
docker ps --filter "status=exited" --filter "status=running"    # list only running and exited containers
docker ps --filter "status=exited" --filter "status=running" -a -q      # list only running and exited containers ids


docker images     # list all images
docker images -q  # list all images ids
docker images --filter "dangling=true" # list only dangling images
docker images --filter "dangling=false" # list only non-dangling images

docker pull

docker pull node    # docker pull image-name : here image name is name of image on docker registry

docker run node     # pull docker image from the registry and run it on local 

docker pull node
docker run node  # run docker image on local machine

docker run -it node    # run docker image on local machine in interactive mode

docker run -it node bash    # run docker image on local machine in interactive mode in bash shell   

docker run -it node /bin/bash    # run docker image on local machine in interactive mode in bash shell

docker run -it node /bin/bash -c "ls -la"    # run docker image on local machine in interactive mode in bash shell

docker ps -a # list all containers (running and exited) : here ps: process -a: all processes -q: quiet mode : here quiet mode means no output 

docker ps -a -q # list all containers (running and exited) ids 

docker ps -a -q | xargs docker rm # remove all containers (running and exited) 

docker ps -a -q | xargs docker rm -f # remove all containers (running and exited) -f: force mode : here force mode means no prompt 


docker run -it node # run docker image on local machine in interactive mode in bash shell, use ctrl + c twice to exit interactive mode


## Creating a docker file
# install the docker extension in vscode
# create DockerFile  



"""

"""
docker commands

docker --version
docker version
docker info
docker images   # list all images
docker images --filter "dangling=true"  # list only dangling images
docker images --filter "dangling=false"  # list only non-dangling images
docker pull
docker pull node
docker run node
docker run -it node
docker run -it node bash
docker run -it node /bin/bash
docker run -it node /bin/bash -c "ls -la"
docker ps    # list all running containers  
docker ps -a     # list all containers (running and exited)
docker ps -a -q
docker ps -a -q | xargs docker rm
docker ps -a -q | xargs docker rm -f

docker-compose commands

docker-compose --version
docker-compose version
docker-compose up
docker-compose up -d
docker-compose ps
docker-compose exec
docker-compose logs
docker-compose stop
docker-compose start
docker-compose restart
docker-compose rm"


# docker instructions

docker build .  # build an image from a Dockerfile in the current directory
docker run <image>  # run a container from an image
docker stop <container>  # stop a running container
docker start <container>  # start a stopped container
docker restart <container>  # restart a container
docker rm <container>  # remove a container
docker rmi <image>  # remove an image
docker logs <container>  # fetch logs of a container
docker exec -it <container> <command>  # execute a command inside a running container
docker inspect <object>  # display detailed information on one or more objects
docker network ls  # list all networks
docker volume ls  # list all volumes
docker stats  # display a live stream of container(s) resource usage statistics

# docker-compose instructions

docker-compose build  # build or rebuild services
docker-compose up  # create and start containers
docker-compose up -d  # start containers in detached mode
docker-compose down  # stop and remove containers, networks, images, and volumes
docker-compose stop  # stop running containers without removing them
docker-compose start  # start existing containers
docker-compose restart  # restart running containers
docker-compose exec <service> <command>  # execute a command in a running service container
docker-compose logs  # view output from containers
docker-compose ps  # list containers
docker-compose pull  # pull service images
docker-compose config  # validate and view the Compose file
docker-compose scale <service>=<num>  # set number of containers to run for a service

# DockerFile instructions

# FROM - use an existing image as a base
# COPY - copy files/directories into the build context
# RUN - execute a command in the shell, executed when image is being created
# CMD - set a default command and/or parameters, it runs when container is started not when image is bieng created.
# EXPOSE - expose a port
# ENV - set an environment variable
# ARG - set a build-time variable
# ENTRYPOINT - set the default entrypoint application
# VOLUME - mount a host directory as a volume
# USER - set the user name (or UID) and optionally the user group (or GID)
# WORKDIR - set the working directory
# ONBUILD - add a trigger instruction when the image is used as a base for another build

# docker-compose.yml file instructions

# version - specify the format of the file
# services - define services
#   - name - specify the name of the service
#   - image - specify the image to use
#   - build - specify the path to the build directory
#   - context - specify the path to the build context
#   - dockerfile - specify the path to the Dockerfile
#   - command - override the default command
#   - ports - publish ports
#   - environment - set environment variables
#   - volumes - mount host directories as volumes

"""



############# Master Docker Now  ######################

1️⃣ Fundamentals (Understand Basics First)
    - Topic	What You’ll Learn
    - What is Docker?	Why Docker exists, virtualization vs containerization
    - Docker Architecture	Daemon, Client, Images, Containers, Registries
    - Docker Installation	Install Docker on Ubuntu 20.04, Mac, Windows
    - Hello World with Docker	Run your first container (docker run hello-world)
    - Images vs Containers	Difference, concept, practical examples
    - Basic Docker Commands	docker run, ps, stop, start, restart, rm, rmi, exec

2️⃣ Working with Images and Containers
    - Topic	What You’ll Learn
    - Docker Hub	Pull images from Docker Hub (docker pull, push)
    - Build Custom Images	Create your own images using Dockerfile
    - Dockerfile Deep Dive	Instructions (FROM, RUN, CMD, COPY, WORKDIR, EXPOSE, ENV)
    - Multi-stage Builds	Build small, efficient production images
    - Tagging Images	docker tag, versioning images properly

3️⃣ Networking in Docker
    - Topic	What You’ll Learn
    - Docker Networks	Bridge, Host, None, Overlay
    - Create and Connect Networks	docker network create, inspect, connect
    - Communication Between Containers	Linking containers on the same network
    - Expose vs Publish Ports	Difference between EXPOSE and -p option

4️⃣ Storage in Docker (Volumes and Bind Mounts)
    - Topic	What You’ll Learn
    - Volumes	Persist container data using docker volume
    - Bind Mounts	Mount folders from your machine inside containers
    - Backup and Restore Volumes	Practical backup of databases or media files

5️⃣ Docker Compose (Multi-container Apps)
    - Topic	What You’ll Learn
    - docker-compose.yml syntax	Services, networks, volumes, build
    - Running Multi-container Apps	Example Django + PostgreSQL setup
    - Environment Variables in Compose	env_file, environment options
    - Override Compose Files	docker-compose.override.yml for local/dev/prod

6️⃣ Dockerizing Applications (Practical Hands-on)
    - Application	Concepts Covered
    - Dockerize Django App	.env, PostgreSQL, Gunicorn
    - Dockerize Flask App	With MySQL
    - Dockerize React App	Serve with nginx inside a container
    - Dockerize Full Stack App	React + Django + PostgreSQL

7️⃣ Docker Best Practices
    - Topic	What You’ll Learn
    - Slim and Secure Images	Use python:3.11-slim, node:18-alpine
    - Avoid Root Users	Use non-root users in containers
    - Use .dockerignore	Avoid copying unnecessary files into images
    - Optimize Layers	Reduce image size with correct Dockerfile writing
    - Multi-stage Build	Build separate builder and runtime images

8️⃣ Docker Registry and Image Management
    - Topic	What You’ll Learn
    - Private Registries	Harbor, ECR, GitHub Packages
    - Push/Pull to Private Repo	docker login, push, pull
    - Image Security	Scan Docker images for vulnerabilities

9️⃣ Deploying Production-Ready Docker Applications
    - Topic	What You’ll Learn
    - Use Gunicorn + Nginx	In Django/Flask apps
    - Serve Static Files Properly	Collectstatic in Django
    - Use Docker Compose for Production	docker-compose.prod.yml
    - Using Secrets in Production	Secure .env variables
    - Healthchecks	Set healthchecks in docker-compose.yml and Dockerfile
    - Logging and Monitoring	Collect logs from containers
    - Use SSL (Let's Encrypt + nginx)	SSL termination for Django/Flask

🔥 Bonus Advanced Topics (Once You're Comfortable)
    Topic	                                    What You’ll Learn
    Docker Swarm Basics	                        Native clustering in Docker
    Introduction to Kubernetes	                Container orchestration
    CI/CD with Docker	                        Automate build, test, deploy pipelines
    Docker Secrets Management	                Manage sensitive data securely
    Container Security Best Practices	        Scan, sign images, minimize attack surface

🎯 Study Flow Recommendation
    ✅ Learn →
    ✅ Do small project →
    ✅ Apply best practices →
    ✅ Build production-ready apps →
    ✅ Push to cloud servers

🏆 Mini Projects You Should Try
    Project	Stack
        - Dockerize a Django Blog	Django + PostgreSQL + Gunicorn
        - Dockerize a Chat App	Flask + Redis
        - Fullstack App	React + Django REST API + PostgreSQL
        - Production Deploy	Deploy to AWS EC2 with HTTPS



########## INTERVIEW QUESTIONS  #########################

🐳 1. Docker Basics and Core Concepts — 30 Interview-Centric Questions

1. What problem does Docker solve?

2. How does containerization differ from virtualization?

3. Can you explain Docker architecture in detail?

4. What is the role of Docker Engine?

5. What is a container runtime?

6. What is the difference between Docker CE and Docker EE?

7. Explain images vs containers in Docker.

8. What is a layer in a Docker image?

9. How is a Docker container isolated from the host system?

10. What is the default network driver in Docker?

11. How does Union File System work in Docker?

12. What happens internally when you run docker run hello-world?

13. What is Docker Hub? How does it work?

14. How do you version control a Docker image?

15. Explain Docker architecture with an example.

16. What is the role of Docker Registry?

17. Can you explain namespaces and cgroups in Docker?

18. Why are containers considered lightweight?

19. Explain "Docker is process-level virtualization".

20. What are official images on Docker Hub?

21. What happens if you run a container without a network?

22. What is a dangling image in Docker?

23. Explain ephemeral nature of Docker containers.

24. What happens if a container crashes? How does Docker handle it?

25. Explain stateless vs stateful containers.

26. How do you persist data across container restarts?

27. Can you explain control groups (cgroups) in Docker?

28. How do you secure communication between Docker client and daemon?

29. How does Docker manage resource allocation (CPU/RAM)?

30. How is OCI (Open Container Initiative) related to Docker?

🐳 2. Dockerfile and Images — 30 Interview-Centric Questions

31. What is a Dockerfile? Why do we need it?

32. How do you create a minimal Docker image?

33. What are some best practices for writing a Dockerfile?

34. Difference between CMD and ENTRYPOINT?

35. How can you override CMD instructions?

36. How does multi-stage build help optimize Docker images?

37. What is a build context in Docker?

38. How do you use COPY vs ADD in Dockerfile?

39. What is the use of WORKDIR instruction?

40. What is ARG in Dockerfile? How is it different from ENV?

41. What happens if you miss EXPOSE in Dockerfile?

42. What are healthchecks in Dockerfile?

43. How do you pass dynamic values at build time?

44. How do you make a non-root Dockerfile for security?

45. Why is using Alpine Linux popular for Docker images?

46. What are image labels in Dockerfile?

47. How can you cache dependencies properly in a Dockerfile?

48. Why should you remove unnecessary files in production images?

49. How do you copy secret keys safely in a Dockerfile?

50. What are ONBUILD triggers in Dockerfile?

51. How do you minimize layers in a Dockerfile?

52. What is the ENTRYPOINT script pattern?

53. What is the difference between "exec" and "shell" form CMD?

54. How do you handle application crashes in a Dockerfile?

55. How can you optimize image build time?

56. Why should you separate dependencies and application code in Dockerfile?

57. What happens during a failed build stage?

58. How do you choose a base image for your Dockerfile?

59. Can you explain multi-arch Docker images?

60. How to use .dockerignore and why is it critical?

🐳 3. Docker Container Management — 30 Interview-Centric Questions

61. How do you start, stop, and restart containers?

62. How to list running and stopped containers?

63. How to attach and detach from a running container?

64. How to execute a command inside a running container?

65. How do you copy files into and out of a container?

66. How can you see logs of a container?

67. What is a container ID and container name?

68. How do you restart a container automatically if it crashes?

69. What is a container volume mount?

70. How do you commit changes to a running container into a new image?

71. How can you run multiple processes inside a container?

72. How can you limit CPU and Memory for a container?

73. What is the difference between foreground and detached mode?

74. How to setup an interactive shell inside a running container?

75. How to export and import a container?

76. How to inspect a container’s metadata?

77. How can you troubleshoot a failed container startup?

78. How to handle environment variables inside a container?

79. How to pass secrets to containers securely?

80. What is the difference between soft stop and hard kill for a container?

81. How to pause and unpause a container?

82. How to share files between host and container?

83. What is container snapshotting?

84. What is init system inside a container? Why does it matter?

85. How can you update a running container?

86. Can you connect a running container to another network?

87. How to backup and restore container volumes?

88. How do you remove containers, images, and volumes safely?

89. How to clean up dangling containers and images?

90. What happens when Docker daemon restarts? What happens to running containers?


🐳 4. Docker Compose and Multi-Container Applications — 30 Interview-Centric Questions

91. What is Docker Compose?

92. How is docker-compose.yml structured?

93. How do you define multiple services in docker-compose?

94. How do you configure dependencies between services?

95. What are services, networks, and volumes in docker-compose?

96. How do you scale services in docker-compose?

97. What is the use of depends_on in docker-compose?

98. How do you set environment variables in docker-compose?

99. How can you override default docker-compose.yml settings?

100. What is the difference between build and image in docker-compose?

101. How do you mount volumes in docker-compose?

102. How do you handle service discovery in docker-compose?

103. How do you use multiple compose files?

104. How do you run database migrations with docker-compose up?

105. How to use docker-compose for local development and production?

106. How to view logs from multiple services together?

107. How to restart only one service in docker-compose?

108. How to bring down and clean up a docker-compose project?

109. What is network_mode: host in docker-compose?

110. How do you use named volumes?

111. How to customize ports in docker-compose?

112. How do you handle secret injection in docker-compose?

113. How do you update service containers without downtime?

114. What is the docker-compose.override.yml?

115. How do you build images from private Git repositories in docker-compose?

116. How does healthcheck affect service start order?

117. How do you enable auto-restart policies in docker-compose?

118. Can you run one-off commands using docker-compose?

119. How do you manage multi-environment deployments (dev/stage/prod) using docker-compose?

120. Can docker-compose be used with Kubernetes?

🐳 5. Advanced Topics (Networking, Volumes, Production, Security) — 30 Interview-Centric Questions

121. What are Docker Networks?

122. What are bridge, host, and overlay networks?

123. How do you create a custom bridge network?

124. How do you inspect container networking?

125. How do you link two containers manually?

126. What is an overlay network used for?

127. How do you secure network communication between containers?

128. What are Docker Volumes?

129. What is the difference between volumes and bind mounts?

130. How do you backup volumes in production?

131. How do you persist logs across container restarts?

132. What are different logging drivers available in Docker?

133. How do you monitor running containers in production?

134. How to detect memory or CPU leaks in containers?

135. How do you reduce image size for production deployment?

136. How do you secure images from vulnerabilities?

137. What is Docker Content Trust (DCT)?

138. How do you manage secrets in production Docker?

139. What is docker scan command?

140. How does image signing work in Docker?

141. What is a sidecar container pattern?

142. What is the init container pattern?

143. How do you implement blue/green deployments using Docker?

144. What are rolling updates in Docker Swarm?

145. How do you autoscale containers?

146. What is the difference between Docker Swarm and Kubernetes?

147. How do you configure SSL/TLS for Dockerized apps?

148. How do you make your container immutable?

149. How do you troubleshoot DNS issues inside containers?

150. What are best practices for running databases inside containers?


########## Docker hands on ################

Level	            Hands-on Task	                    Skill
1	            Run containers, pull images	            Basics
2	            Write Dockerfile and build images	    Custom app containerization
3	            Write Docker Compose	                Multi-container orchestration
4	            Use volumes for data persistence	    Storage
5	            Create custom networks	                Networking
6	            Multi-stage builds	                    Optimization
7	            Scheduled backup containers	            Automation
8	            Deploy on AWS ECS/ECR	                Deployment/Cloud



##########################          #################           ######################

🐳 Docker Commands Topic-wise with Uses and Examples
1. Installation and Setup
    Command	                                    Use	                                            Example
    docker --version	                        Check Docker version	                        docker --version
    docker info	                                Show system-wide Docker info	                docker info
    docker login	                            Login to Docker Hub	                            docker login

2. Images Management
    Command	                                    Use	                                            Example
    docker pull <image>	                        Download image from Docker Hub	                docker pull nginx
    docker images	                            List downloaded images	                        docker images
    docker rmi <image_id>	                    Remove image	                                docker rmi nginx
    docker build -t <name> .	                Build image from Dockerfile	                    docker build -t myapp .
    docker tag <image> <repo>:<tag>	            Tag image for pushing	                        docker tag myapp myrepo/myapp:v1
    docker push <repo>:<tag>	                Push image to registry	                        docker push myrepo/myapp:v1

3. Containers Management
    Command	                                    Use	                                            Example
    docker run <image>	                        Run container	d                               ocker run nginx
    docker run -d <image>	                    Run container in background (detached mode)	    docker run -d nginx
    docker run -p 8080:80 <image>	            Map ports (host:container)	                    docker run -p 8080:80 nginx
    docker ps	                                List running containers	                        docker ps
    docker ps -a	                            List all containers	                            docker ps -a
    docker stop <container_id>	                Stop container	                                docker stop 1234abcd
    docker start <container_id>	                Start stopped container	                        docker start 1234abcd
    docker restart <container_id>	            Restart container	                            docker restart 1234abcd
    docker rm <container_id>	                Remove container	                            docker rm 1234abcd
    docker exec -it <container> bash	        Open shell inside container	                    docker exec -it mycontainer bash
    docker logs <container_id>	                See container logs	                            docker logs mycontainer

4. Volumes Management
    Command	                                    Use	                                            Example
    docker volume create <name>	                Create a volume	                                docker volume create mydata
    docker volume ls	                        List volumes	                                docker volume ls
    docker volume inspect <name>	            Inspect volume details	                        docker volume inspect mydata
    docker volume rm <name>	                    Remove volume	                                docker volume rm mydata
    docker run -v <volume>:/path <image>	    Attach volume to container	                    docker run -v mydata:/app/data nginx

5. Networks Management
    Command	                                    Use	                                            Example
    docker network create <name>	            Create a network	                            docker network create mynetwork
    docker network ls	                        List networks	                                docker network ls
    docker network inspect <name>	            Inspect a network	                            docker network inspect mynetwork
    docker network rm <name>	                Remove network	                                docker network rm mynetwork
    docker run --network=<name> <image>	        Connect container to a network	                docker run --network=mynetwork nginx

6. Docker Compose Commands
    Command	                                    Use	                                            Example
    docker-compose up	                        Start all services	                            docker-compose up
    docker-compose up -d	                    Start services in background	                docker-compose up -d
    docker-compose down	                        Stop and remove services	                    docker-compose down
    docker-compose ps	                        List running services	                        docker-compose ps
    docker-compose logs	                        Show service logs	                            docker-compose logs

7. Dockerfile Related Commands
    Command	                                    Use	                                            Example
    docker build -f <Dockerfile> -t <tag> .	    Build using specific Dockerfile	                docker build -f Dockerfile.prod -t myapp:prod .
    docker run -it --rm <image>	                Run and auto-delete after exit	                docker run -it --rm ubuntu

8. Container Inspection and Debugging
    Command	                                    Use	                                            Example
    docker inspect <container/image>	        Show detailed info	                            docker inspect nginx
    docker top <container>	                    Show running processes inside container	        docker top mycontainer
    docker stats	                            Live resource usage (CPU, Memory)	            docker stats

9. Saving and Sharing
    Command	                                    Use	                                            Example
    docker save -o <file>.tar <image>	        Save image to tar file	                        docker save -o nginx.tar nginx
    docker load -i <file>.tar	                Load image from tar file	                    docker load -i nginx.tar
    docker export <container_id> > file.tar	    Export running container's filesystem	        docker export 1234abcd > container.tar
    docker import <file>.tar	                Import container filesystem as image	        docker import container.tar mynewimage

10. Swarm and Orchestration (Advanced)
    Command	                                            Use	                                    Example
    docker swarm init	                                Initialize a swarm	                    docker swarm init
    docker node ls	                                    List swarm nodes	                    docker node ls
    docker service create	                            Create service in swarm	                docker service create --name web nginx
    docker service ls	                                List services	                        docker service ls
    docker service scale <service>=<replicas>	        Scale service	                        docker service scale web=5
    docker stack deploy -c <compose-file> <stackname>	Deploy full stack	                    docker stack deploy -c docker-compose.yml mystack

🎯 BONUS: Useful Shortcuts
    Shortcut	                    Description
    docker system prune	            Remove all unused images, containers, volumes, networks
    docker container prune	        Remove all stopped containers
    docker volume prune	            Remove all unused volumes
    docker image prune	            Remove dangling images


