import phonenumbers
from phonenumbers import geocoder, carrier, timezone

ph1 = phonenumbers.parse("+919903377282")

# Get location
location = geocoder.description_for_number(ph1, "en")

# Get carrier name
carrier_name = carrier.name_for_number(ph1, "en")

# Get time zone
time_zones = timezone.time_zones_for_number(ph1)

print(f"Location: {location}")
print(f"Carrier: {carrier_name}")
print(f"Time Zones: {time_zones}")
