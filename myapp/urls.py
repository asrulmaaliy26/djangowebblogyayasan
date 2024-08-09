from django.urls import path
from .views import (
    index,
    contact_view,
    beritadetail,
    berita,
    pendidikan_ma,
    pendidikan_smp,
    pendidikan_mahad,
    pendidikan_tpq,
    pendidikan_kampus,
    profil,
    struktur_organisasi,
    akreditasi,
    prestasi,
    helpdesk,
    ppdb,
    profillpi
)

urlpatterns = [
    path('', index, name="index"),
    path('index/', index, name="index"),
    path('faqs/', contact_view, name='faqs'),
    path('berita/<int:id>', beritadetail, name="beritadetail"),
    path('berita/', berita, name="berita"),
    path("pendidikan_ma/", pendidikan_ma, name="pendidikan_ma"),
    path("pendidikan_smp/", pendidikan_smp, name="pendidikan_smp"),
    path("pendidikan_mahad/", pendidikan_mahad, name="pendidikan_mahad"),
    path("pendidikan_tpq/", pendidikan_tpq, name="pendidikan_tpq"),
    path("pendidikan_kampus/", pendidikan_kampus, name="pendidikan_kampus"),
    path('profil/', profil, name='profil'),
    path('profillpi/', profillpi, name='profillpi'),
    path('struktur_organisasi/', struktur_organisasi, name='struktur_organisasi'),
    path('akreditasi/', akreditasi, name='akreditasi'),
    path('prestasi/', prestasi, name='prestasi'),
    path('helpdesk/', helpdesk, name='helpdesk'),
    path('ppdb/', ppdb, name='ppdb'),
]
