# Generated by Django 3.0.6 on 2020-06-04 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20200604_0153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='favorite',
        ),
        migrations.AddField(
            model_name='author',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='fave', to='recipes.Recipe'),
        ),
    ]
