import validators
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from short_url.forms import CreateRandomUrlForm
from short_url.models import Links
from short_url.utils import generate_random_short_url, check_short_url


def index(request):
    return redirect('short_url:links')


@login_required
def links(request):
    return render(request, 'short_url/links.html')


@login_required
def create(request):
    if request.method == 'POST':
        form = CreateRandomUrlForm(data=request.POST)
        if form.is_valid() and check_short_url(form.data['short_url']) and validators.url(form.data['url']):
            short_url = form.data['short_url'] if form.data['short_url'] else generate_random_short_url()
            Links.objects.create(user=request.user, short_url=short_url, url=form.data['url'],
                                 description=form.data['description'])
            messages.success(request, "Success")
            return redirect("short_url:create")
        else:
            messages.error(request, 'Enter the correct url')
            return redirect("short_url:create")
    else:
        form = CreateRandomUrlForm()
    context = {'form': form}
    return render(request, 'short_url/links_create.html', context)


@login_required
def info(request):
    records = Links.objects.filter(user=request.user)
    context = {'links': records}
    return render(request, 'short_url/info.html', context)


@login_required
def delete_link(request, short_url):
    record = Links.objects.filter(user=request.user, short_url=short_url)
    if record:
        record.delete()
    return redirect('short_url:info')


def short_url_redirect(request, short_url):
    try:
        record = Links.objects.get(short_url=short_url)
        record.first().quantity += 1
        record.save()
        url = record.first().url
        return redirect(url)
    except ObjectDoesNotExist:
        return redirect('index')
