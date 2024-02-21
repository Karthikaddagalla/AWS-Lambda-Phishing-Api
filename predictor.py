
import pickle
import time

import features_extractor
import numpy as np




start_load_time = time.time()
with open("Models/gradient_classifier_98_accuracy", "rb") as file:
    gbc = pickle.load(file)

print("Pickle file loading time", time.time() - start_load_time)



# Loading the normalization object



def predictor(url):

    start_features = time.time()
    obj = features_extractor.FeatureExtraction(url)
    print("Feature extraction time: ", time.time()-start_features)
    x = np.array(obj.getFeaturesList()).reshape(1,30) 

    start_pred = time.time()
    y_pred =gbc.predict(x)[0]
    print("Prediction time", time.time() - start_pred)


            
    if y_pred==1:
        print("The link is Good link")
        return 0
        
    else:
        print("The link is phishing link")
        return 1
    
# predictor("https://github.com/Karthikaddagalla/Phishing-Domain-Detection")





    


