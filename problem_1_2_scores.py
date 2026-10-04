import requests
import matplotlib.pyplot as plt

API_URL = "https://api.slingacademy.com/v1/sample-data/files/student-scores.json"

# 1. Fetch student data
response = requests.get(API_URL, timeout=10)
response.raise_for_status()

students = response.json()

# 2. Subjects to analyze
subjects = {
    "Math": "math_score",
    "History": "history_score",
    "Physics": "physics_score",
    "Chemistry": "chemistry_score",
    "Biology": "biology_score",
    "English": "english_score",
    "Geography": "geography_score"
}

# 3. Calculate average score for each subject
average_scores = {}

for subject, field in subjects.items():
    total = sum(student[field] for student in students)
    average = total / len(students)
    average_scores[subject] = average

# 4. Display averages
print("Average Scores:")

for subject, average in average_scores.items():
    print(f"{subject}: {average:.2f}")

# 5. Create bar chart
plt.figure(figsize=(10, 6))

plt.bar(
    average_scores.keys(),
    average_scores.values()
)

plt.xlabel("Subjects")
plt.ylabel("Average Score")
plt.title("Average Student Scores by Subject")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()