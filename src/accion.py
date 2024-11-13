class Accion:
    def __init__(self, **args) -> None:
        self.__nombre_empresa: str = args['nombre_empresa']
        self.__ticker: str = args['ticker']
        self.__sector: str = args['sector']
        self.__pais: str = args['pais']
        self.__divisa: str = args['divisa']
        self.__precio_actual: float = args['precio_actual']
        self.__historico = args['historico']

    @property
    def nombre_empresa(self) -> str:
        return self.__nombre_empresa

    @property
    def ticker(self) -> str:
        return self.__ticker

    @property
    def sector(self) -> str:
        return self.__sector

    @property
    def pais(self) -> str:
        return self.__pais

    @property
    def divisa(self) -> str:
        return self.__divisa

    @property
    def precio_actual(self) -> float:
        return self.__precio_actual

    @property
    def historico(self):
        return self.__historico
