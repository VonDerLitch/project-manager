# Generated by Django 5.0 on 2024-02-20 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0007_cancelarp'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='motivo_cancelamento',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='MotivoCancelamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.TextField()),
                ('data_cancelamento', models.DateTimeField(auto_now_add=True)),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projetos.projeto')),
            ],
        ),
    ]
