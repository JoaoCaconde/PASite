from django.shortcuts import render
from .models import Post,PostImage
from django.shortcuts import get_object_or_404


def post_list(request):
    posts = Post.objects.all()
    context = {
        "projects": posts
    }
    return render(request, 'portfolio/post_list.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    photos = PostImage.objects.filter(post=post)
    project = Post.objects.get(pk=pk)
    return render(request, 'portfolio/post_detail.html', {'post': post, 'photos': photos, 'project': project})

def sobreMim(request):
    return render(request, 'portfolio/sobreMim.html')

def contato(request):
    return render(request, 'portfolio/contato.html')

def habilidades(request):  
    return render(request, 'portfolio/habilidades.html')

