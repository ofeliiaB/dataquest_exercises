## 1. Introduction ##

import pandas as pd

job_postings = pd.read_csv("DataEngineer.csv")


num_rows = job_postings.shape[0]
num_cols = job_postings.shape[1]

## 2. Counting Word Occurrences ##

job_postings["Job Description"] = job_postings["Job Description"].str.lower()

frequency = {}

frequency["postgres"] = job_postings["Job Description"].str.count("postgres").sum()

frequency["sql"] = job_postings["Job Description"].str.count("sql").sum()

print(frequency)

## 3. Counting All Skills ##

import pandas as pd

skills = pd.read_csv("Skills.csv")

frequency = {}

for skill_name in skills["Name"]:
    frequency[skill_name] = job_postings["Job Description"].str.count(skill_name).sum()

print(frequency["programming"])
    

## 4. Functionize the Code ##

import time

#frequency = {}
#for skill_name in skills["Name"]:
#    frequency[skill_name] = job_postings["Job Description"].str.count(skill_name).sum()

def count_skills(job_postings, skills):
    frequency = {}
    for skill_name in skills["Name"]:
        frequency[skill_name] = job_postings["Job Description"].str.count(skill_name).sum()
    return frequency


start = time.time()
count_skills(job_postings, skills)
end = time.time()
runtime = end-start
print(runtime)

## 5. Splitting a DataFrame into Chunks ##

import math


def make_chunks(df, num_chunks):
    num_rows = df.shape[0]
    chunk_size = math.ceil(num_rows/num_chunks)
    
    num_chunks = [df[i:i+chunk_size] for i in range(0, num_rows, chunk_size)]
    return num_chunks


skill_chunks = make_chunks(skills, 8)

## 6. Process Pool Executor ##

import concurrent.futures

def increment(value):
    return value + 1

values = [1, 2, 3, 4, 5, 6, 7, 8]

with concurrent.futures.ProcessPoolExecutor() as executor:
    futures = [executor.submit(increment, val) for val in values]

results = [future.result() for future in futures]
print(results)

## 7. Multiprocessing Job Posting Analysis ##

import concurrent.futures

skill_chunks = make_chunks(skills, 8)

with concurrent.futures.ProcessPoolExecutor() as executor:
    futures = [executor.submit(count_skills, job_postings, skill_chunk) for skill_chunk in skill_chunks]

results = [future.result()  for future in futures]

print(results[0])

## 8. Merging Results ##

merged_results = {}

for result in results:
    merged_results.update(result)

## 9. Performance Improvement ##

def count_skills(job_postings, skills):
    frequency = {}
    for skill_name in skills["Name"]:
        frequency[skill_name] = job_postings["Job Description"].str.count(skill_name).sum()
    return frequency

def count_skills_parallel(job_postings, skills, num_processes=4):
    # Calculate results using paralleld processing
    skill_chunks = make_chunks(skills, num_processes)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(count_skills, job_postings, skill_chunk) for skill_chunk in skill_chunks]
    results = [future.result() for future in futures]
    # Merge results
    merged_results = {}
    for result in results:
        merged_results.update(result)
    return merged_results

import time
start = time.time()
count_skills(job_postings, skills)
end = time.time()
time_normal = end-start

start_2 = time.time()
count_skills_parallel(job_postings, skills)
end_2 = time.time()
time_parallel = end_2 - start_2

print(time_normal/time_parallel)