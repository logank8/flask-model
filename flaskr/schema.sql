DROP TABLE IF EXISTS prediction;

--predictions stored in the prediction table--
CREATE TABLE prediction (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    song TEXT NOT NULL,
    pred INTEGER NOT NULL,
    realnum INTEGER NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);