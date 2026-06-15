from django.conf import settings
from django.core.mail import EmailMessage
from orders.models import Order
from celery import shared_task

@shared_task
def order_created_send_mail(order_id):
    order = Order.objects.get(id=order_id)
    email = EmailMessage(
        subject=f"Ваш заказ №{order.id} от {order.created_at.strftime('%d.%m.%Y %H:%M')}",
        body=f"Спасибо за покупку!\n\nВаш номер заказа: {order.id}\n\n В ближайшее время с вами свяжется оператор!",
        from_email=settings.EMAIL_HOST_USER,
        to=[order.mail]
    )
    email.send()
