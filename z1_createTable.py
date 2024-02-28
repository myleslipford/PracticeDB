import sqlite3

conn = sqlite3.connect("datdbaseFile.db")
cr = conn.cursor()

cr.execute("""CREATE TABLE IF NOT EXISTS movies( 
           Id INTERGER PRIMARY KEY,
           title TEXT,
           dircector TEXT,
           year Integer,
           genre TEXT )
           """)

#table should be created with those attributes/colummn names 