import pg

database=pg.DB(
    host='localhost',
    user='postgres',
    passwd='Kristine'
)

database.query("CREATE DATABASE dcrm")

print("All done!")