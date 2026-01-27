from tkinter import *
from tkinter import ttk
from time import *
#===========================================DATABASE==========================================================#
utc_minus_10 = [
    "Honolulu", "Hilo", "Kailua", "Pearl City", "Papeete", "Faaa", "Adak", 
    "Johnston Atoll", "Lihue", "Kahului", "Kapolei", "Waipahu", "Kaneole",
    "Mililani", "Ewa Beach", "Makakilo", "Haiku-Pauwela", "Kihei", "Lahaina",
    "Wailuku", "Lanai City", "Kaunakakai", "Atuona", "Taiohae"
]

utc_minus_09 = [
    "Anchorage", "Juneau", "Fairbanks", "Sitka", "Nome", "Ketchikan", 
    "Gambier Islands", "Badger", "College", "Kodiak", "Wasilla", "Kenai",
    "Palmer", "Bethel", "Homer", "Unalaska", "Barrow", "Soldotna", 
    "Valdez", "Petersburg", "Seward", "Kotzebue", "Rikitea"
]

utc_minus_08 = [
    "Los Angeles", "San Francisco", "San Jose", "Oakland", "San Diego", 
    "Sacramento", "Seattle", "Tacoma", "Portland", "Vancouver", "Richmond", 
    "Las Vegas", "Tijuana", "Victoria", "Whitehorse", "Spokane", "Anaheim", 
    "Long Beach", "Irvine", "Surrey", "Burnaby", "Eugene", "Salem", 
    "Bakersfield", "Fresno", "Riverside", "Santa Ana", "Coquitlam", 
    "Kelowna", "Nanaimo", "Abbotsford", "Everett", "Bellevue", "Reno", 
    "Henderson", "Ensenada", "Mexicali", "Santa Rosa", "Oxnard", "Fontana",
    "Modesto", "Oxnard", "Huntington Beach", "Glendale", "Santa Clarita",
    "Kamloops", "Prince George", "Nanaimo", "New Westminster", "Bellingham"
]

utc_minus_07 = [
    "Phoenix", "Tucson", "Denver", "Boulder", "Salt Lake City", "Provo", 
    "Calgary", "Red Deer", "Edmonton", "Albuquerque", "Boise", "Chihuahua", 
    "Hermosillo", "Yellowknife", "Mazatlan", "Colorado Springs", "Aurora", 
    "Scottsdale", "Mesa", "Chandler", "Lethbridge", "Medicine Hat", 
    "Fort McMurray", "Santa Fe", "Saltillo", "Torreon", "La Paz", 
    "Cabo San Lucas", "Missoula", "Billings", "Cheyenne", "Casper", 
    "Grand Junction", "Pueblo", "Fort Collins", "Greeley", "Ogden", 
    "St. George", "Las Cruces", "Flagstaff", "Yuma", "Airdrie", "Grande Prairie"
]

utc_minus_06 = [
    "Chicago", "Naperville", "Aurora", "Dallas", "Fort Worth", "Austin", 
    "Houston", "Mexico City", "Guadalajara", "Monterrey", "Guatemala City", 
    "San Salvador", "Winnipeg", "San Jose", "Tegucigalpa", 
    "Managua", "Regina", "Saskatoon", "New Orleans", "San Antonio", 
    "Kansas City", "Oklahoma City", "Minneapolis", "St. Louis", "Milwaukee", 
    "Belize City", "Des Moines", "Little Rock", "Birmingham", 
    "Jackson", "Memphis", "Nashville", "Tulsa", "Wichita", "Omaha", 
    "Lincoln", "Madison", "Puebla", "Leon", "Zapopan", "Juarez", "Merida",
    "San Luis Potosi", "Aguascalientes", "Queretaro", "Veracruz", "Morelia",
    "Toluca", "Torreon", "Brandon", "Steinbach", "Kenora"
]

utc_minus_05 = [
    "New York", "Brooklyn", "Queens", "Manhattan", "Washington D.C.", 
    "Baltimore", "Philadelphia", "Boston", "Toronto", "Mississauga", 
    "Ottawa", "Bogota", "Medellin", "Lima", "Havana", "Miami", "Atlanta", 
    "Detroit", "Montreal", "Quebec City", "Kingston", "Panama City", 
    "Quito", "Guayaquil", "Nassau", "Indianapolis", "Charlotte", "Columbus", 
    "Cleveland", "Pittsburgh", "Hamilton", "London", "Cali", 
    "Port-au-Prince", "Orlando", "Tampa", "Jacksonville", "Raleigh", 
    "Richmond", "Brampton", "Markham", "Vaughan", "Kitchener", 
    "Windsor", "Cuzco", "Arequipa", "Cartagena", "Barranquilla", "Iquitos",
    "Louisville", "Cincinnati", "Dayton", "Buffalo", "Rochester", "Syracuse",
    "Providence", "Hartford", "New Haven", "Kingston", "Ibagué",
    "Bucaramanga", "Pereira", "Trujillo", "Chiclayo", "Piura"
]

