from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User,auth,Group
from django.contrib import admin

from django.contrib import messages
from django.utils.text import capfirst
from django.contrib.auth.decorators import login_required
#from .models import *

from hospApp.models import department, doctor, inpatient_bill, pathology, patient
from hospApp.models import qualification,room,path_test,outpatient_bill,prescription



# Create your views here.

def is_admin(user):
    return user.groups.filter(name='Admin').exists()
def is_doctor(user):
    return user.groups.filter(name='Doctor').exists()
def is_patient(user):
    return user.groups.filter(name='Patient').exists()

def home(request):
    return render(request,'home.html')

@login_required(login_url='login')
def admin_home(request):
    return render(request,'admin/admin_home.html')

@login_required(login_url='login')
def user_home(request):
    usr = doctor.objects.get(user = request.user)
    context = {
            'doc' : usr
        }
    return render(request,'user/user_home.html',context)

@login_required(login_url='login')
def patient_home(request):
    usr = patient.objects.get(user = request.user)
    context = {
            'pat' : usr
        }
    return render(request,'patient/patient_home.html',context)

@login_required(login_url='login')
def add_dept(request):

    if request.method == "POST":

        dprt = department(department = request.POST['dpt'])
        dprt.save()
        return redirect('/show_dept')

    return render(request,'admin/add_dept.html')

@login_required(login_url='login')
def show_dept(request):
    dpt = department.objects.all()
    context = {
        'dpt' : dpt
    }
    return render(request, 'admin/show_dept.html', context)

@login_required(login_url='login')
def del_dept(request,pk):
    dpt = department.objects.get(id = pk)
    dpt.delete()
    return redirect('show_dept')

@login_required(login_url='login')
def add_qual(request):

    if request.method == "POST":

        qual = qualification(qualification = request.POST['qual'])
        qual.save()
        return redirect('/show_qual')

    return render(request,'admin/add_qual.html')

@login_required(login_url='login')
def show_qual(request):
    qual = qualification.objects.all()
    context = {
        'qual' : qual
    }
    return render(request, 'admin/show_qual.html', context)

@login_required(login_url='login')
def del_qual(request,pk):
    qual = qualification.objects.get(id = pk)
    qual.delete()
    return redirect('show_qual')

@login_required(login_url='login')
def add_doctor(request):

    if request.method=='POST':

        first_name=capfirst(request.POST['fname'])
        last_name=capfirst(request.POST['lname'])
        username=request.POST['uname']
        password=request.POST['pwd']
        cpassword=request.POST['cpwd']
        email=request.POST['email']
        address = capfirst(request.POST['address'])
        gender = request.POST['gender']
        c_num = request.POST['cnum']
        j_date = request.POST['date']
        fee = request.POST['fee']
        fkey1 = request.POST['qual']
        qual_id = qualification.objects.get(id = fkey1)
        fkey2 = request.POST['dpt']
        dpt_id = department.objects.get(id = fkey2)
        if request.FILES.get('file') is not None:
           pic=  request.FILES.get('file')
        else:
            pic = ''
            
        if password==cpassword:  #  password matching......
            if User.objects.filter(username=username).exists(): #check Username Already Exists..
                messages.info(request, 'This username already exists!!!!!!')
                return redirect('add_doctor')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                user.save()
                u = User.objects.get(id = user.id)
                
                dr = doctor(
                    address = address,
                    gender = gender,
                    contact_num = c_num,
                    qualification = qual_id,
                    department = dpt_id,
                    user = u,
                    profile_pic = pic,
                    joining_date = j_date,
                    fees = fee
                    )
                dr.save()
                    
                
               
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('add_doctor')   
        return redirect('add_doctor')

    qual = qualification.objects.all()
    dpt = department.objects.all()
    context = {
        'qual' : qual,
        'dpt'  : dpt
    }

    return render(request,'admin/doctor/add_doctor.html',context)

