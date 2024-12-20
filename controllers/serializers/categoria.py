from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import Categoria
from marshmallow import fields
from .libro_serializer import LibroSerializer

class CategoriaSerializer(SQLAlchemyAutoSchema):
    # libros = fields.Nested(LibroSerializer, many=True)
    librosDeLaCategoria = fields.Nested(LibroSerializer, many = True, attribute='libros')
    
    class Meta:
        # Si queremos que este serializador incluya las relaciones
        model = Categoria
        # Si queremos q este serializador incluya las relaciones
        # include_relationships = True