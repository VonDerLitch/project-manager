# Generated by Django 5.0 on 2024-02-20 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0006_projeto_projeto_principal'),
    ]

    operations = [
        migrations.CreateModel(
            name='CancelarP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancelar', models.CharField(default='', max_length=255, verbose_name='cancelarP')),
            ],
        ),
    ]