utc_minus_04 = [
    "Santiago", "Valparaiso", "Caracas", "La Paz", "Halifax", 
    "Santo Domingo", "San Juan", "Manaus", "Asuncion", "Cuiaba", 
    "Georgetown", "Bridgetown", "Port of Spain", "Santa Cruz", "Moncton", 
    "Fredericton", "Charlottetown", "Antofagasta", "Cochabamba", 
    "Barquisimeto", "Concepcion", "Temuco", "Maracaibo", 
    "Valencia", "Porto Velho", "Boa Vista", "Castries", 
    "St. George's", "Basseterre", "Saint John", "Sydney (Nova Scotia)",
    "Punta Arenas", "Iquique", "Oruro", "Sucre", "Potosi", "Ciudad Bolivar",
    "San Cristobal", "Roseau", "Saint John's", "Tortola"
]

utc_minus_03 = [
    "Buenos Aires", "La Plata", "Montevideo", "Rio de Janeiro", "Niteroi", 
    "São Paulo", "Campinas", "Curitiba", "Salvador", "Fortaleza", 
    "Belo Horizonte", "Brasilia", "Recife", "Cayenne", "Stanley", 
    "Porto Alegre", "Mendoza", "Rosario", "Cordoba", "Mar del Plata", 
    "Belem", "Goiania", "Paramaribo", "Florianopolis", "Vitoria", "Santos", 
    "Sao Luis", "Maceio", "Natal", "Bahia Blanca", "Tucuman", "Salta",
    "Santa Fe", "San Juan", "Neuquen", "Maldonado",
    "Salto", "Paysandú", "Nuuk", "Thule", "Aracaju", "Joao Pessoa", "Teresina"
]

utc_00 = [
    "London", "Manchester", "Birmingham", "Dublin", "Cork", "Lisbon", 
    "Porto", "Reykjavik", "Casablanca", "Rabat", "Accra", "Dakar", 
    "Abidjan", "Freetown", "Monrovia", "Bamako", "Nouakchott", 
    "Ouagadougou", "Glasgow", "Liverpool", "Leeds", "Sheffield", "Belfast", 
    "Edinburgh", "Cardiff", "Lome", "Conakry", "Banjul", "Bissau", 
    "Sao Tome", "Akureyri", "Bristol", "Newcastle upon Tyne", "Nottingham", 
    "Southampton", "Leicester", "Portsmouth", "Plymouth", "Aberdeen", 
    "Swansea", "Derry", "Galway", "Limerick", "Waterford", "Santa Cruz de Tenerife",
    "Las Palmas de Gran Canaria", "Arrecife", "Funchal", "Angra do Heroismo"
]

utc_plus_01 = [
    "Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt", "Vienna", 
    "Graz", "Paris", "Marseille", "Lyon", "Rome", "Milan", "Naples", 
    "Madrid", "Barcelona", "Valencia", "Amsterdam", "Rotterdam", 
    "Brussels", "Warsaw", "Krakow", "Prague", "Stockholm", "Oslo", 
    "Copenhagen", "Leogang", "Zurich", "Geneva", "Budapest", "Belgrade", 
    "Lagos", "Kinshasa", "Algiers", "Tunis", "Luanda", "Bratislava", 
    "Stuttgart", "Dusseldorf", "Dortmund", "Leipzig", "Bremen", "Linz", 
    "Salzburg", "Innsbruck", "Toulouse", "Nice", "Nantes", "Turin", 
    "Palermo", "Genoa", "Florence", "Seville", "Zaragoza", "Malaga", 
    "Antwerp", "Utrecht", "Luxembourg", "Ljubljana", "Zagreb", "Sarajevo", 
    "Skopje", "Tirana", "Libreville", "Brazzaville", "Douala", "Yaounde", 
    "Kano", "Ibadan", "Niamey", "Cotonou", "Ndjamena", "Bangui", "Bern",
    "Basel", "Lausanne", "Lucerne", "Lugano", "Vaduz", "Monaco", "San Marino",
    "Valletta", "Andorra la Vella", "Gdansk", "Wroclaw", "Poznan", "Lodz",
    "Szczecin", "Bialystok", "Gdynia", "Katowice"
]

