from tkinter import Entry
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.files.storage import default_storage
from django.contrib.auth import logout
# from django.contrib.auth.decorators import login_required

from ZakatApp.models import Pengguna, Penerima, Jadwal, Pembayaran
from ZakatApp.serializers import PenggunaSerializers, PenerimaSerializers, JadwalSerializers, PembayaranSerializers



@csrf_exempt
def penggunaApi(request, id=0):
    if request.method == 'GET':
        penggunas = Pengguna.objects.all()
        pengguna_serializer = PenggunaSerializers(penggunas, many=True)
        return JsonResponse(pengguna_serializer.data, safe=False)
    elif request.method == 'POST':
        pengguna_data = JSONParser().parse(request)
        pengguna_serializer = PenggunaSerializers(data=pengguna_data)
        if pengguna_serializer.is_valid():
            pengguna_serializer.save()
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


def signup(request):
    if request.method == 'GET':
        # if request.user.is_authenticated :
        #     return redirect('pemberi/home.html')
        # else :
        #     return render(request, 'signup.html')
        return render(request, 'signup.html')
    elif request.method == 'POST':
        # if request.user.is_authenticated :
        #     return redirect('pemberi/home.html')
        # else :
        pemberi_data = {
            'peran': 1,
            'username': request.POST['username'],
            'password': request.POST['password'],
            'email': request.POST['email'],
            'nama': request.POST['nama'],
            'nomor_hp': request.POST['email'],
        }
        
        # Cek kesamaan password dengan konfirmasi password
        password = request.POST['password']
        konfirmasi_password = request.POST['konfirmasi']
        
        if password != konfirmasi_password :
            messages.error(request, "Konfirmasi password tidak cocok!")
            return redirect('/signup')
        
        # Cek pengguna trsbt dh ada apa blm di database
        # Kita cuma cek username nya aja krn cara kita login cuma ambil satu data dr database yg sesuai dgn username yg diinput untuk disamakan dgn password yg diinput
        try :
            pemberi = Pengguna.objects.get(username = pemberi_data['username'])
        except :
            pemberi = None
        
        if pemberi is not None :
            messages.error(request, "Pengguna sudah ada!")
            return redirect('/signup')
        
        pemberi_serializer = PenggunaSerializers(data = pemberi_data)
        
        if pemberi_serializer.is_valid() :
            pemberi_serializer.save()
            messages.success(request, "Pendaftaran berhasil!")
            return redirect('/login')

        messages.error(request, 'Gagal menambahkan pemberi baru!')
        return redirect('/login')
        # return JsonResponse("Gagal menambahkan pemberi baru!", safe=False)


def loginPengguna(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try :
            pengguna = Pengguna.objects.get(username = username, password = password)
        except Pengguna.DoesNotExist :
            pengguna = None
        
        # Perbaiki cara penanganan pengguna tidak ditemukan !
        if pengguna == None :
            messages.error(request, 'Pengguna tidak ditemukan!')
            return redirect('/signup')
        
        if pengguna.peran == 0 :
            return redirect('/operator/home')
        elif pengguna.peran == 1 :
            return redirect('/pemberi/home')
        
        
def logoutPengguna(request) :
    logout(request)
    return redirect('/login')


# @login_required(login_url='login')
def homeOperator(request):
    if request.method == 'GET':
        return render(request, 'operator/home.html')
    elif request.method == 'POST':
        jadwal_data = {
            "tanggal_mulai_pembayaran": request.POST['mulaibayar'],
            "tanggal_akhir_pembayaran": request.POST['akhirbayar'],
            "tanggal_mulai_penyaluran": request.POST['mulaipenyaluran'],
            "tanggal_akhir_penyaluran": request.POST['akhirpenyaluran'],
            "harga_beras": int(request.POST['hargaberas'])
        }
        
        jadwals_serializer = JadwalSerializers(data=jadwal_data)
    
        if jadwals_serializer.is_valid():
            jadwals_serializer.save()
            messages.success(request, "Berhasil mengubah jadwal!")
            return redirect('/operator/home')
        
        messages.error(request, "Gagal menambahkan jadwal!")
        return redirect('/operator/home')
        # return JsonResponse("Gagal menambahkan jadwal!", safe=False)


def pemberiOperator(request):
    return render(request, 'operator/pemberi.html')


def penerimaOperator(request):
    return render(request, 'operator/penerima.html')

def ubahStatusPemberi(request) :
    if request.method == 'POST' :
        id = request.POST['id']
        status = request.POST['status']
        
        Pembayaran.objects.filter(pemberi_id = id).update(status = status)
        
        # pemberi = Pembayaran.objects.get(pemberi_id = id)
        # pemberi.status = status
        # pemberi.save()

def ubahStatusPenerima(request) :
    if request.method == 'POST' :
        id = request.POST['id']
        status = request.POST['status']
        
        Penerima.objects.filter(penerima_id = id).update(status = status)


def homePemberi(request):
    return render(request, 'pemberi/home.html')


def profilePemberi(request):
    return render(request, 'pemberi/profile.html')


def historyPemberi(request):
    return render(request, 'pemberi/history.html')


def paymentPemberi(request):
    return render(request, 'pemberi/payment.html')


def paymethodPemberi(request):
    return render(request, 'pemberi/paymethod.html')


def scanqrPemberi(request):
    return render(request, 'pemberi/scanqr.html')
