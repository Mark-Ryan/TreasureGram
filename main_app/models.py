from django.db import models

# Creating models to edit treasures directly from the website and maintain easily over time.
# Adding Django field types that correspond to both python types and sql types.
# Defining rules for model attributes to avoid errors.

class Treasure(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    img_url = models.CharField(max_length=100)

# Treasures name will be shown whenever we output the object in the interactive shell.

    def __str__(self):
        return self.name


t1 = Treasure(name = 'Gold Nugget', value = 500.00, material = 'gold', location = "Curley's Creek, NM", img_url = 'http://courseware.codeschool.com/try_django/images/treasuregram-gold-nugget.png'),
t2 = Treasure(name = "Fool's Gold", value = 0, material = 'pyrite', location = "Fool's Falls, CO", img_url = 'http://courseware.codeschool.com/try_django/images/treasuregram-fools-gold.png'),
t3 = Treasure(name = 'Coffee Can', value = 20.00, material = 'tin', location = 'Acme, CA', img_url = 'http://courseware.codeschool.com/try_django/images/treasuregram-coffee-can.png')




