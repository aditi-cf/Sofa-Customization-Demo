import sys, os

import django
from django.core.files import File

sys.path.append('/Users/aditijain/PycharmProjects/CUSTSOFA/custsofa')
os.environ['DJANGO_SETTINGS_MODULE'] = 'custsofa.settings'
django.setup()

from csofa.models import ArmVariant, Arm, Color, BackVariant, Back, Leg, LegVariant, Pipe, PipeVariant
from django.conf import settings

'''
for dirpath, dirnames, filenames in os.walk("./sofa/kind_1/arm"):
    for filename in [f for f in filenames if not f.startswith(".")]:
        a = ArmVariant()
        l = dirpath.split('/')
        print l[4]
        a.armId = Arm.objects.get(name=unicode(l[4]))
        a.size = l[5]
        a.color = Color.objects.get(name=unicode(filename.split('.')[0]))
        a.price = 100
        a.image = File(open(dirpath + "/" + filename))
        a.save()
'''
'''

for dirpath, dirnames, filenames in os.walk("./sofa/kind_1/back"):
    for filename in [f for f in filenames if not f.startswith(".")]:
        l = dirpath.split('/')
        a = BackVariant()
        a.backId = Back.objects.get(name=unicode(l[4]))
        a.armId = Arm.objects.get(name=unicode(l[6]))
        a.color = Color.objects.get(name=unicode(filename.split('.')[0]))
        a.price = 1000
        a.size = l[5]
        a.image = File(open(dirpath + "/" + filename))
        a.save()
'''

'''

for dirpath, dirnames, filenames in os.walk("./sofa/kind_1/leg"):
    for filename in [f for f in filenames if not f.startswith(".")]:
        l = dirpath.split('/')
        a = LegVariant()
        print l[4]
        a.legId = Leg.objects.get(name=unicode(l[4]))
        a.armId = Arm.objects.get(name=unicode(l[6]))
        a.price = 1000
        a.size = l[5]
        a.image = File(open(dirpath + "/" + filename))
        a.save()
'''
'''
for dirpath, dirnames, filenames in os.walk("./sofa/kind_1/pipe"):
    for filename in [f for f in filenames if not f.startswith(".")]:
        l = dirpath.split('/')
        a = PipeVariant()
        a.pipeId = Pipe.objects.get(name=unicode(l[4]))
        a.armId = Arm.objects.get(name=unicode(l[6]))
        a.backId = Back.objects.get(name=unicode(l[7]))
        a.color = Color.objects.get(name=filename.split('.')[0])
        a.price = 500
        a.size = l[5]
        a.image = File(open(dirpath + "/" + filename))
        a.save()
'''