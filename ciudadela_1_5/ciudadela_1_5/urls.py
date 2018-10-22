"""
Definition of urls for ciudadela_1_5.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.inicio, name='inicio'),
    url(r'^nosotros$', app.views.nosotros, name='nosotros'),
    url(r'^proyectos$', app.views.proyectos, name='proyectos'),
    url(r'^eventos$', app.views.eventos, name='eventos'),
    url(r'^actividades$', app.views.actividades, name='actividades'),
    url(r'^cuentas$', app.views.cuentas, name='cuentas'),
    url(r'^estadisticas$', app.views.estadisticas, name='estadisticas'),
    url(r'^camaras$', app.views.about, name='camaras'),
    url(r'^quejas$', app.views.about, name='quejas'),
    url(r'^nosotros$', app.views.about, name='nosotros'),
    url(r'^contactenos$', app.views.contact, name='contactenos'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
