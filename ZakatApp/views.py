from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.files.storage import default_storage
from django.contrib.auth import logout

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
        return render(request, 'signup.html')
    elif request.method == 'POST':
        pemberi_data = {
            'peran': 1,
            'username': request.POST['username'],
            'password': request.POST['password'],
            'email': request.POST['email'],
            'nama': request.POST['nama'],
            'nomor_hp': request.POST['email'],
        }
        
        password = request.POST['password']
        konfirmasi_password = request.POST['konfirmasi']
        
        if password != konfirmasi_password :
            messages.error(request, "Konfirmasi password tidak cocok!")
            return redirect('/signup')
        
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
    
        # Cara debugging tanpa tampilin halaman
        # return JsonResponse("Gagal menambahkan pemberi baru!", safe=False)
        # return JsonResponse(pemberi_data, safe=False)


def loginPengguna(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try :
            pengguna = Pengguna.objects.get(username = username, password = password)
        except Pengguna.DoesNotExist :
            messages.error(request, 'Pengguna tidak ditemukan!')
            return redirect('/login')
        
        request.session['pengguna_id'] = pengguna.pengguna_id
        request.session['peran_pengguna'] = pengguna.peran
        
        if pengguna.peran == 0 :
            return redirect('/operator/home')
        elif pengguna.peran == 1 :
            return redirect('/pemberi/home')
        
        
def logoutPengguna(request) :
    logout(request)
    return redirect('/login')


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


def pemberiOperator(request):
    data = Pembayaran.objects.filter()
    return render(request, 'operator/pemberi.html', {'data' : data})


def penerimaOperator(request):
    return render(request, 'operator/penerima.html')


def ubahStatusPemberi(request) :
    if request.method == 'POST' :
        id = request.POST['id']
        status = request.POST['status']
        
        Pembayaran.objects.filter(pemberi_id = id).update(status = status)
        

def ubahStatusPenerima(request) :
    if request.method == 'POST' :
        id = request.POST['id']
        status = request.POST['status']
        
        Penerima.objects.filter(penerima_id = id).update(status = status)


def homePemberi(request):
    jadwal = Jadwal.objects.latest('jadwal_id')
    mulai_pembayaran = jadwal.tanggal_mulai_pembayaran.strftime("%d/%m/%Y")
    akhir_pembayaran = jadwal.tanggal_akhir_pembayaran.strftime("%d/%m/%Y")
    harga_beras = jadwal.harga_beras
    
    return render(request, 'pemberi/home.html', {'mulai_pembayaran' : mulai_pembayaran, 'akhir_pembayaran' : akhir_pembayaran, 'harga_beras': harga_beras})
 

def profilePemberi(request):
    pengguna_id = request.session['pengguna_id']
    data = Pengguna.objects.filter(pengguna_id = pengguna_id)
    return render(request, 'pemberi/profile.html', {'data' : data})


def ubahProfile(request):
    if request.method == 'POST' :
        email = request.POST['email']
        nohp = request.POST['nohp']
        nokk = request.POST['nokk']
        alamat = request.POST['alamat']
        pengguna_id = request.session['pengguna_id']
        
        Pengguna.objects.filter(pengguna_id = pengguna_id).update(email = email, nomor_hp = nohp, nomor_kk = nokk, alamat = alamat)
        
        return redirect('/pemberi/profile')


def historyPemberi(request):
    del request.session['nominal']
    
    pengguna_id = request.session['pengguna_id']
    try :
        data = Pembayaran.objects.filter(pemberi_id = pengguna_id)
        
        for d in data :
            if d.status == 0 :
                d.status = 'Gagal'
            elif d.status == 1 :
                d.status = 'Menunggu'
            elif d.status == 2 :
                d.status = 'Diterima'

            d.tanggal = d.tanggal.strftime("%d - %m - %Y, %H:%M:%S")
        
        return render(request, 'pemberi/history.html', {'data' : data})
    except :
        render(request, 'pemberi/history.html')


def paymentPemberi(request):
    if request.method == 'GET' :
        return render(request, 'pemberi/payment.html')
    elif request.method == 'POST' :
        jumlah_pemberi_zakat = request.POST['jumlah']
        
        if jumlah_pemberi_zakat == '' :
            messages.error(request, "Harap isi jumlah pemberi zakat!")
            return redirect('/pemberi/payment')
        
        nominal = int(2.5 * 14000 * int(jumlah_pemberi_zakat))
        
        request.session['nominal'] = nominal
        
        return redirect('/pemberi/paymethod')


def paymethodPemberi(request):
    if request.method == 'GET' :
        nominal = request.session['nominal']
        
        return render(request, 'pemberi/paymethod.html', {'nominal': nominal})
    elif request.method == 'POST' :
        pengguna_id = request.session['pengguna_id']
        jadwal_id = Jadwal.objects.latest('jadwal_id').jadwal_id
        nominal = request.POST['nominal']
        status = 1
        metode = request.POST['paymentmethod']
        
        pemberi_data = {
            'pemberi_id': pengguna_id,
            'jadwal_id': jadwal_id,
            'nominal': nominal,
            'status': status
        }
        
        pembayaran_serializer = PembayaranSerializers(data = pemberi_data)
        
        if pembayaran_serializer.is_valid() :
            pembayaran_serializer.save()
        
            return render(request, 'pemberi/scanqr.html', {'metode': metode, 'nominal': nominal})

        messages.error(request, "Gagal melanjutkan pembayaran!")
        return redirect('/pemberi/paymethod')


def scanqrPemberi(request):
    try :
        pengguna_id = request.session['pengguna_id']
        pembayaran = Pembayaran.objects.filter(pemberi_id = pengguna_id, jadwal_id = Jadwal.objects.latest('jadwal_id'))
        
        for p in pembayaran :
            nominal = p.nominal
        
        return render(request, 'pemberi/scanqr.html', {'nominal' : nominal})
    except :
        return render(request, 'pemberi/scanqr.html', {'nominal' : 0})

