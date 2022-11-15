# ------------------------------------------------------
# IMPORTANTE:
#    ESTE FICHERO NO DEBE MODIFICARSE DE NINGÚN MODO
# ------------------------------------------------------

from collections.abc import Iterable
from enum import Enum


# Tipo enumerado: Direction
# - Heredar de Enum hace que sea una enumeración. Ejemplo de uso:
#     d = Direction.Right
#     print(d)        # Muestra 'Direction.Right'
#     print(d.name)   # Muestra 'Right'
#     print(d.value)  # Muestra 'R'    <- Este es el que nos interesa para convertir list[Direction] en list[str]
class Direction(Enum):
    Left = "L"
    Right = "R"
    Up = "U"
    Down = "D"


# Función auxiliar 'directions2string'
# - Convierte una secuencia del tipo enumerado Direction en una cadena
# - Ejemplo:
#      ds = [Directions.Right, Direction.Up, Direction.Up, Direction.Left]
#      res = solution2string(ds)
#   res contiene la cadena 'RUUL'
def directions2string(solution: Iterable[Direction]) -> str:
    return ''.join(d.value for d in solution)
