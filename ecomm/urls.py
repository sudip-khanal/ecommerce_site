
from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm,MyPasswordChange


urlpatterns = [
    path('',views.ProductView.as_view(),name='home'),
    path('product-detail/<int:pk>',views.ProdectDetailView.as_view(), name='product-detail'),
    path('cart/', views.show_cart, name='showcart'),
    path('add_to_cart/', views.add_to_cart, name='add-to-cart'),
    path('pluscart/', views.plus_cart,name='pluscart'),
    path('minuscart/', views.minus_cart,name='minuscart'),
    path('removecart/', views.remove_cart,name='removecart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='changepassword.html',form_class =MyPasswordChange,success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name='changepassworddone.html'),name='passwordchangedone'),

    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('accounts/login/',auth_views.LoginView.as_view (template_name='login.html', authentication_form=LoginForm),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('customerregistration/', views.CustomerRegistration.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment_done/', views.payment_done, name='payment_done'),

] + static (settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