@login_required(login_url='login')
def show_doctor(request):
    doc = doctor.objects.all()
    context = {
        'doc' : doc
    }
    return render(request, 'admin/doctor/show_doc.html', context)

@login_required(login_url='login')
def edit_doctor(request,pk):
    doc = doctor.objects.get(id = pk)
    user2 = User.objects.get(id = doc.user_id)
    dpt = department.objects.all()
    qual = qualification.objects.all()
    if request.method == "POST":

      
        user2.first_name = capfirst(request.POST.get('f_name'))
        user2.last_name  = capfirst(request.POST.get('l_name'))
        user2.username = request.POST.get('uname')
        doc.address = capfirst(request.POST.get('address'))
        doc.gender = request.POST.get('gender')
        user2.email = request.POST.get('email')
        doc.contact_num = request.POST.get('cnum')
        doc.joining_date = request.POST.get('jdate')
        doc.fees = request.POST.get('fee')
        fkey1= request.POST.get('qual')
        doc.qualification = qualification.objects.get(id = fkey1)
        fkey2 = request.POST['dpt']
        doc.department= department.objects.get(id = fkey2)
        if len(request.FILES)!=0 :
            doc.profile_pic = request.FILES.get('file')

        doc.save()
        user2.save()
        return redirect('show_doctor')

    context = {
        'user1' : doc, 
        'user2' : user2,
        'dpt' : dpt,
        'qual' : qual
    }
    return render(request,'admin/doctor/edit_doc.html',context)

@login_required(login_url='login')
def del_doctor(request,pk):
    doc = doctor.objects.get(id = pk)   
    user = User.objects.get(id = doc.user_id)
    doc.delete()
    user.delete()
    return redirect('show_doctor')

@login_required(login_url='login')
def add_room(request):

    if request.method == "POST":

        room1 = room(room_number = request.POST['r_num'],
                    room_type = request.POST['r_type'],
                    room_charge = request.POST['r_chrg'])
        room1.save()
        return redirect('/show_room')

    return render(request,'admin/add_room.html')

@login_required(login_url='login')
def show_room(request):
    room1 = room.objects.all()
    context = {
        'room' : room1
    }
    return render(request, 'admin/show_room.html', context)

@login_required(login_url='login')
def del_room(request,pk):
    room1 = room.objects.get(id = pk)
    room1.delete()
    return redirect('show_room')

@login_required(login_url='login')
def add_test(request):

    if request.method == "POST":

        test1 = path_test(test_name = request.POST['test'],
                          charge = request.POST['chrg'])
        test1.save()
        return redirect('/show_test')

    return render(request,'admin/add_test.html')

@login_required(login_url='login')
def show_test(request):
    test1 = path_test.objects.all()
    context = {
        'test' : test1
    }
    return render(request, 'admin/show_test.html', context)

@login_required(login_url='login')
def del_test(request,pk):
    test1 = path_test.objects.get(id = pk)
    test1.delete()
    return redirect('show_test')

def signup(request):
    if request.method=='POST':

        first_name=capfirst(request.POST['fname'])
        last_name=capfirst(request.POST['lname'])
        username=request.POST['uname']
        password=request.POST['pwd']
        cpassword=request.POST['cpwd']
        email=request.POST['email']
        address = capfirst(request.POST['address'])
        gender = request.POST['gender']
        c_num = request.POST['cnum']
        age = request.POST['age']
        c_date = request.POST['date1']
        fkey1 = request.POST['doc']
        doc_id = doctor.objects.get(id = fkey1)
        if request.FILES.get('file') is not None:
           pic=  request.FILES.get('file')
        else:
            pic = ''
        
        
                 
        if password==cpassword:  #  password matching......
            if User.objects.filter(username=username).exists(): #check Username Already Exists..
                messages.info(request, 'This username already exists!!!!!!')
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                
                user.save()
                u = User.objects.get(id = user.id)

                p = patient(
                    first_name = first_name,
                    last_name = last_name,
                    age = age,
                    email = email,
                    address = address,
                    gender = gender,
                    contact_num = c_num,
                    consulting_date = c_date,
                    doctor =doc_id,
                    patient_type = 0,
                    user = u,
                    profile_pic = pic
                )
                pat_group = Group.objects.get(name = 'Patient')
                pat_group.user_set.add(user)

                p.save()
                
               
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('signup')   
        return redirect('signup')
    
    doc = doctor.objects.all()
    context = {
        'doc' : doc,
    }                
    return render(request,'patient/signup.html',context)


