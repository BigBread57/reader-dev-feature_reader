# Generated by Django 3.1.7 on 2021-06-16 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readerBd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='event',
            field=models.ManyToManyField(blank=True, related_name='days', to='readerBd.Event', verbose_name='Событие'),
        ),
    ]