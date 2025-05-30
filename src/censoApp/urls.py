from django.urls import path, include
from rest_framework.routers import DefaultRouter
from censoApp.views import DomicilioViewSet, MoradorViewSet, FalecimentoViewSet, ReligiaoViewSet, InformanteCivilViewSet, ContatoViewSet, TrabalhoViewSet, DeslocamentoViewSet, RuaViewSet

router = DefaultRouter()
router.register(r'domicilios', DomicilioViewSet)
router.register(r'moradores', MoradorViewSet)
router.register(r'falecimentos', FalecimentoViewSet)
router.register(r'religioes', ReligiaoViewSet)
router.register(r'informantes', InformanteCivilViewSet)
router.register(r'contatos', ContatoViewSet)
router.register(r'trabalhos', TrabalhoViewSet)
router.register(r'deslocamentos', DeslocamentoViewSet)
router.register(r'ruas', RuaViewSet)



urlpatterns = [
    path('api/', include(router.urls)),
]