@login_required(login_url='login')
def add_inpatient(request):

    if request.method=='POST':

        first_name=capfirst(request.POST['fname'])
        last_name=capfirst(request.POST['lname'])
        email=request.POST['email']
        age = request.POST['age']
        address = capfirst(request.POST['address'])
        gender = request.POST.get('gender')
        c_num = request.POST['cnum']
        c_date = request.POST['date1']
        admit_date = request.POST['date2']
        fkey1 = request.POST['doc']
        doc_id = doctor.objects.get(id = fkey1)
        fkey2 = request.POST['room']
        r_id = room.objects.get(id = fkey2)
        desc = request.POST['desc']
        if request.FILES.get('file') is not None:
           pic=  request.FILES.get('file')
        else:
            pic = ''
        
        if patient.objects.filter(contact_num=c_num).exists():
            return redirect('add_inpatient')
        else:
            pt = patient(
                    first_name = first_name,
                    last_name = last_name,
                    age = age,
                    email = email,
                    address = address,
                    gender = gender,
                    contact_num = c_num,
                    doctor = doc_id,
                    room =r_id,
                    consulting_date = c_date,
                    admission_date = admit_date,
                    patient_type = 1,
                    profile_pic = pic
                    
                    )
            pt.save()
            pat =patient.objects.get(id = pt.id)     
            app = appointment(
                patient = pat,
                doctor = doc_id,
                description = desc,
                appointment_date = c_date,
                status = 1
            )
            app.save()

    doc = doctor.objects.all()
    room1 = room.objects.all()
    context = {
        'doc' : doc,
        'room1'  : room1
    }                
    return render(request,'admin/inpatient/add_inpatient.html',context)

@login_required(login_url='login')
def edit_inpatient(request,pk):
    pt = patient.objects.get(id = pk)
    doc = doctor.objects.all()
    room1 = room.objects.all()
    if request.method == "POST":

      
        pt.first_name = capfirst(request.POST.get('f_name'))
        pt.last_name  = capfirst(request.POST.get('l_name'))
        pt.address = capfirst(request.POST.get('address'))
        pt.gender = request.POST.get('gender')
        pt.email = request.POST.get('email')
        pt.contact_num = request.POST.get('cnum')
        pt.age = request.POST.get('age')
        pt.consulting_date = request.POST.get('date1')
        pt.admission_date = request.POST.get('date2')
        fkey1= request.POST.get('doc')
        pt.doctor = doctor.objects.get(id = fkey1)
        fkey2 = request.POST.get('room')
        pt.room= room.objects.get(id = fkey2)
        if len(request.FILES)!=0 :
            doc.profile_pic = request.FILES.get('file')


        pt.save()
        return redirect('show_inpatient')

    context = {
        'doc' : doc, 
        'pt' : pt,
        'room1' : room1
    }
    return render(request,'admin/inpatient/edit_inpatient.html',context)

@login_required(login_url='login')
def show_inpatient(request):
    ip = patient.objects.filter(patient_type = 1)
    context = {
        'inpatient' : ip,
    }
    return render(request, 'admin/inpatient/show_inpatient.html', context)

@login_required(login_url='login')
def del_inpatient(request,pk):
    ip = patient.objects.get(id = pk)   
    ip.delete()
    return redirect('show_inpatient')

