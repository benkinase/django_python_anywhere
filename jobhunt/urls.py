from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from jobhunt import views

urlpatterns = [
    path('api/applications/', views.application_view),
    path('api/applications/<int:pk>', views.application_detail),
    path('api/applications/interviews/',views.interview_view)
]

urlpatterns = format_suffix_patterns(urlpatterns)
