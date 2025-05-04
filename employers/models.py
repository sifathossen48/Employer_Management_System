from accounts.models import User
from django.db import models
# Create your models here.

class Employer(models.Model):
    user = models.ForeignKey(User, related_name="employers", on_delete=models.CASCADE)
    company_name = models.CharField(max_length=60)
    contact_person_name = models.CharField(max_length=40)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact_person_name + " - " + self.company_name