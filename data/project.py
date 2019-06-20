# -*- coding: utf-8 -*-
from model.project import Project
import random
import string

status_list = ['10', '30', '50', '70']
view_status_list = ['10', '50']

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Project(name=random_string('name', 3),
                    description=random_string('description', 3),
                    status=random.choice(status_list),
                    view_status=random.choice(view_status_list))]


