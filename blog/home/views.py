from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.

def index(request):
    blogs = Blog.objects.all().order_by('-created_at')[:3]
    return render(request, 'index.html', {'blogs': blogs})

def blog_list(request):
    blog_list = Blog.objects.all().order_by('-created_at')
    paginator = Paginator(blog_list, 6)  # Show 6 blogs per page
    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)
    return render(request, 'blogs.html', {'blogs': blogs})

def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'blog_detail.html', {'blog': blog})


def features(request):
    return render(request, 'features.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Send email
            send_mail(
                subject=f"New message from {form.cleaned_data['name']}",
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['kratossathya@gmail.com'],
            )
            messages.success(request, 'Your message has been sent successfully!')
            form = ContactForm()  # Clear form
        else:
            messages.error(request, 'There was an error with your submission. Please check the form.')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})