@login_required(login_url='login')
def add_outpatient(request):

    if request.method=='POST':

        first_name=capfirst(request.POST['fname'])
        last_name=capfirst(request.POST['lname'])
        email=request.POST['email']
        age = request.POST['age']
        address = capfirst(request.POST['address'])
        gender = request.POST['gender']
        c_num = request.POST['cnum']
        c_date = request.POST['date1']
        fkey = request.POST['doc']
        doc_id = doctor.objects.get(id = fkey)
        desc = request.POST['desc']
        if request.FILES.get('file') is not None:
           pic=  request.FILES.get('file')
        else:
            pic = ''

        
        if patient.objects.filter(contact_num=c_num).exists():
            return redirect('add_outpatient')
        else:
            pt = patient(
                    first_name = first_name,
                    last_name = last_name,
                    age = age,
                    email = email,
                    address = address,
                    gender = gender,
                    contact_num = c_num,
                    doctor = doc_id,
                    consulting_date = c_date,
                    patient_type = 0,
                    profile_pic = pic
                    )
            pt.save()
            pat =patient.objects.get(id = pt.id)     
            app = appointment(
                patient = pat,
                doctor = doc_id,
                description = desc,
                appointment_date = c_date,
                status = 1
            )
            app.save()

    doc = doctor.objects.all()
    context = {
        'doc' : doc,
    }                
    return render(request,'admin/outpatient/add_outpatient.html',context)

@login_required(login_url='login')
def edit_outpatient(request,pk):
    pt = patient.objects.get(id = pk)
    doc = doctor.objects.all()
   
    if request.method == "POST":

        pt.first_name = capfirst(request.POST.get('f_name'))
        pt.last_name  = capfirst(request.POST.get('l_name'))
        pt.address = capfirst(request.POST.get('address'))
        pt.gender = request.POST.get('gender')
        pt.email = request.POST.get('email')
        pt.contact_num = request.POST.get('cnum')
        pt.age = request.POST.get('age')
        pt.consulting_date = request.POST.get('date1')
        fkey1= request.POST.get('doc')
        pt.doctor = doctor.objects.get(id = fkey1)
        if len(request.FILES)!=0 :
            doc.profile_pic = request.FILES.get('file')


        pt.save()
        return redirect('show_outpatient')

    context = {
        'doc' : doc, 
        'pt' : pt,
        
    }
    return render(request,'admin/outpatient/edit_outpatient.html',context)

@login_required(login_url='login')
def show_outpatient(request):
    op = patient.objects.filter(patient_type = 0)
    appointments = appointment.objects.get(patient_id = op[0].id)
    context = {
        'outpatient' : op,
        'appointments' : appointments
    }
    return render(request, 'admin/outpatient/show_outpatient.html', context)

@login_required(login_url='login')
def del_outpatient(request,pk):
    op = patient.objects.get(id = pk)  
    user = User.objects.get(id = op.user_id) 
    op.delete()
    user.delete()
    return redirect('show_outpatient')


#.......... Patient ......

@login_required(login_url='login')
def view_doctor(request):
    usr = patient.objects.get(user = request.user)
    
    doc=doctor.objects.all()
    context = {
            'doc':doc,
            'pat' : usr
        }
    return render(request,'patient/view_doctors.html',context)

@login_required(login_url='login')
def patient_appointment(request):
    usr = patient.objects.get(user = request.user)
    context = {
            'pat' : usr
        }
    return render(request,'patient/patient_appointment.html',context)

@login_required(login_url='login')
def add_appointment(request):

    pat = patient.objects.get(user= request.user)

    if request.method == "POST":

        fkey = request.POST['doc']
        doc_id = doctor.objects.get(id = fkey)
        date = request.POST['date']
        desc = request.POST['desc']

        app = appointment( patient = pat,
                          doctor = doc_id,
                          appointment_date = date,
                          description = desc,
                          status = 0
                        )
        app.save()
        


    doc = doctor.objects.all()
    context = {'doc' : doc,
                'pat' :pat }
    return render(request,'patient/add_appointment.html',context)

