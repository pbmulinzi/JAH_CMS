# Generated by Django 5.1.1 on 2024-11-27 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jah_Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Quantity',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Flour', 'Flour'), ('Honey', 'Honey'), ('Spice', 'Spice')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
