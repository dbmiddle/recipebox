# Generated by Django 3.0.6 on 2020-06-04 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='fave', to='recipes.Recipe'),
        ),
    ]