@login_required(login_url='login')
def view_appointment(request):
    pat = patient.objects.get(user = request.user)
    appointments=appointment.objects.filter(patient_id=pat.id)
    context = {
        'pat' : pat,
        'appointments':appointments
    }
    return render(request,'patient/view_appointment.html',context)

@login_required(login_url='login')
def pat_profile(request):
    
    pat = patient.objects.get(user = request.user)
    #app = appointment.objects.filter(patient_id = pat.id).filter(status = 1).earliest('appointment_date')
    context = {
        'pat' : pat,
        #'app' : app
    }
    return render(request,'patient/p_profile.html',context)

@login_required(login_url='login')
def edit_pat_profile(request,pk):
    pat = patient.objects.get(id = pk)
    user1 = User.objects.get(id = pat.user_id)
    doc = doctor.objects.all()
    if request.method == "POST":

      
        user1.first_name = capfirst(request.POST.get('f_name'))
        user1.last_name  = capfirst(request.POST.get('l_name'))
        pat.first_name=capfirst(request.POST.get('f_name'))
        pat.last_name  = capfirst(request.POST.get('l_name'))
        user1.username = request.POST.get('uname')
        pat.age = request.POST.get('age')
        pat.address = capfirst(request.POST.get('address'))
        pat.gender = request.POST.get('gender')
        user1.email = request.POST.get('email')
        pat.email = request.POST.get('email')
        pat.contact_num = request.POST.get('cnum')
        #fkey1= request.POST.get('doc')
        #pat.doctor = doctor.objects.get(id = fkey1)
        if len(request.FILES)!=0 :
            doc.profile_pic = request.FILES.get('file')


        pat.save()
        user1.save()
        return redirect('pat_profile')

    context = {
        'pat' : pat, 
        'user1' : user1,
        'doc' : doc,
    }
    return render(request,'patient/edit_p_profile.html',context)

@login_required(login_url='login')
def del_patient(request,pk):
    pat = patient.objects.get(id = pk)   
    user = User.objects.get(id = pat.user_id)
    pat.delete()
    user.delete()
    return redirect('show_outpatient')

@login_required(login_url='login')
def book_appointment(request,pk):

    pat = patient.objects.get(user= request.user)
    doc = doctor.objects.get(id = pk)

    if request.method == "POST":
        
        date = request.POST['date']
        desc = request.POST['desc']

        app = appointment( patient = pat,
                          doctor = doc,
                          appointment_date = date,
                          description = desc,
                          status = 0
                        )
        app.save()

    context = { 
                'doc' : doc,
                'pat' :pat 
            }
    return render(request,'patient/book_appointment.html',context)


@login_required(login_url='login')
def cancel_appointment(request,pk):
    appointment1=appointment.objects.get(id=pk)
    appointment1.delete()
    #messages.error(request,'Your appointment request is rejected')
    return redirect('view_appointment')


#--- admin ----
@login_required(login_url='login')
def admin_appointment(request):
    return render(request,'admin/appointment/admin_appointment.html')



@login_required(login_url='login')
def admin_view_appointment(request):
    appointments1=appointment.objects.all().filter(status= 1)
    appointments2=appointment.objects.all().filter(status= 2)
    context = {
        'appointments1':appointments1,
        'appointments2': appointments2
    }
    return render(request,'admin/appointment/admin_view_appointment.html',context)

@login_required(login_url='login')
def admin_approve_appointment(request):
    appointments=appointment.objects.all().filter(status=False)
    context = {'appointments':appointments}
    return render(request,'admin/appointment/admin_approve_appointment.html',context)



@login_required(login_url='login')
def approve_appointment(request,pk):
    appointment1=appointment.objects.get(id=pk)
    appointment1.status=1
    appointment1.save()
    #messages.success(request,'Your appointment request is approved')

    return redirect('admin_approve_appointment')


@login_required(login_url='login')
def reject_appointment(request,pk):
    appointment1=appointment.objects.get(id=pk)
    appointment1.status = 2
    appointment1.save()
    #messages.error(request,'Your appointment request is rejected')
    return redirect('admin_approve_appointment')

