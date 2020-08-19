from django.shortcuts import render
import subprocess

from homepage.models import CowTextModel

from homepage.forms import InputForm
# Create your views here.


def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            CowTextModel.objects.create(
                body=data.get('body')
            )
        cow_response = subprocess.run(
            ['cowsay', data.get('body')], capture_output=True, text=True)
        return render(request, 'index.html', {"form": InputForm(), "cow_response": cow_response.stdout})
    form = InputForm()
    return render(request, "index.html", {"form": form})


def most_recent_view(request):
    input_now = CowTextModel.objects.filter().order_by('-id')[:10]
    return render(request, "recent_input.html", {"input_now": input_now})