utc_plus_02 = [
    "Athens", "Thessaloniki", "Helsinki", "Espoo", "Kyiv", "Lviv", 
    "Bucharest", "Cairo", "Alexandria", "Jerusalem", "Tel Aviv", 
    "Cape Town", "Johannesburg", "Sofia", "Tallinn", "Riga", "Vilnius", 
    "Beirut", "Amman", "Damascus", "Khartoum", "Harare", "Maputo", 
    "Tripoli", "Gaza", "Nicosia", "Odesa", "Kharkiv", "Cluj-Napoca", 
    "Tampere", "Vantaa", "Pretoria", "Durban", "Port Elizabeth", 
    "Gaborone", "Lusaka", "Lilongwe", "Kigali", "Bujumbura", "Windhoek", 
    "Chisinau", "Giza", "Port Said", "Suez", "Haifa", "Hebron", "Ramallah",
    "Nablus", "Patras", "Heraklion", "Limassol", "Larnaca", "Paphos",
    "Iasi", "Timisoara", "Constanta", "Craiova", "Galati", "Brasov", "Sibiu"
]

utc_plus_03 = [
    "Moscow", "Saint Petersburg", "Istanbul", "Ankara", "Riyadh", 
    "Jeddah", "Baghdad", "Nairobi", "Addis Ababa", "Minsk", "Doha", 
    "Kuwait City", "Manama", "Mogadishu", "Dar es Salaam", "Kampala", 
    "Antananarivo", "Djibouti", "Izmir", "Bursa", "Adana", "Gaziantep", 
    "Mecca", "Medina", "Basra", "Erbil", "Asmara", "Murmansk", "Voronezh", 
    "Rostov-on-Don", "Krasnodar", "Sana'a", "Aden", "Sochi", "Sevastopol",
    "Simferopol", "Tula", "Ryazan", "Lipetsk", "Yaroslavl", "Nizhny Novgorod",
    "Kazan", "Samara", "Volgograd", "Arkhangelsk", "Makhachkala", "Grozny"
]

utc_plus_04 = [
    "Dubai", "Abu Dhabi", "Sharjah", "Muscat", "Baku", "Yerevan", 
    "Tbilisi", "Port Louis", "Victoria", "Reunion", 
    "Samara", "Ajman", "Al Ain", "Ras Al Khaimah", "Ganja", "Batumi", 
    "Kutaisi", "Ulyanovsk", "Izhevsk", "Tolyatti", "Saratov", 
    "Astrakhan", "Fujairah", "Umm Al Quwain", "Sumqayit", "Rustavi",
    "Gyumri", "Vanadzor", "Kirov", "Penza", "Orenburg"
]

utc_plus_05 = [
    "Karachi", "Lahore", "Islamabad", "Tashkent", "Samarkand", 
    "Yekaterinburg", "Ashgabat", "Dushanbe", "Male", "Astana", "Oral", 
    "Faisalabad", "Rawalpindi", "Multan", "Hyderabad", "Perm", 
    "Chelyabinsk", "Ufa", "Tyumen", "Orenburg", "Magnitogorsk", "Khujand",
    "Bukhara", "Namangan", "Andijan", "Nukus", "Quetta", "Peshawar",
    "Gujranwala", "Sialkot", "Aktobe", "Atyrau", "Mangystau"
]

utc_plus_06 = [
    "Dhaka", "Chittagong", "Almaty", "Bishkek", "Omsk", "Thimphu", 
    "Novosibirsk", "Khulna", "Rajshahi", "Sylhet", "Taraz", 
    "Pavlodar", "Shymkent", "Barnaul", "Tomsk", "Kemerovo", "Novokuznetsk",
    "Osh", "Jalal-Abad", "Karakol", "Semey", "Ust-Kamenogorsk", "Kyzylorda"
]

utc_plus_07 = [
    "Bangkok", "Chiang Mai", "Hanoi", "Ho Chi Minh City", "Jakarta", 
    "Surabaya", "Phnom Penh", "Vientiane", "Krasnoyarsk", "Pontianak", 
    "Banda Aceh", "Nonthaburi", "Phuket", "Da Nang", "Haiphong", 
    "Bandung", "Medan", "Semarang", "Palembang", "Makassar", "Can Tho",
    "Denpasar", "Yogyakarta", "Solo", "Malang", "Batam", "Padang",
    "Udon Thani", "Nakhon Ratchasima", "Hat Yai", "Siem Reap", "Battambang"
]

