from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from censoApp.views import DomicilioViewSet, MoradorViewSet, FalecimentoViewSet, ReligiaoViewSet, InformanteCivilViewSet, ContatoViewSet, TrabalhoViewSet, DeslocamentoViewSet, RuaViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
       openapi.Info(
           title="API de Conteúdos do Censo",
           default_version='v1',
           description="Documentação da API de Conteúdos do Censo",
           terms_of_service="https://www.google.com/policies/terms/",
           contact=openapi.Contact(email="suporte@exemplo.com"),
           license=openapi.License(name="Licença BSD"),
       ),
       public=True,
       permission_classes=(permissions.AllowAny,),
   )

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
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
 
]
