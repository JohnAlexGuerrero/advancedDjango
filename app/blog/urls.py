from django.urls import path

from blog.views import TutorialView

urlpatterns = [
    path('tutorial/template-tags/', TutorialView.as_view(), name='tutorial')
]
