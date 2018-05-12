from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogUploadForm

def index(request):
    blog_list = Blog.objects.filter(is_published=True)
    context = {
        'blog_list': blog_list
    }
    return render(request, 'blog/index.html', context)

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    context = {
        'blog': blog
    }
    return render(request, 'blog/detail.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = BlogUploadForm(request.POST, request.FILES)

        if form.is_valid():
            blog = form.save(commit=False)
            blog.user=request.user
            blog.save()
            # title = form.cleaned_data['title']
            # content = form.cleaned_data['content']
            # thumbnail = form.cleaned_data['thumbnail']
            #
            # Blog.objects.create(
            #     title=title,
            #     content=content,
            #     thumbnail=thumbnail,
            #     is_published=True,
            # )
            return redirect('blog:list')
        else:
            return render(request, 'blog/create.html', {
                'form': form
            })
    else:
        form = BlogUploadForm()
        return render(request, 'blog/create.html',{
            'form': form
        })


def delete(request):
    if request.method == 'POST':
        blog_pk = request.POST.get('blog_pk','')
        blog = Blog.object.get(pk=blog_pk)
        if blog.user== request.user:
            blog.delete()
        return redirect('blog:list')
    else:
        return redirect('blog:list')

