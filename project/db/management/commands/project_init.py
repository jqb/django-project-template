#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):
    help = "Loads project initial data"

    def handle_noargs(self, **options):
        from db import project_init
        project_init.load()
