from django.shortcuts import render, get_object_or_404, redirect
from borrow.models import BorrowList
from borrow.forms import FormBorrow


# Create your views here.
def borrow_list(request):
    borrows = BorrowList.objects.all()
    return render(request, 'borrow_list.html', {'borrows': borrows})


def borrow_detail(request, pk):
    borrow = get_object_or_404(BorrowList, pk=pk)
    return render(request, 'borrow_detail.html', {'borrow': borrow})


def borrow_create(request):
    if request.method == 'POST':
        form = FormBorrow(request.POST)
        if form.is_valid():
            form.save()
            return redirect('borrow_list')
    else:
        form = FormBorrow()
    return render(request, 'borrow_form.html', {'form': form})


def borrow_update(request, pk):
    borrow = get_object_or_404(BorrowList, pk=pk)
    if request.method == 'POST':
        form = FormBorrow(request.POST, instance=borrow)
        if form.is_valid():
            form.save()
            return redirect('borrow_list')
    else:
        form = FormBorrow(instance=borrow)
    return render(request, 'borrow_form.html', {'form': form})


def borrow_delete(request, pk):
    borrow = get_object_or_404(BorrowList, pk=pk)
    if request.method == 'POST':
        borrow.delete()
        return redirect('borrow_list')
    return render(request, 'myapp/borrow_confirm_delete.html', {'borrow': borrow})
