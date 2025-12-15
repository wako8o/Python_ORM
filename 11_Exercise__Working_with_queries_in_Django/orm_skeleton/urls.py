

from django.contrib import admin
from django.urls import path, include

import main_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chess/', include('main_app.urls')),
    path('dungeon/', include('main_app.urls')),
]
