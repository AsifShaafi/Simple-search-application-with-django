from django.shortcuts import render
from django.http import *
from .models import *
import random


# Create your views here.
def index(request):
    return render(request, 'searchapp/index.html')


# showing a particular developer info
def show(request, dev_id):
    try:
        dev = Developer.objects.get(pk=dev_id)
    except Developer.DoesNotExist:
        raise Http404("Developer does not exist")
    return render(request, 'searchapp/details.html', {'dev': dev})


# showing a particular developer info
def details(request):
    try:
        developers_who_can_write_multi_lang = list()

        # getting the ids of the required programming languages
        requested_programming_languages = request.GET.getlist('canWrite')
        requested_languages = request.GET.getlist('canSpeak')

        # getting the developers who can write the required programming languages and speak the given languages
        selected_developers = SearchDeveloper.get_selected_developers(
            programming_languages=requested_programming_languages, languages=requested_languages)

        for dev in selected_developers:
            developers_who_can_write_multi_lang.append(
                {
                    'developers': dev,
                    'programming_languages': dev.get_programming_languages(),
                    'languages': dev.get_languages()
                }
            )

        context = {
            "filtered_developers": developers_who_can_write_multi_lang,
        }
    except Developer.DoesNotExist:
        raise Http404("Developer does not exist")
    return render(request, 'searchapp/details.html', context)
