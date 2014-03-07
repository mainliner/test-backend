#!/bin/bash
uwsgi -s 127.0.0.1:8080 -w app:app --processes 2
