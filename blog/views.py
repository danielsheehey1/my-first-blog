from django.shortcuts import render, render_to_response
from .models import Post, Comment, Machine, Customer, Employee, Work_Order, Work_Order_Item
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import EmployeeForm, MachineForm, CustomerForm, Work_OrderForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

def table_view(request):
    posts = Work_Order.objects.all()
    return render(request, 'blog/table_view.html', {'posts': posts})

def admin_view(request):
    return render(request, 'blog/admin_view.html')

def test(request):
    return render(request, 'blog/employee.html')

def employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():

            return redirect('admin_view')
    else:
        form = EmployeeForm()
    return render(request, 'blog/employee.html', {'form': form})

def work_order(request):
    if request.method == 'POST':
        form = Work_OrderForm(request.POST)
        if form.is_valid():

            return redirect('admin_view')
    else:
        form = Work_OrderForm()
    return render(request, 'blog/work_order.html', {'form': form})

def customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():

            return redirect('admin_view')
    else:
        form = CustomerForm()
    return render(request, 'blog/customer.html', {'form': form})

def machine(request):
    if request.method == 'POST':
        form = MachineForm(request.POST)
        if form.is_valid():

            return redirect('admin_view')
    else:
        form = MachineForm()
    return render(request, 'blog/machine.html', {'form': form})


#
#test for tables
#

def people(request):
    return render(request, 'people.html', {'people': Person.objects.all()})

