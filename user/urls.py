from django.urls import path
from.views import *
urlpatterns = [
    path('',home,name='user_home'),
    path('book/<int:id>',book,name='book'),
    path('savebook/',savebook,name='savebook'),
    path('viewmybooking/',view_mybookings,name='view_mybookings'),
    path('details/',person_details,name='person_details'),
    path('update_details/',update_details,name='update_details'),
    path('cancel_booking/<int:id>',cancel_booking,name='cancel_booking'),
]