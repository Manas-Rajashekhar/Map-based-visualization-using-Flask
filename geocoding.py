import requests
import googlemaps


def get_geocoding(add):
    api_key = "AIzaSyAfuVK5Ii2p5t1K0bUUkFWk8xvZkxuwyQE"
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    endpoint = f"{url}?address={add}&key={api_key}"
    # see how our endpoint includes our API key? Yes this is yet another reason to restrict the key
    r = requests.get(endpoint)
    latt = 0
    lngg = 0
    if r.status_code not in range(200, 299):
        return None, None
    try:
        '''
        This try block incase any of our inputs are invalid. This is done instead
        of actually writing out handlers for all kinds of responses.
        '''
        results = r.json()['results'][0]
        latt = results['geometry']['location']['lat']
        lngg = results['geometry']['location']['lng']
    except:
        pass
    return latt,lngg





