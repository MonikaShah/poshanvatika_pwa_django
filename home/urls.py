from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('accounts/', include('allauth.urls')),
    path('login/', views.login_request, name='login'),
    path('logout/',views.logout, name='logout'),
    path('register/', views.register_request, name='register'),
    path('myPoshan/', views.myPoshan, name='myPoshan'),
    path('news/', views.news, name='news'),
    path('howto/', views.howto, name='howto'),
    path('captvatikapic/', views.captvatikapic, name='captvatikapic'),
    path('uploadvatikapic/', views.uploadvatikapic, name='uploadvatikapic'),
    path('captwellpic/', views.captwellpic, name='captwellpic'),
    path('uploadwellpic/', views.uploadwellpic, name='uploadwellpic'),
    path('viewLayers/', views.viewLayers, name='viewLayers')




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

