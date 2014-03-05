from django.db import models

# Create your models here.

class Skill(models.Model):
	name = models.CharField(max_length=10)
	description = models.TextField()

	def __unicode__(self):
		return U'%s %s' %(self.name, self.description)

class Mentor(models.Model):
    nameFirst = models.CharField(max_length=20)
    nameLast = models.CharField(max_length=20)
    company = models.CharField(max_length=30)
    companyUrl = models.TextField()
    companyImgUrl = models.TextField()
    email = models.CharField(max_length=50)
    twitter = models.TextField()
    linkedIn = models.TextField()
    gitHub = models.TextField()
    website = models.TextField()
    linkOther = models.TextField()
    skills = models.ManyToManyField(Skill)
    skillsOther = models.TextField()
    language = models.CharField(max_length=20)
    languageUrl = models.TextField()
    almaMater = models.CharField(max_length=50)
    photoUrl = models.TextField()
    color = models.CharField(max_length=20)
    hexCode = models.CharField(max_length=7)
    highlight = models.CharField(max_length=7)
    allWomen = models.TextField()
    afraid = models.TextField()
    proud = models.TextField()
    about = models.TextField()
    hobbies = models.TextField()
    techTalk = models.BooleanField()
    judge = models.BooleanField()
    mentor = models.BooleanField()

    # pub_date = models.DateTimeField('date published')

    class Meta(object):
		ordering = ('nameFirst', 'nameLast', 'company')
