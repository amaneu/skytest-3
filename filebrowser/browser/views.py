# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
import json
import os
import time
import random


def index(request):
    return render(
        request,
        'index.html',
        {})


def node_contents(request):
    base_path = '/var'  # this is a hardcoded root path
    node = base_path + request.GET['node']
    data = {}

    if not os.path.exists(node):
        data = {'error': 'node does not exist'}
        return HttpResponse(json.dumps(data), content_type="application/json", status=400)

    children = []

    if os.path.isdir(node):
        # return directory contents
        for f in os.listdir(node):
            child = {'name': f}
            if os.path.isfile(node + f):
                child['type'] = 'file'
            else:
                child['type'] = 'dir'

            children.append(child)

        children = sorted(children, key=lambda k: k['type'])

    data = {'node': node, 'children': children}

    time.sleep(0.5 + random.random() / 2)

    return HttpResponse(json.dumps(data), content_type="application/json")
