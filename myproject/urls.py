"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path

#vistas que nos van a permitir optener la autenticacion del usuario
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

from rest_framework import permissions

#importando el yasg
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from app1 import views as app

schema_view = get_schema_view(
    openapi.Info(
        title = "project django",
        default_version = "v1",
        description = "proyecto de prueba",
        terms_of_service ="https://www.google.com/policies/terms/",
        contact = openapi.Contact(email = "contact@snippets.local"),
        license = openapi.License(name = "BSD License")
    ),
    public = True,
    permission_classes = (permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<str:name>', app.hello),
   # path('class/view/', app.ClaseUnoAPIView.as_view()),

   #-- urls apiview
    path('person/', app.PersonListAPIView.as_view()),
    path('person/create/', app.PersonCreateAPIView.as_view()),
    path('person/<int:pk>/', app.PersonRetrieveUpdateDeleteAPIView.as_view()),

    #-- urls viewset
    path('list/', app.PersonViewSet.as_view({'get':'list'})),
    path('create/', app.PersonViewSet.as_view({'post':'create'})),
    path('<int:pk>/', app.PersonViewSet.as_view({'get':'retrieve', 'put':'partial_update', 'delate':'destroy'})),

    #--JWT
    path('login/', obtain_jwt_token),
    path('refresh/', refresh_jwt_token),
    path('verify/', verify_jwt_token),

    #--YASG
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]       

