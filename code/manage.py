#!/usr/bin/env python
import os
import sys
import django

import torch.nn as nn
import torch.nn.functional as F

class module(nn.Module):
    def __init__(self, num_hidden_neurons):
        super(module, self).__init__()
        self.fc1 = nn.Linear(3, num_hidden_neurons)
        self.fc2 = nn.Linear(num_hidden_neurons, 1)
        
    def forward(self, X_train):
        X_train = self.fc1(X_train)
        X_train = F.relu(X_train)
        X_train = self.fc2(X_train)
        return X_train



if __name__ == "__main__":

    if str(sys.argv[0]).endswith('manage.py'):
        if 'runserver' in sys.argv or 'migrate' in sys.argv or 'createsuperuser' in sys.argv or 'syncdb' in sys.argv or 'collectstatic' in sys.argv:
            if 'test' in sys.argv or '--test' in sys.argv:
                os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mgi.settings_test")
            else:
                os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mgi.settings")
        else:
            os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mgi.settings_test")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mgi.settings_test")

    print 'loading settings at...:' + os.environ.get("DJANGO_SETTINGS_MODULE")

    args = sys.argv
    if '--no-selenium' in args:
        os.environ.setdefault("SELENIUM", "false")
        args.remove('--no-selenium')
    else:
        os.environ.setdefault("SELENIUM", "true")
    if '--test' in args:
        args.remove('--test')
    from django.core.management import execute_from_command_line
    execute_from_command_line(args)
