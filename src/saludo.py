from datetime import datetime
hora_actual = datetime.now().hour
if hora_actual < 12:
    print("Buenos días")
elif 12 <= hora_actual < 18:
    print("Buenas tardes")
else:
    print("Buenas noches")  
