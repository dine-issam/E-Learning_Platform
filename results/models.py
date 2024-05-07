from django.db import models

# Quiz model        
from quizes.models import Quiz

# User model
from accounts.models import User

# Validators
from validators.validators import PERCENTAGE_VALIDATOR


# Result model
class Result(models.Model):
    """
    The results for the quiz answers of a given user
    """ 
    
    date = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True
    )

    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=PERCENTAGE_VALIDATOR
    )

    
    def __str__(self):
        return str(self.pk)