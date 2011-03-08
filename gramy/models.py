from django.db import models

# Create your models here.

class Granie(models.Model):
    def __unicode__(self):
        return ("%s" %  self.date)
    date = models.DateTimeField()
#    chetni = models.IntegerField()
    

class Uczestnik(models.Model):
    def __unicode__(self):
        return ("%s" % (self.nick))
    
    granie = models.ForeignKey(Granie)
    nick = models.CharField(max_length = 20)
    chce = models.IntegerField()
#    email = models.CharField(max_length = 60)