utc_plus_08 = [
    "Beijing", "Shanghai", "Shenzhen", "Guangzhou", "Hong Kong", "Macau", 
    "Singapore", "Kuala Lumpur", "Manila", "Perth", "Taipei", "Ulaanbaatar", 
    "Makassar", "Irkutsk", "Denpasar", "Kuching", "Brunei", "Tianjin", 
    "Wuhan", "Chengdu", "Chongqing", "Nanjing", "Hangzhou", "Xian", 
    "George Town", "Ipoh", "Quezon City", "Davao City", "Cebu City", 
    "Zamboanga City", "Kota Kinabalu", "Sandakan", "Johor Bahru", "Malacca",
    "Kuantan", "Bandar Seri Begawan", "Xiamen", "Suzhou", "Harbin", "Dalian"
]

utc_plus_09 = [
    "Tokyo", "Yokohama", "Osaka", "Kyoto", "Seoul", "Busan", "Pyongyang", 
    "Sapporo", "Nagoya", "Fukuoka", "Hiroshima", "Dili", "Jayapura", 
    "Yakutsk", "Incheon", "Daegu", "Daejeon", "Gwangju", "Ulsan", "Sendai", 
    "Saitama", "Chiba", "Nara", "Kanazawa", "Kagoshima", "Okayama",
    "Kobe", "Kawasaki", "Kitakyushu", "Hamamatsu", "Niigata", "Jeju City"
]

utc_plus_10 = [
    "Sydney", "Melbourne", "Brisbane", "Canberra", "Gold Coast", 
    "Port Moresby", "Hobart", "Guam", "Saipan", "Vladivostok", 
    "Townsville", "Adelaide (Summer)", "Cairns", "Darwin", "Geelong", 
    "Newcastle", "Wollongong", "Launceston", "Sunshine Coast", 
    "Toowoomba", "Chita", "Khabarovsk", "Komsomolsk-on-Amur", "Ussuriysk",
    "Rockhampton", "Mackay", "Bundaberg", "Hervey Bay"
]

utc_plus_11 = [
    "Noumea", "Honiara", "Port Vila", "Magadan", "Sakhalin", 
    "Bougainville", "Srednekolymsk", "Pohnpei", "Yuzhno-Sakhalinsk",
    "Luganville", "Tanna", "Arawa", "Buka"
]

utc_plus_12 = [
    "Auckland", "Wellington", "Christchurch", "Suva", "Majuro", 
    "Tarawa", "Funafuti", "Petropavlovsk-Kamchatskiy", "Dunedin", 
    "Hamilton (NZ)", "Tauranga", "Napier", "Anadyr", "Yaren", "Nauru", 
    "Kwajalein", "Palmerston North", "Nelson", "New Plymouth", "Invercargill",
    "Labasa", "Lautoka", "Nadi"
]
#=======================================Funktionen===============================================#

