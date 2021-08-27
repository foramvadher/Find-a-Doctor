from django.db import models
REGION = (
	('NT','New Territories'),
	('KLN','Kowloon'),
	('HK','Hong Kong Island'),
)
DAYS = (
	('MON','Monday'),
	('TUE','Tuesday'),
	('WED','Wednesday'),
	('THU','Thusday'),
	('FRI','Friday'),
	('SAT','Saturday'),
	('SUN','Sunday'),
)
class District(models.Model):
	distID = models.IntegerField(primary_key = True)
	distName = models.CharField(max_length=10)
	region = models.CharField(max_length=3, choices=REGION)
	class Meta:
		unique_together = ['distName', 'region']
	
class Specialization(models.Model):
	spID = models.IntegerField(primary_key = True)
	spName = models.CharField(max_length=60,unique=True)
	
class Doctor(models.Model):
	docID = models.IntegerField(primary_key = True)
	name = models.CharField(max_length=50)
	eMail = models.CharField(max_length=50)
	qualification = models.CharField(max_length=20)
	specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
	addr = models.CharField(max_length=50)
	dist = models.ForeignKey(District, on_delete=models.CASCADE)
	price = models.IntegerField()
	priceRemarks = models.CharField(max_length=30)
	holidayRemarks = models.CharField(max_length=20)
	
class Contact(models.Model):
	docID = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	contactNo = models.CharField(max_length=13)
	class Meta:
		unique_together = ['docID', 'contactNo']
		
class Availability(models.Model):
	docID = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	day = models.CharField(max_length=3, choices=DAYS)
	startTime = models.TimeField()
	endTime = models.TimeField()
	class Meta:
		unique_together = ['docID','day']
	
	