from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=User)
def enviar_email_boas_vindas(sender, instance, created, **kwargs):
    if created:
        # Esta função será chamada sempre que um novo objeto User for criado.

        # Personalize o conteúdo do email de acordo com suas necessidades.
        assunto = 'Cadastro Confirmado'
        conteudo_html = render_to_string(
            'emails/email_boas_vindas.html', {'user': instance}
        )
        conteudo_texto = strip_tags(conteudo_html)

        # Endereços de email do remetente e destinatário
        email_remetente = settings.EMAIL_HOST_USER
        email_destinatario = instance.email

        # Crie o objeto EmailMultiAlternatives e envie o email
        email = EmailMultiAlternatives(
            assunto, conteudo_texto, email_remetente, [email_destinatario]
        )
        email.attach_alternative(conteudo_html, 'text/html')
        email.send()
