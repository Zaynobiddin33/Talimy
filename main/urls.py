from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('blogs/', views.blogs, name='blogs'),
    path('blog-detail/<int:id>', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    path('approve-request/', views.approve_request, name='approve_request'),
    path('register/', views.register, name='register')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)