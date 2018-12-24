from django.db import models
import datetime
from tinymce import HTMLField


# Create your models here.
class AboutMembers(models.Model):
	name = models.CharField("Name of User", max_length=100, unique=True)
	institution = models.CharField("Institution Name", max_length=100)
	degree = models.CharField("Highest Degree Held", max_length=20, blank=True)
	profession = models.CharField("Profession", max_length=100)
	team_role = models.CharField("Role in Team", max_length=100)
	team_department = models.CharField("Team Department", max_length=100, blank=True)
	headshot = models.ImageField()

	def __str__(self): 
		return self.name
	class Meta: 
		verbose_name = "Team Member"
		verbose_name_plural = "Team Members"


class Updates(models.Model): 
	TYPE_OF_UPDATE = (
		('C', 'Clinical'),
		('B', 'Business and Funding'),
		('T', 'Technology')
	)
	type_of_update = models.CharField("Update",max_length=1, choices=TYPE_OF_UPDATE)
	title = models.CharField("Title", max_length=250, blank=True)
	description = HTMLField("Description")
	image = models.ImageField()
	article_link = models.URLField()
	publication_date = models.DateField("Date", default=datetime.date.today)
	class Meta: 
		verbose_name = "Update"
		verbose_name_plural = "Updates"
	def __str__(self):
		return "%s: %s" % (self.publication_date.strftime("%Y-%m-%d"), self.description[:20], )

class Company(models.Model):
	company_logo = models.ImageField()
	company_name = models.CharField("Name of Company", max_length=250)
	company_description = models.CharField("Company Description", max_length=1000)
	company_link = models.URLField()
	class Meta: 
		verbose_name = "Company"
		verbose_name_plural = "Companies"
	def __str__(self): 
		return self.company_name

class Career(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	career_role = models.CharField("Position", max_length=250)
	career_location = models.CharField("Location", max_length=250, blank=True)
	posting_link = models.URLField()
	class Meta: 
		verbose_name = "Career"
		verbose_name_plural = "Careers"
	def __str__(self): 
		return "%s, %s" % (self.company, self.career_role, )

class Seminar(models.Model):
	term_list = (
		('1808', 'Fall 2018'),
		('1901', 'Spring 2019'),
		('1906', 'Summer 2019'),
		('1908', 'Fall 2019'),
		('2001', 'Spring 2020'),

	)
	term = models.CharField("Term",max_length=4, choices=term_list)
	event_date = models.DateField("Date", default=datetime.date.today)
	location = HTMLField("Time & Location", default="<p>Time:</p><p>Location:</p>")
	description = HTMLField("Presentation")
	recap = HTMLField("Recap", blank=True)


