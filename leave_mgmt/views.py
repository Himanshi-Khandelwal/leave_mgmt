# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect , render_to_response
from django.views.generic import TemplateView

# Create your views here.
def index(request):
	context_list= {}
	return render(request,"index.html",context_list)
	
def signup(request):
	print(request.method)
	if request.method == 'POST':
		# username = request.POST.get('userame_signup')
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		confirm_password = request.POST.get('confirm_password')
		user = User();
		us=username
		username=email               
		if password == confirm_password:
			user = User.objects.create_user(username=username,email=email,password=password)
			user.first_name = first_name
			user.last_name = last_name
			user.username = us
			user.email = email
			request.session['userid'] = user.id
			user.save()
			user.is_active = True
			return HttpResponseRedirect('/accounts/signup/')
		else:
			state = "Passwords do not match."
			print state
			context_list = {
				'state': state,
			}
			return render(request,'signup.html',context_list)
	else:
		#form = LoginForm()
		return render(request,'signup.html')

def signin(request):
	context_list= {}
	return render(request,'login.html',context_list)
	
def choice(request):
	context_list= {}
	return render(request,'login.html',context_list)
	
