"""dressdummy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from fabric.views import *
from patterns.views import *
from users.views import *
from stash.views import *


router = DefaultRouter()
router.register(r'pattern/companies', PatternCompanyViewSet)
router.register(r'pattern/collections', PatternCollectionViewSet)
router.register(r'pattern/designers', PatternDesignerViewSet)
router.register(r'pattern/types', PatternTypeViewSet)
router.register(r'patterns', PatternViewSet)
router.register(r'patterns/sizes', PatternSizeViewSet)
router.register(r'pattern/measurements', PatternFinishedMeasurementViewSet)
router.register(r'fabric/types', FabricTypeViewSet)
router.register(r'fabric/uses', RecommendedUsesViewSet)
router.register(r'fabric/elements', DesignElementsViewSet)
router.register(r'fabric/colors', ColorFamilyViewSet)
router.register(r'fabric/brands', FabricBrandViewSet)
router.register(r'fabric/collection', FabricCollectionViewSet)
router.register(r'fabric/designers', DesignerViewSet)
router.register(r'fabric', FabricViewSet)
router.register(r'users', UserViewSet)
router.register(r'stash/fabric', FabricStashViewSet)
router.register(r'stash/pattern', PatternStashViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path(r'^', TemplateView.as_view(template_name="index.html")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
