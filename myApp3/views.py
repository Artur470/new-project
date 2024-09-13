from django.shortcuts import render, redirect,  HttpResponse, get_object_or_404
from .models import Blog, Area, Comment
from .forms import CreateBlogForm, UpdateBlog, CreateComment

# Create your views h
def vun3(request):
    return render(request, "vun3.html")


def blogList(request):
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs
    }
    return render (request, 'blogs.html', context)


def createBlog(request):

    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        Blog.objects.create(

            title=title,
            body=body

        )
        return redirect('http://127.0.0.1:8000/home3/blog/')

    form = CreateBlogForm()
    context = {

        "form": form
    }
    return render(request, "blog_form.html", context)

def update_blog_view(request, id):

   blog = Blog.objects.get(pk=id)

   if request.method =="POST":
        blog = UpdateBlog(request.POST, instance=blog)
        if blog.is_valid():
            blog.save()
            return redirect("http://127.0.0.1:8000/home3/blog/")
        return HttpResponse('error')
   UpdateBlogForm = UpdateBlog(instance=blog)
   context = {

       'UpdateBlogForm': UpdateBlogForm

   }
   return render(request, "update_blog.html", context)


def deleteBlogview(request,  id):
    blog = Blog.objects.get(pk=id)
    blog.delete()
    return redirect("http://127.0.0.1:8000/home3/blog/")



def area_show(request):
    areas = Area.objects.all()
    context = {
        'areas': areas


    }
    return render(request, "area.html", context)


def blog_comment(request, id):

    if request.method == "POST":
        author = request.POST['author']
        body = request.POST['body']
        blog = Blog.objects.get(id=id)
        Comment.objects.create(

            blog=blog,
            author=author,
            body=body
        )
    blog = Blog.objects.get(id=id)
    comments = Comment.objects.filter(blog=blog)
    form = CreateComment()
    context = {
        "id": id,
        "comments": comments,
        "form": form

    }
    return render(request, "comment.html", context)

def create_comment(request, id):
    form = CreateComment()
    context = {
        'form': form


    }
    return render (request, "create_comment.html", context)