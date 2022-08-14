from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Project, About


class Home(View):
    """This generic based view, list the titles of projects
    and details about me"""
    def get(self, request, *args, **kwargs):
        projects = Project.objects.all().order_by("-pk")
        queryset = About.objects.filter(pk=1)
        about = get_object_or_404(queryset, pk=1)

        return render(
            request,
            "index.html",
            {
                "projects": projects,
                'about': about,
            },
        )
