from django.test import TestCase

from core.forms import ContatoForm

from model_mommy import mommy

class ContatoFormTestCase(TestCase):

    """def setUp(self):
        self.contato = mommy.make('ContatoForm')"""

    def setUp(self):
        self.nome = 'Bruno Rodrigues'
        self.email = ' bruno77_sr@hotmail.com'
        self.assunto = 'Um assunto qualquer'
        self.mensagem = 'Uma mensagem bem legal!'

        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }

        self.form =  ContatoForm(data=self.dados) # ContatoForm(request.POST)

    def test_send_mail(self):
        form1 =  ContatoForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        self.assertEquals(res1, res2)