# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import *

from django.http import *

from .forms import *

from django.contrib import auth

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from .models import *

# Create your views here.


def login(request):
	if request.method=='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			return HttpResponseRedirect('/home/')
		else:
			msg = '*Username or Password not match'
			return render(request,'login.html',{'inv':msg})

	return render(request,'login.html')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')

def signup(request):
	if request.method=='POST':
		form = Regforms(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			User.objects.create_user(username=username,password=password)


			return HttpResponseRedirect('/')
			user = authentication(username=username,password=password)
			login(request,user)
			return render(request,'login.html')

	else:
		form = Regforms()

	return render(request,'signup.html',{'form':form})


@login_required
def home(request):
	if request.user.is_authenticated():
		z = request.user.username
		nm = z.capitalize()

		if request.method == 'POST':
			formbg = bloging(request.POST,request.FILES)

			if formbg.is_valid():
				f = formbg.save(commit=False)
				f.author = request.user
				f.save()

				return HttpResponseRedirect('/home/')

				'''s = ['python','django','Data Science','science','sql','Data Mining']

				for i in s:
					r = re.search(i,c,re.I)

					if r:
						slug_name = i

					print slug_name

					f.slug = slug_name'''


		else:
			formbg = bloging()

		p = blogy.objects.order_by('-date_created')


		return render(request,'home.html',{'username':nm,'form':formbg,'q':p})

	else:
		return HttpResponseRedirect('/')



def view(request,d):
	data = blogy.objects.get(id=d)
	z = request.user.username
	nm = z.capitalize()
	return render(request,'view.html',{'key':data,'username':nm})


def delete(request,d):
	data = blogy.objects.get(id=d)
	data.delete()
	return HttpResponseRedirect('/home/')


def edit(request,d):
	data = blogy.objects.get(id=d)

	if request.method == 'POST':
		form = bloging(request.POST,instance=data)
		if form.is_valid():
			form.save()

			return redirect('home',d)

	else:
		form = bloging(instance=data)

	return render(request,'edit.html',{'form':form})
