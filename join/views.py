# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpRequest
from django.shortcuts import render,HttpResponseRedirect
from .forms import EmailForm,JoinForm
from .models import Join
import uuid

def get_ip(request):
	try:
		x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
		if x_forward:
			ip = x_forward.split(",")[0]
		else:
			ip = request.META.get("REMOTE_ADDR")
	except:
		ip = ""
	return ip

#str(user_id)[:11].replace('-','').upper()
def get_ref_id():
	ref_id = str(uuid.uuid4())[:11].replace('-','').lower()
	try:
		id_exists = Join.objects.get(ref_id=ref_id)
		get_ref_id()


	except:
		return ref_id


def share(request,ref_id):
	#print ref_id
	context = {"ref_id":ref_id}
	template = "share.html"
	return render(request,template,context)


def home(request):
	#print request.META.get("REMOTE_ADDR")
	#print request.META.get("HTTP_X_FORWARDED_FOR")
	#print request.POST['email'],request.POST['email2']
	
	#this is using regular django forms
	#form = EmailForm(request.POST or None)
	#if form.is_valid():
	#	email = form.cleaned_data['email']
	#	new_join,created = Join.objects.get_or_create(email=email)
	#	print new_join,created
	#	print new_join.timestamp

	#	if created:
	#		print "Object was created"


	#this is using moddel form
	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join=form.save(commit=False)
		email = form.cleaned_data['email']
		new_join_old,created = Join.objects.get_or_create(email=email)
		if created:
			new_join_old.ref_id = get_ref_id()
			new_join_old.ip_address = get_ip(request)
			new_join_old.save()
		return HttpResponseRedirect("%s" %(new_join_old.ref_id))
		#new_join.ip_address = get_ip(request)
		#new_join.save()
	context = {'form':form}

	template = "home.html"
	return render(request,template,context)


# Create your views here.
