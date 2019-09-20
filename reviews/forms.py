from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['course','user_name', 'rating', 'comment', 'pub_date']
        