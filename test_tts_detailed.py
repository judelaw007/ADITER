#!/usr/bin/env python3
"""Test OpenAI TTS with detailed error reporting"""

from openai import OpenAI
import os

api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    print("ERROR: OPENAI_API_KEY environment variable not set!")
    print("\nSet it with:")
    print("  export OPENAI_API_KEY='sk-...'")
    import sys
    sys.exit(1)

print("Testing OpenAI TTS API...")
print(f"API Key: {api_key[:20]}...{api_key[-10:]}\n")

try:
    client = OpenAI(api_key=api_key)
    
    print("Attempting to generate speech...")
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input="This is a test of the text to speech system."
    )
    
    # Save to file
    output_file = "/tmp/test_audio.mp3"
    response.stream_to_file(output_file)
    
    # Check file
    size = os.path.getsize(output_file)
    print(f"✓ SUCCESS! Generated audio file: {size} bytes")
    print(f"✓ Saved to: {output_file}")
    
except Exception as e:
    print(f"✗ ERROR: {e}")
    print(f"\nError type: {type(e).__name__}")
    
    # Try to get more details
    if hasattr(e, 'response'):
        print(f"Response: {e.response}")
    if hasattr(e, 'status_code'):
        print(f"Status code: {e.status_code}")
    if hasattr(e, 'message'):
        print(f"Message: {e.message}")
    
    print("\nPossible issues:")
    print("1. API key doesn't have TTS permissions (project-scoped key)")
    print("2. Billing not set up or no credits remaining")
    print("3. Rate limits exceeded")
    print("4. Invalid API key")
    
    import sys
    sys.exit(1)
