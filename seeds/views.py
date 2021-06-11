from django.shortcuts import render, redirect
from .models import Seeds
from .forms import SeedForm
from django.contrib import messages


def enter_seeds(request):
    if request.method == 'POST':
        seed_name = request.POST['seed_name']
        seed_variety = request.POST['seed_variety']
        seed_type = request.POST['seed_type']
        seed_planting_zone = request.POST['seed_planting_zone']
        germination_period = request.POST['germination_period']
        days_to_harvest = request.POST['days_to_harvest']
        plant_spacing = request.POST['plant_spacing']
        row_spacing = request.POST['row_spacing']
        plant_depth = request.POST['plant_depth']
        sun_requirements = request.POST['sun_requirements']
        water_requirements = request.POST['water_requirements']

        seed_information = Seeds(seed_name=seed_name, seed_variety=seed_variety, seed_type=seed_type,
                                 seed_planting_zone=seed_planting_zone, germination_period=germination_period,
                                 days_to_harvest=days_to_harvest, plant_spacing=plant_spacing,
                                 row_spacing=row_spacing, plant_depth=plant_depth, sun_requirements=sun_requirements,
                                 water_requirements=water_requirements)
        seed_information.save()
        messages.success(request, 'Seed information has been entered successfully.')
        return redirect('enter_seeds')
    else:
        return render(request, 'enter_seeds.html', {})


def list_seeds(request):
    all_seeds = Seeds.objects.all()
    return render(request, 'list_seeds.html', {'seeds': all_seeds})


def delete(request, seed_id):
    seeds = Seeds.objects.get(pk=seed_id)
    seeds.delete()
    messages.success(request, 'Seed information has been deleted.')
    return redirect('list_seeds')


def edit_seeds(request, seed_id):
    seeds = Seeds.objects.get(pk=seed_id)
    return render(request, 'edit_seeds.html', {'seeds': seeds})


def update_seeds(request, seed_id):
    seeds = Seeds.objects.get(pk=seed_id)
    seed_form = SeedForm(request.POST or None, instance=seeds)
    if seed_form.is_valid():
        seed_form.save()
        messages.success(request, 'Seed information has been updated successfully.')
        return redirect('list_seeds')
    return render(request, 'update_seeds.html', {'seeds': seeds, 'seed_form': seed_form})

