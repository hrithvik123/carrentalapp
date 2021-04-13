from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import User, Customer, Booking, Rental_Package, Manager
from django.utils import timezone
from datetime import datetime


# if User is created, automatically create a customer instance
@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        cust = instance
        cust.__class__ = Customer
        cust.drivers_license = 0
        cust.save(force_insert=True)


def create_salesassociate(sender, instance, created, **kwargs):
    if instance.is_staff:
        mang = instance
        mang.__class__ = Manager
        mang.manager_ssn = 0
        mang.save(force_insert=True)

# if Booking is created or changed, update price if applicable
# use temp_amount to avoid an infinite loop


@receiver(post_save, sender=Booking)
def apply_booking(sender, instance, created, **kwargs):
    if created:
        instance.vehicle.availability = False
        instance.vehicle.save()
        duration_seconds = instance.end_time - instance.start_time
        duration = duration_seconds.total_seconds()
        duration = duration/(60*60*24)

        if duration < 15:
            temp_amount = instance.vehicle.package.per_day_rent*duration
            if instance.amount != temp_amount:
                instance.amount = temp_amount
                instance.save()
            return
        if duration >= 15 and duration < 30:
            temp_amount = instance.vehicle.package.touring_package * \
                (duration/15)
            if instance.amount != temp_amount:
                instance.amount = temp_amount
                instance.save()
            return
        if duration >= 30:
            temp_amount = instance.vehicle.package.per_month_rent*(duration/30)
            if instance.amount != temp_amount:
                instance.amount = temp_amount
                instance.save()
            return

    elif not created:
        # start = datetime.combine(datetime.now(), instance.start_time)
        # end = datetime.combine(datetime.now(), instance.end_time)
        duration_seconds = instance.end_time - instance.start_time
        duration = duration_seconds.total_seconds()
        duration = duration/(60*60*24)

        if duration < 15:
            temp_amount = instance.vehicle.package.per_day_rent*duration
            if instance.amount != temp_amount:
                instance.amount = temp_amount
                instance.save()
            return
        if duration >= 15 and duration < 30:
            temp_amount = instance.vehicle.package.touring_package * \
                (duration/15)
            if instance.amount != temp_amount:
                instance.amount = temp_amount
                instance.save()
            return
        if duration >= 30:
            temp_amount = instance.vehicle.package.per_month_rent*(duration/30)
            if instance.amount != temp_amount:
                instance.amount = temp_amount
                instance.save()
            return


@receiver(post_delete, sender=Booking)
def apply_booking(sender, instance, **kwargs):
    instance.vehicle.availability = True
    instance.vehicle.save()

    # implement automatic updation of booking prices if rental package prices change
    # incomplete
    # @receiver(post_save, sender=Rental_Package)
    # def update_amount(sender, instance, created, **kwargs):
    #     for book in Booking.objects.filter(vehicle.package == instance):
    #         duration_seconds = book.end_time - book.start_time
    #         duration = duration_seconds.total_seconds()
    #         duration = duration/(60*60*24)

    #         if duration < 15:
    #             temp_amount = instance.package.per_day_rent*duration
    #             if book.amount != temp_amount:
    #                 book.amount = temp_amount
    #                 book.save()
    #             return
    #         if duration >= 15 and duration < 30:
    #             temp_amount = instance.package.touring_package * \
    #                 (duration/15)
    #             if book.amount != temp_amount:
    #                 book.amount = temp_amount
    #                 book.save()
    #             return
    #         if duration >= 30:
    #             temp_amount = instance.package.per_month_rent*(duration/30)
    #             if book.amount != temp_amount:
    #                 book.amount = temp_amount
    #                 book.save()
    #             return
