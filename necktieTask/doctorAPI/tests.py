import json
from django.test import TestCase, Client
from .models import *
from .serializers import *
# Create your tests here.
class Tests(TestCase):

	def setUp(self):

		self.client = Client()

		dist1 = District(distID=1, distName='Yuen Long', region='New Territories')
		dist2 = District(distID=2, distName='Tuen Mun', region='New Territories')
		dist3 = District(distID=3, distName='Tsuen Wan', region='New Territories')
		dist4 = District(distID=4, distName='Central and Western', region='Hong Kong Island')
		dist5 = District(distID=5, distName='Wan Chai', region='Hong Kong Island')
		dist6 = District(distID=6, distName='Kwun Tong', region='Kowloon')
		dist7 = District(distID=7, distName='Wong Tai Sin', region='Kowloon')
		dist8 = District(distID=8, distName='Sham Shui Po', region='Kowloon')
		dist1.save()
		dist2.save()
		dist3.save()
		dist4.save()
		dist5.save()
		dist6.save()

		cat1 = Specialization(spID=1, spName='General Practice')
		cat2 = Specialization(spID=2, spName='Dermatology')
		cat3 = Specialization(spID=3, spName='Anaesthesiology')
		cat4 = Specialization(spID=4, spName='Cardiology')
		cat5 = Specialization(spID=5, spName='Dentistry')
		cat6 = Specialization(spID=6, spName='Physiotherapy')
		cat1.save()
		cat2.save()
		cat3.save()
		cat4.save()
		cat5.save()
		cat6.save()
		
		doc1 = Doctor(docID=1,name='Charlotte',eMail='charlotte@gmail.com',qualification='MBBS',specialization=cat1,addr='Room 824, 8/F, Leighton Centre, 77 Leighton Road',dist=dist1,price=800,priceRemarks='Not inclusive medicine',holidayRemarks='No holidays')
		doc2 = Doctor(docID=2,name='Natalie',eMail='natalie@gmail.com',qualification='MD',specialization=cat2,addr='',dist=dist1,price=1000,priceRemarks='Inclusive of 3 days medicine',holidayRemarks='Closed on sunday')
		doc3 = Doctor(docID=3,name='Catherine',eMail='catherine@gmail.gom',qualification='PHD',specialization=cat3,addr='Room 1902A, 19/F, East Point Centre, 555 Hennessy Road',dist=dist2,price=1500,priceRemarks='Not inclusive medicine',holidayRemarks='Closed on sunday')
		doc4 = Doctor(docID=4,name='Wong',eMail='wong@gmail.com',qualification='MD',specialization=cat1,addr='Room 14C, 14/F, Hang Seng Causeway Bay Building, 28 Yee Wo Street',dist=dist3,price=2000,priceRemarks='Not inclusive medicine',holidayRemarks='No holidays')
		doc5 = Doctor(docID=5,name='Dylan',eMail='dylan@gmail.com',qualification='PHD',specialization=cat2,addr='Room 1902A, 19/F, East Point Centre, 555 Hennessy Road',dist=dist4,price=2500,priceRemarks='Inclusive of 3 days medicine',holidayRemarks='Closed on sunday')
		doc1.save()
		doc2.save()
		doc3.save()
		doc4.save()
		doc5.save()

		Contact.objects.create(docID=doc1,contactNo='25705734')
		Contact.objects.create(docID=doc1,contactNo='25705735')
		Contact.objects.create(docID=doc2,contactNo='23705434')
		Contact.objects.create(docID=doc3,contactNo='25470534')
		Contact.objects.create(docID=doc4,contactNo='25470573')
		Contact.objects.create(docID=doc4,contactNo='25705344')
		Contact.objects.create(docID=doc5,contactNo='25235734')
		Contact.objects.create(docID=doc5,contactNo='21235734')
		Contact.objects.create(docID=doc5,contactNo='25235624')
		Contact.objects.create(docID=doc5,contactNo='25725712')

		Language.objects.create(docID=doc1,langCode='English')
		Language.objects.create(docID=doc2,langCode='Chinese')
		Language.objects.create(docID=doc2,langCode='English')
		Language.objects.create(docID=doc3,langCode='Chinese')
		Language.objects.create(docID=doc4,langCode='English')
		Language.objects.create(docID=doc5,langCode='Japanese')
		Language.objects.create(docID=doc5,langCode='Chinese')

		Availability.objects.create(docID=doc1,day='Monday',startTime='06:00:00',endTime='18:00:00')
		Availability.objects.create(docID=doc1,day='Tuesday',startTime='06:00:00',endTime='18:00:00')
		Availability.objects.create(docID=doc2,day='Wednesday',startTime='06:00:00',endTime='18:00:00')
		Availability.objects.create(docID=doc2,day='Thusday',startTime='06:00:00',endTime='18:00:00')
		Availability.objects.create(docID=doc2,day='Friday',startTime='06:00:00',endTime='18:00:00')
		Availability.objects.create(docID=doc3,day='Monday',startTime='06:00:00',endTime='18:00:00')
		Availability.objects.create(docID=doc4,day='Monday',startTime='06:00:00',endTime='18:00:00')
		Availability.objects.create(docID=doc4,day='Tuesday',startTime='06:00:00',endTime='18:00:00')
		Availability.objects.create(docID=doc5,day='Wednesday',startTime='06:00:00',endTime='18:00:00')
		Availability.objects.create(docID=doc5,day='Thusday',startTime='06:00:00',endTime='18:00:00')


	# Serializers
	def test_district_serializer(self):
		expected = {
			'distName':'Yuen Long',
			'region':'New Territories'
		}

		district = District.objects.get(distID=1)
		serializer = DistrictSerializer(district)
		self.assertEqual(expected, json.loads(json.dumps(serializer.data)))

	def test_category_serializer(self):
		expected = {
			"spName": "General Practice",
		}

		category = Specialization.objects.get(spID=1)
		serializer = SpecializationSerializer(category)
		self.assertEqual(expected, json.loads(json.dumps(serializer.data)))

	def test_doctor_serializer(self):
		expected = (
		{
			"docID": 1,
			"name": "Charlotte",
			"specialization": {
				"spName": "General Practice"
			},
			"contacts": [
				"25705734",
				"25705735"
			],
			"eMail": "charlotte@gmail.com",
			"qualification": "MBBS",
			"languages": [
				"English"
			],
			"addr": "Room 824, 8/F, Leighton Centre, 77 Leighton Road",
			"dist": {
				"distName":"Yuen Long",
				"region":"NT"
			},
			"price": 800,
			"priceRemarks": "Not inclusive medicine",
			"availability": [
				{
					"day": "MON",
					"startTime": "06:00:00",
					"endTime": "18:00:00"
				},
				{
					"day": "TUE",
					"startTime": "06:00:00",
					"endTime": "18:00:00"
				}
			],
			"holidayRemarks": "No holidays"
		}
		)
		doctor = Doctor.objects.get(docID=1)
		serializer = DoctorSerializer(doctor)
		self.assertEqual(list(expected), list(serializer.data))

	# Views and APIs
	def test_get_all_doctors(self):
		res = self.client.get('/doctor/')
		res = json.loads(res.content)
		self.assertEqual(5, len(res))

	def test_get_doctor_by_id(self):
		expected_id = 2
		res = self.client.get('/doctor/' + str(expected_id)+'/')
		res = json.loads(res.content)
		self.assertEqual(expected_id, res['docID'])

	def test_get_doctor_filter_by_district(self):
		expected_district = 'Tuen Mun'
		res = self.client.get('/doctor/', {'dist': expected_district})
		res = json.loads(res.content)
		for doc in res:
			self.assertEqual(expected_district, doc['dist']['distName'])

	def test_get_doctor_filter_by_district_n_price(self):
		expected_district = 'Yuen Long'
		expected_price_max = 1500
		res = self.client.get('/doctor/', {'dist': expected_district,'price':expected_price_max})
		res = json.loads(res.content)
		for doc in res:
			self.assertEqual(expected_district, doc['dist']['distName'])
			self.assertTrue(doc['price'] <= expected_price_max)

	def test_get_doctor_filter_by_language(self):
		expected_language = 'English'
		res = self.client.get('/doctor/', {'lang': expected_language})
		res = json.loads(res.content)
		for doc in res:
			if expected_language in doc['languages']:
				check = True
			else:
				check = False
				break
			# language array must contain the expected language
			self.assertTrue(check)

	def test_get_doctor_filter_by_category(self):
		expected_category = 'General Practice'
		res = self.client.get('/doctor/', {'category': expected_category})
		res = json.loads(res.content)
		for doc in res:
			self.assertEqual(expected_category, doc['specialization']['spName'])