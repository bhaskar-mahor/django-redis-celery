from celery import shared_task

@shared_task
def celery_task(data):
    try:
        print("data ",data)
        # Perform any operation inside this celery task function
        pass
    except Exception as e:
        print("exception add numbers ",e)