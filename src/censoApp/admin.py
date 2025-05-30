from django.contrib import admin

from censoApp.models import (
    Domicilio,
    Morador,
    Rendimento,
    Mortalidade,
    PrestadorInformacao,
    RegistroCivil,
    Contato,
)

admin.site.register(Domicilio)
admin.site.register(Morador)
admin.site.register(Rendimento)
admin.site.register(Mortalidade)
admin.site.register(PrestadorInformacao)
admin.site.register(RegistroCivil)
admin.site.register(Contato)
