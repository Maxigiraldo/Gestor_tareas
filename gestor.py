from models import Tarea
class GestorTareas:
    def __init__(self):
        self.id = 1
    
    def agregar(self, descripcion: str, prioridad: str):
        tarea = Tarea(self.id, descripcion, prioridad)
        self.id += 1
    
    def completar(self, id: int):
        pass
    
    def eliminar(self, id: int):
        pass
    
    def listar(self):