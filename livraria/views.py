from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .form import SingUpForm, AddBookForm
from .models import Book
# Create your views here.
def home(request):
   books = Book.objects.all
   if request.method == "POST":
       username = request.POST['username']
       password = request.POST['password']
       #autenticação
       user = authenticate(request,username=username,password=password)
       if user is not None:
           login(request,user)
           messages.success(request, "login feito com sucesso")
           return redirect('home')
       else:
           messages.error(request,"Erro na autenticação. Tente novamente ")
           return redirect('home')
   else:
      return render(request,'home.html', {'books':books})

def sobre(request):
    return render(request,'sobre.html')

def logout_user(request):
    logout(request)
    messages.success(request,"voce fez o logout com sucesso")
    return redirect('home')


def create_user(request):
    if request.method == "POST":
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            #autenticação e login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request, user)
            messages.success(request, "Voce fez o login com sucesso")
            return redirect('home')
    else:
        form = SingUpForm()
        return render(request, 'create.html', {'form':form})
    return render(request, 'create.html', {'form':form})



def deleteBook(request,id):
    if request.user.is_authenticated:
        book = Book.objects.get(id=id)
        book.delete()
        messages.success(request, 'Livro excluído com sucesso')
        return redirect('home')
    else:
        messages.error(request,'Voce precisa estar logado')
        return redirect('home')
    

def create_book(request):
    form = AddBookForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, 'Livro adicionado com sucesso')   
                return redirect('home')

        return render(request, 'createBook.html', {'form':form})    
    else:
        messages.error(request, 'Voce precisa estar logado')
        return redirect('home')
    

def update_book(request, id):
    if request.user.is_authenticated:
        book = Book.objects.get(id=id) 
        form = AddBookForm(request.POST or None, instance=book)   
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro atualizado com sucesso')
            return redirect('home')           
        return render(request,'update.html', {'form':form}) 
    else:
        messages.error(request, 'Voce precisa estar logado')
        return redirect('home')         