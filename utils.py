from datetime import datetime

def parse_location(location_str):
    country, city, area, factory, section = location_str.split("/")
    return {
        "country": country,
        "city": city,
        "area": area,
        "factory": factory,
        "section": section
    }

def iso_to_millis(iso_str):
    dt = datetime.strptime(iso_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    return int(dt.timestamp() * 1000)
