import pytest
from gestor import GestorTareas
from storage import Storage

gestor = GestorTareas()
storage = Storage()

def test_leer():
    data = storage.leer()
    assert type(data) == list or data is None

def test_guardar():
    storage.guardar([{'ID': 1, 'Descripcion': "Prueba", 'Prioridad': "Normal", 'Estado': "Pendiente"}])
    data = storage.leer()
    assert data[0] == {'ID': 1, 'Descripcion': "Prueba", 'Prioridad': "Normal", 'Estado': "Pendiente"}

def test_agregar():
    tarea = gestor.agregar(1, "Prueba", "Normal", "Pendiente")
    Prueba = {
            'ID': 1,
            'Descripcion': "Prueba",
            'Prioridad': "Normal",
            'Estado': "Pendiente"
        }
    assert Prueba == tarea
    

    
def test_completar():
    data = gestor.completar(1, storage.leer())
    assert data[0] == {
            'ID': 1,
            'Descripcion': "Prueba",
            'Prioridad': "Normal",
            'Estado': "Completado"
        }

def test_eliminar():
    data = storage.leer()
    gestor.eliminar(1, data)
    storage.guardar(data)
    cambio = storage.leer()
    assert cambio == []

def test_completar_no_existente():
    data = [
        {'ID': 1, 'Descripcion': "Prueba", 'Prioridad': "Normal", 'Estado': "Pendiente"}
    ]

    resultado = gestor.completar(999, data)

    assert resultado[0]['Estado'] == "Pendiente"
    
def test_eliminar_no_existente():
    data = [
        {'ID': 1, 'Descripcion': "Prueba", 'Prioridad': "Normal", 'Estado': "Pendiente"}
    ]

    gestor.eliminar(999, data)

    assert len(data) == 1

def test_leer_archivo_inexistente():
    storage = Storage()
    resultado = storage.leer()

    assert isinstance(resultado, list)
    
def test_listar_sin_filtro(capsys):
    data = [
        {'ID': 1, 'Descripcion': "Prueba", 'Prioridad': "Normal", 'Estado': "Pendiente"}
    ]

    gestor.listar(data, None)

    salida = capsys.readouterr()

    assert "Prueba" in salida.out
    
def test_listar_con_filtro(capsys):
    data = [
        {'ID': 1, 'Descripcion': "Tarea 1", 'Prioridad': "Alta", 'Estado': "Pendiente"},
        {'ID': 2, 'Descripcion': "Tarea 2", 'Prioridad': "Baja", 'Estado': "Pendiente"}
    ]

    gestor.listar(data, ("Prioridad", "Alta"))

    salida = capsys.readouterr()

    assert "Tarea 1" in salida.out
    assert "Tarea 2" not in salida.out