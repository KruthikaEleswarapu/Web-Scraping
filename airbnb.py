from bs4 import BeautifulSoup
import requests
import pandas as pd

url="https://www.airbnb.co.in/s/delhi/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-02-01&monthly_length=3&price_filter_input_type=0&channel=EXPLORE&date_picker_type=calendar&checkin=2024-01-20&checkout=2024-01-25&source=structured_search_input_header&search_type=user_map_move&query=New%20Delhi%2C%20Delhi%2C%20India&place_id=ChIJLbZ-NFv9DDkRzk0gTkm3wlI&price_filter_num_nights=5&ne_lat=28.787154292898396&ne_lng=77.46380436479575&sw_lat=28.425404629744914&sw_lng=77.07103346402732&zoom=10.23585043836283&zoom_level=10&search_by_map=true&federated_search_session_id=2fc08737-211a-4fb2-b525-0bd1fc131bf5&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MCwiaXRlbXNfb2Zmc2V0IjowLCJ2ZXJzaW9uIjoxfQ%3D%3D"
r=requests.get(url)

soup=BeautifulSoup(r.text,"lxml")

while True:
    np=soup.find("a",class_="").get(url)
    cnp="https://www.airbnb.co.in"+np
    print(cnp)
