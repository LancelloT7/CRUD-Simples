from django.db import models
from django.utils.html import mark_safe

# Create your models here.




class Produto(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    img = models.ImageField(upload_to='img')

    def __str__(self):
        return f'{self.nome}'
   
    @mark_safe
    def icone(self):
        if self.img:
            return mark_safe(f'<img width="30px" src="/media/{self.img.url}" alt="{self.nome}">')
        return "Sem imagem"  
