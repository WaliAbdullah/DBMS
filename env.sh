#!/bin/bash

PYTHON_VERSION="3.10"
VENV_DIR=".venv"

error=false

# 1. Create a virtual environment (if not exists)
if [ ! -d "$VENV_DIR" ]; then
    if command -v python$PYTHON_VERSION &> /dev/null; then
        python$PYTHON_VERSION -m venv "$VENV_DIR" || error=true
    elif command -v python3 &> /dev/null; then
        python3 -m venv "$VENV_DIR" || error=true
    else
        echo "Python 3.x is required but not found."
        error=true
    fi
    if [ "$error" = true ]; then
        echo "Failed to create virtual environment."
        return 1 2>/dev/null || exit 1
    fi
    echo "Virtual environment created at $VENV_DIR"
else
    echo "Virtual environment already exists at $VENV_DIR"
fi

# 2. Activate the venv
# shellcheck source=/dev/null
if ! source "$VENV_DIR/bin/activate"; then
    echo "Failed to activate virtual environment."
    return 1 2>/dev/null || exit 1
fi

# 3. Upgrade pip, install Poetry in venv
if ! pip install --upgrade pip; then
    echo "Failed to upgrade pip."
    return 1 2>/dev/null || exit 1
fi

if ! pip install poetry; then
    echo "Failed to install Poetry."
    return 1 2>/dev/null || exit 1
fi

# 4. Install project dependencies via Poetry (inside venv)
if ! poetry install; then
    echo "Poetry failed to install dependencies."
    return 1 2>/dev/null || exit 1
fi

echo ""
echo "--------------------------------------------------"
echo "Environment setup complete!"
echo "--------------------------------------------------"

