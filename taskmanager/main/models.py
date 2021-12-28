from django.db import models

# Create your models here.
class Quiz(models.Model):
    name = models.CharField("имя пользователя" , max_length=30)
    feedback = models.TextField("отзыв")

    def __str__(self):
        return self.name