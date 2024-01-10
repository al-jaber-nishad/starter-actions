from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def get_data(request):
	text = "Hello from Django"

	response = {
		'text': text
	}

	return Response(response, status=status.HTTP_200_OK)

