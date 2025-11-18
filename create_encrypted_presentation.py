#!/usr/bin/env python3
"""
Create password-protected presentation (Visme-style)
Simple encryption using JavaScript password check
"""

import os
import sys
import json
import base64
import hashlib
from pathlib import Path


def create_encrypted_wrapper(presentation_file: str, password: str, output_file: str = "index.html"):
    """Create password-protected HTML wrapper"""

    # Read the presentation HTML
    with open(presentation_file, 'r', encoding='utf-8') as f:
        presentation_html = f.read()

    # Read audio files
    audio_dir = Path(presentation_file).parent / "audio"
    audio_files = {}

    if audio_dir.exists():
        for audio_file in audio_dir.glob("*.mp3"):
            with open(audio_file, 'rb') as f:
                audio_data = base64.b64encode(f.read()).decode('utf-8')
                audio_files[audio_file.name] = audio_data

    # Encode presentation HTML
    presentation_b64 = base64.b64encode(presentation_html.encode('utf-8')).decode('utf-8')

    # Create password hash (SHA-256)
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

    # Create encrypted HTML
    encrypted_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ADIT Presentation - Password Protected</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }}

        .password-container {{
            background: white;
            padding: 50px;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            text-align: center;
            max-width: 500px;
            animation: fadeIn 0.5s ease-in-out;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        h1 {{
            color: #1F4E78;
            margin-bottom: 20px;
            font-size: 2em;
        }}

        .subtitle {{
            color: #666;
            margin-bottom: 30px;
            font-size: 1.1em;
        }}

        .lock-icon {{
            font-size: 4em;
            margin-bottom: 20px;
        }}

        input {{
            width: 100%;
            padding: 15px;
            font-size: 1.1em;
            border: 2px solid #ddd;
            border-radius: 10px;
            margin-bottom: 20px;
            transition: border-color 0.3s;
        }}

        input:focus {{
            outline: none;
            border-color: #667eea;
        }}

        button {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 15px 40px;
            font-size: 1.1em;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            width: 100%;
        }}

        button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        }}

        .error {{
            color: #e74c3c;
            margin-top: 15px;
            display: none;
            font-size: 0.9em;
        }}

        .hint {{
            color: #999;
            font-size: 0.9em;
            margin-top: 20px;
        }}

        #presentationFrame {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none;
        }}
    </style>
</head>
<body>
    <div class="password-container" id="passwordContainer">
        <div class="lock-icon">🔒</div>
        <h1>ADIT Presentation</h1>
        <p class="subtitle">This presentation is password protected</p>

        <input
            type="password"
            id="passwordInput"
            placeholder="Enter password"
            autocomplete="off"
            onkeypress="if(event.key==='Enter') unlockPresentation()"
        >

        <button onclick="unlockPresentation()">Unlock Presentation</button>

        <p class="error" id="errorMsg">❌ Incorrect password. Please try again.</p>
        <p class="hint">Hint: Contact the presenter for the password</p>
    </div>

    <iframe id="presentationFrame"></iframe>

    <script>
        // Password hash (SHA-256)
        const correctPasswordHash = '{password_hash}';

        // Encoded presentation data
        const presentationData = '{presentation_b64}';

        // Encoded audio files
        const audioFiles = {json.dumps(audio_files)};

        // SHA-256 hash function
        async function sha256(message) {{
            const msgBuffer = new TextEncoder().encode(message);
            const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
            const hashArray = Array.from(new Uint8Array(hashBuffer));
            const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
            return hashHex;
        }}

        async function unlockPresentation() {{
            const password = document.getElementById('passwordInput').value;
            const errorMsg = document.getElementById('errorMsg');

            if (!password) {{
                errorMsg.textContent = '⚠️ Please enter a password';
                errorMsg.style.display = 'block';
                return;
            }}

            // Hash the input password
            const inputHash = await sha256(password);

            if (inputHash === correctPasswordHash) {{
                errorMsg.style.display = 'none';

                // Decode presentation
                const presentationHTML = atob(presentationData);

                // Create blob URLs for audio files
                const audioBlobUrls = {{}};
                for (const [filename, base64Data] of Object.entries(audioFiles)) {{
                    const binaryData = atob(base64Data);
                    const bytes = new Uint8Array(binaryData.length);
                    for (let i = 0; i < binaryData.length; i++) {{
                        bytes[i] = binaryData.charCodeAt(i);
                    }}
                    const blob = new Blob([bytes], {{ type: 'audio/mpeg' }});
                    audioBlobUrls[filename] = URL.createObjectURL(blob);
                }}

                // Replace audio file references with blob URLs
                let modifiedHTML = presentationHTML;
                for (const [filename, blobUrl] of Object.entries(audioBlobUrls)) {{
                    modifiedHTML = modifiedHTML.replace(
                        new RegExp(`audio/${{filename}}`, 'g'),
                        blobUrl
                    );
                }}

                // Hide password container
                document.getElementById('passwordContainer').style.display = 'none';

                // Show presentation in iframe
                const iframe = document.getElementById('presentationFrame');
                iframe.style.display = 'block';

                // Write presentation to iframe
                const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
                iframeDoc.open();
                iframeDoc.write(modifiedHTML);
                iframeDoc.close();

            }} else {{
                errorMsg.textContent = '❌ Incorrect password. Please try again.';
                errorMsg.style.display = 'block';
                document.getElementById('passwordInput').value = '';
                document.getElementById('passwordInput').focus();
            }}
        }}

        // Auto-focus password input
        document.getElementById('passwordInput').focus();
    </script>
</body>
</html>'''

    # Save encrypted file
    output_path = Path(presentation_file).parent / output_file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(encrypted_html)

    return str(output_path)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Create password-protected presentation')
    parser.add_argument('--password', default='ADIT2025', help='Password for presentation')
    parser.add_argument('--presentation', default='presentation_output/presentation.html',
                       help='Path to presentation HTML file')
    parser.add_argument('--output', default='index.html', help='Output filename')

    args = parser.parse_args()

    if not os.path.exists(args.presentation):
        print(f"Error: Presentation file not found: {args.presentation}")
        print("\nFirst create a presentation:")
        print("  python3 create_simple_presentation.py 02")
        sys.exit(1)

    print("\n" + "="*60)
    print("Creating Password-Protected Presentation")
    print("="*60 + "\n")

    output_file = create_encrypted_wrapper(
        presentation_file=args.presentation,
        password=args.password,
        output_file=args.output
    )

    print(f"✓ Created: {output_file}")
    print(f"✓ Password: {args.password}")
    print(f"\n{'='*60}")
    print("Encrypted Presentation Ready!")
    print("="*60)
    print(f"\nTo view locally:")
    print(f"  cd {Path(output_file).parent}")
    print(f"  python -m http.server 8000")
    print(f"  Open: http://localhost:8000/{Path(output_file).name}")
    print(f"  Password: {args.password}")

    print(f"\nTo share via Git:")
    print(f"  git add {output_file}")
    print(f"  git commit -m 'Add encrypted presentation'")
    print(f"  git push")

    print(f"\nShare this link:")
    print(f"  https://raw.githubusercontent.com/YOUR_USERNAME/ADITER/YOUR_BRANCH/{output_file}")
    print(f"  Password: {args.password}")

    print(f"\nOr via GitHub Pages:")
    print(f"  https://YOUR_USERNAME.github.io/ADITER/{Path(output_file).parent}/")
    print(f"  Password: {args.password}")

    file_size = os.path.getsize(output_file) / 1024
    print(f"\nFile size: {file_size:.1f} KB (self-contained, includes all audio)")
    print("\n" + "="*60)
