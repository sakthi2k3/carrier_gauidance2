from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from datasets import domain_all_datasets as all_datasets
from datasets import domain_question_options as question_options
from datasets import domain_questions as questions





labels = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2,  3, 3, 3, 3, 3, 3]



vectorizer = CountVectorizer()
classifier = MultinomialNB()
model = make_pipeline(vectorizer, classifier)


X_train = vectorizer.fit_transform([' '.join([d['interest'], d['helping_others'], d['enjoy_learning'], d['dabbled'], d['learn_more'], d['discuss_with_friends'], d['online_communities'], d['content_preference'], d['career_path'], d['blog_or_channel'], d['reading_preference'], d['conference_preference'], d['documentary_preference'], d['hobby'], d['new_skill'], d['youtube_channel']]) for d in all_datasets])
classifier.fit(X_train, labels)


def predict_domain(responses):
    transformed_responses = vectorizer.transform([responses])
    prediction = classifier.predict(transformed_responses)
    domains = ["Technology", "Finance", "E-commerce", "Healthcare"]  
    return domains[prediction[0]]


# def ask_questions():
#     user_responses = []
#     for i, question in enumerate(questions, start=1):
#         print(f"Question {i}: {question}")
#         response_key = input("Your answer: ").strip().lower()
#         while response_key not in ["a", "b", "c", "d"]:
#             print("Invalid choice. Please choose a valid option.")
#             response_key = input("Your answer: ").strip().lower()
#         response = question_options[question][response_key]
#         user_responses.append(response)
#     return ' '.join(user_responses)


def domain1(l):
    user_responses = []
    for i in range(15):
        response = question_options[questions[i]][l[i]]
        user_responses.append(response)
    user_responses=' '.join(user_responses)    
    # user_responses = ask_questions()
    predicted_domain = predict_domain(user_responses)
    

    return predicted_domain


