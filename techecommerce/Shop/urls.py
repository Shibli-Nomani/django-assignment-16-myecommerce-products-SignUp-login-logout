from django.urls import path
# import views of Shop App
from Shop import views
# import settings for MEDIA
from django.conf import settings
from django.conf.urls.static import static
#for login without views.py (coming from forms.py)
from django.contrib.auth import views as auth_views
#import login form class
from . forms import LoginForm

urlpatterns = [
    #ProductView class from views.py and url name 
    path('', views.ProductView.as_view(), name = 'home'),
    #for product page
    path('product-details/<int:pk>', views.ProductDetailView.as_view(), name ='product-details'),
    
    #static Page
    path('profile/', views.profile, name='profile'),
    

    #for actioncamera category, views: def actioncamera html: actioncamera.html
    path('actioncamera/', views.actioncamera, name='actioncamera'),
    #slug use to conditional calling for data attributes(views.py) 
    path('actioncamera/<slug:data>', views.actioncamera, name='actioncameraitem'),
    
    #accout-forms
    #for Signup and Registration
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    #for login and standard practice accounts/login
    path('accounts/login/', auth_views.LoginView.as_view(template_name = 'Shop/login.html', authentication_form = LoginForm), name='login'),
    #logout and redirect page /next_page = Page Name. Here 'home' page url name
    path('login/', auth_views.LogoutView.as_view(next_page = 'home'), name = 'logout'),
    
    
    ]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#Media Directory settings and root of Media

