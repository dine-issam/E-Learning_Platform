from django.core.validators import MinValueValidator, MaxValueValidator

# Validator used for percentages
PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]