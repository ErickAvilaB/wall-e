from abc import ABC, abstractmethod


class Expresion(ABC):
    @abstractmethod
    def evaluar(self, contexto: dict):
        pass
