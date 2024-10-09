from typing import Any
from django.views.generic import FormView # Do pacóte django.views.generic, estamos importando TemplateView

from django.urls import reverse_lazy
from django.contrib import messages

#Para usar o TemplateView é só imformar o nome do template


from .models import Servico, Funcionario, Recursos
from .forms import ContatoForm




class IndexView(FormView):
    template_name =  'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context =  super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()

        context['funcionarios'] = Funcionario.objects.order_by('?').all()

        context['recursos'] = Recursos.objects.order_by('?').all()

        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()

        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)



