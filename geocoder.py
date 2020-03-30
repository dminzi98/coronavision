from geopy.geocoders import Nominatim
import sys

try:
    address = str(sys.argv[1])
except IndexError:
    print("address must be supplied")
    sys.exit(1)
except ValueError:
    print("address must be string")
    sys.exit(1)

try:
    locator = Nominatim(user_agent="myGeocoder")
    location = locator.geocode(address)

except:
    print("address is no good")
    sys.exit("address is no good")

try:
    fi = open("userGEO.txt", "w")
    fi.write("{}, {}".format(location.latitude, location.longitude))
    fi.close()
except IOError:
    print("could not open userGEO")
    sys.exit(1)
except:
    print("??")
    sys.exit(1)

