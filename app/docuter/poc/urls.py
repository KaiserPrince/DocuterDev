from django.urls import path
from . import views 

app_name = 'poc' # Add this line

urlpatterns = [
    path('school-data/', views.school_data, name='school-data'),
    path('enter-data/', views.data_entry, name='data-entry'),  
    path('data-list/', views.list_data, name='data-list'), 
    path('generate-pdf/', views.export_question_paper_pdf, name='generate-pdf'),  
]
