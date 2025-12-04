from bicycle import Bicycle
from rider import Rider

if __name__ == "__main__":
    print("=" * 50)
    print("  BICYCLE SYSTEM DEMO")
    print("=" * 50 + "\n")

    # Create bicycle and rider
    bike = Bicycle("Cube", 6)
    rider = Rider("Daniel")

    # Start trip
    trip = rider.start_trip(bike)

    # Perform actions
    bike.pedal()
    bike.change_gear(3)
    trip.record_distance(5)
    bike.brake()

    # End trip
    trip.end()
    rider.end_trip(trip)

    print("\n" + "=" * 50)
    print("  DEMO COMPLETED")
    print("=" * 50)