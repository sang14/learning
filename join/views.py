# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpRequest
from django.shortcuts import render
from .forms import EmailForm,JoinForm
from .models import Join

def home(request):
	print request.meta.get(REMOTE_ADDR)
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
		#new_join.save()
	context = {'form':form}

	template = "home.html"
	return render(request,template,context)


# Create your views here.
