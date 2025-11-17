# 🎤 ADIT Interactive Presentation System

Professional presentation builder with **synchronized voice narration** - Visme-quality interactive slides.

## ✨ Features

### 🎯 **Core Capabilities**
- **Interactive Navigation**: Forward/backward with mouse, keyboard, or touch
- **Synchronized Audio**: OpenAI TTS voice narration auto-plays with each slide
- **Real-time Control**: Audio starts/stops as you navigate
- **Professional Design**: Gradient backgrounds, smooth animations, responsive layout
- **Password Protection**: AES-256 encryption for secure delivery
- **Git Hosting**: Deploy via GitHub with public access links

### 🎨 **Visme-Standard Quality**
- Beautiful gradient themes
- Smooth slide transitions
- Progress indicators
- Audio status indicators
- Touch-friendly controls
- Keyboard shortcuts

### 🎙️ **Voice Integration**
Uses OpenAI's **TTS-1-HD** model with 6 professional voices:
- **alloy** - Neutral, balanced (default)
- **echo** - Clear, professional
- **fable** - Warm, expressive
- **onyx** - Deep, authoritative
- **nova** - Energetic, friendly
- **shimmer** - Smooth, calm

---

## 🚀 Quick Start

### **1. Prerequisites**

```bash
# Install required Python packages
pip install openai python-docx cryptography

# Set your OpenAI API key
export OPENAI_API_KEY='sk-...'
```

**Get OpenAI API Key**: https://platform.openai.com/api-keys

### **2. Create Your First Presentation**

```bash
# Simple usage - creates presentation from first DOCX found
python create_presentation.py

# Create presentation for specific topic
python create_presentation.py 03

# The script will prompt you for:
# - Voice selection (alloy, echo, fable, onyx, nova, shimmer)
# - Encryption password (optional)
```

### **3. View the Presentation**

```bash
# Option 1: Direct file open
# Open presentation_output/presentation.html in your browser

# Option 2: Local server (recommended)
cd presentation_output
python -m http.server 8000

# Then visit: http://localhost:8000/presentation.html
```

---

## 🎮 Navigation Controls

### **Mouse/Click**
- Click **"Next"** / **"Previous"** buttons
- Click **"Audio On/Off"** to toggle narration

### **Keyboard**
- **→** or **Space** - Next slide
- **←** - Previous slide
- **M** - Mute/unmute audio

### **Touch Devices**
- **Swipe left** - Next slide
- **Swipe right** - Previous slide

### **Audio Behavior**
- ✅ Auto-plays when slide loads (if audio enabled)
- ✅ Stops when navigating to another slide
- ✅ Can be toggled on/off anytime
- ✅ Visual indicator shows when playing

---

## 📁 Project Structure

```
ADITER/
├── presentation_builder.py      # Core builder class
├── create_presentation.py       # CLI tool for creating presentations
├── presentation_output/         # Generated presentations
│   ├── presentation.html        # Main presentation file
│   ├── index.html              # Encrypted wrapper (if password-protected)
│   └── audio/                  # Generated MP3 files
│       ├── slide_000.mp3
│       ├── slide_001.mp3
│       └── ...
└── generated_notes/            # Source DOCX files
    ├── 01_Fundamental_tax_issues/
    ├── 02_Tax_and_fiscal_regimes/
    ├── 03_Country_tax_examples/
    └── ...
```

---

## 🔧 Advanced Usage

### **Programmatic API**

```python
from presentation_builder import PresentationBuilder

# Initialize builder
builder = PresentationBuilder(
    openai_api_key="sk-...",
    output_dir="my_presentation"
)

# Build presentation
output_file = builder.build_presentation(
    docx_path="path/to/notes.docx",
    title="My ADIT Presentation",
    voice="nova",           # Choose your voice
    password="MySecret123"  # Optional encryption
)

print(f"Created: {output_file}")
```

### **Batch Processing**

```python
from pathlib import Path
from presentation_builder import PresentationBuilder

builder = PresentationBuilder(openai_api_key="sk-...")

# Create presentations for all topics
for docx_file in Path("generated_notes").glob("**/*.docx"):
    print(f"Processing: {docx_file.name}")

    builder.build_presentation(
        docx_path=str(docx_file),
        title=docx_file.stem.replace("_", " "),
        voice="alloy",
        password="ADIT2025"
    )
```

---

## 🔒 Encryption & Security

### **How It Works**
1. **AES-256 Encryption**: Industry-standard encryption using Fernet
2. **PBKDF2 Key Derivation**: 100,000 iterations for password security
3. **Embedded Decryption**: Password entry page included in output
4. **Base64 Encoding**: Safe for web transmission

### **Accessing Encrypted Presentations**
When encryption is enabled:
1. Open `index.html` (the encrypted wrapper)
2. Enter password
3. Presentation unlocks and loads