@login_required(login_url='login')
def del_appointment(request,pk):
    appointment1=appointment.objects.get(id=pk)
    appointment1.delete()
    #messages.error(request,'Your appointment request is rejected')
    return redirect('admin_view_appointment')


# --- login ----
@login_required(login_url='login')
def add_pathology(request):

    if request.method == "POST":
        p = request.POST['p_id']
        p_id = patient.objects.get(id = p)
        fkey = request.POST['test']
        test_id = path_test.objects.get(id = fkey)
        t_date = request.POST['date']
        desc = request.POST['desc']

        test = pathology( patient = p_id,
                          path_test = test_id,
                          test_date = t_date,
                          description = desc
                        )
        test.save()

    test = path_test.objects.all()    
    context = {
        'test' : test, 
        }
    return render(request,'admin/pathology/add_pathology.html',context)

@login_required(login_url='login')
def show_pathology(request):
    pat = pathology.objects.all()
    context = {
        'pathology' : pat,
    }
    return render(request, 'admin/pathology/show_pathology.html', context)

@login_required(login_url='login')
def del_pathology(request,pk):
    pat = pathology.objects.get(id = pk)   
    pat.delete()
    return redirect('show_pathology')

@login_required(login_url='login')
def add_ipbill(request):

    if request.method == "POST":
        p = request.POST['p_id']
        p_id = patient.objects.get(id = p)
        d_id = doctor.objects.get(id = p_id.doctor_id)
        room_id = room.objects.get(id = p_id.room_id)
        b_date = request.POST['b_date']
        d_date = request.POST['d_date']

        if pathology.patient_id == p_id.id is not None: 
            
            path_id = pathology.objects.filter(patient_id = p_id.id)
            total = d_id.fees + path_id.path_test.charge + room_id.room_charge
        else:
            total = d_id.fees+room_id.room_charge

        if p_id.patient_type == 1:
            bill = inpatient_bill( patient = p_id,
                          #doctor = d_id,
                          #pathology = path_id,
                          #room = room_id,
                          bill_date = b_date,
                          discharge_date = d_date,
                          total = total
                        )
            bill.save()
        

    return render(request,'admin/billing/add_ipbill.html' )

@login_required(login_url='login')
def add_opbill(request):

    if request.method == "POST":
        p = request.POST['p_id']
        p_id = patient.objects.get(id = p)
        d_id = doctor.objects.get(id = p_id.doctor_id)
        #path_id = pathology.objects.get(patient_id = p_id)
        b_date = request.POST.get('b_date')
        total = d_id.fees #+ pathology.objects.get(patient_id = p_id).path_test.charge
        

        if p_id.patient_type == 0:

            bill = outpatient_bill( patient = p_id,
                          #doctor = d_id,
                          #pathology = path_id,
                          bill_date = b_date,
                          total = total
                        )
            bill.save()
        else:
            messages.info(request, 'Not an outpatient !!!!!')


    
    return render(request,'admin/billing/add_opbill.html')

@login_required(login_url='login')
def show_bill(request):
    ip = inpatient_bill.objects.all()
    op = outpatient_bill.objects.all()
    context = {
        'ip' : ip,
        'op' : op
    }
    return render(request, 'admin/billing/show_bill.html', context)

@login_required(login_url='login')
def del_ipbill(request,pk):
    ip = inpatient_bill.objects.get(id = pk)   
    ip.delete()
    return redirect('show_bill')

@login_required(login_url='login')
def del_opbill(request,pk):
    op = outpatient_bill.objects.get(id = pk)   
    op.delete()
    return redirect('show_bill')

@login_required(login_url='login')
def profile(request):
    
    doc = doctor.objects.get(user = request.user)
    context = {
        'doc' : doc
    }
    return render(request,'user/profile.html',context)

