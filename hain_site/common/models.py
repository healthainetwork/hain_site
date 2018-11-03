from django.db import models

# Create your models here.
class AboutMembers(models.Model):
	name = models.CharField("Name of User", max_length=101)
	institution = models.CharField("Institution Name", max_length=25)
	degree = models.CharField("Highest Degree Held", max_length=10, blank=True)
	profession = models.CharField("Profession", max_length=25)
	team_role = models.CharField("Role in Team", max_length=30)
	headshot = models.ImageField()

# class Seminars():
# 	date = DateField()
# 	startTime = TimeField()
# 	endTime = TimeField(blank=True);
# 	location = CharField(_("Location"), max_length=100, blank=True)
# 	title = CharField(_("Name of Seminar"))

class Updates(models.Model): 
	TYPE_OF_UPDATE = (
		('C', 'Clincal'),
		('B', 'Business and Funding'),
		('T', 'Technology')
	)
	type_of_update = models.CharField("Update",max_length=1, choices=TYPE_OF_UPDATE)
	title = models.CharField("Title", max_length=250)
	description = models.CharField("Description", max_length=1000)
	image = models.ImageField()
	article_link = models.URLField()

class Career(models.Model):
	company_logo = models.ImageField()
	company_name = models.CharField("Name of Company", max_length= 250)
	company_description = models.CharField("Company Description", max_length=1000)
	company_link = models.URLField()
	posting_link = models.URLField()
