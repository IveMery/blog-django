from django.contrib import admin
from django.urls import path,include
from blog.views import boardsView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',boardsView, name ='home'),
    path('blog/', include('blog.urls'))

]
