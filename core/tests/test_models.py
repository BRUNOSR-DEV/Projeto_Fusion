import uuid

from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path

class GetFilePathTestCase(TestCase):

    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'  #gerando o arquivo

    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')  # istanciando o método
        self.assertTrue(len(arquivo), len(self.filename)) #comparando o arquivo gerado com o arquivo do método

class ServicoTestCase(TestCase):
    
    def setUp(self):
        self.servico = mommy.make('Servico') 

    def test_str(self):
        self.assertEquals
        (str(self.servico), self.servico.servico)

class CargoTestCase(TestCase):
    
    def setUp(self):
        self.cargo = mommy.make('Cargo')

    def test_str(self):
        self.assertEquals(str(self.cargo), self.cargo.cargo)

class FuncionarioTestCase(TestCase):
    
    def setUp(self):
        self.funcionario = mommy.make('Funcionario')

    def test_str(self):
        self.assertEquals(str(self.funcionario), self.funcionario.nome)

class RecursosTestCase(TestCase):
    
    def setUp(self):
        self.recursos = mommy.make('Recursos')

    def test_str(self):
        self.assertEquals(str(self.recursos), self.recursos.nome)

class ClientesTestCase(TestCase):
    
    def setUp(self):
        self.cliente = mommy.make('Clientes')

    def test_str(self):
        self.assertEquals(str(self.cliente), self.cliente.nome)