def check_time_dif():
    try:
        if ort_1_e.get() in utc_00:
            time_1 = 0
        elif ort_1_e.get() in utc_minus_03:
            time_1 = -3
        elif ort_1_e.get() in utc_minus_04:
            time_1 = -4
        elif ort_1_e.get() in utc_minus_05:
            time_1 = -5
        elif ort_1_e.get() in utc_minus_06:
            time_1 = -6
        elif ort_1_e.get() in utc_minus_07:
            time_1 = -7
        elif ort_1_e.get() in utc_minus_08:
            time_1 = -8
        elif ort_1_e.get() in utc_minus_09:
            time_1 = -9
        elif ort_1_e.get() in utc_minus_10:
            time_1 = -10
        elif ort_1_e.get() in utc_plus_01:
            time_1 = 1
        elif ort_1_e.get() in utc_plus_02:
            time_1 = 2
        elif ort_1_e.get() in utc_plus_03:
            time_1 = 3
        elif ort_1_e.get() in utc_plus_04:
            time_1 = 4  
        elif ort_1_e.get() in utc_plus_05:
            time_1 = 5
        elif ort_1_e.get() in utc_plus_06:
            time_1 = 6
        elif ort_1_e.get() in utc_plus_07:
            time_1 = 7
        elif ort_1_e.get() in utc_plus_08:
            time_1 = 8
        elif ort_1_e.get() in utc_plus_09:
            time_1 = 9
        elif ort_1_e.get() in utc_plus_10:
            time_1 = 10
        elif ort_1_e.get() in utc_plus_11:
            time_1 = 11
        elif ort_1_e.get() in utc_plus_12:
            time_1 = 12
    except Exception as e:    
        print(e)
    try:
        if ort_2_e.get() in utc_00:
            time_2 = 0
        elif ort_2_e.get() in utc_minus_03:
            time_2 = -3
        elif ort_2_e.get() in utc_minus_04:
            time_2 = -4
        elif ort_2_e.get() in utc_minus_05:
            time_2 = -5
        elif ort_2_e.get() in utc_minus_06:
            time_2 = -6
        elif ort_2_e.get() in utc_minus_07:
            time_2 = -7
        elif ort_2_e.get() in utc_minus_08:
            time_2 = -8
        elif ort_2_e.get() in utc_minus_09:
            time_2 = -9
        elif ort_2_e.get() in utc_minus_10:
            time_2 = -10
        elif ort_2_e.get() in utc_plus_01:
            time_2 = 1
        elif ort_2_e.get() in utc_plus_02:
            time_2 = 2
        elif ort_2_e.get() in utc_plus_03:
            time_2 = 3
        elif ort_2_e.get() in utc_plus_04:
            time_2 = 4
        elif ort_2_e.get() in utc_plus_05:
            time_2 = 5
        elif ort_2_e.get() in utc_plus_06:
            time_2 = 6
        elif ort_2_e.get() in utc_plus_07:
            time_2 = 7
        elif ort_2_e.get() in utc_plus_08:
            time_2 = 8
        elif ort_2_e.get() in utc_plus_09:
            time_2 = 9
        elif ort_2_e.get() in utc_plus_10:
            time_2 = 10
        elif ort_2_e.get() in utc_plus_11:
            time_2 = 11
        elif ort_2_e.get() in utc_plus_12:
            time_2 = 12
    except Exception as e:    
        print(e)
    x = time_1 - time_2
    if x < 0:
        x *= -1
    result_d.config(text="Die Zeitdifferenz beträgt: {} Stunden".format(x))

def submit_s_time():
    global standort_uhr
    standort_info = "Salzburg"
    standort_uhr.config(text="Die Uhrzeit in {} ist gerade:".format(standort_info))

def submit_g_time():
    update_z()
    global gefragt_uhr 
    gefragt_info = gefragt.get()
    gefragt_uhr.config(text="Die Uhrzeit in {} ist gerade:".format(gefragt_info))

def update_s():
    time_string = strftime("%H:%M:%S")  
    date_string = strftime(" %d. %B, %Y") 
    standort_zeit.config(text="{} Uhr und der {}".format(time_string,date_string))
    standort_zeit.after(500,update_s)

