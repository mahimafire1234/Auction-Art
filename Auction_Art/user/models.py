from django.db import models

# Create your models here.
class USER(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    Email = models.EmailField()
    Password = models.CharField(max_length=300)

    class Meta:
        db_table = "tableuser"