import json

class Storage:
    def __init__(self):
        self.data = None
        
    def leer(self):
        try:
            with open('datos.json', 'r', encoding='utf-8') as archivo:
                self.data = json.load(archivo)
        except:
            print("No existe el archivo no se pudo abrir")
    
    def guardar(self):
        with open('datos.json', 'w', encoding='utf-8') as archivo:
                json.dump(self.data, "lista.json", indent=4)