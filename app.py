from fastapi import FastAPI, Query, HTTPException
from typing import List, Dict, Any
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()
df = pd.read_csv('jobs_with_skills.csv')


def recommend_jobs(user_skills: str, df: pd.DataFrame, top_n: int = 3) -> List[Dict[str, Any]]:
    # Convert user skills to a set
    user_skills_set = set(user_skills.lower().split(', '))

    def count_matching_skills(job_skills: str) -> int:
        job_skills_set = set(eval(job_skills))
        return len(user_skills_set.intersection(job_skills_set))

    # Count matching skills for each job
    df['matching_skills'] = df['skills'].apply(count_matching_skills)

    # Iterate from full skill set down to 1
    for required_skills in range(len(user_skills_set), 0, -1):
        df_filtered = df[df['matching_skills'] >= required_skills]

        if not df_filtered.empty:
            vectorizer = TfidfVectorizer()
            job_skills_tfidf = vectorizer.fit_transform(df_filtered['skills'].apply(lambda x: ' '.join(eval(x))))
            user_skills_tfidf = vectorizer.transform([user_skills])
            similarity_scores = cosine_similarity(user_skills_tfidf, job_skills_tfidf)
            df_filtered['similarity'] = similarity_scores.flatten()

            # Sort by matching skills and similarity
            df_sorted = df_filtered.sort_values(by=['matching_skills', 'similarity'], ascending=[False, False])
            top_recommendations = df_sorted.head(top_n)[['Name', 'matching_skills', 'similarity', 'skills']]
            return top_recommendations.to_dict(orient='records')

    return []


# @app.get("/")
# def read_root():
#     return {"message": "Welcome"}


@app.get("/recommend/")
def get_recommendations(skills: str = Query(..., description="Comma-separated list of skills")) -> Dict[str, Any]:
    user_skills = skills.strip()

    # Validate input
    if not user_skills:
        raise HTTPException(
            status_code=400, detail="Skills list cannot be empty.")

    recommendations = recommend_jobs(user_skills, df)

    if recommendations:
        return {
            "user_skills": user_skills,
            "recommendations": [
                {
                    "job_title": job["Name"],
                    "matching_skills": job["matching_skills"],
                    "similarity_score": round(job["similarity"], 2),
                    # Consider replacing eval() with safer methods
                    "job_skills": eval(job["skills"])
                }
                for job in recommendations
            ]
        }
    else:
        return {"message": "No matching jobs found."}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
