from django.contrib import admin
from django.urls import path, include
from mynewblog.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing_page'),
    path('form-data/', blog_post, name='form_data'),
    path('post-delete/<id>', post_delete, name="post-delete"),
    path('post-update/<id>', post_update, name="post-update"),
    path('accounts/', include('accounts.urls')),
]
