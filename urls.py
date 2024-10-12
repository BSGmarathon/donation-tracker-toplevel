from django.contrib import admin
from django.urls import path, include

import tracker.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tracker/', include(tracker.urls, namespace='tracker')),
]
