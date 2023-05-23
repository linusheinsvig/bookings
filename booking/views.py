from django.shortcuts import render, redirect
from .models import Restaurant, Table, Booking
from .forms import BookingForm

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'booking/restaurant_list.html', {'restaurants': restaurants})

def table_list(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    tables = Table.objects.filter(restaurant=restaurant)
    return render(request, 'booking/table_list.html', {'restaurant': restaurant, 'tables': tables})

def make_booking(request, table_id):
    table = Table.objects.get(id=table_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.table = table
            booking.save()
            return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm()

    return render(request, 'booking/make_booking.html', {'table': table, 'form': form})

def booking_confirmation(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'booking/booking_confirmation.html', {'booking': booking})