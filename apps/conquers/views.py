from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import UserForm, ProfileForm,ProfileForm2,ProfileForm2, ActivityForm,NotaForm
from .models import UserProfile, Activity, Comunity, Nota



def valida(username):
    if username != '':

        u = User.objects.get(username=username)
        up = UserProfile.objects.get(nickname=u)
    else:
        usu = ''
        return {'usu':usu, 'user':''}
    if up.type_user == 2:
        usu = 2
        return {'usu':usu, 'user':up}
    else:
        usu = 1
        return {'usu':usu, 'user':up}


def index(request):
    hola = [1,2,3]
    username = request.user.username
    usu = valida(username)
    ti = usu['usu']
    # if username :
        # return render(request, 'conquers/index.html')
    # else:
        # usu = valida(username)
    total = Nota.objects.raw('select n.id,sum(n.puntuacion) as total,c.name,n.name as logro from conquers_nota n inner join conquers_comunity c on n.comunity_id == c.id group by c.name order by total DESC')
    print(usu)
    return render(request, 'conquers/index.html',{'tipo':ti, 'puntos':total, 'hola':hola})


def register(request, pk):
    # if pk == '1':
    #     print("hola")
    # else:
    #     print("no hola")
    if pk == '1':
        print("Soy Presidente")
        if request.method == 'POST':
            user_form = UserForm(data=request.POST)
            profile_form = ProfileForm(data=request.POST)

            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                profile = profile_form.save(commit=False)
                profile.nickname = user
                profile.save()


                return redirect('conquers:index')
            else:
                print("hay error")

        else:
            user_form = UserForm()
            profile_form = ProfileForm()
    else:
        print("Soy Auditor")
        if request.method == 'POST':
            user_form = UserForm(data=request.POST)
            profile_form = ProfileForm2(data=request.POST)

            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                profile = profile_form.save(commit=False)
                profile.nickname = user

                profile.type_user = 2
                profile.comunity = Comunity.objects.get(pk=1)
                profile.save()

                return redirect('conquers:index')
            else:
                print("hay error")

        else:
            user_form = UserForm()
            profile_form = ProfileForm2()

    return render(request, 'conquers/admin/registro.html', {'user': user_form,'profile': profile_form})
    # return render(request, 'conquers/admin/registro.html',{})


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                login(request, user)

                return redirect('conquers:index')
            else:
                return HttpResponse("tu cuenta esta desactivada")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("login invalido")
    else:
        return render(request, 'conquers/admin/login.html', {})


def user_logout(request):
    logout(request)
    return redirect('conquers:index')


@login_required()
def envio_actividad(request):
    usutp = valida(request.user.username)
    if usutp['usu'] == 1:
        if request.method == 'POST':
            acty_form = ActivityForm(request.POST, request.FILES)
            if acty_form.is_valid():
                actividad = acty_form.save(commit=False)
                comuni = usutp['user'].comunity
                actividad.comunity = comuni
                actividad.save()
                return redirect('conquers:index')
            else:
                print("hay error")

        else:
            acty_form = ActivityForm()
    else:
        return HttpResponse("Eres Un auditor o un usuario sin registrar. No puedes enviar Archivos")
    return render(request, 'conquers/admin/actividad.html', {'form':acty_form})

@login_required()
def consulta_activity(request):
    usutp = valida(request.user.username)
    if usutp['usu'] == 2:
        dic = Activity.objects.all()
    else:
        return HttpResponse("Eres Un Presidente o un usuario sin registrar. No puedes ver archivos")
    return render(request, 'conquers/admin/consulta.html', {'archivos': dic})

@login_required()
def descarga_documentos(request,pk):
    doc = Activity.objects.get(pk=pk)
    response = HttpResponse(content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename=%s' % doc.fields
    response.write(doc.fields)
    return response



class AddNota(CreateView):
    form_class = NotaForm
    template_name = 'conquers/admin/nota.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AddNota, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        # esta funcion es para que me deje en la misma url donde me encuentro :D
            return self.request.path

def tabla_puntuaciones(request):
    nota = Nota.objects.all().order_by('comunity')

    return render(request, 'conquers/admin/notas_sesiones.html',{'nota':nota})


def discusiones(request):
    return render(request, 'conquers/admin/discus.html')
