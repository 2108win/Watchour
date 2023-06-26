from django import forms
from .models import ReviewRating, Product


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm focus:border-primary-color rounded-lg  block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-color dark:focus:border-primary-hover-color'}),
            'slug': forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm  rounded-lg focus:border-primary-color block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-color dark:focus:border-primary-hover-color'}),
            'description': forms.Textarea(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm focus:border-primary-color rounded-lg  block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-color dark:focus:border-primary-hover-color'}),
            'price': forms.NumberInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm  rounded-lg focus:border-primary-color block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-color dark:focus:border-primary-hover-color'}),
            'images': forms.FileInput(attrs={'class': 'block w-full border border-gray-300 rounded-lg text-sm focus:border-primary-color dark:bg-gray-700 dark:border-gray-600 dark:text-white file:border-0 file:bg-gray-100 file:mr-4 file:py-2 file:px-3 dark:file:bg-gray-700 dark:file:text-gray-400'}),
            'stock': forms.NumberInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-primary-color block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-color dark:focus:border-primary-hover-color'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'shrink-0 mt-0.5 border-gray-200 rounded text-blue-600 pointer-events-none checked:bg-primary-color focus:ring-primary-color dark:bg-gray-800 dark:border-gray-700 dark:checked:bg-primary-color dark:checked:border-primary-color dark:focus:ring-offset-gray-800" id="af-submit-application-privacy-check'}),
            'category': forms.Select(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm  rounded-lg  focus:border-primary-color block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-primary-hover-color'}),
            'created_date': forms.DateInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-primary-color block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-color dark:focus:border-primary-hover-color'}),
            'modified_date': forms.DateInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-primary-color block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-color dark:focus:border-primary-hover-color'}),
        }

