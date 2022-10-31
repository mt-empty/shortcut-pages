# Docker

> Source: https://docs.docker.com/engine/reference/commandline/

$ Management Commands
    `docker dockerd                {{Launch the Docker daemon}} 
    `docker info                   {{Display system-wide information}} 
    `docker inspect                {{Return low-level information on a container or image}} 
    `docker version                {{Show the Docker version information}} 

$ Image Commands
    `docker build                  {{Build an image from a Dockerfile}} 
    `docker commit                 {{Create a new image from a container’s changes}} 
    `docker history                {{Show the history of an image}} 
    `docker images                 {{List images}} 
    `docker import                 {{Import the contents from a tarball to create a filesystem image}} 
    `docker load                   {{Load an image from a tar archive or STDIN}} 
    `docker rmi                    {{Remove one or more images}} 
    `docker save                   {{Save images to a tar archive}} 
    `docker tag                    {{Tag an image into a repository}} 

$ Container Commands
    `docker attach                 {{Attach to a running container}} 
    `docker cp                     {{Copy files/folders from a container to a HOSTDIR or to STDOUT}} 
    `docker create                 {{Create a new container}} 
    `docker diff                   {{Inspect changes on a container’s filesystem}} 
    `docker events                 {{Get real time events from the server}} 
    `docker exec                   {{Run a command in a running container}} 
    `docker export                 {{Export a container’s filesystem as a tar archive}} 
    `docker kill                   {{Kill a running container}} 
    `docker logs                   {{Fetch the logs of a container}} 
    `docker pause                  {{Pause all processes within a container}} 
    `docker port                   {{List port mappings or a specific mapping for the container}} 
    `docker ps                     {{List containers}} 
    `docker rename                 {{Rename a container}} 
    `docker restart                {{Restart a running container}} 
    `docker rm                     {{Remove one or more containers}} 
    `docker run                    {{Run a command in a new container}} 
    `docker start                  {{Start one or more stopped containers}} 
    `docker stats                  {{Display a live stream of container(s) resource usage statistics}} 
    `docker stop                   {{Stop a running container}} 
    `docker top                    {{Display the running processes of a container}} 
    `docker unpause                {{Unpause all processes within a container}} 
    `docker update                 {{Update configuration of one or more containers}} 
    `docker wait                   {{Block until a container stops, then print its exit code}} 

$ Hub and Registry Commands
    `docker login                  {{Register or log in to a Docker registry}} 
    `docker logout                 {{Log out from a Docker registry}} 
    `docker pull                   {{Pull an image or a repository from a Docker registry}} 
    `docker push                   {{Push an image or a repository to a Docker registry}} 
    `docker search                 {{Search the Docker Hub for images}} 

$ Network and Connectivity Commands
    `docker network connect        {{Connect a container to a network}} 
    `docker network create         {{Create a new network}} 
    `docker network disconnect     {{Disconnect a container from a network}} 
    `docker network inspect        {{Display information about a network}} 
    `docker network ls             {{Lists all the networks the Engine daemon knows about}} 
    `docker network rm             {{Removes one or more networks}} 

$ Shared Data Volume Commands
    `docker volumes create         {{Creates a new volume where containers can consume and store data}} 
    `docker volumes inspect        {{Display information about a volume}} 
    `docker volumes ls             {{Lists all the volumes Docker knows about}} 
    `docker volumes rm             {{Remove one or more volumes}} 

$ Swarm Node Commands
    `docker node promote           {{Promote a node that is pending a promotion to manager}} 
    `docker node demote            {{Demotes an existing manager so that it is no longer a manager}} 
    `docker node inspect           {{Inspect a node in the swarm}} 
    `docker node update            {{Update attributes for a node}} 
    `docker node ps                {{List tasks running on a node}} 
    `docker node ls                {{List nodes in the swarm}} 
    `docker node rm                {{Remove one or more nodes from the swarm}} 

$ Swarm Swarm Commands
    `docker swarm init             {{Initialize a swarm}} 
    `docker swarm join             {{Join a swarm as a manager node or worker node}} 
    `docker swarm leave            {{Remove the current node from the swarm}} 
    `docker swarm update           {{Update attributes of a swarm}} 
    `docker swarm join-token       {{Display or rotate join tokens}} 

$ Swarm Service Commands
    `docker service create         {{Create a new service}} 
    `docker service inspect        {{Inspect a service}} 
    `docker service ls             {{List services in the swarm}} 
    `docker service rm             {{Remove a service from the swarm}} 
    `docker service scale          {{Set the number of replicas for the desired state of the service}} 
    `docker service ps             {{List the tasks of a service}} 
    `docker service update         {{Update the attributes of a service}} 

