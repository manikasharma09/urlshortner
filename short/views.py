from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.views import View
from .models import KirrURL
from .forms import SubmitUrlForm
#from short.models import ClickEvent

def home_view_fbv(request,*args,**kwargs):
	if request.method=="POST":
		print(request.POST)
	return render(request,"short/home.html",{})	

class HomeView(View):
	def get(self,request,*args,**kwargs):
		the_form=SubmitUrlForm()
		return render(request,"short/home.html",{})

	def post(self,request,*args,**kwargs):
		form=SubmitUrlForm(request.POST)
		context={
		    "title": "kirr.co",
		    "form": form
		}
		template="short/home.html"
		if form.is_valid():
			new_url=form.cleaned_data.get("url")
			obj,created=KirrURL.objects.get_or_create(url=new_url)
			context= {
			"object": obj,
			"created": created,
			}
			if created:
				template="short/success.html"
			else:
			    template="short/already-exists.html"
		return render(request,template,context)


class KirrCBVView(View):
	def get(self,request,shortcode=None,*args,**kwargs):
		obj=get_object_or_404(KirrURL,shortcode=shortcode)
		return HttpResponseRedirect(obj.url)

	def post(self,request,*args,**kwargs):
	    return HttpResponse()	






		
