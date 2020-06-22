from django.shortcuts import render
from testapp.models import GroupModel,TaskAssignModel
from django.contrib.auth.models import User
# Create your views here.


def groupview(request):

	
	if request.method == 'POST':
		flag = False
		addGrp = GroupModel()
		allGroupData = GroupModel.objects.all()
		for data in allGroupData:
			if data.created_by == str(request.user) and data.group == request.POST.get('group'):
				flag = True

		if flag == False:
			addGrp.member = request.user
			addGrp.created_by = str(request.user) 
			addGrp.group = request.POST.get('group')
			addGrp.save()

		

	grpdata_member=GroupModel.objects.filter(member=request.user)

	return render(request,'testapp/creategroup.html',{'grpdata_member':grpdata_member})


def addMemberview(request,created_by=None,group=None,member=None):
	flag = False
	noneflag = False
	if member != None:
		allGroupData = GroupModel.objects.all()
		for grpData in allGroupData:
			if grpData.created_by == created_by and grpData.group == group and str(grpData.member) == member:
				flag = True
			
		
		if flag == False:
				userData = User.objects.all()		
				addMember = GroupModel()
				addMember.created_by = created_by
				addMember.group = group
				for x in userData:
					if str(x.username) == member:
						addMember.member = x
						addMember.save()
						break
	grp_member = GroupModel.objects.filter(created_by=created_by,group=group)
	

	return render(request, 'testapp/addmember.html',{'created_by':created_by,'group':group,'data':grp_member})



def assigntaskview(request,id):

	

	if request.method == 'POST':
		memberObject= GroupModel.objects.get(id=id)

		task_assign = TaskAssignModel()
		task_assign.assigned_to = memberObject
		task_assign.task = request.POST.get('task')
		task_assign.assigned_by = str(request.user)
		task_assign.save()


	member_task = TaskAssignModel.objects.filter(assigned_to=id)

	return render(request,'testapp/assigntask.html',{'member_task':member_task})





