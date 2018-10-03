#! /usr/bin/env python3
# coding: utf-8
import random
import time
import tkinter as tk
from typing import List

BG_COLOR = 'black'
LINE_COLOR = 'white'
CELL_COLOR = 'green'


class PyLife(tk.Tk):

    def __init__(self, title: str, width: int = 400, height: int = 400, num: int = 20, interval_sec: int = 0.2):
        super().__init__()
        self._title = title
        self._width = width
        self._height = height
        self._block_num = num
        self._interval_sec = interval_sec
        self._block_size = self._width // num
        self.geometry(f"{self._height}x{self._width}")
        self.canvas = tk.Canvas(self, bg=BG_COLOR, height=self._height, width=self._width)
        self.canvas.pack()

        # セルの初期化
        self.cells = []
        for r in range(self._block_num):
            cols = []
            for c in range(self._block_num):
                cols.append(random.randint(0, 1))
            self.cells.append(cols)

    def start(self):
        self.after(0, self.run)
        self.mainloop()

    def run(self):
        while True:
            self.cells = self.gen_next_cells()
            self.draw()
            time.sleep(self._interval_sec)

    def gen_next_cells(self) -> List[List[int]]:
        rows = []
        for r in range(self._block_num):
            cols = []
            for c in range(self._block_num):
                alive = self.count_alive_cells(r, c)
                if alive == 2:
                    cols.append(self.cells[r][c])
                elif alive == 3:
                    cols.append(1)
                else:
                    cols.append(0)
            rows.append(cols)
        return rows

    def count_alive_cells(self, r: int, c: int) -> int:
        alive = 0

        if r > 0:
            if c > 0:
                if self.cells[r - 1][c - 1]:
                    alive += 1
            if self.cells[r - 1][c]:
                alive += 1
            if c < self._block_num - 1:
                if self.cells[r - 1][c + 1]:
                    alive += 1

        if c > 0:
            if self.cells[r][c - 1]:
                alive += 1
        if self.cells[r][c]:
            alive += 1
        if c < self._block_num - 1:
            if self.cells[r][c + 1]:
                alive += 1

        if r < self._block_num - 1:
            if c > 0:
                if self.cells[r + 1][c - 1]:
                    alive += 1
            if self.cells[r + 1][c]:
                alive += 1
            if c < self._block_num - 1:
                if self.cells[r + 1][c + 1]:
                    alive += 1
        return alive

    def draw(self):
        self.canvas.delete('all')
        for r in range(self._block_num):
            for c in range(self._block_num):
                if self.cells[r][c]:
                    self.canvas.create_oval(r * self._block_size,
                                            c * self._block_size,
                                            r * self._block_size + self._block_size,
                                            c * self._block_size + self._block_size,
                                            fill=CELL_COLOR)

        # for x in range(0, HEIGHT, BLOCK_HEIGHT):
        #     canvas.create_line(x, 0, x, HEIGHT, fill=LINE_COLOR)
        # for y in range(0, HEIGHT, BLOCK_HEIGHT):
        #     canvas.create_line(0, y, WIDTH, y, fill=LINE_COLOR)
        self.update()


if __name__ == '__main__':
    pylife = PyLife(title='PyLife', width=500, height=500, num=50, interval_sec=0.2)
    pylife.start()
