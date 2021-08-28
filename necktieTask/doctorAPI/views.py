from rest_framework import viewsets,status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.db import IntegrityError, transaction
from .serializers import DoctorSerializer
from .models import *
# Create your views here.
class DoctorsViewSet(viewsets.ModelViewSet):
	queryset = Doctor.objects.all()
	serializer_class = DoctorSerializer
	def get_queryset(self):
		qs = super().get_queryset()
		distName_ = self.request.GET.get('dist')
		price_ = self.request.GET.get('price')
		lang_=self.request.GET.get('lang')
		category = self.request.GET.get('category')
		if distName_ is not None:
			dist_ = District.objects.get(distName__icontains=distName_)
			qs = qs.filter(dist=dist_)
		if lang_ is not None:
			doctor = Language.objects.filter(langCode__icontains=lang_).values_list('docID', flat=True).distinct()
			qs = qs.filter(docID__in=doctor)
		if category is not None:
			categoryID = Specialization.objects.get(spName__icontains=category)
			qs = qs.filter(specialization=categoryID)
		if price_ is not None:
			qs = qs.filter(price__lte=price_)
		return qs
	
	def create(self,request):
		validated_datas = request.data.copy()
		for validated_data in validated_datas:
			contact_data=validated_data.pop('contacts')
			lang_data=validated_data.pop('languages')
			availability_data=validated_data.pop('availability')
			msg=''
			status_ = status.HTTP_201_CREATED
			try:
				dist_data=validated_data.pop('dist')
				distID,created=District.objects.get_or_create(**dist_data)
			except (IntegrityError,AttributeError):
				return Response({"message": "Couldn't save the Doctor data.","status":status.HTTP_400_BAD_REQUEST})

			try:
				sp_data=validated_data.pop('specialization')
				spID, created=Specialization.objects.get_or_create(**sp_data)
			except (IntegrityError,AttributeError):
				return Response({"message": "Couldn't save the Doctor data.","status":status.HTTP_400_BAD_REQUEST})

			try:
				doctor=Doctor.objects.create(specialization=spID, dist=distID, **validated_data)
			except IntegrityError:
				return Response({"message": "Couldn't save the Doctor data.","status":status.HTTP_400_BAD_REQUEST})
			for contact in contact_data:
				try:
					Contact.objects.create(docID=doctor, contactNo=contact)
				except (IntegrityError,AttributeError):
					msg+="Errror saving Doctor's contact details. "
					status_ = status.HTTP_207_MULTI_STATUS
			for lang in lang_data:
				try:
					Language.objects.create(docID=doctor, langCode=lang)
				except (IntegrityError,AttributeError):
					msg+="Errror saving Doctor's language details. "
					status_ = status.HTTP_207_MULTI_STATUS
			for availability in availability_data:
				try:
					Availability.objects.create(docID=doctor, **availability)
				except (IntegrityError,AttributeError):
					msg+="Errror saving Doctor's availability details. "
					status_ = status.HTTP_207_MULTI_STATUS
		return Response({"message": "Successfully saved the Doctor data. "+msg,"status":status_})
