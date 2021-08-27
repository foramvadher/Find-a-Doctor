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
	def get_contacts(self,obj):
		return Contact.objects.filter(docID=obj).values('contactNo')
	def get_availability(self,obj):
		return Availability.objects.filter(docID=obj).values('day','startTime','endTime')
	class Meta:
		model = Doctor
		fields = ('docID','name','specialization','contacts','eMail','qualification','addr','dist','price','priceRemarks','availability','holidayRemarks')