### **Git Hosting**
The encrypted `index.html` can be:
- Pushed to GitHub
- Served via GitHub Pages
- Shared as a public link
- Password protects the actual content

---

## 🌐 Deploying to Git/GitHub Pages

### **Option 1: GitHub Pages (Public Access)**

```bash
# 1. Commit presentation to repo
git add presentation_output/
git commit -m "Add ADIT presentation with voice narration"
git push origin claude/ai-presentation-voice-slides-01DvPSGAbKbi64FsfMW4vK2n

# 2. Enable GitHub Pages on your repo
# Settings → Pages → Source: main branch → /presentation_output

# 3. Access via:
# https://yourusername.github.io/ADITER/presentation_output/
```

### **Option 2: Direct Git Link**

```bash
# Push to your branch
git add presentation_output/
git commit -m "Add encrypted ADIT presentation"
git push -u origin claude/ai-presentation-voice-slides-01DvPSGAbKbi64FsfMW4vK2n

# Share the raw GitHub link:
# https://raw.githubusercontent.com/yourusername/ADITER/branch/presentation_output/index.html
```

### **Option 3: Release Asset**

```bash
# Create a zip of the presentation
cd presentation_output
zip -r ../adit-presentation.zip .
cd ..

# Create GitHub release with the zip
gh release create v1.0 adit-presentation.zip \
  --title "ADIT Interactive Presentation" \
  --notes "Password-protected presentation with voice narration"

# Users download, extract, and open index.html
```

---

## 💡 Tips & Best Practices

### **Voice Selection**
- **Educational content**: Use `echo` or `onyx` (clear, authoritative)
- **Long presentations**: Use `shimmer` (calm, less fatiguing)
- **Engaging delivery**: Use `nova` or `fable` (energetic, expressive)

### **Content Optimization**
- **Slide length**: Keep narration under 60 seconds per slide
- **Bullet points**: Work better for TTS than long paragraphs
- **Technical terms**: TTS handles most tax terminology well
- **Numbers/Calculations**: Format clearly for better pronunciation

### **Performance**
- Each slide generates one MP3 file (~50-200KB)
- Total presentation size: HTML (50KB) + Audio (varies)
- Load time: Instant for HTML, audio streams as needed

### **Encryption**
- Use strong passwords (12+ characters)
- Default password `ADIT2025` is for demos only
- Change password for production deployments

---

## 🛠️ Troubleshooting

### **"OPENAI_API_KEY not set"**
```bash
# Set the environment variable:
export OPENAI_API_KEY='sk-your-key-here'

# Or create .env file:
echo "OPENAI_API_KEY=sk-your-key-here" > .env
```

### **Audio Not Playing**
- Check browser console for errors
- Some browsers block autoplay - click the audio toggle
- Ensure audio files are in the `audio/` subdirectory
- Try using a local server instead of `file://` protocol

### **"No DOCX files found"**
```bash
# Check available topics:
ls generated_notes/

# Specify topic number explicitly:
python create_presentation.py 03
```

### **Slides Look Wrong**
- Ensure DOCX uses Heading 1/2 styles for slide breaks
- Check content formatting in original document
- HTML conversion works best with structured documents

---

## 📊 Costs & Pricing

### **OpenAI TTS Pricing** (as of 2025)
- **TTS-1-HD**: $0.030 per 1,000 characters
- Average slide narration: ~500 characters = $0.015
- **20-slide presentation**: ~$0.30
- **100-slide course**: ~$1.50

Very affordable for professional presentations!

---

## 🎓 Example Use Cases

### **1. ADIT Course Modules**
Convert all 15 ADIT topics into interactive voice presentations

### **2. Student Study Guides**
Self-paced learning with audio narration for each concept

### **3. Professional Training**
Corporate tax training materials with consistent voice delivery

### **4. Exam Preparation**
Past exam question walkthroughs with audio explanations

### **5. Conference Presentations**
Pre-recorded presentations that can be shared or presented remotely

---

## 🔄 Updates & Versions

**Version 1.0** (Current)
- ✅ Interactive HTML5 presentations
- ✅ OpenAI TTS-1-HD integration
- ✅ 6 professional voices
- ✅ AES-256 encryption
- ✅ Touch/keyboard/mouse navigation
- ✅ Audio synchronization
- ✅ Progress indicators

**Planned Features**
- 📋 Slide notes/annotations
- 🎨 Custom themes/branding
- 📝 Live transcript display
- ⏱️ Timing controls (auto-advance)
- 📊 Analytics (slide views, completion)
- 🌍 Multi-language support

---

## 📞 Support

For issues or questions:
1. Check this README
2. Review the troubleshooting section
3. Check OpenAI API documentation
4. Open an issue on GitHub

---

## 📜 License

This tool is for ADIT educational content creation. Use responsibly and in compliance with OpenAI's usage policies.

---

**Built with ❤️ for ADIT Module 3.04 Energy Resources**

Ready to create professional presentations? Run `python create_presentation.py` to get started!
