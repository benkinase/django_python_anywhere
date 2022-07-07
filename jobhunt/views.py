from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from jobhunt.models import Application, Interview
from jobhunt.serializers import ApplicationSerializer, InterviewSerializer


@api_view(['GET', 'POST'])
# @permission_classes([permissions.AllowAny])
def application_view(request, format=None):
    print(request)
    """
    List all code applications, or create a new application
    """
    if request.method == 'GET':
        applications = Application.objects.all()
        serializer = ApplicationSerializer(applications, many=True)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([permissions.AllowAny])
def application_detail(request, pk, format=None):
    """
    Retrieve, update or delete an application.
    """
    try:
        application = Application.objects.get(pk=pk)
    except Application.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ApplicationSerializer(application)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ApplicationSerializer(application, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny])
def interview_view(request, format=None):
    """
    List all interviews, or schedule a new interview
    """
    if request.method == 'GET':
        interviews = Interview.objects.all()
        serializer = InterviewSerializer(interviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InterviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    pass
