import csv
import logging
import time
import threading
import numpy as np
import psycopg2

start_time_entire_project = time.time()

logging.basicConfig(filename='sample.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def process_row(row):
    distribution = row[0]
    sample_size = int(row[1])
    arg1 = float(row[2]) if row[2] else None
    arg2 = float(row[3]) if row[3] else None

    if distribution == 'poisson':
        sample = np.random.poisson(arg1, sample_size)
    elif distribution == 'uniform':
        sample = np.random.uniform(arg1, arg2, sample_size)
    elif distribution == 'weibull':
        sample = np.random.weibull(arg1, sample_size)
    elif distribution == 'normal':
        sample = np.random.normal(arg1, arg2, sample_size)
    elif distribution == 'binomial':
        sample = np.random.binomial(arg1, arg2, sample_size)

    start_time = time.time()
    mean = np.mean(sample)
    std_dev = np.std(sample)
    elapsed_time = time.time() - start_time

    log_msg = f"Row: {row}, Mean: {mean}, Standard deviation: {std_dev}, Time elapsed: {elapsed_time:.6f} seconds"
    logging.info(log_msg)

"""
- Funkcija kao argument uzima niz redova
- Prolazi kroz svaki red i od svakog reda pravi jednu nit
- zatim je pokrece i dodaju u listu niti (t.start i threads.append(t))
- potom ceka da se sve niti zavrse (t.join)
"""
def process_rows_parallel(rows):
    threads = []

    for row in rows:
        t = threading.Thread(target=process_row, args=(row,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    rows = list(reader)

start_time = time.time()
process_rows_parallel(rows)
elapsed_time = time.time() - start_time

logging.info(f"Total elapsed time: {elapsed_time:.6f} seconds")


def inserting_time_into_stats_table():
    conn = psycopg2.connect(host="localhost",database="db_project",user="postgres",password="uros")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS stats (
            id SERIAL PRIMARY KEY,
            duration REAL NOT NULL
        );
    """)
    conn.commit()
    insert_data = (1,finale_converted_time)
    cur.execute("INSERT INTO stats (id, duration) VALUES (%s, %s)", insert_data)
    conn.commit()
    
    cur.close()
    conn.close()

# inserting_time_into_stats_table()

def update_sample_size():
    conn = psycopg2.connect(host="localhost",database="db_project",user="postgres",password="uros")
    cur = conn.cursor()
    cur.execute("SELECT sample_size FROM db_table")
    rows = cur.fetchall()
    
    for row in rows:
        if row[0] == 1000:
            new_value = 100000
        elif row[0] == 100000:
            new_value = 1000
        else:
            continue
        
        cur.execute("UPDATE db_table SET sample_size = %s WHERE sample_size = %s", (new_value, row[0]))
        conn.commit()
    
    cur.close()
    conn.close()

end_time_entire_project = time.time()
total_time_entire_project = end_time_entire_project - start_time_entire_project
rounded_number = round(total_time_entire_project,4)
finale_converted_time = str(rounded_number)
print("Time of executing whole process with THREADS is : ", finale_converted_time)