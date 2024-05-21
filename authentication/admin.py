from django.contrib import admin
from .models import ElaClass
from .models import MathClass
from .models import ScienceClass
from .models import SocialClass
# Register your models here.

admin.site.register(ElaClass)
admin.site.register(MathClass)
admin.site.register(ScienceClass)
admin.site.register(SocialClass)
