class GestorTareas:
    def agregar(self, id, descripcion: str, prioridad: str, estado: str):
        tarea = {'ID': id, 'Descripcion': descripcion, 'Prioridad': prioridad, 'Estado': estado}
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
    
    def listar(self, data: list):
        print("ID\tPRIORIDAD\tESTADO\tTAREA")
        for i in data:
            print(f"{data['ID']}\t{data['Prioridad']}\t{data['Estado']}\t{data['Descripcion']}")