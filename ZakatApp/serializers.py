from rest_framework import serializers
from ZakatApp.models import Pengguna, Penerima, Jadwal, Pembayaran


class PenggunaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pengguna
        fields = ('pengguna_id', 'peran', 'username', 'password', 'email', 'nama',
                  'nomor_hp', 'nomor_kk', 'alamat', 'jumlah_anggota_keluarga', 'foto')


class JadwalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jadwal
        fields = ('jadwal_id', 'tanggal_mulai_pembayaran', 'tanggal_akhir_pembayaran',
                  'tanggal_mulai_penyaluran', 'tanggal_akhir_penyaluran', 'harga_beras')


class PenerimaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Penerima
        fields = ('penerima_id', 'jadwal', 'nama', 'email',
                  'nomor_hp', 'nomor_kk', 'alamat', 'status')


class PembayaranSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pembayaran
        fields = ('pembayaran_id', 'pemberi', 'jadwal',
                  'tanggal', 'nominal', 'status')
