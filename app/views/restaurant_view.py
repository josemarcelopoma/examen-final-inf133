def render_hotel_list(hotels):

    return [
        {
            "id": hotel.id,
            "name": hotel.name,
            "address": hotel.address,
            "city": hotel.city,
            "description": hotel.description,
            "rating": hotel.rating,
        }
        for hotel in hotels
    ]


def render_hotel_detail(hotel):
  
    return {
        "id": hotel.id,
        "name": hotel.name,
        "address": hotel.address,
        "city": hotel.city,
        "description": hotel.description,
        "rating": hotel.rating,
    }
