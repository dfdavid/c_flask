# mongodb_docker

proyecto para instanciar una base de datos mongo con docker y configurarla para el Proyecto Final

## Pre requisitos

- Docker Engine
<https://docs.docker.com/engine/install/>

- Docker Compose
<https://docs.docker.com/compose/install/>

## Pasos para el despliegue

1_ Clonar el repositorio.
Preferentemente en /opt.

2_ Ingresar al directorio /mongodb_docker y ejecutar el comando "docker-compose up -d". Al desplegar, se llena el directorio "datadir" con los archivos propios del servicio y quedan mapeados en el disco local del host. Al mismo tiempo, el contenedor toma la configuracion del archivo de este repositorio.

3_ Crear la base de datos y el/los usuarios necesarios:

    a- Ejecutar docker exec -it <nombre_del_contenedor> bash
    
    b- entrar en la consola de mongo con el comando mongosh "mongodb://192.168.1.7:27016" (validar IP y puertos correctos)
    
    c- Dentro de la consola ejecutar: "use tesis" donde -tesis- es el nombre de la base a crear.
    
    d- usar el comando db.createUser({
                                      ... user: "nombre_usuario",
                                      ... pwd: "1234",
                                      ... roles: ["dbOwner", "readWrite"]
                                      ... }
                                      )
                                      
    Lista la base para usar. 

## Backup DB

### Backup

    ```bash
    mongodump -d djongo --uri="mongodb://roberto:sanchez@150.136.250.71:27017" --authenticationDatabase admin
    ```

### Restore

    ```bash
    mongorestore --uri="mongodb://roberto:sanchez@192.168.1.110:27017" --authenticationDatabase admin
    ```
