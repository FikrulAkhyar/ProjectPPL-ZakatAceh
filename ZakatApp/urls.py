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

    re_path(r'^pengguna/savefile', views.saveFile),

    re_path(r'^login', views.login),
    re_path(r'^signup', views.signup),

    re_path(r'^~/home', views.homeAdmin),
    re_path(r'^~/pemberi', views.pemberiAdmin),
    re_path(r'^~/penerima', views.penerimaAdmin),

    re_path(r'^user/home', views.homeUser),
    re_path(r'^user/profile', views.profileUser),
    re_path(r'^user/history', views.historyUser),
    re_path(r'^user/payment', views.paymentUser),
    re_path(r'^user/paymethod', views.paymethodUser),
    re_path(r'^user/scanqr', views.scanqrUser),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
