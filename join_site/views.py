from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.template import loader
from rest_framework.views import Response
from json import dumps

from .forms import TargetForm
from .models import Target
from .serializers import TargetSerializer


@api_view(('GET', 'POST'))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def index(request):
    template = loader.get_template('site/index.html')
    form = TargetForm()

    if request.method == "POST":
        form = TargetForm(request.POST)
        if form.is_valid():
            target = form.save(commit=False)
            target.save()

    serializer = TargetSerializer(Target.objects.all(), many=True)
    data_json = dumps(serializer.data)
    context = {
        'form': form,
        'target': data_json
    }

    return Response(context, template_name='site/index.html')