def update_z():
    z = 0 
    gefragt_info = gefragt.get()
    try:
        if gefragt_info in utc_00:
            text = "utc_00"
            z = ((int(text[-2:]))*-1) - 1 #die 1 ist nur wegen Leogang, weil es utc_plus_01 ist
        elif gefragt_info in utc_minus_03:
            text = "utc_03"
            z = ((int(text[-2:]))*-1) - 1 
        elif gefragt_info in utc_minus_04:
            text = "utc_04"
            z = ((int(text[-2:]))*-1) - 1 
        elif gefragt_info in utc_minus_05:
            text = "utc_05"
            z = ((int(text[-2:]))*-1) - 1 
        elif gefragt_info in utc_minus_06:
            text = "utc_06"
            z = ((int(text[-2:]))*-1) - 1
        elif gefragt_info in utc_minus_07:
            text = "utc_07"
            z = ((int(text[-2:]))*-1) - 1
        elif gefragt_info in utc_minus_08:
            text = "utc_08"
            z = ((int(text[-2:]))*-1) - 1
        elif gefragt_info in utc_minus_09:
            text = "utc_09"
            z = ((int(text[-2:]))*-1) - 1
        elif gefragt_info in utc_minus_10:
            text = "utc_10"
            z = ((int(text[-2:]))*-1) - 1
        elif gefragt_info in utc_plus_01:
            text = "utc_01"
            z = int(text[-2:]) - 1
        elif gefragt_info in utc_plus_02:
            text = "utc_02"
            z = int(text[-2:]) - 1
        elif gefragt_info in utc_plus_03:
            text = "utc_03"
            z = int(text[-2:]) - 1
        elif gefragt_info in utc_plus_04:
            text = "utc_04"
            z = int(text[-2:]) - 1
        elif gefragt_info in utc_plus_05:
            text = "utc_05"
            z = int(text[-2:]) - 1
        elif gefragt_info in utc_plus_06:
            text = "utc_06"
            z = int(text[-2:]) - 1
        elif gefragt_info in utc_plus_07:
            text = "utc_07"
            z = int(text[-2:]) - 1
        elif gefragt_info in utc_plus_08:
            text = "utc_08"
            z = int(text[-2:]) - 1
        elif gefragt_info in utc_plus_09:
            text = "utc_09"
            z = int(text[-2:]) - 1
        elif gefragt_info in utc_plus_10:
            text = "utc_10"
            z = int(text[-2:]) - 1
        elif gefragt_info in utc_plus_11:
            text = "utc_11"
            z = int(text[-2:]) - 1
        elif gefragt_info in utc_plus_12:
            text = "utc_12"
            z = int(text[-2:]) - 1
    except Exception as e:    
        print(e)
    y = int(strftime("%H"))+z 
    day = int(strftime("%d"))
    if y > 23:
        day += 1
        y -= 24  # wenn es keine Uhrezeit ergibt
    elif y < 0:
        day -= 1
        y += 12
    time_string = strftime("{}:%M:%S".format(y))  
    date_string = strftime(" {}. %B, %Y".format(day)) 
    gefragt_zeit.config(text="{} Uhr und der {}".format(time_string,date_string))
    gefragt_zeit.after(500,update_z)

window = Tk()
#===========================Design======================================#
window.title("Zeitrechner_Mei")
notebook = ttk.Notebook(window)
tab1 = Frame(notebook)                        #Tabs
tab2 = Frame(notebook)
about = Frame(notebook)
notebook.add(tab1,text="Uhrzeit")
notebook.add(tab2,text="Zeitdifferenzrechner")
notebook.add(about,text="Gründer")
Label(about,text="Lukas Meissner hat dieses Tool gebaut!!",width=50,height=25).pack()
notebook.pack(expand=True, fill="both")
#=========================tab1=====================================#
standort_b = Label(tab1, text="Standort:").grid(row=0,column=0) 
standort_info = ""  
standort = Label(tab1,text="Salzburg", highlightthickness=2, highlightbackground="red")                                     #Standort
standort.grid(row=0, column=1)
standort_uhr = Label(tab1,text="Die Uhrzeit in Salzburg ist gerade:",highlightthickness=2, highlightbackground="blue")
standort_uhr.grid(row=1,column=0,columnspan=3)

gefragt_b = Label(tab1,text="Wie spät ist es in:").grid(row=0,column=3,pady=15)
gefragt_info = ""
gefragt = Entry(tab1)
gefragt.grid(row=0,column=4,pady=15)                                                           #Gefragter Ort
gefragt_uhr = Label(tab1,text="Die Uhrzeit in ? ist gerade:", highlightthickness=2, highlightbackground="blue")
gefragt_uhr.grid(row=1,column=3,columnspan=3) 
gefragt_sub = Button(tab1,text="enter",command=submit_g_time)
gefragt_sub.grid(row=0,column=5)
#================================tab2====================================#
ort_1 = Label(tab2, text="Ort 1:").grid(row=0,column=0)
ort_1_e = Entry(tab2)
ort_1_e.grid(row=0,column=1)

ort_2 = Label(tab2, text="Ort 2:").grid(row=0,column=3)
ort_2_e = Entry(tab2)
ort_2_e.grid(row=0,column=4)

d_berechener = Button(tab2, text="Differenz berechnen", command=check_time_dif)
d_berechener.grid(row=1,column=2)

result_d = Label(tab2, text="")
result_d.grid(row=2,column=0,columnspan=5)
#=============================Uhren===================================#
standort_zeit = Label(tab1,text="",highlightthickness=2, highlightbackground="red") #uhr standort
standort_zeit.grid(row=2,column=0,columnspan=3)

gefragt_zeit = Label(tab1,text="?",highlightthickness=2, highlightbackground="red") #uhr gefragt
gefragt_zeit.grid(row=2,column=3,columnspan=3)

update_s()

window.update_idletasks()
window.geometry("")
window.resizable(False, False)

window.mainloop()