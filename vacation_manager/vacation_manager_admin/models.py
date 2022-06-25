from django.db import models


class Vacation(models.Model):
    status_choices = (
        ("N", "New"),
        ("P", "Past"),
        ("O", "Opened for registration"),
        ("C", "Closed for registration"),
        ("X", "Canceled"),
    )
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=1, default="N", choices=status_choices)
    # start_date =
    # end_date =
    description = models.TextField(null=True, blank=True)
    identification_number = models.CharField(max_length=100)


class Contact(models.Model):
    primary_vacation = models.ForeignKey(Vacation, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)



