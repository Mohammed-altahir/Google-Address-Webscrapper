def storeInADatabase():
    import sqlite3
    import json
    
    files = []
    with open('results.json','r') as file:
        
        files = json.load(file)
        print(type(files))
    

    data = 'database' #Enter your database name here
    connection = sqlite3.connect(f'{data}.db')
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE "YOUR TABLE NAME" (
        Name text,
        Address text,
        "Google Maps Address" text
    )''')
    connection.commit()
    records = []
    for record in files:
        columns = (record['name'],record['address'],record['google_maps_address'])
        records.append(columns)
    cursor.executemany('INSERT INTO "YOUR TABLE NAME" VALUES (?,?,?)',(records))
    connection.commit()
    
    # this code is justt only for check everything went fine :)

    # cursor.execute(f'SELECT rowid, * from "YOUR TABLE NAME"')
    # items = cursor.fetchall()
    # for item in items:
    #     print(item)
    
    # connection.commit()


