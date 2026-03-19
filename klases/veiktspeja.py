from time import time_ns
class Veiktspeja:
    def __init__(self):
        self.uzs_laiks = 0
        self.pab_laiks = 0
        self.laiks = 0
        self.generets = 0
        self.izskatits = 0
    
    def stop(self):
        self.pab_laiks = time_ns()
        self.laiks += self.pab_laiks - self.uzs_laiks

    def run(self):
        self.uzs_laiks = time_ns()

    def __str__(self):
        return f"{self.generets} | {self.izskatits} | {self.laiks / 10e9 :.6f}"
    