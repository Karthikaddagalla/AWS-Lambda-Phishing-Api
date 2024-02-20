
import pickle


import features_extractor
import numpy as np




with open("Models/gradient_classifier_98_accuracy", "rb") as file:
    gbc = pickle.load(file)



# Loading the normalization object



def predictor(url):

    obj = features_extractor.FeatureExtraction(url)
    x = np.array(obj.getFeaturesList()).reshape(1,30) 
    y_pred =gbc.predict(x)[0]


            
    if y_pred==1:
        print("The link is Good link")
        return 0
        
    else:
        print("The link is phishing link")
        return 1
    



