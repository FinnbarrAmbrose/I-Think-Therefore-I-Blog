# filepath: /workspaces/I-Think-Therefore-I-Blog/blog/views.py
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Event  # Import Event model

# Create your views here.

def home(request):
    return render(request, "blog/home.html")


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

class EventsList(generic.ListView):
    model = Event
    template_name = "index.html"
    paginate_by = 12

def event_detail(request, event_id):
    queryset = Event.objects.all()
    event = get_object_or_404(Event, event_id=event_id)

    return render(
        request,
        "events/event_detail.html",
        {"event": event}
    )

def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post, "coder": "Matt Rudge"},
    )

def about(request):
    about_content = About.objects.first()
    return render(request, 'about/about.html', {'about': about_content})