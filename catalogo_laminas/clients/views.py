# imports de django
from django.http import HttpResponse
from django.template import loader

# imports de terceros

# imports locales
from clients import models as clients_models
from clients import forms as clients_forms


def company_detail(request, company_id, employee_id):
    """
    muestra nombre y teléfonos de contacto de la compañia via un id

    """
    template = loader.get_template('company/detail.html')
    # traer la compañia
    try:
        company = clients_models.Company.objects.get(pk=company_id)
        siguiente = clients_models.Company.objects.last()
    except clients_models.Company.DoesNotExist:
        error = f'Compañia {company_id} no existe.'

    context = {
        'company_name': company.name,
        'contact_number': company.contact_phone,
    }

    return HttpResponse(template.render(context, request))


def company_list(request):
    """
    regresar la lista de compañias

    """
    template = loader.get_template('company/list.html')
    companies = clients_models.Company.objects.all()

    if request.method == 'POST':
        form_subscripcion = clients_forms.CompanyForm(request.POST)
        if form_subscripcion.is_valid():
            clients_models.Company.objects.create(
                name=request.POST.get('nombre', ''),
                contact_phone=request.POST.get('contacto', ''),
                support_phone=request.POST.get('soporte', ''),
                sales_phone=request.POST.get('ventas', ''),
            )
    else:
        form_subscripcion = clients_forms.CompanyForm()

    context = {
        'companies': companies,
        'form': form_subscripcion,
    }

    return HttpResponse(template.render(context, request))
