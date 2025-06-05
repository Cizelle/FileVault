from django.db import models
from django.utils import timezone
import uuid

def upload_to(instance, filename):
    return f'encrypted_files/{instance.token}/{filename}'

class FileVault(models.Model):
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    encrypted_file = models.FileField(upload_to=upload_to)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_viewed = models.BooleanField(default=False)

    def has_expired(self):
        return timezone.now() > self.expires_at or self.is_viewed
