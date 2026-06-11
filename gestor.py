from models import Tarea

class GestorTareas:
    def agregar(self, id, descripcion: str, prioridad: str, estado: str):
        tarea = Tarea(id, descripcion, prioridad, estado)
        return tarea
    
    def completar(self, id: int, data: list):
        for i in data:
            if data['ID'] == id:
                data['Estado'] = 'Completado'
                break
        return data
    
    def eliminar(self, id: int, data: list):
        for i in data:
            if data['ID'] == id:
                data.remove(i)
    
    def listar(self, data: list, filtro):
        print("ID\tPRIORIDAD\tESTADO\tTAREA")
        for tarea in data:
            if filtro is None or tarea[filtro[0]] == filtro[1]:
                print(
                f"{tarea['ID']}\t"
                f"{tarea['Prioridad']}\t"
                f"{tarea['Estado']}\t"
                f"{tarea['Descripcion']}"
                )