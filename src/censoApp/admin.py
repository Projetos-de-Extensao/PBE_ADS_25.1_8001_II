from django.contrib import admin

from censoApp.models import (
    Deslocamento,
    Trabalho,
    Falecimento,
    Morador,
    Domicilio,
    Contato,
    Informante,
    Religiao,
    Rua,
)

admin.site.register(Deslocamento)
admin.site.register(Trabalho)
admin.site.register(Falecimento)
admin.site.register(Morador)
admin.site.register(Domicilio)
admin.site.register(Contato)
admin.site.register(Informante)
admin.site.register(Religiao)
admin.site.register(Rua)

