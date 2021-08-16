from blog.models import Blogpost
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from .decoraters import only_superuser_allow
from .models import Product, Contact, Order, OrderUpdate
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def signin(request):
    return render(request, 'signin.html', {})


def signup(request):
    if request.method == 'POST':
        # get the post parameters
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        # Error check
        if password != repassword:
            messages.error(request, "Passwors does not match plz try again")
            # print("here i am")
            return redirect('/')

        else:
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(
                request, "Welcome!! Your account has been successfully created")
            # print("here i am")
            return redirect('/Login')

    else:
        return HttpResponse('404 Not Found')


def Login(request):
    while True:
        products = Product.objects.all()
        parameters = {'product': products}
        if request.method == "POST":
            loginusername = request.POST["loginusername"]
            loginpass = request.POST["loginpass"]

            user = authenticate(username=loginusername, password=loginpass)

            if user is None:
                messages.error(request, "Invalid credentials, plz try again")
                return redirect("/")
            else:
                login(request, user)
                messages.success(request, "Welcome!! Logged in success")
                return redirect("/")

        # else:
            # this work when u type direct "/Login" in url bar
        return HttpResponse('404 Not Found')
        # return render(request, "signin.html", parameters)


def Logout(request):
    # if request.method == "POST":
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("/")


def search(request):
    # allprods = Product.objects.all()
    query = request.GET["query"]
    if len(query) > 50:
        allprods = []
        messages.warning(
            request, "Inappropriate search query, plz refine your query")

    else:
        allprodsprname = Product.objects.filter(product_name__icontains=query)
        allprodsbrname = Product.objects.filter(brand_name__icontains=query)
        allprodsprice = Product.objects.filter(price__icontains=query)
        allprodscategory = Product.objects.filter(category__icontains=query)
        # print(allprodsprice)
        # print(query)

        allprods = allprodsprname.union(
            allprodsbrname, allprodsprice, allprodscategory)

        #  allprods = allprodsprname.union(allprodsbrname)
    params = {"allprods": allprods, 'query': query}
    return render(request, "search.html", params)
    # return HttpResponse("this is search")


##########  All product Fetching for product page  ###########
def home(request):
    while True:
        products = Product.objects.all()
        parameters = {'product': products}
        # print(products)
        return render(request, 'home.html', parameters)
        # return render(request, 'home2.html', parameters)
        # return render(request, 'product.html', parameters)


# def category(request):
# category1 = Product.objects.filter(category = "Fashion")
# category2 = Product.objects.filter(category = "Electronics")
# category3 = Product.objects.filter(category = "Home appliances")
# category4 = Product.objects.filter(category = "Clothing")

# allproducts = {category1,category2,category3,category4}
# hi={"hello":category1}
# return render(request, 'category.html')

def fashion(request):
    category1 = Product.objects.filter(category="Fashion")
    # for i in category1:
    #     print(i.id)
    # print(category1, "cat 1")
    # onlyfashion = Product.objects.value()
    # allproducts = {category1,category2,category3,category4}
    hi = {"hello": category1}
    return render(request, 'fashion.html', hi)


def clothing(request):
    category2 = Product.objects.filter(category="Clothing")
    # allproducts = {category1,category2,category3,category4}
    hi = {"hello": category2}
    return render(request, 'clothing.html', hi)


def electronics(request):
    category3 = Product.objects.filter(category="Electronics")
    # allproducts = {category1,category2,category3,category4}
    hi = {"hello": category3}
    return render(request, 'electronics.html', hi)


def home_appliances(request):
    category4 = Product.objects.filter(category="Home appliances")
    print(category4)
    for i in category4:
        print(i.id)
    # allproducts = {category1,category2,category3,category4}
    hi = {"hello": category4}
    return render(request, 'home_appliances.html', hi)

def automotive(request):
    category5 = Product.objects.filter(category="Automotive")
    hi = {"hello":category5}
    return render(request, "automotive.html", hi)
############  ProductDetailView  ##############

# @method_decorator(only_superuser_allow, name = 'dispatch')
# @only_superuser_allow


def productdetail(request, myid):
    product = Product.objects.get(id=myid)
    allproduct = Product.objects.all()
    # print(product.id, "productssss")
    return render(request, 'productdetails.html', {'product': product, "allproduct": allproduct})


