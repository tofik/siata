from django.db import models

# Create your models here.

class Granie(models.Model):
    def __unicode__(self):
        return ("%s" %  self.date)
    date = models.DateTimeField()
#    chetni = models.IntegerField()
    

class Uczestnik(models.Model):
    def __unicode__(self):
        return ("%s %s" % (self.surname, self.forname))
    
    granie = models.ForeignKey(Granie)
    forname = models.CharField(max_length = 20)
    surname = models.CharField(max_length = 40)
    created = models.DateTimeField(auto_now_add = True)
#    email = models.CharField(max_length = 60)
