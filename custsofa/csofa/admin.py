from django.contrib import admin
from .models  import SofaKind, Arm, ArmVariant, Back, BackVariant, Leg, LegVariant, Pipe, PipeVariant, Color, Size
# Register your models here.


class SizeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Size()._meta.fields]
    pass
admin.site.register(Size, SizeAdmin)


class SofaKindAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SofaKind()._meta.fields]
    pass
admin.site.register(SofaKind, SofaKindAdmin)


class ColorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Color()._meta.fields]
    pass
admin.site.register(Color, ColorAdmin)


class ArmAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Arm()._meta.fields]
    pass
admin.site.register(Arm, ArmAdmin)

class ArmVariantAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ArmVariant()._meta.fields]
    pass
admin.site.register(ArmVariant, ArmVariantAdmin)


class BackAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Back()._meta.fields]
    pass
admin.site.register(Back, BackAdmin)


class BackVariantAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BackVariant()._meta.fields]
    pass
admin.site.register(BackVariant, BackVariantAdmin)


class PipeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Pipe()._meta.fields]
    pass
admin.site.register(Pipe, PipeAdmin)


class PipeVariantAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PipeVariant()._meta.fields]
    pass
admin.site.register(PipeVariant, PipeVariantAdmin)


class LegAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Leg()._meta.fields]
    pass
admin.site.register(Leg, LegAdmin)


class LegVariantAdmin(admin.ModelAdmin):
    list_display = [field.name for field in LegVariant()._meta.fields]
    pass
admin.site.register(LegVariant, LegVariantAdmin)




