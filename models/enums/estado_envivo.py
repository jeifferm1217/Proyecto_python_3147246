#enums: tipo de dato personalizados
#uso: restringir variables de algunos valores

from enum import Enum

class Estado_Envivo(Enum):
    activo = "Activo"
    finalizado = "Finalizado"