from django.urls import re_path
from ZakatApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^pengguna$', views.penggunaApi),
    re_path(r'^pengguna/([0-9]+)$', views.penggunaApi),

    re_path(r'^penerima$', views.penerimaApi),
    re_path(r'^penerima/([0-9]+)$', views.penerimaApi),

    re_path(r'^jadwal$', views.jadwalApi),
    re_path(r'^jadwal/([0-9]+)$', views.jadwalApi),

    re_path(r'^pembayaran$', views.pembayaranApi),
    re_path(r'^pembayaran/([0-9]+)$', views.pembayaranApi),

    re_path(r'^pemberi/savefile', views.saveFile),

    re_path(r'^login', views.loginPengguna, name='login'),
    re_path(r'^logout', views.logoutPengguna, name='logout'),
    re_path(r'^signup', views.signup),

    re_path(r'^operator/home', views.homeOperator),
    re_path(r'^operator/pemberi', views.pemberiOperator),
    # re_path(r'^ubahStatus', views.ubahStatusPemberi),
    re_path(r'^operator/pemberi/ubahStatus', views.ubahStatusPemberi),
    re_path(r'^operator/penerima', views.penerimaOperator),
    re_path(r'^operator/penerima/ubahStatus', views.ubahStatusPenerima),

    re_path(r'^pemberi/home', views.homePemberi),
    re_path(r'^pemberi/profile', views.profilePemberi),
    re_path(r'^pemberi/history', views.historyPemberi),
    re_path(r'^pemberi/payment', views.paymentPemberi),
    re_path(r'^pemberi/paymethod', views.paymethodPemberi),
    re_path(r'^pemberi/scanqr', views.scanqrPemberi),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
