from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import ProductoModel

class ProductoSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = ProductoModel
        # Para indicar al serializador que tambien haga la validacion de las columnas que son
        # llaves foraneas (FK), su valor por defecto es False
        include_fk = True