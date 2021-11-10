import pytest
from sitio.models import Producto, Categoria
from faker import Faker
fake = Faker()

@pytest.fixture
def product_creation():
    return Producto(
        titulo ='sdfghj',
        imagen ='dfn',
        descripcion ='dfg',
        precio = 122.00000,
        categoria = '1'
    )

@pytest.mark.django_db
def test_create_product(product_creation):
    product_creation.save()
    assert product_creation.titulo =='sdfghj'

    