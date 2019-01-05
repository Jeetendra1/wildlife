from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.views import View
from django.shortcuts import render_to_response
from myapp.models import Registration
from django.template import RequestContext

class IndexView(ListView):
	context_object_name = 'user_list'
	template_name = 'myapp/index.html'
	def get_queryset(self):
		return Registration.objects.all()

class DetailView(DetailView):
	
	model = Registration
	template_name ='myapp/detail.html'


class UserRegistration(View):
	template_name ='myapp/create.html'
	model = Registration
	# fields = ['name','email', 'contact', 'gender','delete']

	def get(self,request,*args,**kwargs):
		return render(request,self.template_name)
		# return HttpResponse('testing')
	def post(self,required,*args,**kwargs):
		print('gagan')
		name = required.POST['name']
		email = required.POST['email']
		contact = required.POST['contact']
		gender = required.POST['gender']
		instance = Registration(name=name, email=email,contact=contact,gender=gender);
		instance.save()
		# import ipdb;ipdb.set_trace()
		return HttpResponse(email)	
	



