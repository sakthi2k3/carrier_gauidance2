from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from datasets import technology_data_set as data_set
from datasets import technology_question_options as question_options
from datasets import technology_questions as questions


labels = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2,  3, 3, 3, 3, 3, 3]
# Assuming each dataset corresponds to a different startup domain

# Creating a text classification pipeline
vectorizer = CountVectorizer()
classifier = MultinomialNB()
model = make_pipeline(vectorizer, classifier)


X_train = vectorizer.fit_transform([' '.join([    d['passionate_about'],
    d['excited_about_innovation'],
    d['preferred_startup_focus'],
    d['aligned_expertise_interest'],
    d['prior_experience_domain'],
    d['envisioned_tech_products'],
    d['tech_solution_preference'],
    d['targeted_industry_or_market'],
    d['comfort_with_hardware_dev_cycles'],
    d['impactful_tech_area']]) for d in data_set])
classifier.fit(X_train, labels)

def predict_domain(responses):
    transformed_responses = vectorizer.transform([responses])
    prediction = classifier.predict(transformed_responses)
    domains = ["Software and app development", "Hardware and Electronics", "Data Science and Artificial Intelligence", "Hardware and IoT"] 
    return domains[prediction[0]]

def ask_questions():
    user_responses = []
    for i, question in enumerate(questions, start=1):
        print(f"Question {i}: {question}")
        response_key = input("Your answer: ").strip().lower()
        while response_key not in ["a", "b", "c", "d"]:
            print("Invalid choice. Please choose a valid option.")
            response_key = input("Your answer: ").strip().lower()
        response = question_options[question][response_key]
        user_responses.append(response)
    return ' '.join(user_responses)

# Main function to run the quiz

def technology1(l):
    user_responses = []
    for i in range(10):
        response = question_options[questions[i]][l[i]]
        user_responses.append(response)
    user_responses=' '.join(user_responses)    
    predicted_domain = predict_domain(user_responses)
    return predicted_domain