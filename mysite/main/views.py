from django.shortcuts import render,redirect
from .models import Product
from django.core.paginator import Paginator
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout, authenticate
from .forms import NewUserForm, UserForm, ProfileForm, VoteForm

def homepage(request):
    if request.method=="POST":
        product_id=request.POST.get("product_pk")
        product = Product.objects.get(id = product_id)
        request.user.profile.products.add(product)
        messages.success(request,(f'{product} added to wishlist.'))
        return redirect ('main:products')
    product=Product.objects.all()[:4]
    return render(request=request,template_name='main/home.html',context={'product':product})

def products(request):
    if request.method=="POST":
        if "score_submit" in request.POST:
            vote_form = VoteForm(request.POST)
            if vote_form.is_valid():
                form = vote_form.save(commit=False)
                form.profile = request.user.profile
                product_id = request.POST.get("product")
                form.product = Product.objects.get(id=product_id)
                form.save()
                messages.success(request,(f'{form.product} product score submitted.'))
                return redirect ("main:products")
            messages.error(request,('Form is invalid.'))
            return redirect ("main:products")
        product_id=request.POST.get("product_pk")
        product = Product.objects.get(id = product_id)
        request.user.profile.products.add(product)
        messages.success(request,(f'{product} added to wishlist.'))
        return redirect ('main:products')
    products = Product.objects.all()
    paginator=Paginator(products,2)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    vote_form=VoteForm()
    return render(request = request, template_name="main/products.html", context = {"page_obj":page_obj,"vote_form":vote_form})



def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("main:homepage")

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()     
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request,"main/register.html", {"form":form})


def userpage(request):
    if request.method=="POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid():
            user_form.save()
            messages.success(request,('Your profile was successfully updated!'))
        elif profile_form.is_valid():
            profile_form.save()
            messages.success(request,('Your wishlist was successfully updated!'))
        else:
            messages.error(request,('Unable to complete request'))    
    
        return redirect("main:userpage")

    user_form=UserForm(instance=request.user)   
    profile_form=ProfileForm(instance=request.user.profile)
    return render(request=request, template_name="main/user.html", context={"user":request.user, "user_form":user_form, "profile_form":profile_form})



# Niesh512@
# y2cxFtCkPt"M$"p