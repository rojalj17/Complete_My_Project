"""completemyproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from completemp import views

urlpatterns = [
     path('admin/', admin.site.urls),
     path('', views.login_get),
     path('login_post', views.login_post),
     path('admin_home',views.admin_home),
     path('ajax_email_already',views.ajax_email_already),
     path('admin_add_external_guide_get',views.admin_add_external_guide_get),
     path('admin_view_external_guide',views.admin_view_external_guide),
     path('admin_add_external_guide_post',views.admin_add_external_guide_post),
     path('admin_update_external_guide_get/<id>',views.admin_update_external_guide_get),
     path('admin_update_external_guide_post/<id>',views.admin_update_external_guide_post),
     path('admin_external_guide_delete/<id>',views.admin_external_guide_delete),
     path('admin_project_circular_get/<id>', views.admin_project_circular_get),
     path('admin_project_circular_post/<id>', views.admin_project_circular_post),
     path('admin_view_circular/<id>', views.admin_view_circular),




     path('admin_batch_add_get',views.admin_batch_add_get),
     path('admin_batch_add_post',views.admin_batch_add_post),
     path('batch_view', views.batch_view),
     path('batch_add_student_get/<id>', views.batch_add_student_get),
     path('batch_add_student_post/<id>', views.batch_add_student_post),
     path('batch_view_student/<id>', views.batch_view_student),
     path('admin_update_batch_student_get/<id>', views.admin_update_batch_student_get),
     path('admin_update_batch_student_post/<id>', views.admin_update_batch_student_post),
     path('admin_batch_student_delete/<id>', views.admin_batch_student_delete),






     path('admin_batch_delete/<id>', views.admin_batch_delete),
     path('admin_batch_delete/<id>', views.admin_batch_delete),
     path('admin_delete_circular/<id>/<cid>', views.admin_delete_circular),




     path('ajax_grp_batch',views.ajax_grp_batch),
     # path('ajax_grp_batch/<eid>',views.ajax_grp_batch),
     path('admin_group_management_add_get',views.admin_group_management_add_get),
     path('admin_group_management_add_post',views.admin_group_management_add_post),
     path('group_management_view', views.group_management_view),
     path('group_management_view', views.group_management_view),
     path('ajax_email_already_student', views.ajax_email_already_student),
     path('admin_update_group_management_get/<id>', views.admin_update_group_management_get),
     path('admin_update_group_management_post/<id>', views.admin_update_group_management_post),
     path('admin_group_management_delete/<id>', views.admin_group_management_delete),
     path('group_management_add_student_get/<id>',views.group_management_add_student_get),
     path('group_management_add_student_post/<id>',views.group_management_add_student_post),
     path('group_management_view_student/<id>',views.group_management_view_student),
     # path('admin_update_student_management_get/<id>',views.admin_update_student_management_get),
     # path('admin_update_student_management_post/<id>',views.admin_update_student_management_post),
     # path('admin_student_management_delete/<id>',views.admin_student_management_delete),


     path('admin_add_internal_guide_get', views.admin_add_internal_guide_get),
     path('admin_add_internal_guide_post', views.admin_add_internal_guide_post),
     path('admin_view_internal_guide', views.admin_view_internal_guide),
     path('admin_update_internal_guide_get/<id>', views.admin_update_internal_guide_get),
     path('admin_update_internal_guide_post/<id>', views.admin_update_internal_guide_post),
     path('admin_Internal_guide_delete/<id>', views.admin_Internal_guide_delete),

     path('admin_add_project_management_get', views.admin_add_project_management_get),
     path('admin_add_project_management_post', views.admin_add_project_management_post),
     path('admin_view_project_management', views.admin_view_project_management),

     path('admin_update_project_management_get/<id>', views.admin_update_project_management_get),
     path('admin_update_project_management_post/<id>', views.admin_update_project_management_post),
     path('admin_delete_project_management_post/<id>', views.admin_delete_project_management_post),


     path('admin_search_attendance_get', views.admin_search_attendance_get),
     path('ajax_grp_by_batch', views.ajax_grp_by_batch),
     path('ajax_att_by_group', views.ajax_att_by_group),
     path('admin_search_attendance_post', views.admin_search_attendance_post),
     path('admin_view_attendance', views.admin_view_attendance),
     # path('batch', views.batch),
     path('group/<id>', views.group),
     path('ajax_progress_by_group', views.ajax_progress_by_group),



     path('admin_progress_get', views.admin_progress_get),
     path('admin_progress_post', views.admin_progress_post),
     path('group_progress/<id>', views.group_progress),

     path('admin_add_scores_get/<id>', views.admin_add_scores_get),
     path('admin_add_scores_get_post/<id>', views.admin_add_scores_get_post),
     path('admin_view_scores/<id>', views.admin_view_scores),
     path('admin_update_scores_get/<id>', views.admin_update_scores_get),
     path('admin_update_scores_post/<id>', views.admin_update_scores_post),







     ########################INTERNAL GUIDE####################

     path('internal_home',views.internal_home),
     path('internal_view_groups', views.internal_view_groups),
     path('internal_view_external_organisation', views.internal_view_external_organisation),

     path('internal_view_attendance/<id>', views.internal_view_attendance),
     path('internal_group_management_view_student/<id>', views.internal_group_management_view_student),

     path('internal_group/<eid>', views.internal_group),
     path('internal_view', views.internal_view),
     # path('internal_progress_view', views.internal_progress_view),
     path('internal_progress_view/<id>', views.internal_progress_view),
     path('internal_group_view/<id>',views.internal_group_view),
     path('internal_view_progress_post',views.internal_view_progress_post),

     path('internal_view_project_schedule',views.internal_view_project_schedule),

     path('internal_progress_remark_get/<id>',views.internal_progress_remark_get),
     path('internal_progress_remark_post/<id>',views.internal_progress_remark_post),


     path('internal_progress_view/<id>',views.internal_progress_view),
     path('internal_view_scores/<id>',views.internal_view_scores),
     path('internal_view_circular/<id>',views.internal_view_circular),


     # --------chat
     path('chatt_internal/<u>', views.chatt_internal),
     path('chatsnd_internal/<u>', views.chatsnd_internal),
     path('chatrply_internal', views.chatrply_internal),






     ################################# EXTERNAL GUIDE #########################

     path('external_home', views.external_home),
     path('external_view_groups',views.external_view_groups),
     path('external_view_attendance',views.external_view_attendance),
     path('external_group',views.external_group),
     path('external_view',views.external_view),
     path('external_add_attendance_get/<id>',views.external_add_attendance_get),
     path('external_add_attendance_post/<gpid>',views.external_add_attendance_post),
     path('external_add_progress_get/<id>',views.external_add_progress_get),
     path('external_add_progress_post/<gpid>',views.external_add_progress_post),

     path('external_progress_grp',views.external_progress_grp),
     path('external_view_progress_get',views.external_view_progress_get),
     path('external_view_progress_post',views.external_view_progress_post),
     path('external_view_schedule',views.external_view_schedule),
     path('external_view_schedule_post',views.external_view_schedule_post),

     path('external_view_circular/<id>',views.external_view_circular),



     # -----------chat-------

      path('chatt/<u>',views.chatt),
      path('chatsnd/<u>',views.chatsnd),
      path('chatrply',views.chatrply),
     ##############################GROUP########################################
     path('logout', views.logout),

     ###########android##############################################
     path('android_login', views.android_login),
     path('android_project_schedule', views.android_project_schedule),
     path('android_work_progress', views.android_work_progress),
     path('android_internal_guide', views.android_internal_guide),
     path('android_project_list_public', views.android_project_list_public),
     path('android_circular', views.android_circular),
     path('android_public_list_schedule', views.android_public_list_schedule),
     path('android_scores', views.android_scores),

]
