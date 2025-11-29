import random
import uuid
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Listing, Booking, Review
from datetime import date, timedelta

User = get_user_model()

class Command(BaseCommand):
    help = "Seed the database with sample Listings, Bookings, and Reviews"

    def handle(self, *args, **kwargs):
        # Make sure at least 1 user exists
        user = User.objects.first()
        if not user:
            self.stdout.write(self.style.ERROR(
                "No users found! Please create a user before running the seeder."
            ))
            return

        # Create sample listings
        titles = [
            "Ocean View Apartment",
            "Cozy Mountain Cabin",
            "Luxury City Penthouse",
            "Desert Retreat House",
            "Modern Studio Downtown"
        ]

        listings = []

        for title in titles:
            listing = Listing.objects.create(
                listing_id=uuid.uuid4(),
                title=title,
                description="This is a sample listing for testing.",
                price=random.randint(50, 400),
                host=user,
            )
            listings.append(listing)

        self.stdout.write("Sample listings created.")

        # Create bookings + reviews for each listing
        for listing in listings:
            # Create 1 booking
            Booking.objects.create(
                booking_id=uuid.uuid4(),
                listing=listing,
                user=user,
                start_date=date.today(),
                end_date=date.today() + timedelta(days=3),
                status="confirmed",
            )

            # Create 1 review
            Review.objects.create(
                review_id=uuid.uuid4(),
                listing=listing,
                user=user,
                rating=random.randint(3, 5),
                comment="This is a sample review.",
            )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))