from django.shortcuts import render
from subprocess import check_output
from django.conf import settings
import os

# Create your views here.

base_dir = settings.BASE_DIR


def execute_scripts(data):
    op = dict()
    for file in data:
        cmd = 'python ' + file
        op[file] = check_output(cmd, shell=True)
    return op


def base_view(request):
    return render(request, 'base.html')


def audio_view(request):
    data = request.POST.getlist('script')
    output = None
    if data:
        os.chdir(base_dir + '\\audio')
        output = execute_scripts(data)
        os.chdir(base_dir)
    return render(request, 'audio.html', {'data': output})


def display_view(request):
    data = request.POST.getlist('script')
    output = None
    if data:
        os.chdir(base_dir + '\display')
        output = execute_scripts(data)
        os.chdir(base_dir)
    return render(request, 'display.html', {'data': output})


def video_view(request):
    data = request.POST.getlist('script')
    output = None
    if data:
        os.chdir(base_dir + '\\video')
        output = execute_scripts(data)
        os.chdir(base_dir)
    return render(request, 'video.html', {'data': output})
