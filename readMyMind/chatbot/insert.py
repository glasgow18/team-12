from .models import User

def some_name(request):
    foo_instance = User.objects.create(id = '123',name = 'Name', age = '20', location = 'glasgow', gender = 'female')
    return render(request, 'some_name.html.html')