#!/bin/bash

celery -A Backend flower -l info --basic_auth=twtrubiks:password123
