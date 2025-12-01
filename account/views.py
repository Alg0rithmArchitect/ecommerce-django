from django.shortcuts import redirect, render

from .forms import CreateUserForm, LoginForm

from payment.forms import ShippingForm

from payment.models import ShippingAddress, Order, OrderItem

from django.contrib.auth.models import auth

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


def register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('store')
        
    context = {'form':form}

    return render(request, 'account/registration/register.html', context=context)




def my_login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request,user)

                return redirect ("store")
            
    context = {'form': form }

    return render (request,'account/my-login.html', context=context)


# Logout

def user_logout(request):

    auth.logout(request)

    return redirect("store")


# Shipping view

@login_required
def manage_shipping(request):

    try:

        shipping = ShippingAddress.objects.get(user=request.user.id)

    except ShippingAddress.DoesNotExist:

        shipping = None

    form = ShippingForm(instance=shipping)

    

    if request.method == 'POST':

        form = ShippingForm(request.POST, instance=shipping)

        if form.is_valid():

            # Assign the user FK on the object

            shipping_user = form.save(commit=False)

            # Adding the FK itself

            shipping_user.user = request.user

            shipping_user.save()

            return redirect ('store')

    context = {'form': form}
        
    return render(request, 'account/manage-shipping.html', context=context)


# @login_required
# def manage_shipping(request):

#     shipping = ShippingAddress.objects.filter(user=request.user).first()

#     if request.method == 'POST':
#         form = ShippingForm(request.POST, instance=shipping)
#         if form.is_valid():

#             shipping_obj = form.save(commit=False)   # 1️⃣ do not save yet
#             shipping_obj.user = request.user         # 2️⃣ attach FK
#             shipping_obj.save()                      # 3️⃣ save fully

#             return redirect('store')

#     else:
#         form = ShippingForm(instance=shipping)

#     return render(request, 'account/manage-shipping.html', {'form': form})



@login_required
def track_orders(request):

    try:

        orders = OrderItem.objects.filter(user=request.user)

        context = {'orders':orders}

        return render(request, 'account/track-orders.html', context=context)

    except:

        return render(request, 'account/track-orders.html')
        
    
    
    



