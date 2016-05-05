from django.db import models


class Rater(models.Model):
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('Q', 'Genderqueer'))
    AGE_GROUPS = ((1, 'Under 18'), (18, '18-24'), (25, '25-34'), (35, '35-44'),
                  (45, '45-49'), (50, '50-55'), (56, '56+'))
    OCCUPATION_CHOICES = ((0, "Other"), (1, "Academic/Educator"),
                          (2, "Artist"), (3, "Clerical/Admin"),
                          (4, "College/Grad Student"), (5, "Customer Service"),
                          (6, "Doctor/Health Care"),
                          (7, "Executive/Managerial"), (8, "Farmer"),
                          (9, "Homemaker"), (10, "K-12 Student"),
                          (11, "Lawyer"), (12, "Programmer"), (13, "Retired"),
                          (14, "Sales/Marketing"), (15, "Scientist"),
                          (16, "Self-employed"), (17, "Technician/Engineer"),
                          (18, "Tradesman/Craftsman"), (19, "Unemployed"),
                          (20, "Writer"))

    rater_id = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, blank=True)
    age = models.IntegerField(choices=AGE_GROUPS, blank=True)
    occupation = models.IntegerField(choices=OCCUPATION_CHOICES, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)


class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=90)
    genre = models.CharField(max_length=60)


class Rating(models.Model):
    rater = models.ForeignKey('Rater', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    rating = models.IntegerField()
    # timestamp = models.DateTimeField()
