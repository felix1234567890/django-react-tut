#!/bin/bash

# Change to the project directory
cd "$(dirname "$0")"

# Activate the virtual environment
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    source backend/env/bin/activate 2>/dev/null || source backend/env/Scripts/activate 2>/dev/null
else
    # Windows with Git Bash or Linux
    source backend/env/Scripts/activate 2>/dev/null || source backend/env/bin/activate 2>/dev/null
fi

# Change to the Django project directory
cd backend/src

# Run the Django command passed as arguments
python3 manage.py "$@"

# Deactivate the virtual environment when done
deactivate
