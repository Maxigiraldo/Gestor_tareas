import argparse
from gestor import GestorTareas
from storage import Storage

parser = argparse.ArgumentParser()
parser.add_argument('gestor_action', type=str, help='Accion que desea realizar')
parser.add_argument('-descripcion', type=str, help='Descripcion de la nueva tarea')
parser.add_argument('-id', type=int, help="Identificador de la tarea")
parser.add_argument('-filtro', type=str, help="Categoria", default=None)
parser.add_argument('--atributo', type=str, help="Atributo. Debe ir despues de -filtro", default=None)
parser.add_argument('--prioridad', type=str, help="Defina la prioridad de la tarea", default="Normal")
args = parser.parse_args()

gestor = GestorTareas()
storage = Storage()

data = storage.leer()

if args.gestor_action == 'agregar':
    tarea_final = max(data, key=lambda lista: lista['ID'], default=1)
    id = tarea_final['ID'] + 1
    data.append(gestor.agregar(id, args.descripcion, args.prioridad, "Pendiente"))

if args.gestor_action == 'completar':
    gestor.completar(args.id, data)
    
if args.gestor_action == 'eliminar':
    gestor.eliminar(args.id, data)

if args.gestor_action == 'listar':
    gestor.listar(data, [args.filtro, args.atributo])

storage.guardar(data)