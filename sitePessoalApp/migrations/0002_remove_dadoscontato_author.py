# Generated by Django 2.2.2 on 2019-06-06 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitePessoalApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dadoscontato',
            name='author',
        ),
    ]
