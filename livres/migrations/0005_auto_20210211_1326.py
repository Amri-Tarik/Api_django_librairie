# Generated by Django 3.1.5 on 2021-02-11 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livres', '0004_auto_20210210_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livre',
            name='auteur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='livres', to='livres.auteur'),
        ),
    ]