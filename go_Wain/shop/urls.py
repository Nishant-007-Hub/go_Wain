from django.urls import path
from .import views
from .views import productdetail, productdetailview, clothing, fashion, Login, Logout, blog, search, track
app_name = "shop"
urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('blog', views.blog, name="blog"),
    path('Login', views.Login, name="Login"),
    path('Logout', views.Logout, name="Logout"),
    path('search', views.search, name="search"),
    path('track/', views.track, name="track"),
    # path('home/', views.product, name = 'product'),
    # path('product/', views.product, ),
    # path('addproduct/', views.addproduct, name = 'addproduct'),
    path('product/<int:myid>', views.productdetail, name='productdetail'),
    # path('product/category/', views.category, name = 'category'),
    path('fashion/', views.fashion, name='fashion'),
    path('clothing/', views.clothing, name='clothing'),
    path('electronics/', views.electronics, name='electronics'),
    path('home_appliances/', views.home_appliances, name='home_appliances'),
    path('companydetails/', views.companydetails, name='product'),
    path('checkout/', views.checkout, name='checkout'),
    path('contactus/', views.contactus, name='contactus'),
    path('clear/', views.signin),


    # Class based generic Views URLS
    #     path('product/<int:myid>', productdetailview.as_view(), name = "productdetailview")

]
