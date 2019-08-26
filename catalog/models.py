from django.db import models
import uuid # Required for unique book instances

from django.urls import reverse


#####################################


#########################################




class Article(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)
    

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    author = models.CharField(max_length=200)

    
    
    summary = models.TextField(max_length=50000, help_text='Enter a brief description of the Article')
    
    date_publication = models.DateField(null=True, blank=True)

    topic = models.CharField(max_length=200)
    
    
 
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('Article-detail', args=[str(self.id)])
