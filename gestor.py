from models import Tarea

class GestorTareas:
    def agregar(self, id, descripcion: str, prioridad: str, estado: str):
        tarea_nueva = Tarea(id, descripcion, prioridad, estado)
        print(f"Tarea agregada con exito (id: {tarea_nueva.id})")
        return tarea_nueva.crear()
    
    def completar(self, id: int, data: list):
        for tarea in data:
            if tarea['ID'] == id:
                tarea['Estado'] = 'Completado'
                print(f"Tarea '{tarea['Descripcion']}' completada con exito")
                break
    
    def eliminar(self, id: int, data: list):
        for tarea in data:
            if tarea['ID'] == id:
                data.remove(tarea)
    
    def editar(self, id: int, descripcion, prioridad, data: list):
        for tarea in data:
            if tarea['ID'] == id:
                tarea['Descripcion'] = descripcion
                if  tarea['Prioridad'] != prioridad:
                    tarea['Prioridad'] = prioridad
                print(f"Tarea '{tarea['Descripcion']}' editada con exito")
                break
    
    def listar(self, data: list, filtro):
        if data == []:
            print("No hay tareas")
            return
        
        print("ID\tPRIORIDAD\tESTADO\tTAREA")
        for tarea in data:
            if filtro[0] is None or tarea[filtro[0]] == filtro[1]:
                print(
                f"{tarea['ID']}\t"
                f"{tarea['Prioridad']}\t"
                f"{tarea['Estado']}\t"
                f"{tarea['Descripcion']}"
                )