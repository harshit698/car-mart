from django.shortcuts import render,redirect
from .models import car,extended
from django.contrib.auth.models import User
from django.views import generic,View
from .forms import loginform,CreateUserForm
from django.contrib.auth import authenticate,login,logout
# from django.core.urlresolvers import reverse_lazy

class IndexView(generic.ListView):
	template_name='mycollections/index.html'
	def get(self,request):
		if(self.request.user.is_authenticated):
			print("Yes")
			return render(request,'mycollections/index.html',{'car':car.objects.only('name','price','brand','horsepower','color','model_year','stock')})
		else:
			return redirect('/login/')


class LoginView(generic.edit.FormView):
	def get(self,request):
		form=loginform()
		return render(request,'mycollections/login.html',{'form':form})
	def post(self,request):
		form=loginform(request.POST)
		if form.is_valid():
			user=authenticate(username=request.POST["name"],password=request.POST["password"])
			if user is not None:
				login(request,user)
				print(user)
				url='/userprofile/'+str(request.user.id)+'/'
				return redirect(url)
			else:
				return render(request,'mycollections/login.html',{'form':form,'error':"You are not validated!"})
		else:
			form=loginform()
			return render(request,'mycollections/login.html',{'form':form,'error':"Please Fill The Form Correctly!"})

class ProfileView(View):
	def get(self,request,user_id):
		if(int(request.user.id)!=int(user_id)):
			print(user_id,end=" ")
			print(request.user.id)
			return redirect('/userprofile/'+str(request.user.id)+'/')
		else:
			return render(request,'mycollections/userprofile.html',{'object':request.user})

def BuyCar(request,car_id):
	car_obj=car.objects.get(id=car_id)
	user_obj=request.user
	if(request.user.is_authenticated):
		user_obj.ext.value=str(float(user_obj.ext.value)+float(car_obj.price))
		user_obj.ext.save()
		print(user_obj.ext.value)
		car_obj.stock-=1
		car_obj.owner.add(user_obj)
		car_obj.save()
		return redirect('/')
	else:
		return redirect('/login/')

def end(request):
	print(request.user.is_authenticated)
	logout(request)
	print(request.user.is_authenticated)
	return redirect('/login/')

class DetailView_Car(View):
	def get(self,request,pk):
		if(request.user.is_authenticated):
			return render(request,'mycollections/car_detail.html',{'object':car.objects.get(id=pk)})
		else:
			return redirect('/login/')

class CreateUser(generic.edit.FormView):
	template_name='mycollections/createuser.html'
	def get(self,request):
		form=CreateUserForm()
		return render(request,'mycollections/createuser.html',{'form':form})
	def post(self,request):
		form=CreateUserForm(request.POST)
		user=User()
		e=extended()
		if(User.objects.filter(username=request.POST["username"]).count()!=0):
			err="Username Already Exists!"
			return render(request,'mycollections/createuser.html',{'form':form,'err':err})
		elif(len(request.POST["password"])<8):
			err="Password Should Be Greater Than 8 Characters!"
			return render(request,'mycollections/createuser.html',{'form':form,'err':err})
		elif form.is_valid():
			user.username=request.POST["username"]
			user.set_password(request.POST["password"])
			user.email=request.POST["email"]
			user.save()
			e.user=user
			e.save()
			user=authenticate(username=user.username,password=request.POST["password"])
			login(request,user)
			return redirect('/userprofile/'+str(request.user.id)+'/')
		else:
			return render(request,'mycollections/createuser.html',{'form':form,'err':err})