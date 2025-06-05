def download_file(request, token):
    file_instance = get_object_or_404(FileVault, token=token)
    if file_instance.has_expired():
        return render(request, 'expired.html')

    file_instance.is_viewed = True
    file_instance.save()

    decrypted_data = decrypt_file(file_instance.encrypted_file.path)
    file_stream = io.BytesIO(decrypted_data)

    response = FileResponse(file_stream, as_attachment=True, filename=file_instance.encrypted_file.name[:-4])  # remove '.enc'
    return response
