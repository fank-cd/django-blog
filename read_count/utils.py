from django.contrib.contenttypes.models import ContentType
from .models import ReadNum


def read_count_once_read(request, obj,):
    ct = ContentType.objects.get_for_model(obj)
    key = "%s_%s_read" % (ct.model, obj.pk)
    if not request.COOKIES.get(key):
        """
        if ReadNum.objects.filter(content_type=ct,object_id=blog.pk).count():
            readnum = ReadNum.objects.get(content_type=ct,object_id=blog.pk)
        else:
            readnum = ReadNum(content_type=ct,object_id=blog.pk)
        """
        readnum = ReadNum.objects.get_or_create(
            content_type=ct, object_id=obj.pk)[0]
        readnum.read_num += 1
        readnum.save()
    return key
