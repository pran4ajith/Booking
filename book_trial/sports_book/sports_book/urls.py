"""sports_book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from book import views
from book.views import ProfileUpdate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
#password reset are django admin password reset urls
urlpatterns = [

    url(r'^password_reset/$',
        auth_views.PasswordResetView.as_view(),
        name='password_reset'),#ask email
    url(r'^password_reset/done/$',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),#shows mail has been sent
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),#change password
    url(r'^reset/done/$',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),#done
    url(r'^admin/', admin.site.urls),
    url(r'^book/', views.booking_view, name='book'),
    url(r'^history/', views.history, name='history'),
    url(r'^bookings/', views.book_new, name='bookings'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^register/', views.register_view, name='register'),
    url(r'^editprofile/', ProfileUpdate.as_view(), name='editprofile'),
    url(r'^changepassword/', views.change_password, name='changepassword'),
    url(r'^$', views.index, name='index'),
    url(r'^item/(?P<id>\d+)/', views.facility_detail, name='facility_detail'),
    
]
'''NOTE:
    the 404 and 500 html files only work when DEBUG=FALSE. DEBUG=FALSE does not wor in localhost. though there are ways 
    the static files won't be rendered correctly. Added those files for use when deployed.
'''
admin.site.site_header = 'Booking Facility Admin'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
