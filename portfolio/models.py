from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    habilidades = models.TextField(max_length=350)
    image = models.ImageField(blank=True)
    
    
    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        
        
    def __str__(self):
        return self.title
    
class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    
    
    class Meta:
        verbose_name = 'Imagens dos projetos'
        verbose_name_plural = 'Imagens dos projetos'
    
    
    def __str__(self):
        return self.post.title
    
