from django.db import models

class Peran(models.IntegerChoices):
    OPERATOR = 0
    PEMBERI = 1


class Status(models.IntegerChoices):
    GAGAL = 0
    MENUNGGU = 1
    DITERIMA = 2


class Pengguna(models.Model):
    pengguna_id = models.AutoField(primary_key=True)
    peran = models.IntegerField(choices=Peran.choices)
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    email = models.EmailField(max_length=254, null=True)
    nama = models.CharField(max_length=500, null=True)
    nomor_hp = models.CharField(max_length=500, null=True)
    nomor_kk = models.CharField(max_length=500, null=True)
    alamat = models.CharField(max_length=500, null=True)
    jumlah_anggota_keluarga = models.IntegerField(null=True)
    foto = models.CharField(max_length=500, null=True)


class Jadwal(models.Model):
    jadwal_id = models.AutoField(primary_key=True)
    tanggal_mulai_pembayaran = models.DateField()
    tanggal_akhir_pembayaran = models.DateField()
    tanggal_mulai_penyaluran = models.DateField()
    tanggal_akhir_penyaluran = models.DateField()
    harga_beras = models.IntegerField()


class Penerima(models.Model):
    penerima_id = models.AutoField(primary_key=True)
    jadwal = models.ForeignKey(Jadwal, on_delete=models.CASCADE)
    nama = models.CharField(max_length=500)
    email = models.EmailField(max_length=254)
    nomor_hp = models.CharField(max_length=500)
    nomor_kk = models.CharField(max_length=500)
    alamat = models.CharField(max_length=500)
    status = models.IntegerField(choices=Status.choices)


class Pembayaran(models.Model):
    pembayaran_id = models.AutoField(primary_key=True)
    pemberi = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
    jadwal = models.ForeignKey(Jadwal, on_delete=models.DO_NOTHING)
    tanggal = models.DateTimeField(auto_now_add=True)
    nominal = models.IntegerField()
    status = models.IntegerField(choices=Status.choices)
