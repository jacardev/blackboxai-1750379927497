from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, RegistrationForm, PasswordEntryForm
from .utils import load_records, save_records

def home_redirect(request):
    """Redirect to dashboard if authenticated, otherwise to login."""
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('login')

def login_view(request):
    """Handle user login."""
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "Credenciais inválidas!")
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})

def register_view(request):
    """Handle user registration."""
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Conta criada com sucesso! Faça login para continuar.")
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'auth/register.html', {'form': form})

@login_required
def logout_view(request):
    """Handle user logout."""
    logout(request)
    messages.info(request, "Você foi desconectado com sucesso!")
    return redirect('login')

@login_required
def dashboard_view(request):
    """Display the main dashboard with all password entries."""
    records = load_records()
    return render(request, 'manager/dashboard.html', {
        'records': records,
        'username': request.user.username
    })

@login_required
def add_record_view(request):
    """Handle adding new password entries."""
    if request.method == 'POST':
        form = PasswordEntryForm(request.POST)
        if form.is_valid():
            records = load_records()
            new_entry = form.cleaned_data
            new_entry['id'] = len(records) + 1
            records.append(new_entry)
            if save_records(records):
                messages.success(request, "Senha salva com sucesso!")
                return redirect('dashboard')
            else:
                messages.error(request, "Erro ao salvar a senha. Tente novamente.")
    else:
        form = PasswordEntryForm()
    return render(request, 'manager/add_record.html', {'form': form})

@login_required
def edit_record_view(request, record_id):
    """Handle editing existing password entries."""
    records = load_records()
    record = next((r for r in records if r.get('id') == record_id), None)
    
    if not record:
        messages.error(request, "Registro não encontrado!")
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = PasswordEntryForm(request.POST)
        if form.is_valid():
            updated_data = form.cleaned_data
            # Update the record while preserving its ID
            updated_data['id'] = record_id
            records = [updated_data if r.get('id') == record_id else r for r in records]
            if save_records(records):
                messages.success(request, "Senha atualizada com sucesso!")
                return redirect('dashboard')
            else:
                messages.error(request, "Erro ao atualizar a senha. Tente novamente.")
    else:
        form = PasswordEntryForm(initial=record)
    
    return render(request, 'manager/edit_record.html', {
        'form': form,
        'record_id': record_id
    })

@login_required
def delete_record_view(request, record_id):
    """Handle deleting password entries."""
    records = load_records()
    records = [r for r in records if r.get('id') != record_id]
    if save_records(records):
        messages.success(request, "Senha excluída com sucesso!")
    else:
        messages.error(request, "Erro ao excluir a senha. Tente novamente.")
    return redirect('dashboard')
