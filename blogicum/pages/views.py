from django.views.generic.base import TemplateView  # type: ignore


class About(TemplateView):

    template_name = "pages/about.html"


class Rules(TemplateView):

    template_name = "pages/rules.html"
