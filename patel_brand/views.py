from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib import messages 
from service.models import homepro,mens,womens,Cart,Checkout,Order
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# from .forms import registers

def home(request):
    categories=mens.objects.all().order_by("-mname")[:3]
    return render(request,'index.html',{'categories':categories})

def product(request):
    menca=mens.objects.all()
    womenca=womens.objects.all()


    return render(request,'product.html',{'menca':menca,'womenca':womenca})

# @login_required(login_url='login')
def men(request):
    mencategory=mens.objects.all()


    #add Paginator
    paginator = Paginator(mencategory,4) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)



    mendata={
        'mencategory':mencategory,
        'page_obj':page_obj,
    }

    return render(request,'men.html',mendata)

# @login_required(login_url='login')
def women(request):
    wcategories=womens.objects.all()



    #add Paginator
    paginator = Paginator(wcategories,2) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)



    data={
        'wcategories':wcategories,
        'page_obj':page_obj,
    }
    return render(request,'women.html',data)

@login_required(login_url='login')
def cart_view(request):
    a=Cart.objects.filter(user=request.user)  
    total_a=0
    for i in a:
        total_a+=i.total_p
    print(total_a)  
    
    if request.user.is_authenticated:
        count_=Cart.objects.filter(user=request.user).count()
        print(count_)

    else:
        count_=None
    context={'a':a,'total_a':total_a,'count_':count_} 

    return render(request,'cart.html',context)

@login_required(login_url='login')
def addtocart(request,id,category):
    
    if category=='Mens':
        product=mens.objects.get(id=id)
        pname=product.mname
        pdes=product.mdescriptions
        pprice=product.mprice
        pimage=product.mimage

    elif category=='Womens':
        product=womens.objects.get(id=id)
        pname=product.wname
        pdes=product.wdescriptions
        pprice=product.wprice
        pimage=product.wimage
    else:
        return redirect('/')

    try:
        c=Cart.objects.get(name=pname,host=request.user)
        c.q+=1
        c.total_p+=pprice
        c.save()
    except:
        Cart.objects.create(name=pname,
                            desc=pdes,
                            price=pprice,
                            user=request.user,
                            q=1,
                            total_p=pprice,
                            image=pimage)
 
    return redirect('cart')

def remove(request,id):

    c_i=Cart.objects.get(id=id)
    c_i.delete()
    return redirect('cart')

# def contact(request):
#     return render(request,'contact.html')

def about(request):
    return render(request,'about.html')


def register(request):
    if request.method == 'POST':
       username = request.POST['username']
       email = request.POST['email']
       password = request.POST['password']
       confirmpassword = request.POST['confirmpassword']

       if password != confirmpassword:
           messages.error(request, "Passwords do not match!")
           return render(request, 'register.html')

       if User.objects.filter(username=username).exists():
           messages.error(request, "Username already taken!")
           return render(request, 'register.html')

       if User.objects.filter(email=email).exists():
           messages.error(request, "Email already registered!")
           return render(request, 'register.html')

       user = User.objects.create_user(username=username, email=email, password=password)
       user.save()

       messages.success(request, "Registration successful!!")
       return redirect('login') 
    return render(request, 'register.html')

    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            messages.success(request, "Login successful!")
            return redirect('home')  # Change 'home' to wherever you want to redirect
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')

def logout_(request):
    logout(request)
    return  redirect ('login')

    
def increase_quantity(request,id):
    q=Cart.objects.get(id=id)
    q.q=q.q+1
    q.save()
    q.total_p=q.price*q.q
    q.save()
    
    return redirect('cart') 


def decrease_quantity(request,id):
    q=Cart.objects.get(id=id)
    q.q=q.q-1
    q.save()
    q.total_p=q.price*q.q
    q.save()
    return redirect('cart') 


def profile(request):
    user = request.user 
    return render(request,'profile.html',{'user':user})

def checkout_(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_amount = sum(item.total_p for item in cart_items)  # Calculate total price
    
    if request.method == 'POST':
        # Form fields
        full_name = request.POST['fullname']
        address = request.POST['address']
        phone = request.POST['phonenumber']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        card_num = request.POST['card_num']
        e_date = request.POST['e_date']
        cvv = request.POST['cvv']

        # Replace this with actual cart logic (session or DB)
        cart = request.session.get('cart', [])  # assuming cart is in session

        # Save checkout info
        checkout = Checkout.objects.create(
            fullname=full_name,
            address=address,
            phonenumber=phone,
            city=city,
            state=state,
            zipcode=zipcode,
            card_num=card_num,
            e_date=e_date,
            cvv=cvv,
            host=request.user
        )

        # Save order details for each item
        for item in cart_items:
            Order.objects.create(
                name=item.name,
                price=item.price,
                q=item.q,
                total_p=item.total_p,
                host=request.user,
                status='pending'
            )
        # Optional: Clear cart after order
        cart_items.delete() 
        return redirect('order')
    return render(request, 'checkout.html', {'total_amount': total_amount})


def order(request):
    fc =Checkout.objects.filter(host=request.user).order_by('-id')   
    return render(request, 'order.html',{'fc':fc})


def trackorder(request):
    tr=Order.objects.filter(host=request.user).order_by('-id')
    return render(request,'trackord.html',{'tr':tr})


# def search(request):
#     query=request.GET.get('query')
#     results=[]
#     if query:
#         results=mens.objects.filter(name__icontains=query)

#     return render(request,'search.html',{'results':results,'query':query})