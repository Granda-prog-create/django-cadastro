# Generated by Django 5.0.1 on 2024-03-05 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cadastro', '0005_remove_usuario_idade_alter_usuario_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]