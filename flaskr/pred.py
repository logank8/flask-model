import numpy as np
import pandas as pd
import tekore as tk

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import tree

## How to connect the model:
## At the start of each new session, retrain the model and create one instance of an object that can take arguments
##  and spit out a prediction

class Prediction:

    def __init__(self, song, prediction, real):
        self.song = song
        self.pred = prediction
        self.real = real

    # Function to make predictions 
    def cal_error(self):
        return round(np.mean(abs(self.pred - self.real)), 2)

    # Function to calculate accuracy 
    def cal_accuracy(self):
        errors = abs(self.pred - self.real)
        mape = 100 * (errors / (self.real + (self.real==0)))
        accuracy = abs(100 - np.mean(mape))
        return round(accuracy, 2)


class Predictor:

    client_id = '6787818da98841849bfc8ff0e1abd171'
    client_secret = '3127ad9f874541f797e881976a3152fd'
    app_token = tk.request_client_token(client_id, client_secret)
    spotify = tk.Spotify(app_token)

    song_data = pd.read_csv("./flaskr/song_data.csv")
    df = (pd.DataFrame(song_data)).drop_duplicates(subset='song_name')

    X = (df.drop(labels=['song_popularity', 'song_name'], axis=1)).to_numpy()
    Y = (df.song_popularity).to_numpy()
    rf = RandomForestRegressor(n_estimators=1000, random_state=42)

    def __init__(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.Y, test_size=0.25, random_state=42)
        self.rf.fit(X_train, y_train)



    def predict(self, search):

        songs, = self.spotify.search(search, types=('track',), limit=1)
        song = songs.items[0]

        val = song.popularity

        aud_features = self.spotify.track_audio_features(song.id)
        y_pred = self.rf.predict([[
            aud_features.duration_ms, 
            aud_features.acousticness,
            aud_features.danceability,
            aud_features.energy,
            aud_features.instrumentalness,
            aud_features.key,
            aud_features.liveness,
            aud_features.loudness,
            aud_features.mode,
            aud_features.speechiness,
            aud_features.tempo,
            aud_features.time_signature,
            aud_features.valence
        ]])
        
        prediction = Prediction(song, y_pred, val)
        return prediction