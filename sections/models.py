from django.db import models
import json
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import HtmlFormatter
from django.utils.safestring import mark_safe


# Create your models here.


class NavigationElement(models.Model):
    display_name = models.CharField(max_length=15)
    is_cta = models.BooleanField(default=False)


class SectionHero(models.Model):
    hero_title = models.CharField(max_length=40)
    hero_description = models.CharField(max_length=216)
    hero_bg = models.CharField(max_length=20)

    left_button_displayed = models.BooleanField(default=True)
    right_button_displayed = models.BooleanField(default=True)

    left_button_content = models.CharField(max_length=15)
    right_button_content = models.CharField(max_length=20)

    def has_add_permission(self, request):
        return (
            False
            if self.model.objects.count() > 0
            else super().has_add_permission(request)
        )


class SectionFeaturedInGeneral(models.Model):
    featured_in_title = models.CharField(max_length=40)
    featured_in_visibility = models.BooleanField(default=True)
    featured_in_logos_gap = models.FloatField()


class SectionFeaturedInLogo(models.Model):
    logo_name = models.CharField(max_length=50)
    logo_url = models.CharField(max_length=1000)


class SectionAboutUs(models.Model):
    about_us_subheading = models.CharField(max_length=15)
    about_us_primary_heading = models.CharField(max_length=70)
    about_us_content = models.TextField()

    about_us_circle_animation = models.BooleanField(default=True)
    about_us_image_url = models.CharField(max_length=1000)


class SectionDepartments(models.Model):
    departments_subheading = models.CharField(max_length=25)
    departments_primary_heading = models.CharField(max_length=70)
    department_icon_animation = models.BooleanField(default=True)

    departments = models.JSONField()


class SectionTeam(models.Model):
    team_subheading = models.CharField(max_length=25)
    team_primary_heading = models.CharField(max_length=70)

    team = models.JSONField()


class SectionCTA(models.Model):
    cta_primary_heading = models.CharField(max_length=70)
    cta_description = models.CharField(max_length=250)

    where_found_options = models.JSONField()
    image_animation = models.BooleanField(default=True)


class SectionFooter(models.Model):
    social_icons = models.JSONField()

    address_line = models.CharField(max_length=100)
    tel_line = models.CharField(max_length=15)
    mail_line = models.EmailField()
