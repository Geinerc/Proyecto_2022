from django.shortcuts import render

# # Create your views here.
#
def owner_list(request):
    data_context = {
        'nombre_owner': 'Geiner',
        'edad': 18,
        'pais': 'Perú',
        'Vigente': True
    }
    return render(request, 'owners_list.html', context={'data': data_context})
