from django.urls import path
from.views import *
urlpatterns = [
    path('',home,name='adm'),
    path('addroom/',add_room,name='add_room'),
    path('viewroom/',view_room,name='view_room'),
    path('viewcustomer/',view_customer,name='view_customer'),
    path('updateroom/<int:id>',update_room,name='upadate_room'),
    path('viewbookings/',view_bookings,name='view_bookings'),
    path('deletecustomer/<int:id>',delete_customer,name='delete_customer'),
    path('deleteroom/<int:id>',delete_room,name='delete_room'),
]