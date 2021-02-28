from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.views import Response
from json import dumps

from .forms import TargetForm
from .models import Target
from .serializers import TargetSerializer


@api_view(('GET', 'POST'))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def index(request):
    form = TargetForm()

    if request.method == "POST":
        form = TargetForm(request.POST)
        if form.is_valid():
            form.save()

    serializer = TargetSerializer(Target.objects.all(), many=True)
    data_json = dumps(serializer.data)
    context = {
        'form': form,
        'target': data_json
    }

    return Response(context, template_name='site/index.html')


@api_view(('POST',))
def update(request, pk):
    target = Target.objects.get(pk=pk)
    serializer = TargetForm(request.POST, instance=target)
    if serializer.is_valid():
        serializer.save()

    return HttpResponseRedirect(reverse('index'))