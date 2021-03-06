# Generated by Django 4.0.4 on 2022-05-20 18:02

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
        migrations.AddField(
            model_name='pembayaran',
            name='alamat',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='pembayaran',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='pembayaran',
            name='jumlah_anggota_keluarga',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pembayaran',
            name='nama',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='pembayaran',
            name='nomor_hp',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='pembayaran',
            name='nomor_kk',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='pengguna',
            name='peran',
            field=models.IntegerField(choices=[(0, 'Operator'), (1, 'Pemberi')]),
        ),
    ]
