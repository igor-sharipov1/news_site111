from django import forms

class SearchForm(forms.Form):
    search_title = forms.CharField(max_length=200, required=True,
                                   widget=forms.TextInput(attrs={'class':"search_text", 'placeholder':"Искать", 'type':"input"}))

    def save(self):
        search_text = self.cleaned_data['search_title']

        return search_text