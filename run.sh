#!/bin/bash
python -m uvicorn --host localhost --port=8000 --workers 1 main:app