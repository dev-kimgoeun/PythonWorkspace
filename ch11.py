import thrater_module as mv
import travel.thailand
from travel import vietnam

mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

trip_to = vietnam.VietnamPackage()
trip_to.detail()
