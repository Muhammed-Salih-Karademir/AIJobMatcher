""" OpenAI’s text embeddings measure the relatedness of text strings. """
import numpy as np
from openai import OpenAI
import json

api_key = 'YOUR_OPENAI_API_KEY_HERE'

client = OpenAI(
    api_key=api_key,
)

def read_and_process_jobs(file_path):
    """
    Reads job listings from a JSON file and processes them into a list of dictionaries.
    Each dictionary contains the URL and job description.
    
    :param file_path: Path to the JSON file containing job listings.
    :return: A list of dictionaries, each containing a job's URL and description.
    """
    job_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        jobs = json.load(file)  # Load jobs from JSON file into a list of dictionaries
    
    for job in jobs:
        url = job.get("URL", "").strip()
        job_description = job.get("Job Description", "").strip().replace('\n', ' ')
        job_list.append({"url": url, "job_description": job_description})
    
    return job_list

def determine_fit_class(score, low_limit, high_limit):
    """
    Determines the fit class based on the similarity score and predefined limits.
    
    :param score: The similarity score to classify.
    :param low_limit: The lower limit for classification.
    :param high_limit: The higher limit for classification.
    :return: A string representing the fit class ('Low Fit', 'Medium Fit', 'High Fit').
    """
    if score < low_limit:
        return "Low Fit"
    elif low_limit <= score < high_limit:
        return "Medium Fit"
    else:
        return "High Fit"

def process_jobs_and_save_results(cv_path, jobs_path, output_path):
    """
    Processes job listings, calculates similarity scores between a CV and job descriptions,
    classifies the results, and saves them to a JSON file.
    
    :param cv_path: Path to the file containing the CV text.
    :param jobs_path: Path to the file containing job listings.
    :param output_path: Path where the results JSON will be saved.
    """

    with open(cv_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    
    cv = data.get("resume", "").replace('\n', '') 

    # Read and process job listings
    jobs = read_and_process_jobs(jobs_path)

    similarity_scores = []

    # Calculate similarity scores for each job description
    for job in jobs:
        try:
            resp = client.embeddings.create(
                input=[cv, job["job_description"]],
                model="text-embedding-ada-002"
            )
            embedding_a = np.array(resp.data[0].embedding)
            embedding_b = np.array(resp.data[1].embedding)

            # Normalize embeddings and calculate similarity score
            norm_a = np.linalg.norm(embedding_a)
            norm_b = np.linalg.norm(embedding_b)
            embedding_a_normalized = embedding_a / norm_a
            embedding_b_normalized = embedding_b / norm_b

            similarity_score = np.dot(embedding_a_normalized, embedding_b_normalized)
            similarity_scores.append(similarity_score)

        except Exception as e:
            print(f"An error occurred: {e}")

    # Calculate statistics for classification limits
    mean_score = np.mean(similarity_scores)
    std_dev = np.std(similarity_scores)
    low_limit = mean_score - std_dev
    high_limit = mean_score + std_dev

    # Classify and save results to a JSON file
    results = []
    for score, job in zip(similarity_scores, jobs):
        fit_class = determine_fit_class(score, low_limit, high_limit)
        results.append({"url": job["url"], "similarity_score": score, "fit_class": fit_class})

    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(results, file, indent=4)

# Call the main function with file paths
process_jobs_and_save_results('resume.json', 'jobs.json', 'similarity_scores.json')
