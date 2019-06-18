from django.db import models
from django.conf import settings
from django.urls import reverse
#from django_hosts.resolvers import reverse
from.utils import code_generator,create_shortcode
from .validators import validate_url,validate_dot_com

SHORTCODE_MAX= getattr(settings,"SHORTCODE_MAX",15)

class KirrURLManager(models.Manager):
	def all(self,*args,**kwargs):
		qs_main=super(KirrURLManager,self).all(*args,**kwargs)
		qs=qs_main.filter(active=True)
		return qs

	def refresh_shortcodes(self,items=100):
		#print(items)
	    qs=KirrURL.objects.filter(id__gte=1)
	    if items is not None and isinstance(items,int):
	    	qs=qs.order_by('-id')[:items]
	    new_codes=0
	    for q in qs:
	        q.shortcode=create_shortcode(q)
	        print(q.id)
	        q.save()
	        new_codes+=1
	    return "New codes made: {i}".format(i=new_codes)   	

class KirrURL(models.Model):
	url=models.CharField(max_length=220, validators=[validate_url,validate_dot_com])
	shortcode=models.CharField(max_length=SHORTCODE_MAX,unique=True,blank=True)
	timestamp=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	active=models.BooleanField(default=True)
	objects=KirrURLManager()

	def save(self,*args,**kwargs):
	    if self.shortcode is None or self.shortcode == "":
		    self.shortcode=create_shortcode(self)
	    super(KirrURL,self).save(*args,**kwargs)

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)

	'''def get_short_url(self):
		url_path=reverse("scode",kwargs={'shortcode':self.shortcode})
		return  url_path


class ClickEventManager(models.Manager):
	def create_event(self,kirrInstance):
		if isinstance(kirrInstance,KirrURL):
			obj,created=self.get_or_created(kirr_url=kirrInstance)
			obj.count+=1
			obj.save()
			return obj.count
		return None
		
class ClickEvent(models.Model):
    kirr_url=models.OneToOneField(KirrURL,on_delete=models.CASCADE)
    count=models.IntegerField(default=0)
    updated=models.DateTimeField(auto_now=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    objects=ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)		'''			




    