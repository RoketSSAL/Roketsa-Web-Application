import json
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import HtmlFormatter

from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import (
    NavigationElement,
    SectionHero,
    SectionFeaturedInGeneral,
    SectionFeaturedInLogo,
    SectionAboutUs,
    SectionDepartments,
    SectionTeam,
    SectionCTA,
    SectionFooter,
)

# Register your models here.

admin.site.register(NavigationElement)
admin.site.register(SectionHero)
admin.site.register(SectionFeaturedInGeneral)
admin.site.register(SectionFeaturedInLogo)
admin.site.register(SectionAboutUs)


class SectionTeamAdmin(admin.ModelAdmin):
    readonly_fields = ("data_prettified",)

    def data_prettified(self, instance):
        """Function to display pretty version of our data"""

        response = json.dumps(instance.team, sort_keys=True, indent=2)

        response = response[:5000]

        formatter = HtmlFormatter(style="colorful")

        response = highlight(response, JsonLexer(), formatter)

        style = "<style>" + formatter.get_style_defs() + "</style><br>"

        return mark_safe(style + response)

    data_prettified.short_description = "data prettified"


class SectionDepartmentsAdmin(admin.ModelAdmin):
    readonly_fields = ("data_prettified",)

    def data_prettified(self, instance):
        """Function to display pretty version of our data"""

        response = json.dumps(instance.departments, sort_keys=True, indent=2)

        response = response[:5000]

        formatter = HtmlFormatter(style="colorful")

        response = highlight(response, JsonLexer(), formatter)

        style = "<style>" + formatter.get_style_defs() + "</style><br>"

        return mark_safe(style + response)

    data_prettified.short_description = "data prettified"


class SectionCTAAdmin(admin.ModelAdmin):
    readonly_fields = ("data_prettified",)

    def data_prettified(self, instance):
        """Function to display pretty version of our data"""

        response = json.dumps(instance.where_found_options, sort_keys=True, indent=2)

        response = response[:5000]

        formatter = HtmlFormatter(style="colorful")

        response = highlight(response, JsonLexer(), formatter)

        style = "<style>" + formatter.get_style_defs() + "</style><br>"

        return mark_safe(style + response)

    data_prettified.short_description = "data prettified"


class SectionFooterAdmin(admin.ModelAdmin):
    readonly_fields = ("data_prettified",)

    def data_prettified(self, instance):
        """Function to display pretty version of our data"""

        response = json.dumps(instance.social_icons, sort_keys=True, indent=2)

        response = response[:5000]

        formatter = HtmlFormatter(style="colorful")

        response = highlight(response, JsonLexer(), formatter)

        style = "<style>" + formatter.get_style_defs() + "</style><br>"

        return mark_safe(style + response)

    data_prettified.short_description = "data prettified"


admin.site.register(SectionDepartments, SectionDepartmentsAdmin)

admin.site.register(SectionTeam, SectionTeamAdmin)

admin.site.register(SectionCTA, SectionCTAAdmin)

admin.site.register(SectionFooter, SectionFooterAdmin)
