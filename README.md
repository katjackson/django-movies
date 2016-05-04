## Movie Lens Online
This project contains a Django app that controls a database of 1M MovieLens data.

#### movieratings
Django project folder

#### ratingbase
Django app for controlling MovieLens data.

### Models
The Rater, Movie, and Rating models control three separate SQL database tables.

#### Rater
Fields:
rater_id | gender | age | occupation | zip_code

age: corresponds to the following groups
   1:  "Under 18"
  18:  "18-24"
  25:  "25-34"
  35:  "35-44"
  45:  "45-49"
  50:  "50-55"
  56:  "56+"
occupation: corresponds to the following codes
   0:  "other" or not specified
   1:  "academic/educator"
   2:  "artist"
   3:  "clerical/admin"
   4:  "college/grad student"
   5:  "customer service"
   6:  "doctor/health care"
   7:  "executive/managerial"
   8:  "farmer"
   9:  "homemaker"
  10:  "K-12 student"
  11:  "lawyer"
  12:  "programmer"
  13:  "retired"
  14:  "sales/marketing"
  15:  "scientist"
  16:  "self-employed"
  17:  "technician/engineer"
  18:  "tradesman/craftsman"
  19:  "unemployed"
  20:  "writer"

#### Movie
Fields:
movie_id | title | genre

genre: separated by pipes

#### Rating
Fields:
id | rating | movie_id | rater_id

id: atomatic primary key
rating: 1 - 5, only whole numbers
movie_id: foreign key corresponds to movie table
rater_id: foreign key corresponds to rater table
