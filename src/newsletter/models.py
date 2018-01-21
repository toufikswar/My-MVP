from django.db import models

# Create your models here.
class SignUp(models.Model):
    email = models.EmailField()
    # blank is a param for the form in the admin
    # null is for the DB
    full_name = models.CharField(max_length=120, blank=True, null=True)
    # auto_now_add : date is added on creation of object
    # aut_now : date updated on object's update
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.email
