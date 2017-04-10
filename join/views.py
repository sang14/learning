# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import EmailForm

def home(request):
	#print request.POST['email'],request.POST['email2']
	form = EmailForm(request.POST or None)
	if form.is_valid:
		print form.cleaned_data['email']
	context = {'form':form}

	template = "home.html"
	return render(request,template,context)


# Create your views here.
