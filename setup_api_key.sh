#!/bin/bash
# Setup script for OpenAI API Key

echo "================================================"
echo "  OpenAI API Key Setup for Presentations"
echo "================================================"
echo ""

# Check if API key is provided as argument
if [ -n "$1" ]; then
    export OPENAI_API_KEY="$1"
    echo "✓ API Key set from argument"
else
    # Prompt for API key
    echo "Please paste your OpenAI API key (starts with sk-):"
    read -s OPENAI_API_KEY
    export OPENAI_API_KEY
fi

# Verify key format
if [[ $OPENAI_API_KEY == sk-* ]]; then
    echo "✓ API Key format looks correct!"
    echo "✓ Key prefix: ${OPENAI_API_KEY:0:15}..."
    echo ""
    echo "API key is now set for this session."
    echo ""
    echo "To make it permanent, add to your ~/.bashrc or ~/.zshrc:"
    echo "  export OPENAI_API_KEY='$OPENAI_API_KEY'"
    echo ""
    echo "Now you can run:"
    echo "  python create_presentation.py"
    echo ""
else
    echo "✗ Invalid API key format. Should start with 'sk-'"
    exit 1
fi
