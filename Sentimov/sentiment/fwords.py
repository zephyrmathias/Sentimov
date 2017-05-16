def create_feature_words(file_name):
    with open(file_name, 'r') as f:
        return [word.strip() for word in f.readlines()]

def find_features(tokens, word_features):
    features = {}
    for w in word_features:
        features[w] = (str(w) in tokens)
    return features
