from urllib.parse import urlencode
import httpx
import pygsheets
import pandas as pd

gc = pygsheets.authorize(service_file='creds.json')

df = pd.DataFrame()

# Create a column
df['name'] = ['John', 'Steve', 'Sarah']

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open('Appartment listings')

#select the first sheet 
wks = sh[0]

records=wks.get_all_records()
addresses=[]
for x, row in enumerate(records):
    add=row['Address']
    test=add.split(" ")
    v1=test[0]
    v2=test[1]
    print([v1,v2])
    addresses.append([v1,v2,x])
    if v2=="First":
        addresses.append([v1,"1st",x])
    if v2=="Third":
        addresses.append([v1,"3rd",x])




#update the first sheet with df, starting at cell B2. 
# wks.set_dataframe(df,(1,1))

# we should use browser-like request headers to prevent being instantly blocked
BASE_HEADERS = {
    "accept-language": "en-US,en;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-language": "en-US;en;q=0.9",
    "accept-encoding": "gzip, deflate, br",
}

output=[]
scraped=[]

cities=["Pawtucket", "Woonsocket", "WestWarwick"]
# Pawtucket=[['93','Tweed'],['13','Sanford'],['17','Sanford'],['132','Spring'],['14','South'],['192','Summit'],['178','Division'],['100','Linwood'],['305','Prospect'],['16','Sisson'],['288','Sayles'],['312','Walcott'],['6','Fletcher'],['98','Railroad'],
# ['15','Sanford'],['19','Sanford'], ['134','Spring'],['78','Pond'],['182','Division'],['184','Division'],['102','Linwood'],['307','Prospect'],['290','Sayles'],['310','Walcott']]
# Woonsocket=[['157','Park'],['149','Park'],['97','Roberts'],['98','Roberts'],['99','Roberts'],['518','Willow'],['132','First'],['132',
# '1st'],['133','First'],['133','1st'],['134','First'],['134','1st'],['672','Fairmount'],['213','Third'],['213','3rd'],['337','3rd'], ['337','Third'],['60','Pleasant'],['62','Pleasant'], ['64','Pleasant'], ['8','Mill'],['10','Mill']]
# WestWarwick=[['15','McNiff'],['16','McNiff'],['17','McNiff'],['19','McNiff'],['72','Highland'], ['306', 'Washington'],['51', 'East'], ['148', 'Brookside'],
# ['149', 'Brookside'],['150', 'Brookside'], ['26','Parker'],['30','Parker'],['31','Parker'],['32','Parker'],['600','Providence'],['25','Prospect','Hill'], ['65', 'Prospect', 'Hill'], ['67','Prospect','Hill'],
# ['28','Weaver'],['30','Weaver'],['87','Pond'], ['89','Pond'],['91','Pond'],['101','Pond'],['102','Pond'], ['103','Pond'],['105','Pond'],['12','Fairview'], ['3','Bowen'], ['5','Bowen'], ['9','Bowen'],
# ['8','Epworth'],['6','Epworth'], ['25','Matteson'],['27','Matteson'],['64','Border'],['5','Anthony'],['7','Anthony'],['9','Anthony']]

WS= {
    "west": -71.540580,
    "east": -71.457945,
    "south": 41.976966,
    "north": 42.017232,
    }

PT={
    "west": -71.420844,
    "east": -71.337517,
    "south": 41.857219,
    "north": 41.894208,
}


WW={
    "west": -71.562659,
    "east": -71.483394,
    "south": 41.662619,
    "north": 41.731763,
}
coords=None

for city in cities:
    print("Scraping "+city)
    if city=="Pawtucket":
        coords=PT
    if city=="Woonsocket":
        coords=WS
    if city=="WestWarwick":
        coords=WW


    url = "https://www.zillow.com/search/GetSearchPageState.htm?"
    parameters = {
        "searchQueryState": {
            "filterState": {
            "isForSaleForeclosure": {"value": False},
            "isMultiFamily": {"value": False},
            "isAllHomes": {"value": True},
            "isAuction": {"value": False},
            "isNewConstruction": {"value": False},
            "isForRent": {"value": True},
            "isLotLand": {"value": False},
            "isManufactured": {"value": False},
            "isForSaleByOwner": {"value": False},
            "isComingSoon": {"value": False},
            "isForSaleByAgent": {"value": False},
        },
            "pagination": {},
            "usersSearchTerm": "",
            "mapBounds": coords
        },
        "wants": {
            # cat1 stands for agent listings
            "cat1": ["mapResults"]
            # and cat2 for non-agent listings
            # "cat2":["mapResults"]
        },
        "requestId": 8,
    }


    response = httpx.get(url + urlencode(parameters), headers=BASE_HEADERS)
    results = response.json()["cat1"]["searchResults"]["mapResults"]
    for data in results:
        scraped.append(data['detailUrl']) 



for a in addresses:
    for b in scraped:
        if a[1].lower() in b.lower():
            t=b.lower()
            thing=t.split(a[1].lower())[0]
            if a[0] in thing:
                print(b)
                output.append(b)
                wks.update_value((a[2]+2,4),"https://www.zillow.com/"+b)



results = response.json()["cat1"]["searchResults"]["mapResults"]
