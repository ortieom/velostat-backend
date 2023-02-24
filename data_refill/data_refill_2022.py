from config_reader import read_config
import psycopg2
import csv

city_folder = './archives/'
city = 'msc'

conn = psycopg2.connect(**read_config("db"))
cursor = conn.cursor()
# print('connected', flush=True)
#
# # copying stations_metadata
# print('metadata: ', end='', flush=True)
# with open(city_folder+'stations_metadata.csv', 'r', encoding="utf-8", newline='') as file:
#     reader = csv.reader(file, quotechar='"')
#     for row in reader:
#         sql = f"INSERT INTO stations_metadata_{city}(velobike_id, lat, lon) VALUES(%s, %s, %s)"
#         cursor.execute(sql, (row[-1], row[4], row[5]))
# print('done', flush=True)
#
#
# # copying testday
# print('testday: ', end='', flush=True)
# with open(city_folder+'testday.csv', 'r', encoding="utf-8", newline='') as file:
#     reader = csv.reader(file, quotechar='"')
#     for row in reader:
#         sql = f"INSERT INTO testday_{city}\
#         (velobike_id, timestamp, ordinarybikes_delta_taken, \
#         ordinarybikes_delta_returned) VALUES (%s, %s, %s, %s)"
#         cursor.execute(sql, tuple('0' if x == '' else x for x in row))
# print('done', flush=True)

conn.commit()
cursor.close()
conn.close()
