from django.shortcuts import render
from accounts.models import Profile
from accounts.serializers import ProfileSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def profile(request):
	permission_classes = (IsAuthenticated)
	if request.method == 'GET':
		try:
			profile = Profile.objects.get(user=request.user)
			serializer = ProfileSerializer(profile)
			return Response(serializer.data)

		except Profile.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

	elif request.method == 'POST':
		serializer = ProfileSerializer(data=request.data)
		if serializer.is_valid():
			serializer.user = request.user
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
