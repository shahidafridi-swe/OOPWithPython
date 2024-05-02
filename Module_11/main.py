from ride import Ride, RideMatching, RideRequest , RideSharing
from users import Rider, Driver
from vehicle import Car,Bike


cholo_jai = RideSharing('Cholo Jai')

shahid = Rider('Shahid Afridi', 'shahid@gmail.com',8702052856,'Mirpur',400)
bean = Driver('Mr. Bean', 'bean@gmail.com', 4201234578, 'Kazipara')

cholo_jai.add_driver(bean)
cholo_jai.add_rider(shahid)

shahid.request_ride(cholo_jai,'Airport','car')
shahid.show_current_ride()
bean.reach_destination(shahid.current_ride)

# print(cholo_jai)