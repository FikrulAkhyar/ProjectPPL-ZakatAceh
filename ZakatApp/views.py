from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.shortcuts import redirect, render

from ZakatApp.models import Pengguna, Penerima, Jadwal, Pembayaran
from ZakatApp.serializers import PenggunaSerializers, PenerimaSerializers, JadwalSerializers, PembayaranSerializers

from django.core.files.storage import default_storage

from datetime import datetime


@csrf_exempt
def penggunaApi(request, id=0):
    if request.method == 'GET':
        penggunas = Pengguna.objects.all()
        penggunas_serializer = PenggunaSerializers(penggunas, many=True)
        return JsonResponse(penggunas_serializer.data, safe=False)
    elif request.method == 'POST':
        pengguna_data = JSONParser().parse(request)
        penggunas_serializer = PenggunaSerializers(data=pengguna_data)
        if penggunas_serializer.is_valid():
            penggunas_serializer.save()
            return JsonResponse("Berhasil mendaftar!", safe=False)
        return JsonResponse("Gagal menambahkan data!", safe=False)
    elif request.method == 'PUT':
        pengguna_data = JSONParser().parse(request)
        pengguna = Pengguna.objects.get(
            pengguna_id=pengguna_data['pengguna_id'])
        pengguna_serializer = PenggunaSerializers(pengguna, data=pengguna_data)
        if pengguna_serializer.is_valid():
            pengguna_serializer.save()
            return JsonResponse("Berhasil memperbarui data!", safe=False)
        return JsonResponse("Gagal memperbarui data!", safe=False)
    elif request.method == 'DELETE':
        pengguna = Pengguna.objects.get(pengguna_id=id)
        pengguna.delete()
        return JsonResponse("Berhasil menghapus data!", safe=False)
    return JsonResponse("Gagal menghapus data!", safe=False)


@csrf_exempt
def penerimaApi(request, id=0):
    if request.method == 'GET':
        penerimas = Penerima.objects.all()
        penerimas_serializer = PenerimaSerializers(penerimas, many=True)
        return JsonResponse(penerimas_serializer.data, safe=False)
    elif request.method == 'POST':
        penerima_data = JSONParser().parse(request)
        penerimas_serializer = PenerimaSerializers(data=penerima_data)
        if penerimas_serializer.is_valid():
            penerimas_serializer.save()
            return JsonResponse("Data berhasil ditambahkan!", safe=False)
        return JsonResponse("Gagal menambahkan data!", safe=False)
    elif request.method == 'PUT':
        penerima_data = JSONParser().parse(request)
        penerima = Penerima.objects.get(
            penerima_id=penerima_data['penerima_id'])
        penerima_serializer = PenerimaSerializers(penerima, data=penerima_data)
        if penerima_serializer.is_valid():
            penerima_serializer.save()
            return JsonResponse("Berhasil memperbarui data!", safe=False)
        return JsonResponse("Gagal memperbarui data!", safe=False)
    elif request.method == 'DELETE':
        penerima = Penerima.objects.get(penerima_id=id)
        penerima.delete()
        return JsonResponse("Berhasil menghapus data!", safe=False)
    return JsonResponse("Gagal menghapus data!", safe=False)


@csrf_exempt
def jadwalApi(request, id=0):
    if request.method == 'GET':
        jadwals = Jadwal.objects.all()
        jadwals_serializer = JadwalSerializers(jadwals, many=True)
        return JsonResponse(jadwals_serializer.data, safe=False)
    elif request.method == 'POST':
        jadwal_data = JSONParser().parse(request)
        jadwals_serializer = JadwalSerializers(data=jadwal_data)
        if jadwals_serializer.is_valid():
            jadwals_serializer.save()
            return JsonResponse("Data berhasil ditambahkan!", safe=False)
        return JsonResponse("Gagal menambahkan data!", safe=False)
    elif request.method == 'PUT':
        jadwal_data = JSONParser().parse(request)
        jadwal = Jadwal.objects.get(jadwal_id=jadwal_data['jadwal_id'])
        jadwal_serializer = JadwalSerializers(jadwal, data=jadwal_data)
        if jadwal_serializer.is_valid():
            jadwal_serializer.save()
            return JsonResponse("Berhasil memperbarui data!", safe=False)
        return JsonResponse("Gagal memperbarui data!", safe=False)
    elif request.method == 'DELETE':
        jadwal = Jadwal.objects.get(jadwal_id=id)
        jadwal.delete()
        return JsonResponse("Berhasil menghapus data!", safe=False)
    return JsonResponse("Gagal menghapus data!", safe=False)


@csrf_exempt
def pembayaranApi(request, id=0):
    if request.method == 'GET':
        pembayarans = Pembayaran.objects.all()
        pembayarans_serializer = PembayaranSerializers(pembayarans, many=True)
        return JsonResponse(pembayarans_serializer.data, safe=False)
    elif request.method == 'POST':
        pembayaran_data = JSONParser().parse(request)
        pembayarans_serializer = PembayaranSerializers(data=pembayaran_data)
        if pembayarans_serializer.is_valid():
            pembayarans_serializer.save()
            return JsonResponse("Data berhasil ditambahkan!", safe=False)
        return JsonResponse("Gagal menambahkan data!", safe=False)
    elif request.method == 'PUT':
        pembayaran_data = JSONParser().parse(request)
        pembayaran = Pembayaran.objects.get(
            pembayaran_id=pembayaran_data['pembayaran_id'])
        pembayaran_serializer = PembayaranSerializers(
            pembayaran, data=pembayaran_data)
        if pembayaran_serializer.is_valid():
            pembayaran_serializer.save()
            return JsonResponse("Berhasil memperbarui data!", safe=False)
        return JsonResponse("Gagal memperbarui data!", safe=False)
    elif request.method == 'DELETE':
        pembayaran = Pembayaran.objects.get(pembayaran_id=id)
        pembayaran.delete()
        return JsonResponse("Berhasil menghapus data!", safe=False)
    return JsonResponse("Gagal menghapus data!", safe=False)


@csrf_exempt
def saveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def homeAdmin(request):
    if request.method == 'GET':
        return render(request, 'admin/home.html')
    if request.method == 'POST':
        jadwal_data = {
            "tanggal_mulai_pembayaran": request.POST['mulaibayar'],
            "tanggal_akhir_pembayaran": request.POST['akhirbayar'],
            "tanggal_mulai_penyaluran": request.POST['mulaipenyaluran'],
            "tanggal_akhir_penyaluran": request.POST['akhirpenyaluran'],
            "harga_beras": int(request.POST['hargaberas'])
        }
        
        jadwals_serializer = JadwalSerializers(data=jadwal_data)
        
        # return JsonResponse(jadwal_data, safe=False)
    
        if jadwals_serializer.is_valid():
            jadwals_serializer.save()
            message = "Berhasil mengubah jadwal!"
            return redirect('/operator/home', message)
        return JsonResponse("Gagal menambahkan jadwal!", safe=False)


def pemberiAdmin(request):
    return render(request, 'admin/pemberi.html')


def penerimaAdmin(request):
    return render(request, 'admin/penerima.html')


def homeUser(request):
    return render(request, 'user/home.html')


def profileUser(request):
    return render(request, 'user/profile.html')


def historyUser(request):
    return render(request, 'user/history.html')


def paymentUser(request):
    return render(request, 'user/payment.html')


def paymethodUser(request):
    return render(request, 'user/paymethod.html')


def scanqrUser(request):
    return render(request, 'user/scanqr.html')
