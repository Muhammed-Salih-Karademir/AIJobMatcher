# AIJobMatcher

AIJobMatcher is an innovative tool designed to bridge the gap between job seekers and their ideal job positions. Leveraging the power of OpenAI's text embeddings, AIJobMatch calculates the similarity between job descriptions and a candidate's CV, classifying jobs such as Low Fit, Medium Fit, and High Fit. This not only streamlines the job search process but also enhances the recruitment pipeline for companies looking for the perfect candidate.

## Features

- **CV to Job Description Matching**: Utilizes advanced AI algorithms to match CV content with job descriptions.
- **Fit Classification**: Classifies jobs into Low, Medium, and High fit based on the similarity score.
- **Easy Integration**: Designed for easy integration with job boards and HR software.
- **Customizable Matching Criteria**: Allows for customization of matching criteria to suit different job sectors and roles.

## Getting Started

### Prerequisites

- Python 3.6+
- OpenAI API key

### Installation

Clone the repository and install the required packages:

```bash
git clone https://github.com/yourusername/AIJobMatch.git
cd AIJobMatch
```
### What input and Output

You will give your resume like a resume.json file.
```
{
    "resume": "I am a Python Developer."
}
```
You will give job descriptions like a jobs.json file.
```
[
    {
        "URL": "https://www.linkedin.com/in/muhammed-salih-karademir/",
        "Job Description": "We are hiring a Python developer."
    },
    {
        "URL": "https://www.linkedin.com/in/muhammed-salih-karademir/",
        "Job Description": "We are hiring a Manager Assistant."
    },
    {
        "URL": "https://www.linkedin.com/in/muhammed-salih-karademir/",
        "Job Description": "We are hiring Rust developer."
    }
]
```
You will get results like a similarity_scores.json file.
```
[
    {
        "url": "https://www.linkedin.com/in/muhammed-salih-karademir/",
        "similarity_score": 0.9165565975468735,
        "fit_class": "High Fit"
    },
    {
        "url": "https://www.linkedin.com/in/muhammed-salih-karademir/",
        "similarity_score": 0.7720302865084372,
        "fit_class": "Low Fit"
    },
    {
        "url": "https://www.linkedin.com/in/muhammed-salih-karademir/",
        "similarity_score": 0.814412820982544,
        "fit_class": "Medium Fit"
    }
]
```
