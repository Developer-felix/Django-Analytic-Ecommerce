from django.conf.urls import include,url
from django.contrib import admin
from django.urls import path


from django.conf.urls.static import static
from django.conf import settings


# app_name="search"
# app_name = "cart"
# app_name="accounts"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('products.urls',"products"),namespace='products')),
    path('search/',include(('search.urls',"search"),namespace='search')),
    path('cart/',include(('cart.urls',"cart"),namespace='cart')),
    path('accounts/',include(('accounts.urls',"accounts"),namespace='accounts')),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
