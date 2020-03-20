from rest_framework import routers
from fecoval.avaluos.viewsets import ClienteViewSet, AvaluoViewSet, EstadoViewSet, ADRViewSet, BienViewSet

router = routers.DefaultRouter()

router.register(r'cliente', ClienteViewSet)
router.register(r'avaluo', AvaluoViewSet)
router.register(r'estado', EstadoViewSet)
router.register(r'bien', BienViewSet)
router.register(r'adr', ADRViewSet)
