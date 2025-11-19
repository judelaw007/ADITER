# 🎓 ADIT Presentation Embed Code

## Visme-Style Embeddable Presentations with Professional TTS Audio

---

## ⚡ Quick Start - Copy & Paste

```html
<!-- Load ADIT Embed Script -->
<script src="https://yoursite.com/presentations/adit-embed.js"></script>

<!-- Embed Presentation -->
<div class="adit-presentation"
     data-subject="fundamental-tax-issues"
     data-chapter="1"
     data-section="0"
     data-width="100%"
     data-height="768px">
</div>
```

**That's it!** Just copy this code and paste it anywhere in your HTML.

---

## 🎯 What You Get

- ✅ **37 HTML5 Presentation Slides** - Professional, responsive design
- ✅ **23 TTS Audio Files** - Google Cloud TTS narration (49MB, ~45-50 minutes)
- ✅ **Auto-play Narration** - Audio plays automatically on each slide
- ✅ **Keyboard Navigation** - Arrow keys + fullscreen support
- ✅ **Progress Tracking** - Visual progress bar and slide counter
- ✅ **Mobile Responsive** - Works on all devices
- ✅ **No Dependencies** - Pure JavaScript, no jQuery required

---

## 📝 Configuration Options

| Attribute | Description | Default |
|-----------|-------------|---------|
| `data-subject` | Subject identifier | `fundamental-tax-issues` |
| `data-chapter` | Chapter number (1-4) | `1` |
| `data-section` | Starting section (0 = topic page) | `0` |
| `data-width` | Player width | `100%` |
| `data-height` | Player height | `768px` |

---

## 📚 Available Chapters

### Chapter 1: International Income Flows
- **Sections:** 6
- **Total Slides:** 9 (topic + 6 content + assessment + completion)
```html
<div class="adit-presentation" data-chapter="1"></div>
```

### Chapter 2: International Investment
- **Sections:** 5
- **Total Slides:** 8
```html
<div class="adit-presentation" data-chapter="2"></div>
```

### Chapter 3: Tax Treaties
- **Sections:** 6
- **Total Slides:** 9
```html
<div class="adit-presentation" data-chapter="3"></div>
```

### Chapter 4: Transfer Pricing
- **Sections:** 6
- **Total Slides:** 9
```html
<div class="adit-presentation" data-chapter="4"></div>
```

---

## 🎬 Usage Examples

### Example 1: Full Width Presentation
```html
<script src="./adit-embed.js"></script>
<div class="adit-presentation"
     data-chapter="1"
     data-section="0">
</div>
```

### Example 2: Fixed Size Presentation
```html
<script src="./adit-embed.js"></script>
<div class="adit-presentation"
     data-chapter="2"
     data-section="0"
     data-width="1366px"
     data-height="900px">
</div>
```

### Example 3: Start at Specific Section
```html
<script src="./adit-embed.js"></script>
<div class="adit-presentation"
     data-chapter="3"
     data-section="2">  <!-- Starts at section 2 -->
</div>
```

---

## 🚀 Hosting Instructions

### Step 1: Upload Files
Upload the entire `presentations/` folder to your web server:
```
presentations/
├── adit-embed.js         ← Main embed script (10KB)
├── index.html            ← Welcome page
├── curriculum.html       ← Course overview
├── 01-*.html            ← Chapter 1 files (9 files)
├── 02-*.html            ← Chapter 2 files (8 files)
├── 03-*.html            ← Chapter 3 files (9 files)
├── 04-*.html            ← Chapter 4 files (9 files)
└── audio/                ← TTS audio files (23 MP3s, 49MB)
    ├── ch01_sec01_*.mp3
    ├── ch01_sec02_*.mp3
    └── ...
```

### Step 2: Update Script URL
Replace `https://yoursite.com` with your actual hosting URL:
```html
<script src="https://your-domain.com/presentations/adit-embed.js"></script>
```

### Step 3: Embed Anywhere
Add the embed code to any HTML page, blog post, or LMS that allows custom HTML.

---

## ⌨️ Keyboard Shortcuts

- **← →** - Navigate between slides
- **F** - Toggle fullscreen mode
- **Esc** - Exit fullscreen

---

## 🎨 Features

### Professional Design
- Gradient-styled player UI
- Smooth transitions and animations
- Progress bar with slide counter
- Chapter and section information display

### Audio Integration
- Auto-play TTS narration (can be disabled)
- Play/pause controls
- Professional male voice (en-US-Neural2-D)
- 2-4 minutes per section

### Navigation
- Previous/Next buttons
- Keyboard shortcuts
- Sequential slide progression
- Topic → Content → Assessment → Completion

---

## 🌐 Browser Support

✅ Chrome 90+
✅ Firefox 88+
✅ Safari 14+
✅ Edge 90+
✅ Mobile browsers (iOS Safari, Chrome Mobile)

---

## 📊 Technical Specs

- **Total Size:** 50MB (577KB HTML + 49MB audio)
- **Audio Files:** 23 MP3 files, Google Cloud TTS
- **Average Audio Duration:** ~2-4 minutes per section
- **Script Size:** ~10KB (adit-embed.js)
- **Dependencies:** None (pure vanilla JavaScript)
- **Framework:** None required

---

## 💡 Examples

### Embed on WordPress
```html
<!-- Add to HTML block or Custom HTML widget -->
<script src="https://cdn.yoursite.com/adit-embed.js"></script>
<div class="adit-presentation" data-chapter="1"></div>
```

### Embed on Ghost Blog
```html
<!-- Add to HTML card -->
<script src="https://cdn.yoursite.com/adit-embed.js"></script>
<div class="adit-presentation" data-chapter="2"></div>
```

### Embed on Canvas LMS
```html
<!-- Add to Page HTML editor -->
<script src="https://yoursite.com/adit-embed.js"></script>
<div class="adit-presentation" data-chapter="3"></div>
```

---

## 📞 Support

For issues or questions:
- Check `EMBED_GUIDE.html` for detailed documentation
- See `embed-example.html` for working example
- Review `README.md` for full presentation details

---

## 🔗 Files Included

- `adit-embed.js` - Main embed script
- `EMBED_GUIDE.html` - Interactive documentation
- `embed-example.html` - Working example
- `EMBED_README.md` - This file
- `README.md` - Full presentation documentation

---

**Ready to Use!** Just copy the embed code and paste it anywhere you want the presentation to appear. 🚀
