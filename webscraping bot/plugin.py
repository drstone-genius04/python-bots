import pickle


with open('C:\Users\allan\Downloads\XGBoostClassifier.pickle(1).dat', 'rb') as f:
    xgb_model = pickle.load(f)

def is_phishing(url):
    features = extract_features(url) 
    prediction = xgb_model.predict(features) 
    return bool(prediction) 


urls = ['http://example.com', 'http://example.org', 'http://example.net']
results = []
for url in urls:
    is_phishing_result = is_phishing(url)
    results.append(is_phishing_result)

print(results)

