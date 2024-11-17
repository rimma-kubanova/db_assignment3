from rest_framework import viewsets
from .models import Users, Disease, Patients, Diseasetype, Country, Discover, Patientdisease, Publicservant, Doctor, Specialize, Record
from .serializers import UsersSerializer, DiseaseSerializer, PatientsSerializer, DiseaseTypeSerializer, CountrySerializer, DiscoverSerializer, PatientDiseaseSerializer, PublicServantSerializer, DoctorSerializer, SpecializeSerializer, RecordSerializer

'''
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def user_detail(request, email):
    user = get_object_or_404(Users, email=email)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
'''

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    lookup_field = 'email'
    lookup_value_regex = '[^@]+@[^@]+\.[^@]+'

class DiseaseViewSet(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer

class PatientsViewSet(viewsets.ModelViewSet):
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializer

class DiseaseTypeViewSet(viewsets.ModelViewSet):
    queryset = Diseasetype.objects.all()
    serializer_class = DiseaseTypeSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class DiscoverViewSet(viewsets.ModelViewSet):
    queryset = Discover.objects.all()
    serializer_class = DiscoverSerializer

class PatientDiseaseViewSet(viewsets.ModelViewSet):
    queryset = Patientdisease.objects.all()
    serializer_class = PatientDiseaseSerializer

class PublicServantViewSet(viewsets.ModelViewSet):
    queryset = Publicservant.objects.all()
    serializer_class = PublicServantSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class SpecializeViewSet(viewsets.ModelViewSet):
    queryset = Specialize.objects.all()
    serializer_class = SpecializeSerializer

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    lookup_field = 'email'
    lookup_value_regex = '[^@]+@[^@]+\.[^@]+'
