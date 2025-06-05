def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['encrypted_file']
            encrypted_data = encrypt_file(uploaded_file)

            file_instance = form.save(commit=False)
            file_instance.expires_at = timezone.now() + timezone.timedelta(hours=24)

            encrypted_filename = uploaded_file.name + '.enc'
            file_instance.encrypted_file.save(encrypted_filename, ContentFile(encrypted_data))
            file_instance.save()

            return render(request, 'successs_upload.html', {'token': file_instance.token})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
