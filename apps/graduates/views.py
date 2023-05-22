from django.shortcuts import render

# Create your views here.
def mi_vista(request):
    # Lógica de tu vista
    # ...
    
    # Renderiza la plantilla y devuelve la respuesta
    return render(request, 'data_form.html')