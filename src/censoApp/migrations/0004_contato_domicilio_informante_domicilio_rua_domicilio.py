# Generated by Django 5.2.2 on 2025-06-06 18:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('censoApp', '0003_remove_domicilio_informante_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='Domicilio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='censoApp.domicilio'),
        ),
        migrations.AddField(
            model_name='informante',
            name='Domicilio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='censoApp.domicilio'),
        ),
        migrations.AddField(
            model_name='rua',
            name='Domicilio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='censoApp.domicilio'),
            preserve_default=False,
        ),
    ]
