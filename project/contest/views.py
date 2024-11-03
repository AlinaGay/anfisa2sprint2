from django.shortcuts import render

from .forms import ContestForm
from .models import Contest


def proposal_create(request):
    form = ContestForm(request.POST or None)
    if form.is_valid():
        pass
    context = {'form': form}
    return render(request, 'contest/form.html', context)


def proposal_list(request):
    contests = Contest.objects.all().order_by('id')
    context = {'contests': contests}
    return render(request, 'contest/contest_list.html', context)
