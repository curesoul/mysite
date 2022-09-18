from django.shortcuts import render, get_object_or_404

from .models import Customer, Operator, Item, Lot, ProductionPlan, Detail, DetailChangeLog


def index(request):
    pps = ProductionPlan.objects.all()
    context = {
        'pps': pps,
    }
    return render(request, 'mixs/index.html', context)


def detail(request, pp_id):
    detailpp = get_object_or_404(ProductionPlan, pk=pp_id)
    return render(request, 'mixs/detail.html', {'detail': detailpp, })


def results_sheet(request, pp_id):
    detailpp = get_object_or_404(ProductionPlan, pk=pp_id)
    batch_start = int(request.POST.get('batch-start'))
    batch_end = int(request.POST.get('batch-end'))
    print(batch_start)
    print(batch_end)
    # batch_control = '"' + batch_start + ':' + batch_end + '"'
    detail_set = detail.detailpp_set.all()[batch_start:batch_end]
    return render(request, 'mixs/results_sheet.html', {'detail': detailpp, 'detail_set': detail_set, })
