from django.shortcuts import render
from .models import Treasure

# Create views here.
def index(request):
    # treasures = Treasure.objects.all()
    return render(request, 'index.html', {'treasures':treasures})

class Treasure:
    def __init__(self, name, value, material, location, img_url):
        self.name = name
        self.value = value
        self.material = material
        self.location = location
        self.img_url = img_url

treasures = [
    Treasure('Gold Nugget', 500.00, 'gold', "Curley's Creek, NM", 'http://courseware.codeschool.com/try_django/images/treasuregram-gold-nugget.png'),
    Treasure("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO", 'http://courseware.codeschool.com/try_django/images/treasuregram-fools-gold.png'),
    Treasure('Coffee Can', 20.00, 'tin', 'Acme, CA', 'http://courseware.codeschool.com/try_django/images/treasuregram-coffee-can.png')
]


t1 = Treasure('Gold Nugget', 500.00, 'gold', "Curley's Creek, NM", 'http://courseware.codeschool.com/try_django/images/treasuregram-gold-nugget.png'),
t2 = Treasure("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO", 'http://courseware.codeschool.com/try_django/images/treasuregram-fools-gold.png'),
t3 = Treasure('Coffee Can', 20.00, 'tin', 'Acme, CA', 'http://courseware.codeschool.com/try_django/images/treasuregram-coffee-can.png')
