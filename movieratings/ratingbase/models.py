from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


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
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.rater_id)

    def get_occupation(self, OCCUPATION_CHOICES=OCCUPATION_CHOICES):
        dict_occ = dict(OCCUPATION_CHOICES)
        return dict_occ[self.occupation]

    def get_age(self, AGE_GROUPS=AGE_GROUPS):
        dict_age = dict(AGE_GROUPS)
        return dict_age[self.age]

    @staticmethod
    def populate_user_model():
        for rater in Rater.objects.all():
            user1 = User.objects.create_user('username{}'.format(rater.rater_id),
                        '{}@fake-email.com'.format(rater.rater_id),
                        'password')
            rater.user = user1
            rater.save()


class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=90)
    genre = models.CharField(max_length=60)
    avg_rating = models.FloatField(null=True, blank=True)
    ratings_count = models.IntegerField(null=True)

    def __str__(self):
        return self.title


class Rating(models.Model):
    rater = models.ForeignKey('Rater', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], help_text='Rate 1 - 5 stars')
    timestamp = models.DateTimeField(auto_now=True)
    review = models.TextField(max_length=250, blank=True)

    def __str__(self):
        return 'Rater: {}, Rating: {}, Movie: {}'.format(self.rater, self.rating, self.movie)

    # class Meta:
    #     unique_together = ('rater', 'movie')

#HI 
