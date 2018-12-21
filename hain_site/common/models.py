from django.db import models
import datetime

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

# class Seminars():
# 	date = DateField()
# 	startTime = TimeField()
# 	endTime = TimeField(blank=True);
# 	location = CharField(_("Location"), max_length=100, blank=True)
# 	title = CharField(_("Name of Seminar"))

class Updates(models.Model): 
	TYPE_OF_UPDATE = (
		('C', 'Clinical'),
		('B', 'Business and Funding'),
		('T', 'Technology')
	)
	type_of_update = models.CharField("Update",max_length=1, choices=TYPE_OF_UPDATE)
	title = models.CharField("Title", max_length=250, blank=True)
	description = models.CharField("Description", max_length=1000)
	image = models.ImageField()
	article_link = models.URLField()
	publication_date = models.DateField("Date", default=datetime.date.today())
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
