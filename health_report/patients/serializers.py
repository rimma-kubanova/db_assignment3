from rest_framework import serializers
from .models import Users, Disease, Patients, Diseasetype, Country, Discover, Patientdisease, Publicservant, Doctor, Specialize, Record

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class DiseaseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diseasetype
        fields = '__all__'

class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = '__all__'

class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class DiscoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discover
        fields = '__all__'

class PatientDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patientdisease
        fields = '__all__'

class PublicServantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicservant
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class SpecializeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialize
        fields = '__all__'

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'