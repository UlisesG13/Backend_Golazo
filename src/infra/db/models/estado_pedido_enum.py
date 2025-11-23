from enum import Enum as PyEnum

class EstadoPedido(PyEnum):
    pendiente = "pendiente"
    procesando = "procesando"
    en_camino = "en_camino"
    completado = "completado"
    cancelado = "cancelado"