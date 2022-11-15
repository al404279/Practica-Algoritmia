# ------------------------------------------------------
# IMPORTANTE:
#    ESTE FICHERO NO DEBE MODIFICARSE DE NINGÚN MODO
# ------------------------------------------------------

from dataclasses import dataclass
from typing import Optional


# dataclass: RowCol
# - Los objetos de esta clase son inmutables. Ejemplo de uso:
#     rc = RowCol(3 ,5)
#     print(rc.row)
@dataclass(frozen=True)
class RowCol:
    row: int
    col: int


# La clase Board construye un puzle a partir de una lista de cadenas con su descipción.
# La lista de cadenas se corresponde con las lineas del fichero de la instancia.
# El primer carácter de la primera cadena se corresponde con la posición RowCol(0, 0) del tablero.
#
# Tiene tres métodos públicos:
# - has_tile(row_col) -> Devuelve True si hay suelo en esa row_col
# - start_pos()       -> Devuelve la row_col inicial (donde se encuentra el bloque al iniciar el nivel)
# - target_pos()      -> Devuelve la row_col objetivo (donde tenemos que colocar el bloque)
class Board:
    valid_chars = {'o', '-', 'S', 'T'}

    def __init__(self, lines: list[str]):
        self._board = [line.strip() for line in lines]
        if len(set(len(line) for line in self._board)) != 1:
            raise RuntimeError("Lines with diferent lengths in board instance")
        self.rows = len(self._board)
        self.cols = len(self._board[0])
        self._sPos = self._find_char('S')
        if self._sPos is None:
            raise RuntimeError("Expected exactly one 'S' char in board")
        self._tPos = self._find_char('T')
        if self._sPos is None:
            raise RuntimeError("Expected exactly one 'T' char in board")
        extra_chars = set(c for line in self._board for c in line).difference(self.valid_chars)
        if len(extra_chars) > 0:
            raise RuntimeError(f"Unknown chars in board instance: {extra_chars}")

    def has_tile(self, pos: RowCol) -> bool:
        if pos.row < 0 or pos.col < 0 or pos.row >= self.rows or pos.col >= self.cols:
            return False
        return self._board[pos.row][pos.col] != '-'

    def start_pos(self) -> RowCol:
        return self._sPos

    def target_pos(self) -> RowCol:
        return self._tPos

    def _find_char(self, char) -> Optional[RowCol]:
        n = 0
        res = None
        for r in range(self.rows):
            for c in range(len(self._board[r])):
                if self._board[r][c] == char:
                    res = RowCol(r, c)
                    n += 1
        if n == 1:
            return res
