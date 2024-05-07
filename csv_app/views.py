# views.py
from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import csv, io
from .models import Person
from .serializers import PersonModelSerializer

class CSVUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        if 'file' not in request.data:
            return Response({"error": "No file was provided."}, status=status.HTTP_400_BAD_REQUEST)

        file = request.data['file']
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.reader(decoded_file)

        # Skip the header row
        next(reader, None)

        # Check if all emails end with @esi-sba.dz
        for row in reader:
            _, email, _ = row
            if not email.endswith('@esi-sba.dz'):
                return Response({"error": "All emails must end with @esi-sba.dz"}, status=status.HTTP_400_BAD_REQUEST)

        # Reset the reader because it was exhausted in the check above
        file.seek(0)
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.reader(decoded_file)
        next(reader, None)  # Skip the header row again

        # Process CSV data
        for row in reader:
            full_name, email, matricule = row
            
            Person.objects.update_or_create(
                matricule=matricule,
                defaults={
                    'full_name': full_name,
                    'email': email,
                    'password':  matricule
                }
            )

        return Response({"success": "File uploaded successfully"}, status=status.HTTP_201_CREATED)



class PersonListCreateView(APIView):
    """
    List all persons, or create a new person.
    """
    def get(self, request, format=None):
        persons = Person.objects.all()
        serializer = PersonModelSerializer(persons, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonBulkCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PersonModelSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
