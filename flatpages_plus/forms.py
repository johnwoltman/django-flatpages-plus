from django import forms
from django.utils.translation import ugettext_lazy as _

from flatpages_plus.models import FlatPage
from tinymce.models import HTMLField


class FlatpageForm(forms.ModelForm):
    url = forms.RegexField(label=_("URL"), max_length=100, regex=r'^[-\w/\.~]+$',
        help_text = _("Example: '/about/contact/'. Make sure to have leading"
                      " and trailing slashes."),
        error_message = _("This value must contain only letters, numbers,"
                          " dots, underscores, dashes, slashes or tildes."))
    
    metadata = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'class': 'span6'}))
    content = HTMLField()
        
    class Meta:
        model = FlatPage
        exclude = ['owner', 'sites', 'enable_comments', 'views', 'registration_required']
        
class FlatpageAdminForm(forms.ModelForm):
    url = forms.RegexField(label=_("URL"), max_length=100, regex=r'^[-\w/\.~]+$',
        help_text = _("Example: '/about/contact/'. Make sure to have leading"
                      " and trailing slashes."),
        error_message = _("This value must contain only letters, numbers,"
                          " dots, underscores, dashes, slashes or tildes."))

    class Meta:
        model = FlatPage
    