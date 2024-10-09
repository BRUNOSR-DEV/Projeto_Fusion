from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):

    def setUp(self):

        self.dados = {
            'nome': 'Bruno Rodrigues',
            'email': 'bruno77_sr@hotmail.com',
            'assunto': 'Um assunto qualquer',
            'mensagem': 'Uma mensagem qualquer',
        }

        self.cliente = Client()

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)

        self.assertEquals(request.status_code, 302)  # 302 código http de movimentação

    def test_form_invalid(self):

        dados = {
            'nome': 'Bruno Rodrigues',
            'email': 'bruno77_sr@hotmail.com',
        }

        request = self.cliente.post(reverse_lazy('index'), data=dados)

        self.assertEquals(request.status_code, 200) #verificação do código de status