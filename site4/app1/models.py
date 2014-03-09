from django.db import models
# Create your models here.
class Publisher(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=20)
    s_province=models.CharField(max_length=20)
    website=models.URLField()

    def __unicode__(self):
        return self.name

class Author(models.Model):
    salutation= models.CharField(max_length=10)
    first_n =models.CharField(max_length=10)
    last_n=models.CharField(max_length=30)
    email= models.EmailField(blank=True)
    headshot=models.ImageField(upload_to='/home/hyc/djangoapp/site4/template')

    def __unicode__(self):
        return u'%s %s' % (self.first_n,self.last_n)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.title
