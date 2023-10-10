from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name="main"

urlpatterns=[
    path("",views.homepage,name='homepage'),
    path("products",views.products,name="products"),
    path("register",views.register,name="register"),
    path("login", views.login_request, name ="login"),
    path("logout", views.logout_request, name= "logout"),
    path('tinymce/', include('tinymce.urls')),
    # path("blog",views.blog,name="blog"),
    # path("<article_page>", views.article, name = "article"),
    path("user", views.userpage, name = "userpage"),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# }#.bHGe_R6?+?e>
#https://ordinarycoders.com/creating-a-blog
#https://ordinarycoders.com/django-custom-user-profile