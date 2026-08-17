from django.db import models

# Create your models here.

"""
Zuhriddin

4. Stadion

id
owner FK User
name
description
price
start time
end time
address
latitude
longitude
is_verified
status (active / inactive )
created at

5. Photos

id
image
stadion_id

6. Booking

id
client
stadion_id
start time
end time null=True
total_summa
status ( booked, playing, finished )
created at
"""
