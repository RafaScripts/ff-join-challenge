from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

from .forms import TargetForm
from .models import Target


def index(request):
    template = loader.get_template('site/index.html')
    form = TargetForm()

    if request.method == "POST":
        form = TargetForm(request.POST)
        if form.is_valid():
            target = form.save(commit=False)
            target.save()

    context = {
        'form': form,
    }

    return HttpResponse(template.render(context, request))

