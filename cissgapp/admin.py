from django.contrib import admin
from .models import extenduser, record, academic, leaves, dependents, triple, other_trainings, details,  vocational, coastguard, coastguard_foreign, coastguard_local, military, military_local, military_foreign, appointments, shipboard, collateral, shorebased, collateral2, government, nongovernment, cgawards, cglcommendation, cgappreciation, cgplaque, mawards, mlcommendation, mappreciation, mplaque, clcommendation, cappreciation, cplaque, career, organization, eligibility, retirement

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# Register your models here.

admin.site.register(extenduser)
admin.site.register(academic)
admin.site.register(other_trainings)
admin.site.register(vocational)
admin.site.register(coastguard)
admin.site.register(coastguard_foreign)
admin.site.register(coastguard_local)
admin.site.register(military)
admin.site.register(military_local)
admin.site.register(military_foreign)

admin.site.register(appointments)
admin.site.register(shipboard)
admin.site.register(collateral)
admin.site.register(shorebased)
admin.site.register(collateral2)
admin.site.register(government)
admin.site.register(nongovernment)
admin.site.register(cgawards)
admin.site.register(cglcommendation)
admin.site.register(cgappreciation)
admin.site.register(cgplaque)
admin.site.register(mawards)
admin.site.register(mlcommendation)
admin.site.register(mappreciation)
admin.site.register(mplaque)
admin.site.register(clcommendation)
admin.site.register(cappreciation)
admin.site.register(cplaque)
admin.site.register(career)
admin.site.register(organization)
admin.site.register(eligibility)
admin.site.register(retirement)
admin.site.register(details)
admin.site.register(dependents)
admin.site.register(triple)
admin.site.register(leaves)
admin.site.register(record)


# admin.site.register(CustomUser)