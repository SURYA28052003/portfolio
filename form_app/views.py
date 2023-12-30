# myapp/views.py
from django.shortcuts import render, redirect
from .forms import UserInfoForm
from django.http import JsonResponse

def user_info(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = UserInfoForm()

    return render(request, 'user_info.html', {'form': form})


# def user_info(request):
#     if request.method == 'POST':
#         form = UserInfoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success')  # Redirect to a success page
#     else:
#         form = UserInfoForm()

#     return render(request, 'user_info.html', {'form': form})


# Create your views here.
