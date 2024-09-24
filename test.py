from config import session  # Ensure to import your session
from models import Band, Venue, Concert  # Import your models

# Create instances
band1 = Band(name="The Rockers", hometown="New York")
venue1 = Venue(title="Central Park", city="New York")
concert1 = Concert(band=band1, venue=venue1, date="2024-09-30")

# Add instances to the session and commit
session.add(band1)
session.add(venue1)
session.add(concert1)
session.commit()

# Query to verify
all_concerts = session.query(Concert).all()
for concert in all_concerts:
    print(f"Concert ID: {concert.id}, Band: {concert.band.name}, Venue: {concert.venue.title}, Date: {concert.date}")
