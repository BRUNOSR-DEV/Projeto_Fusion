import uuid #gera codificação aleatória 

from django.db import models

from stdimage.models import StdImageField

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    criados =  models.DateField('Criação', auto_now_add= True) #auto_now_add colocara a data automaticamente só quando um novo objeto for criado

    modificados = models.DateTimeField('Atualizacao', auto_created=True ) # toda vez que esse objeto for atualizado a data tbm será atualizada 

    ativo =  models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self) -> str:
        return self.cargo


class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField('Serviços', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'  #Faz a apresentação do nome com Ç
        verbose_name_plural = 'Serviços'

    def __str__(self) -> str:
        return self.servico
    

class Recursos(Base):

    ICONE_CHOICES = (
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phonep', 'Not-celular'),
        ('lni-cog', 'Engrenagem'),
        ('lni-leaf', 'Folha'),
        ('lni-layers', 'Camadas'),
        ('lni-leaf', 'Folha'),
    )
    
    nome = models.CharField('Nome', max_length=100)

    descricao = models.TextField('Descrição', max_length=200)

    icone = models.CharField('Icone', max_length=17, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Recurso' 
        verbose_name_plural = 'Recursos'

    def __str__(self) -> str:
        return self.nome
    

class Funcionario(Base):

    nome = models.CharField('Nome', max_length=100)

    cargo = models.ForeignKey('core.Cargo',verbose_name='Cargo', on_delete=models.CASCADE) #Chave estrangeira. 

    bio = models.TextField('Bio', max_length=200)

    imagem = StdImageField('Imagem', upload_to= get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True }}) #variations -  cria uma variação da imagem caso ela for maior, passando largura e comprimento - 'crop' - se necessário cortar, pode!

    facebook = models.CharField('Facebook', max_length=100, default='#' )
    instagram = models.CharField('Instagran', max_length=100, default='#' )
    x = models.CharField('X', max_length=100, default='#' )

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self) -> str:
        return self.nome
    
    
class Clientes(Base):


    nome = models.CharField('Nome', max_length=100,)

    profissao = models.CharField('Cargo', max_length=50)

    descricao = models.TextField('Relato', max_length=400)

    estrelas = models.IntegerField('Quantidade de Estrelas', max_length=5, help_text='Escolha de 1 a 5')

    imagem = StdImageField('Imagem', upload_to= get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True }})


    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self) -> str:
        return self.nome

    