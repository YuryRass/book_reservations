#!/bin/bash

celery -A app.tasks.celery:celery worker --loglevel=info