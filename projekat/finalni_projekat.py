import numpy as np
import pandas as pd
import logging
import time
import psycopg2
from uuid import uuid4

start_time_entire_project = time.time()

logging.basicConfig(filename="rezultati.log", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

data = pd.read_csv("data.csv")

for index, row in data.iterrows():
    distribution = row["distribution"]
    sample_size = row["sample_size"]
    arg1 = row["arg1"]
    arg2 = row["arg2"]
    
    start_time = time.time()
    if distribution == "poisson":
        sample = np.random.poisson(arg1, size=sample_size)
    elif distribution == "uniform":
        sample = np.random.uniform(arg1, arg2, size=sample_size)
    elif distribution == "weibull":
        sample = np.random.weibull(arg1, size=sample_size)
    elif distribution == "normal":
        sample = np.random.normal(arg1, arg2, size=sample_size)
    end_time = time.time()

    #distributions = {'poisson': np.random.poisson, 'uniform': np.random.uniform, 'weibull': np.random.weibull, 'normal': np.random.normal}
    #sample = distributions[distribution](*([arg1, arg2][:len(inspect.signature(distributions[distribution]).parameters)-2]), size=sample_size)

    start_time_2 = time.time()
    std = np.std(sample)
    mean = np.mean(sample)
    end_time_2 = time.time()
    
    logging.info(f"Za red sa indeksom {index}: standardna devijacija = {std}, srednja vrednost = {mean}")
    logging.info(f"Trajanje procesa za red sa indeksom {index} - uzorak: {end_time - start_time:.4f}s, std i mean: {end_time_2 - start_time_2:.4f}s")


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
print("Time of executing whole process is : ", finale_converted_time)