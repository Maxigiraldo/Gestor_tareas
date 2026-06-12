# Sistema gestor de tareas por CLI

## Descripción
Este programa sirve para ingresar mediante comandos en la terminal tus
tareas pendientes, permite llevar un seguimiento y marcar como completadas

## Requisitos
- python 3 o superior
- pytest

## Modo de uso
### Ejecutar
'''
python tareas.py [comandos]
'''

### Comandos
- agregar: permite agregar una tarea al sistema
  - -descripcion: ingresar entre comillas de que se trata la tarea
  - --prioridad: agregar el nivel de prioridad de la tarea. por defecto se pone en "Normal"
- completar: cambia el estado de una tarea de "pendiente" a "completada"
  - -id: para ingresar el numero de la tarea
- eliminar: borrar una tarea del sistema (también usa -id)
- listar: permite ver todas las tareas
  - -filtro: permite elegir la categoria para filtrar
  - --atributo: el atributo especifico a filtrar