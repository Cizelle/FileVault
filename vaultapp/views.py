from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse, Http404
from .models import FileVault
from .forms import UploadFileForm
from cryptography.fernet import Fernet
from django.conf import settings
import tempfile


fernet = Fernet(settings.FERNET_KEY)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.expires_at = timezone.now() + timezone.timedelta(hours=24)
            file_instance.save()
            return render(request, 'upload_success.html', {'token': file_instance.token})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def download_file(request, token):
    file_instance = get_object_or_404(FileVault, token=token)
    if file_instance.has_expired():
        return render(request, 'expired.html')

    file_instance.is_viewed = True
    file_instance.save()
    response = HttpResponse(file_instance.encrypted_file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{file_instance.encrypted_file.name.split("/")[-1]}"'
    return response

def encrypt_file(file_obj):
    data = file_obj.read()
    encrypted = fernet.encrypt(data)
    return encrypted

def decrypt_file(file_path):
    with open(file_path, 'rb') as f:
        encrypted = f.read()
    decrypted = fernet.decrypt(encrypted)
    return decrypted