from django.db.models import Q
from goods.models import ProWomen,ProBaby

def q_search(query):
    keywords = [word for word in query.split() if len(word)>2]
    q_objects=Q()
    for token in keywords:
        q_objects |= Q(name__icontains=token)
        q_objects |=Q(description__icontains=token)

    return ProWomen.objects.filter(q_objects)

def q_search1(query):
    keywords = [word for word in query.split() if len(word)>2]
    q_objects=Q()
    for token in keywords:
        q_objects |=Q(description__icontains=token)
        q_objects |=Q(name__icontains=token)
    return ProBaby.objects.filter(q_objects)