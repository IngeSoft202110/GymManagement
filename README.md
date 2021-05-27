# GymManagement

Este proyecto es desarrollado para la materia de Ingeniería de Software de la Pontificia Universidad Javeriana

## Tecnologías utilizadas

Este aplicativo está basado en `Python 3`. Antes de iniciar debe estar seguro que lo tiene instalado en su máquina.

Python utiliza instaladores para poder configurar sus librería. Asegurese de tener instalado `pip3`.

Además, para la facilidad de distribución de mensajes en el chat, se utiliza `Docker`. 

## Pasos para instalar y correr el proyecto en un entorno local

#### Repositorio

Ahora ustede puede clonar el repositorio:

`git clone https://github.com/IngeSoft202110/GymManagement.git`


#### Intalación de librerias

**Intalación de Django**:
```bash
$ pip install Django
```

**Intalación de Django-channels**:
```bash
$ pip install channels
```

**Intalación de mySQL client**:
```bash
$ pip install mysqlclient
```
**Intalación de channel redis**:
```bash
$ pip install channels_redis
```

#### Correr el programa

**Activar el docker para el paso de mensajes y conexión**:
```bash
$ docker run -p 6379:6379 -d redis:5
```

**Dirigirse a la carpeta del proyecto y ejecutar el servidor**:
```bash
$ cd GymManagement/proyecto/
$ python manage.py runserver
```
