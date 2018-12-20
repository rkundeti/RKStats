import csv, pypyodbc as pyodbc
conn = pyodbc.connect("DRIVER=NetezzaSQL;SERVER=ibmnetqa;PORT=5480;DATABASE=BMIS_STG;UID=BMIS_ETL_USR;PWD=ptmd3233;")
cursor = conn.cursor()
cursor.execute("TRUNCATE TABLE STG_CDM_RGPRID_TEST")
with open('US_MDM_RGPRID_201600430.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['RGPRID'], i['AGECID']) for i in dr]

cursor.executemany("INSERT INTO STG_CDM_RGPRID_TEST (RGPRID , AGECID) VALUES (?, ?);", to_db)
conn.commit()
