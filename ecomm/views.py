from django.shortcuts import render,redirect
from django .views import View
from .models import Customer,Product,Order,Cart,User
from  .forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

# def home(request):
#  return render(request, 'home.html')

class ProductView(View):
 def get(self,request):
  totalitem= 0
  topwears = Product.objects.filter(Category='Top Wear')
  bottomwears = Product.objects.filter(Category='Bottom Wear')
  mobiles = Product.objects.filter(Category='M')
  laptop = Product.objects.filter(Category='L')
  if request.user.is_authenticated:
   totalitem = len(Cart.objects.filter(user=request.user)) 
  return render(request,'home.html',{'topwears':topwears,'bottomwears':bottomwears,
    'mobiles':mobiles,'laptop':laptop,'totalitem':totalitem})

class ProdectDetailView(View):
 def get(self,request,pk):
  products = Product.objects.get(pk=pk)
  item_already_in_cart = False
  item_already_in_cart = Cart.objects.filter(Q( product = products.id) & Q(user=request.user)).exists()
  return render(request,'productdetail.html',{'products':products,'item_already_in_cart':item_already_in_cart})

# def product_detail(request):
#  return render(request, 'productdetail.html')

def add_to_cart(request):
 user = request.user
 product_id = request.GET.get('prod_id')
 product = Product.objects.get(id=product_id)
 Cart(user=user,product=product).save()
 return redirect('/cart')

@login_required
def show_cart(request):
 if request.user.is_authenticated:
  user= request.user
  cart = Cart.objects.filter(user=user)
  amount = 0.0
  shipping_price =50
  total_amount =0.0
  cart_product =[ p for p in Cart.objects.all() if p.user== user ]
  if cart_product:
   for p in cart_product:
    tempamount = (p.quentity * p.product.discunted_prce)
    amount += tempamount
    totalamount = amount + shipping_price
   return render(request, 'addtocart.html',{'carts':cart,'totalamount':totalamount,'amount':amount})
  else:
      return render(request, 'emptycart.html',{})

def plus_cart(request):
 if request.method == 'GET':
  prod_id =request.GET['prod_id']
  c = Cart.objects.get(Q(product=prod_id) & Q(user = request.user))
  c.quentity+=1
  c.save()
  amount = 0.0
  shipping_price =50
  total_amount =0.0
  cart_product =[ p for p in Cart.objects.all() if p.user== request.user ]
  if cart_product:
   for p in cart_product:
    tempamount = (p.quentity * p.product.discunted_prce)
    amount += tempamount
   data ={'quentity':c.quentity,'amount':amount,'totalamount': amount + shipping_price}
   return JsonResponse(data)
  
def minus_cart(request):
 if request.method == 'GET':
  prod_id =request.GET['prod_id']
  c = Cart.objects.get(Q(product=prod_id) & Q(user = request.user))
  c.quentity -= 1
  c.save()
  amount = 0.0
  shipping_price =50
  total_amount =0.0
  cart_product =[ p for p in Cart.objects.all() if p.user== request.user ]
  if cart_product:
   for p in cart_product:
    tempamount = (p.quentity * p.product.discunted_prce)
    amount += tempamount
   data ={'quentity':c.quentity,'amount':amount,'totalamount': amount + shipping_price}
   return JsonResponse(data)
  
def remove_cart(request):
 if request.method == 'GET':
  prod_id =request.GET['prod_id']
  c = Cart.objects.get(Q(product=prod_id) & Q(user = request.user))
  c.delete()
  amount = 0.0
  shipping_price =50
  total_amount =0.0
  cart_product =[ p for p in Cart.objects.all() if p.user== request.user ]
  if cart_product:
   for p in cart_product:
    tempamount = (p.quentity * p.product.discunted_prce)
    amount += tempamount
  data ={'amount':amount,'totalamount': amount + shipping_price}
  return JsonResponse(data)

 

def buy_now(request):
 return render(request, 'buynow.html')

# def profile(request):
#  return render(request, 'profile.html')
@method_decorator(login_required, name='dispatch')
class ProfileView(View):
 def get(seslf,request):
  form = CustomerProfileForm()
  return render(request, 'profile.html',{'form':form,'active':'btn-primary'})
 def post(seslf,request):
  form = CustomerProfileForm(request.POST)
  if form.is_valid():
   usr = request.user
   name = form.cleaned_data['name']
   locations = form.cleaned_data['locations']
   city = form.cleaned_data['city']
   state = form.cleaned_data['state']
   zipcode = form.cleaned_data['zipcode']
   reg = Customer(user=usr,name=name,locations=locations,city=city,state=state,zipcode=zipcode)
   reg.save()
  messages.success(request,'Profile Updated Succcessfully')
  return render(request,'profile.html',{'form':form,'active':'btn-primary'})



@login_required
def address(request):
 add = Customer.objects.filter(user=request.user)
 return render(request, 'address.html',{'add':add,'active':'btn-primary'})
@login_required
def orders(request):
 order_placed = Order.objects.filter(user = request.user)
 return render(request, 'orders.html',{'order_placed':order_placed})



def mobile(request,data = None):
 if data==None:
  mobiles= Product.objects.filter(Category='M')
 elif data == 'redmi' or data=='iphone' or data=='vivo':
  mobiles= Product.objects.filter(Category='M').filter(brand=data)
 return render(request, 'mobile.html',{'mobiles':mobiles})

def login(request):
 return render(request, 'login.html')

# def customerregistration(request):
#  return render(request, 'customerregistration.html')
class CustomerRegistration(View):
 def get(self,request):
  form = CustomerRegistrationForm()
  return render(request, 'customerregistration.html',{'form':form})
 def post(self,request):
  form = CustomerRegistrationForm(request.POST)
  if form.is_valid():
   messages.success(request,'Registered Successfully..........')
   form.save()
  return render(request, 'customerregistration.html',{'form':form})

@login_required
def checkout(request):
 user = request.user
 add = Customer.objects.filter(user=user)
 cart_item = Cart.objects.filter(user=user)
 amount = 0.0
 shipping_price = 50.0
 totalamount= 0.0
 cart_product =[ p for p in Cart.objects.all() if p.user== request.user ]
 if cart_product:
   for p in cart_product:
    tempamount = (p.quentity * p.product.discunted_prce)
    amount += tempamount
   totalamount = amount + shipping_price
 return render(request, 'checkout.html',{'add':add,'totalamount':totalamount,'cart_item':cart_item})

@login_required
def payment_done(request):
 user = request.user
 custid= request.GET.get('custid')
 customer = Customer.objects.get(id=custid)
 cart = Cart.objects.filter(user=user)
 for c in cart:
  Order(user=user,customer=customer,product=c.product,quentity=c.quentity).save()
  c.delete()
 return redirect("orders")
