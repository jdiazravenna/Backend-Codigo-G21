from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import CategoriaModel

class CategoriaSerializer(SQLAlchemyAutoSchema):
    class Meta:
        # para pasarle metadatos a la clase de la cual estamos heredando
        # Obtendrá toda la configuracion del modelo, y la pondra para cuestiones 
        # del serializador
        model = CategoriaModel