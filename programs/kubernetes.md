# Kubernetes

> Source: http://k8s.info/cs.html

> Aliases: kubernetes-cli, basic-kubernetes

$ Physical Layout
    `kubectl version               {{Query the server / client version used}} 
    `kubectl cluster-info          {{Get cluster info}} 
    `kubectl config view           {{Get configuration info}} 
    `kubectl get nodes -w          {{Watch nodes continuously}} 
    `kubectl describe node123      {{Get info about 'node123'}} 

$ Abstraction Overview
    `kubectl get pods              {{List pods}} 
    `kubectl describe pod nginx-hl2nb
>                                  {{Get info about pod 'nginx-hl2nb'}} 
    `kubectl get rc                {{List replication controllers}} 
    `kubectl describe rc nginx     {{Get info about replication controller 'nginx'}} 
    `kubectl expose rc nginx --port=80 --target-port=8000
>                                  {{Expose replication controller 'nginx' as a service on port 80}} 
    `kubectl get svc               {{List services}} 
    `kubectl describe svc nginx    {{Get info about service 'nginx'}} 
    `kubectl delete pod nginx-hl2nb
>                                  {{Destroy/remove a resource}} 
    `kubectl delete rc nginx       {{Remove a replication controller named nginx}} 
    `kubectl delete svc nginx      {{Remove a service named nginx}} 
    `kubectl exec nginx-hl2nb /bin/sh -c $NAME_OF_CONTAINER
>                                  {{Debug container NAME_OF_CONTAINER}} 
    `kubectl logs -f nginx-hl2nb -c $NAME_OF_CONTAINER
>                                  {{See the logs of NAME_OF_CONTAINER}} 
    `kubectl get cs                {{Check the status of components such as the scheduler, etcd, and controller manager}} 

$ Abstraction Details
    `kubectl run ubuntu --image=ubuntu
>                                  {{To launch a pod and implicitly create a RC}} 
    `kubectl create -f nginx-rc.yaml
>                                  {{To create a RC from a manifest}} 
    `kubectl get rc --namespace="kube-system"
>                                  {{To list all RCs in a certain namespace}} 
    `kubectl scale --replicas=2 rc nginx
>                                  {{To change the number of pods in a RC with scaling}} 
    `kubectl create -f my-service.yaml
>                                  {{To create a service from a YAML file}} 
    `kubectl get pods -l="app=webserver"
>                                  {{To list all pods labelled with 'app=webserver'}} 
    `kubectl expose rc nginx --port=80 --target-port=8000
>                                  {{To expose a RC named 'nginx' that has a pod serving on port 8000 as a service on port 80}} 
    `kubectl get ep                {{To list the endpoints}} 
    `kubectl get secrets           {{To list all secrets which are used to handle sensitive information such as password or API credentials}} 
    `kubectl get pods --show-all   {{To view completed pods of a job}} 
    `kubectl get events            {{Changes the resources such as pods, RCs, services, etc. are available through events}} 
    `kubectl get ns                {{To list all namespaces which separate users, groups or applications}} 
    `kubectl get quota             {{To see the resource quotas of a namespace use}} 

