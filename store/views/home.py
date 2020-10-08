from django.shortcuts import render , redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View

# Create your views here.

class Index(View):

    def post(self,request):
        product = request.POST.get('product')
        print(product)
        return redirect('homepage')

    def get(self,request):
        products = None
        categories = Category.get_all_categories()
        categoryId = request.GET.get('category')
        if categoryId:
            products = Product.get_all_proucts_by_categoryid(categoryId)
        else:
            products = Product.get_all_proucts()
        data = {}
        data['products'] = products
        data['categories'] = categories
        print('you are : ', request.session.get('email'))
        return render(request, 'index.html', data)






