
# MaroPolo AI Model Endpoints
![Silk Road Logo](./assets/logo.jpg)

## Overview

This project implements a job recommendation system that analyzes job descriptions and recommends suitable jobs based on a user's skill set. It uses natural language processing (NLP) techniques to extract skills from job summaries and machine learning methods to match these skills with user-provided skills.

![Silk Road Logo](./assets/silkroad.jpg)

### "The journey is long, but with the right path and perseverance, you'll discover new worlds of knowledge."
— Marco Polo

![Silk Road Mood Board](./assets/SilkRoadMoodBoard.png)


## Files

- `app.py`: Contains the FastAPI application code to serve job recommendations via an API endpoint.
- `Final copy.ipynb`: Jupyter Notebook with the final analysis and processing steps.
- `Indeed_10k.csv`: Original dataset containing job summaries and other details.
- `jobs_with_skills.csv`: Processed dataset with extracted skills from job summaries.
- `requirements.txt`: List of Python packages required for the project.
- `skills.csv`: List of relevant skills used for skill extraction.

## Setup

### Create and Activate a Virtual Environment

Create a virtual environment to manage project dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
**Clone the Repository**

   ```bash
   git clone https://github.com/SilckRoad-MarcoPolo/SilkRoad_AI_API.git
   cd SilkRoad_AI_API.git

```

````

### Install Dependencies

Ensure you have the following packages listed in `requirements.txt`:

```
fastapi
uvicorn
pandas
scikit-learn
nltk
```

Install them using:

```bash
pip install -r requirements.txt
```

## Usage

### Data Processing

- **Extract Skills**: The script processes job summaries to extract relevant skills and saves the results to `jobs_with_skills.csv`. It uses predefined skill lists and NLP techniques to identify and extract skills from job descriptions.
- **Recommendation**: The `recommend_jobs` function matches user-provided skills with job skills from the dataset and recommends the top N jobs. It calculates the similarity between user skills and job skills to generate the recommendations. The AI generates three different job recommendations for the user based on the highest matching skills and similarity scores.

### Example Response

````markdown
# API Documentation

## Start the Server

To start the server, run the following command:

```bash
uvicorn app:app --reload
```
````

This will start the server at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## API Endpoint

### Recommendation Endpoint

- **Endpoint:** `/recommend/`
- **Method:** `GET`
- **Query Parameter:** `skills` (comma-separated list of skills)

### Example Request

```http
GET /recommend/?skills=javascript, node.js
```

### Response

The API returns a JSON object with the user's skills and a list of recommended jobs. Here’s a sample response:

The response will include job titles and additional skills needed based on the input skills.

```json
{
    "user_skills": "javascript, node.js",
    "recommendations": [
        {
            "job_title": "full stack software engineer",
            "matching_skills": 1,
            "similarity_score": 0.71,
            "job_skills": [
                "java",
                "scala",
                "Node.js",
                "c++",
                "javascript"
            ]
        },
        {
            "job_title": "full stack developer",
            "matching_skills": 1,
            "similarity_score": 0.65,
            "job_skills": [
                "React",
                "java",
                "Node.js",
                "Angular",
                "c#",
                "javascript",
                "python"
            ]
        },
        {
            "job_title": "growth engineer",
            "matching_skills": 1,
            "similarity_score": 0.59,
            "job_skills": [
                "scripting",
                "React",
                "ply",
                "Node.js",
                "typescript",
                "ai",
                "javascript"
            ]
        },
        {
            "job_title": "software engineer automation - quality",
            "matching_skills": 1,
            "similarity_score": 0.55,
            "job_skills": [
                "Go",
                "java",
                "Node.js",
                "ruby",
                "php",
                "javascript",
                "python"
            ]
        },
        {
            "job_title": "software development engineer in test intern",
            "matching_skills": 1,
            "similarity_score": 0.51,
            "job_skills": [
                "scripting",
                "React",
                "css",
                "visual",
                "scala",
                "ply",
                "js",
                "Node.js",
                "ai",
                "html",
                "Git",
                "automation",
                "javascript",
                "python"
            ]
        }
    ]
}
```

- **user_skills**: The list of skills provided by the user.
- **recommendations**: A list of the top 3 job recommendations generated by the AI.
  - **job_title**: The title of the recommended job.
  - **matching_skills**: The number of skills from the user that match the job requirements.
  - **similarity_score**: A score representing the similarity between the user's skills and the job's required skills.
  - **job_skills**: A list of skills required for the job.

The AI generates and returns three different job recommendations based on:

1. **Matching Skills**: The number of skills that the user has which match the skills required for the job.
2. **Similarity Score**: A calculated score indicating how similar the user's skills are to the job's required skills, with higher scores indicating better matches.

## API Documentation

For detailed API documentation, please refer to the Postman collection:

[Postman API Documentation](https://documenter.getpostman.com/view/29368996/2sAXqne4Yp)

## Deployment

The application is deployed and can be accessed at:

[Deployed Application](https://recipe-recommender-w5nk.onrender.com/recommend/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [NLTK](https://www.nltk.org/) for natural language processing.
- [Scikit-learn](https://scikit-learn.org/) for machine learning tools.


