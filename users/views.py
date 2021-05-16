from django.shortcuts import render
from users.forms import RegisterForm


def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)

    return render(request,
                  'users/register.html',
                  {
                      'form': form
                  })



