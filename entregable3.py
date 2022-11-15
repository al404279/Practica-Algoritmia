from __future__ import annotations

import sys
from collections.abc import Iterator
from dataclasses import dataclass
from typing import Optional, TextIO

from algoritmia.schemes.bt_scheme import bt_min_solve, ScoredDecisionSequence

from board import Board, RowCol
from brick import Brick
from direction import Direction, directions2string

# Variable global con la salida de show_results() si no hay solución
INSTANCE_WITHOUT_SOLUTION = "INSTANCE WITHOUT SOLUTION"

# Tipos que utilizarás en el process() al aplicar el esquema de backtracking
Decision = Direction  # Cuatro valores posibles: Directions.Right, Direction.Left, Direction.Up, Direction.Down
Solution = tuple[Decision, ...]  # Utilizad la función auxiliar 'directions2string' de direction.py para convertir
                                 # una solución en una cadena del tipo 'RRUUULLDR...'


# ---------------------------------------------------------------------------------------------------------------------

def read_data(f: TextIO) -> Board:
    return Board.readLines(f)


def process(board: Board) -> Optional[Solution]:
    raise NotImplementedError()


def show_results(solution: Optional[Solution]):
    if solution is None:
        print(INSTANCE_WITHOUT_SOLUTION)
    else:
        print(directions2string(solution))


# Programa principal --------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    board0 = read_data(sys.stdin)
    solution0 = process(board0)
    show_results(solution0)
