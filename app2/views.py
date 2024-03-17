from django.core.mail import send_mail
from django.shortcuts import render,redirect
from app2.models import product_data,user_Model,Cart_item,CartModel,Address
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required



def registration(request):
    if request.method=='POST':
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        username=request.POST['usname']
        email=request.POST['names']
        # password=request.POST['password']
        address=request.POST['adress']
        birth=request.POST['age']
        mobile=request.POST['phone']
        gender=request.POST['gender']
        district=request.POST['district']
        
        
        
        if User.objects.filter(username=username).exists():
            print('username already exist')
            return render(request,'registration.html')
        else:
            password=request.POST['password']
            c_password=request.POST['cpassword']
            
            if password==c_password:
                if User.objects.filter(username=username):
                    return redirect('register')
                else:
                    
                    user1=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                    user1.save()
                    # print(firstname,lastname,username,email,password,address,birth,mobile,gender,district)
                    #log in the user
                    user1=authenticate(username=username,password=password)
                   
                    
                    
                    newuser=user_Model(user_birth=birth,user_address=address,user_number=mobile,user_gender=gender,user_district=district,user=user1)
                    newuser.save()
                    # print('success')
                    subject = 'Hello, django email'
                    message ='this is a test mail send from django'
                    from_email = 'fathima2336@gmail.com'
                    recipient_list = [user1.email]
                    send_mail(subject, message, from_email, recipient_list)
                    # return render(request,'home.html')
            
            if user1 is not None:
                login(request,user1)
                return redirect('list')
    else:
        return render(request,'registration.html')
    

def logins(request):
    # p=product_available.objects.all()
    # p.delete()
    if request.method=='POST':
        username=request.POST['name']
        password=request.POST['password']
        user2=authenticate(request,username=username,password=password)
        if user2 is not None:
            login(request,user2)
            products=product_data.objects.all()
            return render(request,'index.html',{'products':products})
        
        # print(username,password)
        # return render(request,'login2.html')
    else:
        return render(request,'login.html')
    return render(request,'login.html')

def userlogout(request):
    logout(request)
    return redirect('log')



@login_required(login_url='log')       
def product_list(request):
    products=product_data.objects.all()
   
    return render(request,'index.html',{'products':products})
def shop_view(request):
    products=product_data.objects.all()
   
    return render(request,'shop.html',{'products':products})

def viewcart(request):
    cart = CartModel.objects.get_or_create(user = request.user)[0]
    cartitems = Cart_item.objects.filter(cart = cart)
    selected_option = request.session.get('selected_option','not selected product size')
    total_price = cart.total_price()
    
    
    return render(request,'cart.html',{'cart_item' : cartitems,'selected_size' : selected_option,'total_price' : total_price})

def addToCart(request,i):
    item = product_data.objects.get(id=i)
    cart, create = CartModel.objects.get_or_create(user = request.user)
    
    if request.method == 'POST':
        selectedOption = request.POST.get('size')
        print(selectedOption)
    
    cart_items, create = Cart_item.objects.get_or_create(cart = cart,item = item, size = selectedOption)
    cart_items.quantity +=1
    cart_items.save()
    
    return redirect('viewcart')
    
def deletecart(request):
    current_user=request.user
    crt=CartModel.objects.get(user=current_user)
    
    crt.items.clear()
    crt.save()
    return redirect('viewcart')

def remove(request,j):
    current_user=request.user
    crt=CartModel.objects.get(user=current_user)
    p=Cart_item.objects.get(id=j,cart=crt)
    p.delete()
    return redirect('viewcart')

# def address(request):
#     return render(request,"address.html")

def payment(request):
    return render(request,'payment.html')

def increase_qty(request,k):
    # current_user=request.user
    # crt=CartModel.objects.get(user=current_user)
    cart_item= Cart_item.objects.get(id=k)
    cart_item.quantity +=1
    cart_item.save()
    return redirect('viewcart')
    
def decrease_qty(request,l):
    # current_user=request.user
    # crt=CartModel.objects.get(user=current_user)
    cart_item= Cart_item.objects.get(id=l)
    if (cart_item.quantity > 1):
        
        cart_item.quantity -=1
        cart_item.save()
    return redirect('viewcart')

def save_address(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        mobile = request.POST.get('mobile')
        flat = request.POST.get('flat')
        area = request.POST.get('area')
        landmark = request.POST.get('landmark')
        pincode = request.POST.get('pincode')
        town = request.POST.get('town')
        state = request.POST.get('state')

        # Assuming you have a logged-in user, get the user instance
        user = request.user

        # Create and save the address
        address = Address(
            user=user,
            fullname=fullname,
            mobile=mobile,
            flat=flat,
            area=area,
            landmark=landmark,
            pincode=pincode,
            town=town,
            state=state
        )
        address.save()

        # Redirect to the payment page or another appropriate page
        return redirect('payment')
    else:
        return render(request, 'address.html')
# Create your views here.
