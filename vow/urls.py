from django.urls import path
from .views import *


app_name = 'vow'

urlpatterns = [
    #Category
    
    #Customer_URL
    path('dashboard/', DashboardPageView.as_view(), name="dashboard"),
    path('customers/', customerlist, name="customers-list"),
    path('customers-list/', CustomerListView.as_view(), name="customers-listing"),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name="customer-detail"),
    path('customers/<int:pk>/update/', CustomerUpdateView.as_view(), name="customer-update"),
    path('customers/<int:pk>/delete/', customer_delete, name="customer-delete"),
    #Affirmation_URL
    path('affirmations/', AffirmationListView.as_view(), name="affirmation-list"),
    path('affirmation/<int:pk>/', AffirmationDetailView.as_view(), name="affirmation-detail"),
    path('affirmation/<int:pk>/update/', AffirmationUpdateView.as_view(), name="affirmation-update"),
    path('affirmation/<int:pk>/delete/', AffirmationDeleteView.as_view(), name="affirmation-delete"),
    path('affirmation/create/', AffirmationCreateView.as_view(), name="affirmation-create"),
    #Scores
    
    #Reviews
    
    #Questions
    
    #Answers
    
    #Ajax requests
    path("ajax/classes_std/", getClassesSTD, name = 'getClassesstd'),
    path("ajax/classes_sec/", getClassesSec, name = 'getClassessec'),
    path("ajax/name/", getName, name = 'getName'),
]
