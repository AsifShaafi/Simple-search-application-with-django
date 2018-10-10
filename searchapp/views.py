import rest_framework.views
from django.shortcuts import render
from django.http import *
from .models import *
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DeveloperSerializer


class DeveloperList(generics.ListAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer


# class DeveloperList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         developers = Developer.objects.all()
#         serializer = DeveloperSerializer(developers, many=True)
#         return Response(serializer.data)


class DeveloperAdd(APIView):

    def post(self, request, format=None):
        serializer = DeveloperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeveloperDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Developer.objects.get(pk=pk)
        except Developer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        developer = self.get_object(pk)
        serializer = DeveloperSerializer(developer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        developer = self.get_object(pk)
        serializer = DeveloperSerializer(developer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        developer = self.get_object(pk)
        developer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


# showing developer info
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
