from django.urls import path, include
from rest_framework.routers import DefaultRouter
from censoApp.views import DomicilioViewSet, MoradorViewSet, RendimentoViewSet, MortalidadeViewSet, PrestadorInformacaoViewSet, RegistroCivilViewSet, ContatoViewSet

router = DefaultRouter()
router.register(r'domicilios', DomicilioViewSet)
router.register(r'moradores', MoradorViewSet)
router.register(r'rendimentos', RendimentoViewSet)
router.register(r'mortalidades', MortalidadeViewSet)
router.register(r'prestadores', PrestadorInformacaoViewSet)
router.register(r'registros', RegistroCivilViewSet)
router.register(r'contatos', ContatoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
