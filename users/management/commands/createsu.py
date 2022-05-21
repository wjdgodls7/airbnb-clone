from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):

    help = "This command creates superuser"

    def handle(self, *args, **options):
        admin = User.objects.get_or_none(username="admin")
        if not admin:
            User.objects.create_superuser("admin", "jhi5576@naver.com", "12")
            self.stdout.write(self.style.SUCCESS(f"Superuser Created"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Superuser Exists"))