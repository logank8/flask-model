I created a model that predicts a song's popularity using the dataset provided by https://www.kaggle.com/datasets/yasserh/song-popularity-dataset. For this machine learning model, I used a Random Forest Regressor.

One issue I've run into in this is the accuracy when applied to actual Spotify data - the kaggle data is only simulated, and so the model that is based off of it does not hold up as well as it does with the real data. When applied to the simulated data, the model has an accuracy rate of 83%. In the future, I'd like to see if I could use a model with a constant learning feature to eventually adapt it more to the Spotify data and not the simulated. Or, since the Tekore library has such a vast amount of songs in its library, I could use the same subset of songs used in the Kaggle dataset to create a new training dataset for the model and test its accuracy using the more up-to-date popularity scores.

**Interface preview:**

<img width="984" alt="Screen Shot 2023-08-23 at 7 26 02 PM" src="https://github.com/logank8/flask-model/assets/98340537/ea5c0e22-c489-4edd-804c-faef50c48504">

**Accuracy score on Kaggle**

<img width="572" alt="Screen Shot 2023-08-23 at 7 45 08 PM" src="https://github.com/logank8/flask-model/assets/98340537/f5491d55-963f-4682-a85d-f8761a753812">

Kaggle notebook here: https://www.kaggle.com/code/logankeener/song-popularity-predictive-model?kernelSessionId=140842736


**How to run the flask app:**

Terminal commands

flask --app flaskr init-db

flask --app flaskr run --debug