class productdetailview(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'productdetails.html'
    pk_url_kwarg = 'myid'


################  Add Product  ##############
# def addproduct(request):
#     if request.method == "POST":
#         product_name = request.POST.get('product_name', "")
#         category = request.POST.get('category', "")
#         brand_name = request.POST.get('brand_name', "")
#         price = request.POST.get('price', "")
#         image = request.POST.get('image', "")
#         print(product_name, category, brand_name, price)
#         import pdb
#         pdb.set_trace()
#         addedproduct = Product(product_name=product_name, category=category,
#                                brand_name=brand_name, price=price, image=image)
#         addedproduct.save()

#     def __str__(self):
#         return self.product_name
#     return render(request, 'addproduct.html')


def companydetails(request):
    return render(request, 'companydetails.html')


def contactus(request):
    print("hi")
    if request.method == "POST":
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        contact = request.POST.get('contact', "")
        # print(name, email, contact)
        contactfrom = Contact(name=name, email=email, contact=contact)
        contactfrom.save()
        messages.success(
            request, "Congratulations!! Your contact form has been received successfully")
        # return render(request, 'contactus.html')
    return render(request, 'contactus.html')


def checkout(request):
    if request.method == "POST":
        order_json = request.POST.get("json", "")
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        address = "Address line 1:- " + \
                  request.POST.get("address1", "") + " Address line 2:- " + \
                  request.POST.get("address2", "")
        city = request.POST.get("city", "")
        state = request.POST.get("state", "")
        zip_code = request.POST.get("zip_code", "")
        phone = "Contact Line 1:- " + \
                request.POST.get("phone1", "") + " Contact Line 2:- " + \
                request.POST.get("phone2", "")

        order = Order(order_json=order_json, name=name, email=email,
                      address=address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id,
                             update_desc="The update has been placed")
        update.save()
        thank = True
        id = order.order_id
        # print("hi")
        return render(request, "checkout.html", {"thank": thank, 'id': id})
    return render(request, "checkout.html")


def blog(request):
    return render(request, "blog.html")

# @csrf_exempt


def track(request):
    if request.method == "POST":
        orderId = request.POST.get("orderId", "")
        email = request.POST.get("email", "")
        print(orderId, email, "this is email and id")
        # return HttpResponse(f"{orderId} and {email}")
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            print(order, " this is order")
            if len(order) > 0:
                print("after order")
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({"text": item.update_desc,
                                    "time": item.timestamp, "thank": True})
                    # print(updates,  " this is updates")
                    # print(updates[0], " this is update of 0")
                    response = json.dumps({"status":"success","updates":updates, "items_json":order[0]}, default=str)
                    print(response, " this is response")
                    # print(json.loads(response) , " this is response parsed")
                    # print(response[0], " this is responce of 0")
                return HttpResponse(response)
                #  we put "default=str" because type date is not json serializable
                # return HttpResponse("hello")
            else:
                return HttpResponse('{"status":"else"}')
                 # we r putting else HttpResponse dictionary in the quotes because we r parsing this response at the track.html and if our status==success response is in json formate and else response is not then obviously there must be a problem if we will not put quotes then it gives json error
        except Exception as e:
            # print(f"exception{e}")
            return HttpResponse(e)
    return render(request, "track.html")
# def track(request):
#     if request.method == "POST":
#         orderId = request.POST.get("orderId", "")
#         email = request.POST.get("email", "")
#         # print(orderId)
#         # print(email)
#         return HttpResponse(f"{email}")
#         return HttpResponse("hello")
#         try:
#             order = Order.objects.filter(order_id=orderId, email=email)
#             # print(order)
#             if len(order) > 0:
#                 print(len(order))
#                 update = OrderUpdate.objects.filter(order_id=orderId)
#                 updates = []
#                 for item in update:
#                     updates.append({'text': item.update_desc, 'time': item.timestamp})
#                     # print(item.update_desc)
#                     # print(item.timestamp)
#                     response = json.dumps(updates, default=str)
#                     # print(response)
#                     # if u use json.dumps(update,default=str) than output will be messy
#                 return HttpResponse(response)
#             else:
#                 return HttpResponse('else')
#         except Exception as e:
#             # return HttpResponse(e)
#             return HttpResponse(f"exception{e}")

#     return render(request, "track.html")
