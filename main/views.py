from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from sections.models import (
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

# Create your views here.


def IndexView(request):
    return render(
        request,
        "index.html",
        {
            "navigations": NavigationElement.objects.all(),
            "hero_section": SectionHero.objects.first(),
            "featuredin_section": {
                "general": SectionFeaturedInGeneral.objects.first(),
                "logos": SectionFeaturedInLogo.objects.all(),
            },
            "about_us_section": SectionAboutUs.objects.first(),
            "departments_section": SectionDepartments.objects.first(),
            "team_section": SectionTeam.objects.first(),
            "cta_section": SectionCTA.objects.first(),
            "footer_section": SectionFooter.objects.first(),
            "site_theme": request.session.get("site-theme"),
        },
    )


def ChangeThemeView(request):
    try:
        request.session["site-theme"]
    except KeyError:
        request.session["site-theme"] = "dark-theme"
    else:
        if request.session["site-theme"] == "dark-theme":
            request.session["site-theme"] = "light-theme"
        else:
            request.session["site-theme"] = "dark-theme"
    finally:
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
