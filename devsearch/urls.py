from django.contrib import admin
from django.urls import path, include

def projects(request):
    return HttpResponse('Here are our products')

def project(request, pk):
    return HttpResponse('SINGLE PROJECT' + ' ' + str(pk))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
]
