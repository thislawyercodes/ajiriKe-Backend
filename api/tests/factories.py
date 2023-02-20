from factory import DjangoModelFactory ,Faker
from ..models import Student

class StudentFactory(DjangoModelFactory):
    first_name=Faker('Kipchoge')
    last_name=Faker('Keino')
    email=Faker('Kipchogek@ymail.com')
    city=Faker('Kitale')
    location=Faker('Rift Valley')
    phone_number=Faker('0700000000')
    resume=Faker('https://medium.com/analytics-vidhya/factoryboy-usage-cd0398fd11d2')
    cover_letter=Faker('https://medium.com/analytics-vidhya/factoryboy-usage-cd0398fd11d2')

    class Meta:
        model=Student