import pandas as pd


# EXTRACT
df = pd.read_csv('Football teams.csv')
# print(df.info())
# print(df.head())


import sqlite3


# LOAD DATABASE 
conn = sqlite3.connect('serie_a.db')
# df.to_sql('squadre', conn, if_exists='replace', index=False)
# print('Database creato')


# QUERY SQL
cursor = conn.cursor()

# tutte le squadre di serie A ordinate per gol
query = """ 
SELECT team, Goals, yellow_cards, red_cards
FROM squadre
WHERE Tournament = 'Serie A'
ORDER BY Goals DESC
"""

cursor.execute(query)
risultati = cursor.fetchall()

print('\n--- Squadre Serie A per gol ---')
for riga in risultati:
    print(riga)


# top 3 squadre per possesso palla
query2 = '''
SELECT team, [Possession%]
FROM squadre
WHERE Tournament = 'Serie A'
ORDER BY [Possession%] DESC
LIMIT 3
'''

cursor.execute(query2)
print('\n--- Top 3 possesso palla ---')
for riga in cursor.fetchall():
    print(riga)


# squadre con più di 80 cartellini gialli
query3 = '''
SELECT Team, yellow_cards
FROM squadre
WHERE Tournament = 'Serie A'
AND yellow_cards > 80
ORDER BY yellow_cards DESC
'''

cursor.execute(query3)
print('\n--- Squadre più indisciplinate ---')
for riga in cursor.fetchall():
    print(riga)


# LOAD 
df_risultati = pd.read_sql_query("SELECT * FROM squadre WHERE Tournament = 'Serie A'", conn)
df_risultati.to_csv('risultati_sql.csv', index=False)
print('\nFile salvato: risultati_sql.csv')

# chiusura connessione
conn.close()

                                 


