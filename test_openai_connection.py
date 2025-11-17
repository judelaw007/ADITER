#!/usr/bin/env python3
"""
Quick test to verify OpenAI API key works
"""

import os
import sys

def test_api_key():
    """Test if OpenAI API key is valid"""

    print("\n" + "="*60)
    print("OpenAI API Key Test")
    print("="*60 + "\n")

    # Check environment variable
    api_key = os.getenv('OPENAI_API_KEY')

    if not api_key:
        print("❌ OPENAI_API_KEY not found in environment")
        print("\nTo set it:")
        print("  export OPENAI_API_KEY='sk-...'")
        print("\nOr run with --api-key flag:")
        print("  python create_presentation_with_key.py --api-key sk-...")
        return False

    print(f"✓ API Key found: {api_key[:15]}...{api_key[-4:]}")

    # Verify format
    if not api_key.startswith('sk-'):
        print("⚠️  Warning: Key doesn't start with 'sk-'")
        print("   This might not be a valid OpenAI API key")

    # Try to import OpenAI
    try:
        from openai import OpenAI
        print("✓ OpenAI library imported")
    except ImportError:
        print("❌ OpenAI library not installed")
        print("   Installing now...")
        import subprocess
        subprocess.run([sys.executable, "-m", "pip", "install", "openai"], check=True)
        from openai import OpenAI
        print("✓ OpenAI library installed")

    # Test API connection
    print("\nTesting API connection...")
    try:
        client = OpenAI(api_key=api_key)

        # Try a simple TTS request with minimal text
        print("Generating test audio (this will cost ~$0.001)...")
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input="Testing OpenAI connection."
        )

        # Save test audio
        test_file = "/tmp/test_tts.mp3"
        response.stream_to_file(test_file)

        # Check file size
        import os
        size = os.path.getsize(test_file)

        print(f"✓ API connection successful!")
        print(f"✓ Test audio generated: {size} bytes")
        print(f"✓ Saved to: {test_file}")

        os.remove(test_file)

        print("\n" + "="*60)
        print("✅ SUCCESS! Your API key is working!")
        print("="*60)
        print("\nYou're ready to create presentations!")
        print("\nNext steps:")
        print("  1. Simple: python create_presentation.py")
        print("  2. Advanced: python create_presentation_with_key.py --voice onyx 02")
        print("\n" + "="*60)

        return True

    except Exception as e:
        print(f"\n❌ API Error: {e}")
        print("\nPossible issues:")
        print("  • Invalid API key")
        print("  • No credits/quota remaining")
        print("  • Network connection issue")
        print("\nCheck your API key at:")
        print("  https://platform.openai.com/api-keys")
        return False


if __name__ == "__main__":
    success = test_api_key()
    sys.exit(0 if success else 1)
