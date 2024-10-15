import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.core.files.storage import FileSystemStorage
from django.db.models import Max
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import *

import random
# Create your views here.

def login_get(request):
    return render(request,"Login_index.html")

def login_post(request):
    USERNAME=request.POST['textfield']
    PASSWORD=request.POST['textfield2']
    res=Login.objects.filter(username=USERNAME,password=PASSWORD)
    if res.exists():
        res=res[0]
        if res.usertype=='admin':
            request.session['lg']='lin'
            return redirect('/admin_home')
        elif res.usertype=='Internal Guide':
            request.session['lg'] = 'lin'
            request.session['lid'] = res.id
            return redirect('/internal_home')
        elif res.usertype=='External_Guide':
            request.session['lg'] = 'lin'
            request.session['lid']=res.id
            return redirect('/external_home')


        else:
            return HttpResponse("<script>alert('USER NOT FOUND');window.location='/'</script>")

    else:
        return HttpResponse("<script>alert('INVALID DATA');window.location='/'</script>")



def admin_home(request):
    if request.session['lg']!='lin':
        return redirect('/')
    return render(request,"admin/ADMIN HOME.html")



def admin_add_external_guide_get(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    return render(request,"admin/ADD EXTERNAL GUIDE.html")

def admin_add_external_guide_post(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Name=request.POST['textfield9']
    Posts=request.POST['textfield2']
    Company_name=request.POST['textfield3']
    Place=request.POST['textfield4']
    Post_office=request.POST['textfield5']
    Pin_no=request.POST['textfield6']
    Email=request.POST['textfield7']
    Phn_no=request.POST['textfield8']
    psw=random.randint(0000,9999)
    obj=Login()
    obj.username=Email
    obj.password=psw
    obj.usertype='External_Guide'
    obj.save()

    external_guide_obj=External_Guide()
    external_guide_obj.eg_name=Name
    external_guide_obj.eg_posts=Posts
    external_guide_obj.eg_company_name=Company_name
    external_guide_obj.eg_place=Place
    external_guide_obj.eg_post_office=Post_office
    external_guide_obj.eg_pin=Pin_no
    external_guide_obj.eg_email=Email
    external_guide_obj.eg_phone=Phn_no

    external_guide_obj.EG=obj
    external_guide_obj.save()
    import smtplib

    # s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    # s.starttls()
    # s.login("completemyproject3@gmail.com", "tvgi dsxm dxry kilj")
    # msg = MIMEMultipart()  # create a message.........."
    # msg['From'] = "completemyproject3@gmail.com"
    # msg['To'] = id
    # msg['Subject'] = "Your Username & Password for Complete My Project:"
    # body = "You Username is :- - -"+Email +"\n"+ "Your Password is:- - " + str(psw)
    # msg.attach(MIMEText(body, 'plain'))
    # s.send_message(msg)
    # return HttpResponse("<script>alert('added successfully');window.location='/admin_add_external_guide_get'</script>")
    return redirect('/admin_view_external_guide#cmp')
def admin_view_external_guide(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    res=External_Guide.objects.all()
    return render(request,'admin/VIEW EXT GUIDE.html',{'data':res})

def admin_update_external_guide_get(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    res=External_Guide.objects.get(id=id)
    return render(request, "admin/Update_external_guide.html",{'data':res,'id':id})

def admin_update_external_guide_post(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Name = request.POST['textfield']
    Posts = request.POST['textfield2']
    Company_name = request.POST['textfield3']
    Place = request.POST['textfield4']
    Post_office = request.POST['textfield5']
    Pin_no = request.POST['textfield6']
    Email = request.POST['textfield7']
    Phn_no = request.POST['textfield8']
    External_Guide.objects.filter(id=id).update(eg_name=Name,eg_posts=Posts,eg_company_name=Company_name,eg_place=Place,eg_post_office=Post_office,eg_pin=Pin_no
                                                ,eg_email=Email,eg_phone=Phn_no)
    # return HttpResponse("<script>alert('Updated successfully');window.location='/admin_view_external_guide'</script>")
    return redirect('/admin_view_external_guide#cmp')
def admin_external_guide_delete(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Login.objects.filter(id=id).delete()
    # return HttpResponse("<script>alert('Deleted successfully');window.location='/admin_view_external_guide'</script>")
    return redirect('/admin_view_external_guide#cmp')

def admin_batch_add_get(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    return render(request,"admin/BATCH ADD.html")

def admin_batch_add_post(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Batches=request.POST['textfield']

    batch_obj=Batch()
    batch_obj.batch=Batches

    batch_obj.save()
    # return HttpResponse("<script>alert('added successfully');window.location='/admin_batch_add_get'</script>")
    return redirect('/batch_view#cmp')
def batch_view(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    res=Batch.objects.all()
    return render(request,'admin/BATCH VIEW.html',{'data':res})


def batch_add_student_get(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Res = Group.objects.filter(GRP_BATCHID_id=id)
    data=[]
    for i in Res:
        data.append({'id':i.id, 'grpname':i.grp_topic_name+" (Group " + i.grp_number + ")"})
     # return render(request, "admin/GRP MANAG ADD STUD.html",{'data':Res,'id':id})
    return render(request, "admin/batch add student.html",{'id':id, 'data':data})

def batch_add_student_post(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Name=request.POST['textfield']

    Registration_no=request.POST['textfield2']
    # grpid=request.POST['select']
    Email=request.POST['textfield3']

    Phone=request.POST['textfield4']
    # res=Batch.objects.get(id=id)


    obj=Student()
    obj.std_name=Name
    # obj.std_dob=DOB
    # obj.std_gender=Gender
    obj.std_regno =Registration_no
    # obj.type_mem_lead=Type
    obj.std_email=Email
    obj.std_phone=Phone
    # obj.std_group_id_id=grpid
    obj.std_batch_id=id
    obj.save()
    # return HttpResponse("<script>alert('added successfully');window.location='/batch_view'</script>")
    return redirect('/batch_view_student/'+str(id)+'#cmp')
def batch_view_student(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    res=Student.objects.filter(std_batch=id)
    return render(request,'admin/batch student view.html',{'data':res,"id":id})

def admin_update_batch_student_get(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Res=Student.objects.get(id=id)
    return render(request, "admin/UPDATE batch student.html",{'data':Res,'id':id})


def admin_update_batch_student_post(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Name = request.POST['textfield']
    Registration_no= request.POST['textfield2']
    # type=request.POST['select']
    Email = request.POST['textfield3']
    Phone = request.POST['textfield4']

    # Student.objects.filter(id=id).update(std_name=Name,std_dob=DOB,std_email=Email,std_phone=Phone,std_gender=Gender)
    Student.objects.filter(id=id).update(std_name=Name, std_regno=Registration_no,type_mem_lead=type, std_email=Email, std_phone=Phone)
    res = Student.objects.get(id=id)
    # return HttpResponse("<script>alert('Updated successfully');window.location='/group_management_view'</script>")
    return redirect('/batch_view_student/'+str(res.std_batch.id)+'#cmp')



def admin_batch_delete(request, id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Batch.objects.filter(id=id).delete()
    # return HttpResponse("<script>alert('Deleted successfully');window.location='/batch_view'</script>")
    return redirect('/batch_view#cmp')

def admin_batch_student_delete(request, id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Student.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/batch_view'</script>")
    # return redirect('/batch_view_student'+str(id)+'#cmp')

def admin_group_management_add_get(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    res=Batch.objects.all()

    re=Internal_Guide.objects.all()
    r=External_Guide.objects.all()
    s=Student.objects.all()
    n = 1
    t = Group.objects.all()
    if t.exists():
        n = len(t)+1
    return render(request,"admin/Group Managment Add.html",{'data':res,'data2':re,'data3':r,'data4':s, "data5": n})

def ajax_grp_batch(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    bid=request.POST['bid']
    res=Group.objects.filter(GRP_BATCHID_id=bid).aggregate(Max('grp_number'))
    print(res)
    if res["grp_number__max"] is None:
        grp_no=1

    else:
        grp_no=int(res["grp_number__max"]) + 1
    return JsonResponse({'status':'ok', 'data':grp_no})


# def ajax_grp_batch(request,eid):
#     # bid=request.POST['bid']
#     res=Group.objects.filter(GRP_BATCHID_id=eid).aggregate(Max('grp_number'))
#     res1=Student.objects.filter(std_batch_id=eid)
#     print(res)
#     if res["grp_number__max"] is None:
#         grp_no=1
#
#     else:
#         grp_no=int(res["grp_number__max"]) + 1
#     print(res1)
#     return render(request,'admin/ajax_grp_students.html',{"data":grp_no,"data1":res1})
#     # return JsonResponse({'status':'ok', 'data':grp_no,"data1":res1})


def admin_group_management_add_post(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    #name=request.POST['textfield']
    batch_id=request.POST['select']
    group_no=request.POST['textfield1']
    # group_leader=request.POST['textfield7']
    internal_guide=request.POST['select2']
    external_guide=request.POST['select3']
    leader=request.POST['textfield2']
    email=request.POST['textfield3']
    member1=request.POST['textfield4']
    member2=request.POST['textfield5']
    topic_name=request.POST['textfield6']

    stds = [leader, member1, member2]

    # res = Login.objects.filter(username=email)
    # if res.exists():
    #     return HttpResponse("<script>alert('Email Exists');window.location='/admin_group_management_add_get'</script>")
    # else:

    psw = random.randint(0000, 9999)
    obj = Login()
    obj.username = email
    obj.password = psw
    obj.usertype = 'Group'
    obj.save()


    bid=Batch.objects.get(id=batch_id)
    igid=Internal_Guide.objects.get(id=internal_guide)
    egid=External_Guide.objects.get(id=external_guide)

    group_management_obj=Group()

    group_management_obj.GRP_BATCHID=bid

    group_management_obj.grp_number=group_no
    group_management_obj.GRP_IG=igid
    group_management_obj.GRP_EG=egid
    group_management_obj.grp_leader_id=leader
    group_management_obj.grp_email=email

    group_management_obj. grp_topic_name=topic_name

    group_management_obj.LOGIN= obj
    group_management_obj.save()

    for i in stds:
        group_member_obj=Group_member()
        group_member_obj.GRP_ID=group_management_obj
        group_member_obj.LEADER_STUD_ID_id=i
        group_member_obj.save()

    # return HttpResponse("<script>alert('added successfully');window.location='/admin_group_management_add_get'</script>")
    return redirect('/group_management_view#cmp')

def group_management_view(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    res = Group.objects.all()
    return render(request, 'admin/VIEW GRP MANGMT.html', {'data': res})

def admin_update_group_management_get(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Res=Group.objects.get(id=id)
    res = Batch.objects.all()
    re = Internal_Guide.objects.all()
    r = External_Guide.objects.all()
    s=Student.objects.all()
    return render(request, "admin/UPDATE Group Managment .html",{'data':res,'DATA10':Res,'data2':re,'data3':r,'data4':s,'id':id})

def admin_update_group_management_post(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    batch_id = request.POST['select']
    group_no = request.POST['textfield2']
    internal_guide = request.POST['select2']
    external_guide = request.POST['select3']
    leader=request.POST['select4']
    email = request.POST['textfield5']
    topic_name = request.POST['textfield6']

    Group.objects.filter(id=id).update(GRP_BATCHID=batch_id,grp_number=group_no,GRP_IG=internal_guide,GRP_EG=external_guide,grp_leader=leader,grp_email=email,grp_topic_name=topic_name)
    # return HttpResponse("<script>alert('Updated successfully');window.location='/group_management_view'</script>")
    return redirect('/group_management_view#cmp')
def admin_group_management_delete(request, id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Group.objects.filter(id=id).delete()
    # return HttpResponse("<script>alert('Deleted successfully');window.location='/group_management_view'</script>")
    return redirect('/group_management_view#cmp')

def group_management_add_student_get(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    res = Student.objects.filter(std_group_id_id=id)
    if len(res)<3:
        return render(request, "admin/student management add.html",{'id':id})
    else:
        return HttpResponse("<script>alert('Maximum limit exceeded');window.location='/group_management_view#cmp'</script>")


def group_management_add_student_post(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Name=request.POST['textfield']
    # DOB=request.POST['textfield2']
    # Gender=request.POST['RadioGroup1']

    Registration_no=request.POST['textfield2']
    Type=request.POST['select']
    Email=request.POST['textfield3']

    Phone=request.POST['textfield4']
    res=Group.objects.get(id=id)

    obj=Student()
    obj.std_name=Name
    # obj.std_dob=DOB
    # obj.std_gender=Gender
    obj.std_regno =Registration_no
    obj.type_mem_lead=Type
    obj.std_email=Email
    obj.std_phone=Phone
    obj.std_group_id=res


    obj.save()
    return HttpResponse("<script>alert('added successfully');window.location='/group_management_view'</script>")

def group_management_view_student(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    res = Group_member.objects.filter(GRP_ID=id)
    arr = []

    for i in res:
        type = "Member"
        if Group.objects.get(id=id).grp_leader.id == i.LEADER_STUD_ID_id:
            type = "Leader"
        arr.append({"LEADER_STUD_ID": i.LEADER_STUD_ID,
                    "id": i.LEADER_STUD_ID.id,
                    "type": type})
    return render(request,'admin/student management view.html',{'data':arr})

def admin_add_internal_guide_get(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    return render(request,"admin/INTERNAL MANAG ADD.html")

def admin_add_internal_guide_post(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Name=request.POST['textfield']
    Email=request.POST['textfield2']
    Phone_no=request.POST['textfield3']

    psw = random.randint(0000, 9999)
    obj = Login()
    obj.username = Email
    obj.password = psw
    obj.usertype = 'Internal Guide'
    obj.save()

    internal_guide_obj = Internal_Guide()
    internal_guide_obj.ig_name = Name
    internal_guide_obj.ig_email=Email
    internal_guide_obj.ig_phone=Phone_no

    internal_guide_obj.IG = obj
    internal_guide_obj.save()
    # return HttpResponse("<script>alert('added successfully');window.location='/admin_add_internal_guide_get'</script>")
    return redirect('/admin_view_internal_guide#cmp')
def admin_view_internal_guide(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    res=Internal_Guide.objects.all()
    return render(request,'admin/INTERANAL GUIDE VIEW.html',{'data':res})

def admin_update_internal_guide_get(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Res=Internal_Guide.objects.get(id=id)
    return render(request, "admin/UPDATE INTERNAL_GUIDE.html",{'data':Res,'id':id})

def admin_update_internal_guide_post(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Name = request.POST['textfield']
    Email = request.POST['textfield2']
    Phone_no = request.POST['textfield3']

    Internal_Guide.objects.filter(id=id).update(ig_name=Name,ig_email=Email,ig_phone=Phone_no)
    # return HttpResponse("<script>alert('Updated successfully');window.location='/admin_view_internal_guide'</script>")
    return redirect('/admin_view_internal_guide#cmp')

def admin_Internal_guide_delete(request, id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Login.objects.get(id=id).delete()
    # Internal_Guide.objects.filter(id=id).delete()
    # return HttpResponse"<script>alert('Deleted successfully');window.location='/admin_view_internal_guide'</script>")
    return redirect('/admin_view_internal_guide#cmp')

def admin_add_project_management_get(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    res=Batch.objects.all()
    return render(request,"admin/Project management add.html",{'data':res})

def admin_add_project_management_post(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    b=request.POST['select']
    Note=request.POST['textarea']
    Date=datetime.datetime.now().strftime("%d-%m-%y")
    Time=datetime.datetime.now().strftime("%H:%M")
    res=Batch.objects.get(id=b)
    project_management_obj = Project_schedule()
    project_management_obj.note=Note
    project_management_obj.date=Date
    project_management_obj.BATCH=res
    project_management_obj.time=Time

    project_management_obj.save()
    # return HttpResponse("<script>alert('added successfully');window.location='/admin_add_project_management_get'</script>")
    return redirect('/admin_view_project_management#cmp')

def admin_view_project_management(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    res=Project_schedule.objects.all()
    return render(request,'admin/Project management view.html',{'data':res})


def admin_update_project_management_get(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    res=Batch.objects.all()
    r=Project_schedule.objects.get(id=id)
    return render(request,"admin/update Project management add.html",{'data':res,'data2':r,'id':id})

def admin_update_project_management_post(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    b=request.POST['select']
    Note=request.POST['textfield']
    Date = datetime.datetime.now().strftime("%d-%m-%y")
    Time = datetime.datetime.now().strftime("%H:%M")
    res=Batch.objects.get(id=b)
    Project_schedule.objects.filter(id=id).update(BATCH=res,note=Note,date=Date,time=Time)
    # return HttpResponse("<script>alert('updated successfully');window.location='/admin_view_project_management'</script>")
    return redirect('/admin_view_project_management#cmp')
def admin_delete_project_management_post(request, id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Project_schedule.objects.filter(id=id).delete()
    # return HttpResponse("<script>alert('Deleted successfully');window.location='/admin_view_project_management'</script>")
    return redirect('/admin_view_project_management#cmp')

def admin_view_circular(request, id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    res = Circular.objects.filter(GROUP=id)
    return render(request, 'admin/View circular.html', {'data': res, "id": id})

def admin_project_circular_get(request, id):
    return render(request, "admin/Add circular.html", {"id": id})
def admin_project_circular_post(request, id):
    date = datetime.datetime.now().strftime("%d-%m-%y")
    time = datetime.datetime.now().strftime("%H:%M")
    Note=request.POST['textarea']

    circular_obj=Circular()
    circular_obj.GROUP_id=id
    circular_obj.Date=date
    circular_obj.Time= time
    circular_obj.note = Note
    circular_obj.save()

    # return HttpResponse("<script>alert('Added successfully');window.location='/admin_view_circular/"+id+"'</script>")
    return redirect('/admin_view_circular/'+id+'#cmp')



def admin_delete_circular(request,id, cid):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Circular.objects.filter(id=id).delete()

    return redirect('/admin_view_circular/'+cid+'#cmp')

def admin_search_attendance_get(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    qry=Batch.objects.all()
    return render(request, "admin/VIEW ATTENDANCE.html",{'batches':qry})

def ajax_grp_by_batch(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    bid=request.POST['bid']
    res=Group.objects.filter(GRP_BATCHID_id=bid)
    print(res)
    data=[]
    for i in res:
        data.append({'id':i.id, 'grp_topic_name':i.grp_topic_name})
    return JsonResponse({'status':'ok', 'data':data})

def ajax_att_by_group(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    grpid=request.POST['grpid']
    res=Attendance.objects.filter(GRP_ID=grpid)
    print(res)
    data=[]
    for i in res:
        data.append({'id':i.id, 'file':i.file, 'date_upload':i.date_upload})
    return JsonResponse({'status':'ok', 'data':data})


def admin_search_attendance_post(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Group = request.GET['select2']
    at=Attendance.objects.filter(GRP=Group)

    qry=Batch.objects.all()


    return render(request, "admin/VIEW ATTENDANCE.html",{'data':at,'batches':qry})


def group(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    grp=Group.objects.filter(GRP_BATCHID=id)
    print(grp)
    return render(request, 'admin/GROUP ATTENDANCE.html', {'grp': grp})

# def batch(request):
#     bt=Batch.objects.all()
#     print(bt)
#     return render(request, 'admin/VIEW ATTENDANCE.html', {'bt': bt})

def admin_view_attendance(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    res = Attendance.objects.all()
    return render(request, 'admin/VIEW ATTENDANCE.html', {'data': res})

def admin_progress_get(request):
    if request.session['lg'] != 'lin':
        return redirect('/')

    qry=Batch.objects.all()
    return render(request, "admin/VIEW PROGRESS.html",{'batches':qry})

def admin_progress_post(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Group = request.POST['group']
    at=Progress.objects.filter(GRP=Group)

    qry=Batch.objects.all()
    return render(request, "admin/VIEW PROGRESS.html",{'data':at,'batches':qry})

def group_progress(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    grp=Group.objects.filter(GRP_BATCHID=id)
    print(grp)
    return render(request,"admin/GROUP PROGRESS.html",{'grp':grp})

def ajax_progress_by_group(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    grpid=request.POST['grpid']
    res=Progress.objects.filter(GRP_id=grpid)
    print(res)
    data=[]
    for i in res:
        data.append({'id':i.id, 'Description':i.progress_file, 'date_upload':i.date_upload,'Remark':i.remark})
    return JsonResponse({'status':'ok', 'data':data})

def admin_add_scores_get(request, id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    return render(request, "admin/ADD SCORES ADMIN.html", {'id': id})

def admin_add_scores_get_post(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    punctuality = request.POST['textfield']
    relevance= request.POST['textfield2']
    presentation1 = request.POST['textfield3']
    presentation2 = request.POST['textfield4']
    presentation3 = request.POST['textfield5']
    demo = request.POST['textfield6']
    institution_report = request.POST['textfield7']
    viva = request.POST['textfield8']
    total = request.POST['textfield9']
    ob=Scores.objects.filter(GRP=id)
    if ob.exists():
        return HttpResponse("<script>alert('already added');window.location='/admin_view_scores/"+request.session['scoreid']+"#cmp'</script>")

    marks_obj = Scores()
    marks_obj.Punctuality = punctuality
    marks_obj.Relevance=relevance
    marks_obj.Presentation_1=presentation1
    marks_obj.Presentation_2=presentation2
    marks_obj.Presentation_3=presentation3
    marks_obj.Demo_report=demo
    marks_obj.Institution_copy=institution_report
    marks_obj.Viva=viva
    marks_obj.Total =total
    marks_obj.GRP_id=id

    marks_obj.save()
    # return HttpResponse("<script>alert('added successfully');window.location='/group_management_view#cmp'</script>")
    return redirect('/admin_view_scores/'+id+"#cmp")
def admin_view_scores(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    request.session['scoreid']=id
    res = Scores.objects.filter(GRP=id)
    return render(request, 'admin/VIEW SCORES ADMIN.html', {'data': res,"id":id})

def admin_update_scores_get(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Res=Scores.objects.get(id=id)
    return render(request, "admin/UPDATE SCORES ADMIN.html",{'data':Res,'id':id})

def admin_update_scores_post(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    punctuality = request.POST['textfield']
    relevance = request.POST['textfield2']
    presentation1 = request.POST['textfield3']
    presentation2 = request.POST['textfield4']
    presentation3 = request.POST['textfield5']
    demo = request.POST['textfield6']
    institution_report = request.POST['textfield7']
    viva = request.POST['textfield8']
    total = request.POST['textfield9']


    Scores.objects.filter(id=id).update(Punctuality = punctuality,Relevance=relevance,Presentation_1=presentation1,Presentation_2=presentation2,Presentation_3=presentation3,Demo_report = demo,Institution_copy=institution_report,Viva=viva,Total =total)
    return redirect('/admin_view_scores/'+request.session['scoreid']+'#cmp')



########################################## INTERNAL GUIDE ########################################################################

def internal_home(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    qry = Project_schedule.objects.all()
    if qry.exists():
        note = qry[0].note
        return render(request, "INTERNAL GUIDE/INTERNAL ORGANISATION HOME.html",{"status":note})

    else:
        note = "currently No notifications!!...."
        return render(request, "INTERNAL GUIDE/INTERNAL ORGANISATION HOME.html",{"status":note})

def internal_view_groups(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    print(request.session['lid'])
    grp=Group.objects.filter(GRP_IG=Internal_Guide.objects.get(IG_id=request.session['lid']))
    return render(request,"INTERNAL GUIDE/VIEW ASSIGNED GROUPS OF INTERNAL.html",{'grp':grp})

def internal_view_external_organisation(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    eg=External_Guide.objects.all()
    return render(request,"INTERNAL GUIDE/VIEW EXTERNAL ORGANISATION INTERNAL.html",{'eg':eg})

def internal_view_attendance(request, id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    bt=Attendance.objects.filter(STD_ID=id)
    # grp = Group.objects.filter(GRP_IG=Internal_Guide.objects.get(IG_id=request.session['lid']))
    # return render(request,"INTERNAL GUIDE/VIEW ATTENDANCE INTERNAL.html",{'bt':bt, 'data':grp})
    return render(request,"INTERNAL GUIDE/VIEW ATTENDANCE INTERNAL.html",{'bt':bt})

def internal_group_management_view_student(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    d=Group.objects.get(id=id)
    res=Group_member.objects.filter(GRP_ID=id)
    arr = []

    for i in res:
        type = "Member"
        if Group.objects.get(id=id).grp_leader.id == i.LEADER_STUD_ID_id:
            type = "Leader"
        arr.append({"LEADER_STUD_ID": i.LEADER_STUD_ID,
                    "id": i.LEADER_STUD_ID.id,
                    "type": type})


    return render(request,'INTERNAL GUIDE/internal student details view.html',{'data':arr})


def internal_group(request,eid):
    if request.session['lg'] != 'lin':
        return redirect('/')
    grp=Group.objects.filter(GRP_BATCHID=eid)
    bt = Batch.objects.all()

    return render(request,"INTERNAL GUIDE/INTERNAL GROUP ATTENDANCE.html",{'grp':grp,'bt':bt})

def internal_view(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Group = request.POST['select2']
    at = Progress.objects.filter(GRP=Group)

    qry = Batch.objects.all()
    return render(request, "INTERNAL GUIDE/VIEW ATTENDANCE INTERNAL.html", {'data': at, 'batches': qry})

def internal_progress_view(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    bt=Progress.objects.filter(GRP=id)
    print(bt)
    return render(request,"INTERNAL GUIDE/VIEW PROGRESS INTERNAL.html",{'data':bt})


# def internal_progress_view(request):
#     if request.session['lg'] != 'lin':
#         return redirect('/')
#     bt=Batch.objects.all()
#     print(bt)
#     return render(request,"INTERNAL GUIDE/VIEW PROGRESS INTERNAL.html",{'bt':bt})

def  internal_group_view(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    grp=Group.objects.filter(GRP_BATCHID=id)
    return render(request,"INTERNAL GUIDE/INTERNAL GROUP PROGRESS.html",{'grp':grp})

def internal_view_progress_post(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Group=request.POST['select2']
    print("Grrrrrrrr",Group)
    at=Progress.objects.filter(GRP=Group)
    print(at,"mmmmmmmmmmmmmmmmmmm")

    qry=Batch.objects.all()
    return render(request,"INTERNAL GUIDE/VIEW PROGRESS INTERNAL.html",{'data':at ,'bt':qry})


def internal_view_project_schedule(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    project= Project_schedule.objects.all()
    return render(request, "INTERNAL GUIDE/VIEW PROJ SUB SCHEDULE.html ", {'data': project})

def internal_progress_remark_get(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')

    return render(request, "INTERNAL GUIDE/REMARK INTERNAL.html",{'id':id})


def internal_progress_remark_post(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Remark= request.POST['textarea']

    Progress.objects.filter(id=id).update(remark=Remark)
    return HttpResponse("<script>alert('added successfully');window.location='/internal_progress_view'</script>")

def internal_view_circular(request, id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    res = Circular.objects.filter(GROUP=id)
    return render(request, 'INTERNAL GUIDE/View Circular.html ', {'data': res, "id": id})

# -----------chat with external

def chatt_internal(request,u):
    if request.session['lg']!='lin':
        return redirect('/')
    request.session['head']="CHAT"
    request.session['uid'] = u
    return render(request,'INTERNAL GUIDE/chat_with_external.html',{'u':u})


def chatsnd_internal(request,u):
    # if request.session['lg'] != 'lin':
    #     return redirect('/')
        d=datetime.datetime.now().strftime("%Y-%m-%d")
        # t=datetime.datetime.now().strftime("%H:%M:%S")
        c = request.session['lid']
        b=request.POST['n']
        print(b)
        print(u,"userrrrrrrrrr")
        m=request.POST['m']
        cc=Internal_Guide.objects.get(IG_id=c)
        uu = External_Guide.objects.get(id=request.session['uid'])
        obj=Chat()
        obj.date=d
        obj.send_type='internal'
        obj.INTERNAL=cc
        obj.EXTERNAL=uu
        obj.message=m
        obj.save()
        print(obj)
        v = {}
        if int(obj) > 0:
            v["status"] = "ok"
        else:
            v["status"] = "error"
        r = JsonResponse.encode(v)
        return r
    # else:
    #     return redirect('/')

def chatrply_internal(request):
    # if request.session['lg'] != 'lin':
    #     return redirect('/')
    # if request.session['log']=="lo":
        c = request.session['lid']
        cc=Internal_Guide.objects.get(IG_id=c)
        uu=External_Guide.objects.get(id=request.session['uid'])
        res = Chat.objects.filter(INTERNAL=cc,EXTERNAL=uu)
        print(res)
        v = []
        if len(res) > 0:
            print(len(res))
            for i in res:
                v.append({
                    'type': i.send_type,
                    'chat': i.message,
                    'name': i.EXTERNAL.eg_name,
                    # 'upic':"kk",
                    'dtime': i.date,
                    'tname': i.INTERNAL.ig_name,
                })
            # print(v)
            return JsonResponse({"status": "ok", "data": v, "id": cc.id})
        else:
            return JsonResponse({"status": "error"})

def internal_view_scores(request, id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    res = Scores.objects.filter(GRP=id)
    return render(request, 'INTERNAL GUIDE/VIEW SCORES INTERNAL.html', {'data': res, "id": id})



############################################### EXTERNAL GUIDE #################################################################


def external_home(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    qry = Project_schedule.objects.all()
    if qry.exists():
        note = qry[0].note
        return render(request, "EXTERNAL GUIDE/EXTERNAL ORGANISATION HOME.html", {"status": note})

    else:
        note = "currently No notifications!!...."
    return render(request,"EXTERNAL GUIDE/EXTERNAL ORGANISATION HOME.html")

def external_view_groups(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    grp=Group.objects.filter(GRP_EG=External_Guide.objects.get(EG=request.session['lid']).id)
    datalist=[]
    print(grp)
    for k in grp:
        qry2=Attendance.objects.filter(date_upload=datetime.datetime.now().strftime("%Y-%m-%d"),GRP_ID=k.id)
        print(qry2)
        if qry2.exists():
            datalist.append(
                {
                    "id":k.id,
                    "batch":k.GRP_BATCHID.batch,
                    "grp_number":k.grp_number,
                    "ig_name":k.GRP_IG.ig_name,
                    "grp_email":k.grp_email,
                    "grp_topic_name":k.grp_topic_name,
                    "status":"y",
                    "GRP_IG_id":k.GRP_IG_id
                }
            )
        else:
            datalist.append(
                {
                    "id":k.id,
                    "batch": k.GRP_BATCHID.batch,
                    "grp_number": k.grp_number,
                    "ig_name": k.GRP_IG.ig_name,
                    "grp_email": k.grp_email,
                    "grp_topic_name": k.grp_topic_name,
                    "status": "n",
                    "GRP_IG_id": k.GRP_IG_id
                }
            )
    return render(request,"EXTERNAL GUIDE/VIEW GROUP EXTERNAL.html",{'grp':datalist})


def external_group(request,eid):
    if request.session['lg'] != 'lin':
        return redirect('/')
    grp=Group.objects.filter(GRP_BATCHID=eid)
    return render(request,"EXTERNAL GUIDE/VIEW ATTENDANCE EXTERNAL.html",{'grp':grp})
def external_view_attendance(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    grp=Group.objects.filter(GRP_EG=External_Guide.objects.get(EG=request.session['lid']))
    return render(request,"EXTERNAL GUIDE/VIEW ATTENDANCE EXTERNAL.html",{'grp':grp})

# def external_attendance details

def external_view(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Groups = request.POST['select2']
    print(Group)
    # external_lid = External_Guide.objects.get(EG=request.session['lid'])
    # grp = Group.objects.filter(GRP_EG_id=external_lid)
    # print("hhhhhhh",grp)
    at = Attendance.objects.filter(GRP_ID=Groups)
    grp=Group.objects.filter(GRP_EG=External_Guide.objects.get(EG=request.session['lid']))


    return render(request, "EXTERNAL GUIDE/VIEW ATTENDANCE EXTERNAL.html", {'data': at,"grp":grp})


def external_add_attendance_get(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    qry=Group_member.objects.filter(GRP_ID=id)
    return render(request, "EXTERNAL GUIDE/Student Attendance upload.html", {'id': id,"data":qry})

def external_add_attendance_post(request, gpid):
    if request.session['lg'] != 'lin':
        return redirect('/')
    qry=Group_member.objects.filter(GRP_ID=gpid)
    stud_list=[]
    checked_list=[]

    for k in qry:
        stud_list.append(k.LEADER_STUD_ID_id)
    stud=request.POST.getlist('checkbox')
    for i in stud:
        checked_list.append(i)
    print(checked_list)
    for s in stud_list:
        print(s)
        if str(s) in checked_list:
            obj=Attendance()
            obj.date_upload=datetime.datetime.now().strftime("%Y-%m-%d")
            obj.file="present"
            obj.GRP_ID_id=gpid
            obj.STD_ID_id=str(s)
            obj.save()
        else:
            obj = Attendance()
            obj.date_upload = datetime.datetime.now().strftime("%Y-%m-%d")
            obj.file = "Absent"
            obj.STD_ID_id = str(s)
            obj.GRP_ID_id=gpid
            obj.save()

    # File= request.FILES['fileField']
    # date=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    # date1=datetime.datetime.now().strftime("%Y-%M-%d")
    # fs=FileSystemStorage()
    # fs.save(r"C:\Users\rojal\PycharmProjects\completemyproject\completemp\static\Attendance_files\\"+date+'.xlsx',File)
    # path="/static/Attendance_files/"+date+'.pdf'
    #
    # obj = Attendance()
    # obj.file =str(path)
    # obj.date_upload=date1
    # obj.GRP_id=gpid
    # obj.save()
    # return HttpResponse("<script>alert('added successfully');window.location='/external_view_groups#cmp'</script>")
    return redirect('/external_view_groups#cmp')

def external_add_progress_get(request,id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    return render(request,"EXTERNAL GUIDE/ADD PROGRESS.html", {'id': id})

def external_add_progress_post(request,gpid):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Prog = request.POST['select']
    Remark=request.POST['textfield']
    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    date1 = datetime.datetime.now().strftime("%Y-%m-%d")
    # fs = FileSystemStorage()
    # fs.save(r"C:\Users\rojal\PycharmProjects\completemyproject\completemp\static\progress_files\\" + date + '.pdf',
    #         File)
    # path = "/static/progress_files/" + date + '.pdf'

    obj=Progress()
    obj.progress_file=Prog
    # obj.progress_file=path
    obj.date_upload=date1
    obj.remark=Remark
    obj.GRP=Group.objects.get(id=gpid)

    obj.save()
    # return HttpResponse("<script>alert('added successfully');window.location='/external_view_groups'</script>")
    return redirect('/external_view_groups#cmp')


def external_progress_grp(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    grp=Group.objects.all()
    return render(request,"EXTERNAL GUIDE/VIEW PROGRESS External.html",{'grp':grp})

def external_view_progress_get(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    grp=Group.objects.filter(GRP_EG=External_Guide.objects.get(EG=request.session['lid']))
    return render(request,"EXTERNAL GUIDE/VIEW PROGRESS External.html",{'grp':grp})

def external_view_progress_post(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    Group1 = request.POST['select']
    # print(Group)
    # external_lid = External_Guide.objects.get(EG=request.session['lid'])
    # grp = Group.objects.filter(GRP_EG_id=external_lid)
    # print("hhhhhhh",grp)
    at = Progress.objects.filter(GRP=Group1)

    grp = Group.objects.all()

    return render(request, "EXTERNAL GUIDE/VIEW PROGRESS External.html", {'data': at,'grp':grp})



def external_view_schedule(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    grp=Group.objects.filter(GRP_EG=External_Guide.objects.get(EG=request.session['lid']))
    data=[]
    bid=[]
    for i in grp:
        if i.GRP_BATCHID_id not in bid:
            data.append({'id' : i.GRP_BATCHID_id, 'batch_name':i.GRP_BATCHID.batch})
            bid.append(i.GRP_BATCHID_id)
    return render(request, "EXTERNAL GUIDE/View_schedule.html", {'data':data})
def external_view_schedule_post(request):
    if request.session['lg'] != 'lin':
        return redirect('/')
    bid=request.POST['select']
    res=Project_schedule.objects.filter(BATCH_id=bid)
    grp = Group.objects.filter(GRP_EG=External_Guide.objects.get(EG=request.session['lid']))
    data = []
    bid = []
    for i in grp:
        if i.GRP_BATCHID_id not in bid:
            data.append({'id': i.GRP_BATCHID_id, 'batch_name': i.GRP_BATCHID.batch})
            bid.append(i.GRP_BATCHID_id)
    print(res)
    return render(request, "EXTERNAL GUIDE/View_schedule.html", {'data': data, 'data2':res})

def external_view_circular(request, id):
    if request.session['lg'] != 'lin':
        return redirect('/')
    res = Circular.objects.filter(GROUP=id)
    return render(request, 'EXTERNAL GUIDE/View circular.html ', {'data': res, "id": id})


# =========chat with internal guide


def chatt(request,u):
    if request.session['lg'] != 'lin':
        return redirect('/')
    request.session['head']="CHAT"
    request.session['uid'] = u
    return render(request,'EXTERNAL GUIDE/chat_with_internal.html',{'u':u})


def chatsnd(request,u):
    # if request.session['lg'] != 'lin':
    #     return redirect('/')
        d=datetime.datetime.now().strftime("%Y-%m-%d")
        # t=datetime.datetime.now().strftime("%H:%M:%S")
        c = request.session['lid']
        b=request.POST['n']
        print(b)
        print(u,"userrrrrrrrrr")
        m=request.POST['m']
        cc=External_Guide.objects.get(EG_id=c)
        uu = Internal_Guide.objects.get(id=request.session['uid'])
        obj=Chat()
        obj.date=d
        obj.send_type='external'
        obj.EXTERNAL=cc
        obj.INTERNAL=uu
        obj.message=m
        obj.save()
        print(obj)
        v = {}
        if int(obj) > 0:
            v["status"] = "ok"
        else:
            v["status"] = "error"
        r = JsonResponse.encode(v)
        return r
    # else:
    #     return redirect('/')

def chatrply(request):

    # if request.session['log']=="lo":
        c = request.session['lid']
        cc=External_Guide.objects.get(EG_id=c)
        uu=Internal_Guide.objects.get(id=request.session['uid'])
        res = Chat.objects.filter(EXTERNAL=cc,INTERNAL=uu)
        print(res)
        v = []
        if len(res) > 0:
            print(len(res))
            for i in res:
                v.append({
                    'type':i.send_type,
                    'chat':i.message,
                    'name':i.INTERNAL.ig_name,
                    # 'upic':"kk",
                    'dtime':i.date,
                    'tname':i.EXTERNAL.eg_name,
                })
            # print(v)
            return JsonResponse({"status": "ok", "data": v, "id": cc.id})
        else:
            return JsonResponse({"status": "error"})





################################################################3




def ajax_email_already(request):
    t = request.POST['type']
    if Login.objects.filter(username=t).exists():
        return JsonResponse({"status":"1"})
    else:
        return JsonResponse({"status":"ok"})

def ajax_email_already_student(request):
    t = request.POST['type']
    if Student.objects.filter(std_email=t).exists():
        return JsonResponse({"status":"1"})
    else:
        return JsonResponse({"status":"ok"})


def logout(request):
    request.session.clear()
    request.session['lg']=""
    return redirect('/')

# =================================================================================================

def android_login(request):
    u=request.POST['username']
    p=request.POST['password']
    res = Login.objects.filter(username=u, password=p)
    if res.exists():
       lid=res[0].id
       type=res[0].usertype
       return JsonResponse({'status':"ok",'type':type,'lid':lid})
    else:
        return JsonResponse({'status': "no"})



def android_project_schedule(request):
    lid=request.POST['lid']
    reg=Group.objects.get(LOGIN=lid)
    res=Project_schedule.objects.filter(BATCH=reg.GRP_BATCHID)

    ar=[]
    for i in res:
        ar.append({
            'date':i.date,
            'time':i.time,
            'note':i.note

        })
    print(ar)
    return JsonResponse({'status':"ok",'data':ar})

def android_work_progress(request):
    lid = request.POST['lid']
    res = Progress.objects.filter(GRP__LOGIN=lid)
    ar = []
    for i in res:
        ar.append({
            'date_upload': i.date_upload,
            'remark': i.remark,
            'progress':i.progress_file

        })
    return JsonResponse({'status': "ok", 'users': ar})

def android_internal_guide(request):
    lid = request.POST['lid']
    res = Group.objects.get(LOGIN=lid)
    return JsonResponse({'status': "ok", 'ig_name': res.GRP_IG.ig_name,'ig_phone':res.GRP_IG.ig_phone,'ig_email':res.GRP_IG.ig_email,
                         'eg_name':res.GRP_EG.eg_name,'eg_posts':res.GRP_EG.eg_posts,'eg_company_name':res.GRP_EG.eg_company_name,
                         'eg_email':res.GRP_EG.eg_email,'eg_phone':res.GRP_EG.eg_phone})

def android_project_list_public(request):
    lid = request.POST['lid']
    res = Group.objects.all()

    ar = []
    for i in res:
        ar.append({
            'group': i.grp_number,
            'topic': i.grp_topic_name,


        })
    print(ar)
    return JsonResponse({'status': "ok", 'users': ar})

def android_circular(request):
    lid = request.POST['lid']
    res = Circular.objects.filter(GROUP__LOGIN=lid)
    ar = []
    for i in res:
        ar.append({
            'Date': i.Date,
            'Time': i.Time,
            'note':i.note

        })
    return JsonResponse({'status': "ok", 'users': ar})

def android_public_list_schedule(request):
    lid = request.POST['lid']
    res = Project_schedule.objects.all()

    ar = []
    for i in res:
        ar.append({
            'batch': i.BATCH.batch,
            'schedule': i.note,


        })
    print(ar)
    return JsonResponse({'status': "ok", 'users': ar})

def android_scores(request):
    lid = request.POST['lid']
    res = Scores.objects.get(GRP__LOGIN=lid)
    return JsonResponse({'status': "ok", 'Punctuality': res.Punctuality,'Relevance':res.Relevance,'Presentation_1':res.Presentation_1,
                         'Presentation_2':res.Presentation_2,'Presentation_3':res.Presentation_3,'Demo_report':res.Demo_report,
                         'Institution_copy':res.Institution_copy,'Viva':res.Viva,'Total':res.Total})







