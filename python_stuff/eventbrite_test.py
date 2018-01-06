import requests

# def eventbrite(lat,lon):
response = requests.get("https://www.eventbriteapi.com/v3/events/search?&sort_by=best&location.latitude=37.7947492&location.longitude=-122.4179215&price=free&start_date.keyword=this_month&location.within=1mi&include_all_series_instances=0&include_unavailable_events=0",
headers = {
    "Authorization": "Bearer F7ZFTGYNOYL4254AWMPX",
},
verify = True,  # Verify SSL certificate
)
print response.json()['events'][1]['name']['text']
print response.json()['events'][1]['start']['local']


