# Generated by Django 3.2.4 on 2022-05-19 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZakatApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pembayaran',
            old_name='jadwal_id',
            new_name='jadwal',
        ),
        migrations.RenameField(
            model_name='pembayaran',
            old_name='pemberi_id',
            new_name='pemberi',
        ),
        migrations.RenameField(
            model_name='penerima',
            old_name='jadwal_id',
            new_name='jadwal',
        ),
        migrations.RemoveField(
            model_name='pengguna',
            name='status',
        ),
        migrations.AlterField(
            model_name='pengguna',
            name='peran',
            field=models.IntegerField(choices=[(0, 'Operator'), (1, 'Pemberi')]),
        ),
    ]