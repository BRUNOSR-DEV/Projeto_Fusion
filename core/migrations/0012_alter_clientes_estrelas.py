# Generated by Django 5.1.1 on 2025-02-06 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_clientes_estrelas_alter_clientes_imagem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='estrelas',
            field=models.IntegerField(help_text='Escolha de 1 à 5', verbose_name='Quantidade de Estrelas'),
        ),
    ]
