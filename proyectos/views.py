from django.http import HttpRequest
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from proyectos.forms import ParticipanteForm
from proyectos.models import Participante
from proyectos.models import Proyecto


# Create your views here.
def index(request):
	projects_list = Proyecto.objects.all()
	projects_summary = {}
	for project in projects_list:
		members = Participante.objects.filter(proyecto__pk=project.id)
		quantity = members.count()
		projects_summary[project.id] = {
			'name': project.name,
			'status': project.get_status_display(),
			'quantity': quantity,
			'members': members}
	context = {'projects_list': projects_list, 'projects_summary': projects_summary}
	return render(request, 'proyectos/index.html', context)

def project(request, id_proyecto):
	project = get_object_or_404(Proyecto, pk=id_proyecto)
	participants = Participante.objects.filter(proyecto__pk=project.id)
	current_url = request.build_absolute_uri()
	context = {'project':project, 'current_url':current_url, 'participants':participants}
	return render(request, 'proyectos/project.html', context, context_instance=RequestContext(request))

def register(request, id_proyecto):
	project = get_object_or_404(Proyecto, pk=id_proyecto)
	participants_per_project = Participante.objects.filter(proyecto__pk=project.id).count()
	if participants_per_project >= 5:
		project.status = 'C'
		project.save()
		message = "El proyecto ya tiene los participantes requeridos, elige otro."
		context = {'message':message}
	elif project.status == 'C':
		message = "El proyecto se encuentra CERRADO."
		context = {'message':message}
	else:
		if request.method == 'POST':
			participant_form = ParticipanteForm(request.POST)
			if participant_form.is_valid():
				email_to_register = participant_form.cleaned_data['email']	
				participant = Participante.objects.filter(email=email_to_register)
				if len(participant) == 1:
					if (participant[0].proyecto != None):
						message = "Tu e-mail ya se encuentra registrado en un proyecto."
						context = {'message': message, 'participant_registered':participant[0]}
					else:
						participant[0].proyecto = project
						participant[0].save()
						context = {'participant':participant[0]}
				else:
					message = "El e-mail no se encuentra registrado."
					context = {'message':message}
			else:
				context = {'participant_form':participant_form}
		else:
			participant_form = ParticipanteForm()
			context = {'participant_form':participant_form}
	return render(request, 'proyectos/participant.html', context)