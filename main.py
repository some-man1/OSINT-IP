import requests
import sys

print("\033[32m" + """


                                ,----,                                                 
    ,----..                   ,/   .`|                 ,--.                ,-.----.    
   /   /   \   .--.--.      ,`   .'  :   ,---,       ,--.'|           ,---,\    /  \   
  /   .     : /  /    '.  ;    ;     /,`--.' |   ,--,:  : |        ,`--.' ||   :    \  
 .   /   ;.  \  :  /`. /.'___,/    ,' |   :  :,`--.'`|  ' :        |   :  :|   |  .\ : 
.   ;   /  ` ;  |  |--` |    :     |  :   |  '|   :  :  | |        :   |  '.   :  |: | 
;   |  ; \ ; |  :  ;_   ;    |.';  ;  |   :  |:   |   \ | :        |   :  ||   |   \ : 
|   :  | ; | '\  \    `.`----'  |  |  '   '  ;|   : '  '; |        '   '  ;|   : .   / 
.   |  ' ' ' : `----.   \   '   :  ;  |   |  |'   ' ;.    ;        |   |  |;   | |`-'  
'   ;  \; /  | __ \  \  |   |   |  '  '   :  ;|   | | \   |        '   :  ;|   | ;     
 \   \  ',  / /  /`--'  /   '   :  |  |   |  ''   : |  ; .'        |   |  ':   ' |     
  ;   :    / '--'.     /    ;   |.'   '   :  ||   | '`--'          '   :  |:   : :     
   \   \ .'    `--'---'     '---'     ;   |.' '   : |              ;   |.' |   | :     
    `---`                             '---'   ;   |.'              '---'   `---'.|     
                                              '---'                          `---`     
                                                                                      
""")


shape = '\033[34m' + "[" +  '\033[91m' + "+" + '\033[34m' + "]"

print(str(shape) + '\033[91m' + " My website : " + "\033[32m" + "https://rdkgt7us.000webhostapp.com/")
print(str(shape) + '\033[91m' + " My instgram : " + "\033[32m" + "r_d515\n")


if len(sys.argv) != 2:
    print("")
    sys.exit(1)

ip = sys.argv[1]



url = f"http://ip-api.com/json/{ip}"
response = requests.get(url)

data = response.json()

if data["status"] == "success":
    latitude = data["lat"]
    longitude = data["lon"]
    city = data["city"]
    country = data["country"]
    isp = data["isp"]
    status = data["status"]
    timezone = data["timezone"]
    AS  = data["as"]
    org = data["org"]
    print(str(shape) + '\033[91m'+" status:" + "\033[32m" + f" {status}")
    print(str(shape) + '\033[91m'+" ISP:" + "\033[32m" + f" {isp} "+'\033[91m' + "as " + "\033[32m" + f"{AS}")
    print(str(shape) + '\033[91m'+" oragainztions:" + "\033[32m" + f" {org}")
    print(str(shape) + '\033[91m' +f" Location:" + "\033[32m" + f" {city} , {country}")
    print(str(shape) + '\033[91m'+" timezone:" + "\033[32m" + f" {timezone} ")
    print(str(shape) + '\033[91m' + f" Latitude:"+ "\033[32m" + f"{latitude}," '\033[91m' + "Longitude:" "\033[32m" + f"{longitude}")
else:
    status = data["status"]
    print('\033[91m'+"status:" + "\033[32m" + f" {status}\n")
    print('\033[91m' + "Invalid IPv4 address or geolocation not available!!.")
    print("try type (ip)/24 OR don't make a space")
