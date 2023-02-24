from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from store.models import Product

from store.models import CategoryChoice

from store.forms import ProductForm


class AddView(View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'add_product.html',
                      context={
                          'choices': CategoryChoice.choices,
                          'form': form
                      })

    def post(self, request):
        form = ProductForm(data=request.POST)
        if not form.is_valid():
            return render(request, 'add_product.html',
                          context={
                              'choices': CategoryChoice.choices,
                              'form': form
                          })
        else:
            Product.objects.create(**form.cleaned_data)
            return redirect('index')


class DetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'product.html', context={
            'product': product
        })


class UpdateView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(instance=product)
        return render(request, 'update_product.html',
                      context={
                          'form': form,
                          'choices': CategoryChoice.choices,
                          'product': product
                      })

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'update_product.html', context={'form': form})

# class DeleteView(View):
#     def get(self, request, pk):
#         product = get_object_or_404(Product, pk=pk)
#         return render(request, 'todo_confirm_delete.html', context={'product': product})
#
#
# def confirm_delete(request, pk):
#     todo = get_object_or_404(product, pk=pk)
#     todo.delete()
#     return redirect('index')