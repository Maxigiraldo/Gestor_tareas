import json

class Storage:
    def leer(self):
        try:
            with open('datos.json', 'r', encoding='utf-8') as archivo:
                data = json.load(archivo)
                return data
        except:
            print("No existe el archivo no se pudo abrir")
            return []
    
    def guardar(self, data):
        with open('datos.json', 'w', encoding='utf-8') as archivo:
                json.dump(data, archivo, indent=4)