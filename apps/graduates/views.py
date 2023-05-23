from django.shortcuts import render

# Create your views here.
def mi_vista(request):
    # Lógica de tu vista
    # ...
    
    # Renderiza la plantilla y devuelve la respuesta
    return render(request, 'data_form.html')

def mi_vista_profile(request):
    # Lógica de tu vista
    # ...
    
    # Renderiza la plantilla y devuelve la respuesta
    return render(request, 'profile_graduates.html')