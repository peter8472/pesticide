import json
import os.path
import p.dblog
import sqlite3



if __name__ == "__main__":
    # logger = p.dblog.Dblog("regno.db")
    conn = sqlite3.connect('regno.db')
    cur= conn.cursor()
    cur.execute("select url,stuff from log limit 1990")
    rows = cur.fetchall()
    for x in rows:
        stuff= json.loads(x[1])
        assert len(stuff['items']) ==1
        item=stuff['items'][0]
        # print(item.keys())
        print()
        print(item['productname'])
        for ingred in item['active_ingredients']:
            print(ingred['active_ing'], ingred['active_ing_percent'])
            if ingred['active_ing'] == 'Ferric HEDTA':
                print(json.dumps(item, indent=4))
                exit(0)

