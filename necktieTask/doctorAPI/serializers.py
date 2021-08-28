from rest_framework import serializers
from .models import *

class DistrictSerializer(serializers.ModelSerializer):
	class Meta:
		model = District
		fields = ('distName','region')

class SpecializationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Specialization
		fields = ('spName',)

class DoctorSerializer(serializers.ModelSerializer):
	dist = DistrictSerializer(many=False)
	specialization = SpecializationSerializer(many=False)
	availability = serializers.SerializerMethodField()
	contacts = serializers.SerializerMethodField()
	languages = serializers.SerializerMethodField()
	def get_languages(self,obj):
		return Language.objects.filter(docID=obj).values_list('langCode', flat=True)
	def get_contacts(self,obj):
		return Contact.objects.filter(docID=obj).values_list('contactNo', flat=True)
	def get_availability(self,obj):
		return Availability.objects.filter(docID=obj).values('day','startTime','endTime')
	class Meta:
		model = Doctor
		fields = ('docID','name','specialization','contacts','eMail','qualification','languages','addr','dist','price','priceRemarks','availability','holidayRemarks')