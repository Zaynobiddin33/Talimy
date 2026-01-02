from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from . import models

# Create your views here.

def main(request):
    members  = models.TeamMember.objects.all().order_by('order')
    faqs = models.FAQ.objects.all()
    context = {
        'members':members,
        'faqs':faqs
    }
    return render(request, 'index.html', context)


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        region = request.POST['region']
        organization = request.POST['organization']
        purpose = request.POST['purpose']
        models.Request.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            phone = phone,
            region = region,
            organization = organization,
            purpose = purpose
        )
        return redirect('approve_request')

    return render(request, 'signup.html')

def blogs(request):
    blogs = models.Blog.objects.all()
    paginator = Paginator(blogs, 10)  # Show 10 items per page

    page_number = request.GET.get('page')  # Get current page from query params
    page_obj = paginator.get_page(page_number) 
    context = {
        'blogs':page_obj
    }
    return render(request, 'blog-grid.html', context)

def blog_detail(request, id):
    blog = models.Blog.objects.get(id = id)
    context = {
        'blog': blog
    }
    return render(request, 'blog-details.html', context)

def contact(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        text = request.POST['text']
        models.Contact.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            text = text
        )
        return redirect('approve_request')
    return render(request, 'contact.html')

def approve_request(request):
    return render(request, 'approve-request.html')