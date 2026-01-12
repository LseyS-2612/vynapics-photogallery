from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from photos import views as photo_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', photo_views.gallery, name='gallery'),
    path('add/', photo_views.add_photo, name='add'),
    path('profile/', photo_views.profile, name='profile'),
    path('signup/', photo_views.signup_view, name='signup'),
    
    # Django'nun hazır Login/Logout sistemi
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='gallery'), name='logout'),
    
    path('delete/<int:pk>/', photo_views.delete_photo, name='delete_photo'),
    path('edit/<int:pk>/', photo_views.edit_photo, name='edit_photo'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)