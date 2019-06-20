# -*- coding: utf-8 -*-
from model.project import Project
import random
import string

status_list = ['development', 'release', 'stable', 'obsolete']
view_status_list = ['public', 'private']

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Project(name=random_string('name', 3),
                    description=random_string('description', 3),
                    status=random.choice(status_list),
                    view_status=random.choice(view_status_list))]


