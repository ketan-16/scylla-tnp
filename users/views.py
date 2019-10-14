from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm, ProfileUpdateForm, GrievanceForm
from django.contrib.auth.decorators import login_required
from blog.models import Post
from .models import Grievances, Profile
from blog.models import Post
from django.contrib.admin.views.decorators import staff_member_required
from plotly.offline import plot
from plotly.graph_objs import Scatter, Bar
import csv

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} Successfully! Try logging in below.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def dashboard(request):
    if request.method == 'POST':
        g_form = GrievanceForm(request.POST)
        if g_form.is_valid():
            g_form.save()
            messages.success(request, f'Grievance Submitted Successfully')
            return redirect('dashboard')
    else:
        g_form = GrievanceForm()   
    context = {
        'posts': Post.objects.all(),
        'g_form' : g_form,  
        'title' : 'Dashboard',
        'grievances' : Grievances.objects.all()
    } 
    return render(request, 'users/dashboard.html', context)

@login_required
def update_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm( request.POST,
                                    request.FILES, 
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('blog-home')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form,
        'title' : 'Update Profile'
    } 

    return render(request, 'users/update_profile.html', context)
@staff_member_required
def stats(request):
    y_data1 = [0,0,0,0,0,0,0,0,0,0]
    total_profiles = len(Profile.objects.all())
    for prof in Profile.objects.all() :
        if (int(prof.engaggr) > 99):
            y_data1[9]+=1
        elif (int(prof.engaggr) > 89):
            y_data1[8]+=1
        elif (int(prof.engaggr) > 79):
            y_data1[7]+=1
        elif (int(prof.engaggr) > 69):
            y_data1[6]+=1
        elif (int(prof.engaggr) > 59):
            y_data1[5]+=1
        elif (int(prof.engaggr) > 49):
            y_data1[4]+=1
        elif (int(prof.engaggr) > 39):
            y_data1[3]+=1
        elif (int(prof.engaggr) > 29):
            y_data1[2]+=1
        elif (int(prof.engaggr) > 19):
            y_data1[1]+=1
        else:
            y_data1[0]+=1
            
    x_data1 = [10, 20,30, 40, 50, 60, 70, 80, 90, 100]
    plot_div1 = plot([Bar(x=x_data1, y=y_data1,
                        name='engg_stud',
                        opacity=0.8,)],
               output_type='div')

    y_data2 = [0,0,0,0,0,0,0,0,0,0]
    total_comp = len(Post.objects.all())
    for prof in Post.objects.all() :
        if (int(prof.engg) > 99):
            y_data2[9]+=1
        elif (int(prof.engg) > 89):
            y_data2[8]+=1
        elif (int(prof.engg) > 79):
            y_data2[7]+=1
        elif (int(prof.engg) > 69):
            y_data2[6]+=1
        elif (int(prof.engg) > 59):
            y_data2[5]+=1
        elif (int(prof.engg) > 49):
            y_data2[4]+=1
        elif (int(prof.engg) > 39):
            y_data2[3]+=1
        elif (int(prof.engg) > 29):
            y_data2[2]+=1
        elif (int(prof.engg) > 19):
            y_data2[1]+=1
        else:
            y_data2[0]+=1
            
    x_data2 = [10, 20,30, 40, 50, 60, 70, 80, 90, 100]
    plot_div2 = plot([Bar(x=x_data2, y=y_data2,
                        name='engg_comp',
                        opacity=0.8,)],
               output_type='div')
    context={'plot_div1': plot_div1,'plot_div2': plot_div2,'tot_engg' : total_profiles,'tot_comp' : total_comp, 'title' : 'Stats'}
    return render(request, "users/stats.html", context)

@staff_member_required
def export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['Scylla - Export List'])
    writer.writerow(['First Name', 'Last Name','Tenth', 'Twelfth', 'Engineering Aggregate'])

    profiles = Profile.objects.all().values_list('firstname','lastname','tenth', 'twelveth', 'engaggr',)
    for profile in profiles:
        writer.writerow(profile)
    return response