hotel_dic = {
    'Name': 'Paradise Resort',
    'Stars':'5',
    'Rooms': [
        {
            'Rooms Number': '1',
            'Floor':'1',
            'Price per night':'$1000'
        },
        {
            'Rooms Number': '6',
            'Floor':'6',
            'Price per night':'$1500'
        },
        {
            'Rooms Number': '10',
            'Floor':'Penthouse',
            'Price per night':'$5500'
        }
    ]

}

print(hotel_dic['Rooms'][2]['Price per night'])