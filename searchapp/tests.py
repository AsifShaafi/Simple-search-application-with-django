from django.urls import reverse
from rest_framework.views import status
from .models import Developer
from .serializers import DeveloperSerializer


class GetAllDeveloperTest():

    def test_developer_list(self):
        # hit the API endpoint
        response = self.client.get(
            reverse("all_developers")
        )
        # fetch the data from db
        expected = Developer.objects.all()
        serialized = DeveloperSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
