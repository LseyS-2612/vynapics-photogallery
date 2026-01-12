from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Photo
from .forms import PhotoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# 1. Ana Galeri Görünümü
def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all().order_by('-created_at')
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    
    hero_photos = Photo.objects.all().order_by('-created_at')[:5]
    # --------------------------

    # hero_photos'u context'e ekle
    context = {
        'categories': categories,
        'photos': photos,
        'hero_photos': hero_photos, # <-- BURAYA EKLEDİK
    }
    return render(request, 'gallery.html', context)
    context = {'categories': categories, 'photos': photos}
    return render(request, 'gallery.html', context)

# 2. Tek Fotoğraf Görünümü (İsteğe bağlı, şu an Lightbox kullanıyoruz)
def view_photo(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photo.html', {'photo': photo})

# 3. Fotoğraf Yükleme
@login_required(login_url='login')
def add_photo(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            return redirect('gallery')
    else:
        form = PhotoForm()
    return render(request, 'add.html', {'form': form, 'categories': categories})

# 4. Profil Sayfası
@login_required(login_url='login')
def profile(request):
    photos = Photo.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'profile.html', {'photos': photos})

# 5. Kayıt Olma
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('gallery')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# 6. Fotoğraf Silme (BURASI EKSİKTİ)
@login_required(login_url='login')
def delete_photo(request, pk):
    photo = get_object_or_404(Photo, id=pk)
    if request.user == photo.user:
        photo.delete()
    return redirect('profile')

# 7. Fotoğraf Düzenleme
@login_required(login_url='login')
def edit_photo(request, pk):
    photo = get_object_or_404(Photo, id=pk)

    if request.user != photo.user:
        return redirect('profile')

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PhotoForm(instance=photo)

    return render(request, 'edit_photo.html', {'form': form})