@login_required(login_url='login')
def edit_profile(request,pk):
    doc = doctor.objects.get(id = pk)
    user1 = User.objects.get(id = doc.user_id)
    dpt = department.objects.all()
    qual = qualification.objects.all()
    if request.method == "POST":

      
        user1.first_name = capfirst(request.POST.get('f_name'))
        user1.last_name  = capfirst(request.POST.get('l_name'))
        doc.address = capfirst(request.POST.get('address'))
        user1.username = request.POST.get('uname')
        doc.gender = request.POST.get('gender')
        user1.email = request.POST.get('email')
        doc.contact_num = request.POST.get('cnum')
        fkey1= request.POST.get('qual')
        doc.qualification = qualification.objects.get(id = fkey1)
        fkey2 = request.POST['dpt']
        doc.department= department.objects.get(id = fkey2)
        if len(request.FILES)!=0 :
            doc.profile_pic = request.FILES.get('file')

        doc.save()
        user1.save()
        return redirect('profile')

    context = {
        'doc' : doc, 
        'user1' : user1,
        'dpt' : dpt,
        'qual' : qual
    }
    return render(request,'user/edit_profile.html',context)

@login_required(login_url='login')
def show_patient(request):

    usr = doctor.objects.get(user = request.user)
    pat = patient.objects.filter(doctor_id = usr.id)
    appointments = appointment.objects.filter(doctor_id = usr.id).filter(status = 1)
    context = {
        'pat' : pat,
        'doc' : usr,
        'appointments' : appointments,
        
    }
    return render(request,'user/show_patient.html',context)

'''@login_required(login_url='login')
def remove_patient_view(request,pk):
    appointment1=appointment.objects.get(id=pk)
    #appointment1.delete()
    usr = doctor.objects.get(user = request.user)
    appointments = appointment.objects.filter(doctor_id = usr.id).filter(status = 1).filter(id != appointment1.id)
    context = {
        #'pat' : pat,
        'doc' : usr,
        'appointments' : appointments,
        
    }
    return redirect('show_patient',context)

@login_required(login_url='login')
def patient_count(request):

    usr = doctor.objects.get(user = request.user)
    op_count = patient.objects.filter(doctor_id = usr.id).count()
    ip_count = patient.objects.all().filter(patient_type = 0).count()
    #path =  pathology.objects.get(patient = pat)
    context = {
        'op' : op_count,
        'ip' : ip_count
    }
    return render(request,'user/show_patient.html',context)'''

@login_required(login_url='login')
def add_prescription(request):

    if request.method == "POST":

        date1 = request.POST['date']
        p = request.POST['p_id']
        p_id = patient.objects.get(id = p)
        d_id = doctor.objects.get(user = request.user)
        med = request.POST['med']
        desc = request.POST['desc']  
        
        med1 = prescription( 
                date = date1,
                patient = p_id,
                doctor = d_id,
                medicine_name = med,
                description = desc
                )
        med1.save()
        

    usr = doctor.objects.get(user = request.user)
    context = {
        'doc' : usr 
    }

    return render(request,'user/add_prescription.html',context)

@login_required(login_url='login')
def show_details(request,pk):

    pat = patient.objects.get(id = pk)
    doc = doctor.objects.get(user = request.user)
    med = prescription.objects.filter(patient_id = pk)
    path = pathology.objects.filter(patient_id = pk)

    context = { 
                'pat' : pat, 
                'doc' : doc,
                'med' : med,
                'path' :path
            }
    return render (request, 'user/show_pat_details.html',context)





def login(request):
        
    if request.method == 'POST':
        
        username = request.POST['uname']
        password = request.POST['pswd']
        user = auth.authenticate(username= username,password=password)
        if user is not None:
          if user.is_staff:
                auth.login(request,user)
                return redirect('admin_home')
          else:
                
            if user.groups.filter(name='Patient').exists():
                auth.login(request,user)
                return redirect('patient_home')
            else:
                auth.login(request,user)
                return redirect('user_home')
            
        else:
            messages.info(request,"Invalid Username or Password")
            return redirect('/home')
    
    return render(request,'base.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('home')

