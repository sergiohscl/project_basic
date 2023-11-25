from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core import mail

User = get_user_model()


class CustomUserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )

    def test_custom_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertTrue(self.user.check_password("testpassword"))
        self.assertEqual(self.user.email, "testuser@example.com")
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_custom_user_signal_email(self):
        # Verifique se um email foi enviado
        self.assertEqual(len(mail.outbox), 1)

        email = mail.outbox[0]
        # Verifique o assunto do email
        self.assertEqual(email.subject, "Cadastro Confirmado")
        # Verifique o destinatário do email
        self.assertEqual(email.to, [self.user.email])
