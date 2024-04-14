while True:

    def find_nth_occurrence(string, sub_string, n):
        start_index = string.find(sub_string)
        while start_index >= 0 and n > 1:
            start_index = string.find(sub_string, start_index + 1)
            n -= 1
        return start_index
    
    def bekol(x):
        dest = input("Enter the destination airport ICAO: ")
        if dest == "ZGGG":
            print("4200M(FL138) / 4500M(FL148)")
        elif dest == "ZGSZ":
            print("1800M(5900ft)")
        elif x.find("B330") != -1:
            print("9200M(FL301)\n9800M(FL321)\n10400M(FL341)\n11000M(FL361)\n11600M(FL381)\n12200M(FL401)")
        else:
            print("8900M(FL291)\n9500M(FL311)\n10100M(FL331)\n10700M(FL351)\n11300M(FL371)\n11900M(FL391)\n12500M(FL411)")
    
    def ocean():
        print("FL290 / FL330 / FL370 / FL390 / FL410")
        
    def lakes():
        dest = input("Enter the destination ICAO: ")
        if dest == "ZSHC" or dest == "ZSYW" or dest == "ZSNB":
            print("8100M(FL266) / FL330")
        elif dest == "ZGOW":
            print("4500M(FL148)")
        elif dest == "ZSAM" or dest == "ZSQZ":
            print("5100M(FL167) / 6300M(FL207) / 7500M(FL246)")
        elif dest == "ZSFZ" or dest == "ZSWY" or dest == "ZSWZ":
            print("6300M(FL207) / 7500M(FL246)")
        else:
            print("8100M(FL266) / FL330 / FL350 / FL390")
    
    def pecan(x):
        print("")
    
    
    route = input("Enter the route: ")
    
    sid = 5
    
    if sid == -1:
        print("Invalid SID")
    else:
        if route[0:sid] == "BEKOL":
            bekol(route)
        elif route[0:sid] == "LAKES":
            exitAirway = find_nth_occurrence(route, " ", 4)
            if route[exitAirway-4:exitAirway] == "A470":
                lakes()
            elif route[exitAirway-4:exitAirway] == "M503":
                print("FL330 / FL350")
        elif route[0:sid] == "OCEAN":
            exitFix = find_nth_occurrence(route, " ", 3)
            if route[exitFix-5:exitFix] == "ELATO":
                print("Odd number FL at or below FL270")
            elif route[exitFix-5:exitFix] == "ENVAR":
                print("FL270 / ... (ODD num) / FL410 / FL450 / FL490")
            elif route[exitFix-5:exitFix] == "NOMAN" or route[exitFix-5:exitFix] == "SABNO":
                print("FL290 / FL330 / FL370 / FL410")
            else:
                ocean()
        elif route[0:sid] == "PECAN":
            #PECAN V10 SIKOU A202 ISBIG
            
            exitFix = find_nth_occurrence(route, " ", 3)
            if route[exitFix-5:exitFix] == "SIKOU":
                exitAirway = find_nth_occurrence(route, " ", 4)
                if route[exitAirway-4:exitAirway] == "A202":
                    dest = input("Enter the destination ICAO: ")
                    if dest == "ZJHK" or dest == "ZJQH":
                        print("6600M(FL217) / 7200M(FL236)")
                    elif dest == "ZJSY":
                        print("8400M(FL276)")
                    else:
                        print("10400M(FL341) / 11600M(FL381) / 12200M(FL401)")
                elif route[exitAirway-4:exitAirway] == "R339":
                    dest = input("Enter the destination ICAO: ")
                    if dest == "ZGBH" or dest == "ZGNN":
                        print("7200M(FL236) / 7800M(FL256)")
                    elif dest == "ZGZJ":
                        print("6000M(FL197)")
                    else:
                        print("9200M(FL301)\n9800M(FL321)\n10400M(FL341)\n11000M(FL361)\n11600M(FL381)\n12200M(FL401)")
            elif route[exitFix-5:exitFix] == "IDOSI":
                print("FL280 / FL300 / FL340 / FL380 / FL400 / FL430")
            elif route[exitFix-5:exitFix] == "EPDOS":
                print("FL280 / FL310 / FL320 / FL350 / FL360 / FL390 / FL400")