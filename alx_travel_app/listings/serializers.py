from rest_framework import serializers
from .models import Listing, Booking
# , Review*/

# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = ['review_id', 'listing', 'user', 'rating', 'comment', 'created_at']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['booking_id', 'listing', 'user', 'start_date', 'end_date', 'status', 'created_at']

class ListingSerializer(serializers.ModelSerializer):
    bookings = BookingSerializer(many=True, read_only=True)
    # reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Listing
        fields = ['listing_id', 'title', 'description', 'price', 'host', 'created_at', 'bookings', 'reviews']
