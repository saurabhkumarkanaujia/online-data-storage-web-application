from django.urls import path
from.import views
urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('my_drive/',views.my_drive,name='my_drive'),
    path('all_files/',views.all_files,name='all_files'),
    path('photos/',views.photos,name='photos'),
    path('videos/',views.videos,name='videos'),
    path('documents/',views.documents,name='documents'),
    path('upload_f/',views.upload_f,name='upload_f'),
    path('logout/',views.logout,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('delete_user/<pk>',views.delete_user,name='delete_user'),
]
