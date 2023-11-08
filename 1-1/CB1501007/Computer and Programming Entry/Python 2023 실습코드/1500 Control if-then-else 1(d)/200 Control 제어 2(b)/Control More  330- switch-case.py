
def switch_demo(argument):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    return(  switcher.get(argument, "Invalid month") )


for w in [1,5, 8, 9, 12, 15] :
    mname = switch_demo( w )
    print ( f' Number= {w},  { mname }')






