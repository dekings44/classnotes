# Generated by Django 3.2.5 on 2021-09-06 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notebooks', '0005_auto_20210906_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='notebooks.category'),
        ),
    ]