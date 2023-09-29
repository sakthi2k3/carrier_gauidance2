from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from datasets import e_comerce_data_set as data_set
from datasets import e_comerce_question_options as question_options
from datasets import e_comerce_questions as questions




labels = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2,  3, 3, 3, 3, 3, 3]
vectorizer = CountVectorizer()
classifier = MultinomialNB()
model = make_pipeline(vectorizer, classifier)


X_train = vectorizer.fit_transform([' '.join([    d['question_1'],
    d['question_2'],
    d['question_3'],
    d['question_4'],
    d['question_5'],
    d['question_6'],
    d['question_7'],
    d['question_8'],
    d['question_9'],
    d['question_10']]) for d in data_set])
classifier.fit(X_train, labels)

def predict_domain(responses):
    transformed_responses = vectorizer.transform([responses])
    prediction = classifier.predict(transformed_responses)
    domains = ["Telemedicine and telehealth", "Healthcare data and analyticse", "Digital health and wearables", "Biotechnology and medical devices"]  # Update with actual domain names
    return domains[prediction[0]]

def e_comerce1(l):
    user_responses = []
    for i in range(10):
        response = question_options[questions[i]][l[i]]
        user_responses.append(response)
    user_responses=' '.join(user_responses)    
    predicted_domain = predict_domain(user_responses)
    return predicted_domain