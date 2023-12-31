#!/bin/bash

# 啟動 Celery worker 並將日誌級別設為 info
celery -A Backend worker -l info &
