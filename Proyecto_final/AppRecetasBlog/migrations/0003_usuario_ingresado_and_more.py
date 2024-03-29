# Generated by Django 5.0 on 2024-01-12 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppRecetasBlog', '0002_recetas_ingresadas_ingredientes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='usuario_ingresado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField(max_length=20)),
                ('email', models.EmailField(default='', max_length=254)),
                ('pais', models.CharField(max_length=2000)),
                ('fecha_de_nacimiento', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='recetas_ingresadas',
            name='ingredientes',
            field=models.TextField(),
        ),
    ]
