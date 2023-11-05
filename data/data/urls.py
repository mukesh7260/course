
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('course/',views.get,name="course"),
    path('create/',views.create , name="create"),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)