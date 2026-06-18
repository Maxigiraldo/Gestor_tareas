class Tarea:
    def __init__(self, id: int, descripcion:str, prioridad: str, estado:str):
        self.id = id
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.estado = estado
    
    def crear(self):
        tarea = {
            'ID': self.id,
            'Descripcion': self.descripcion,
            'Prioridad': self.prioridad,
            'Estado': self.estado
        }
        return tarea