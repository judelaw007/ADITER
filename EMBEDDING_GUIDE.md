# 🔗 Embedding Guide - Share Your Presentations Anywhere

## ✅ **Yes! Your Presentations Can Be Embedded Like Visme**

Just like Visme's embed codes, your HTML5 presentations can be embedded in:
- 🌐 Websites and blogs
- 📚 LMS pages (Moodle, Canvas, etc.)
- 📱 Mobile apps (webview)
- 📧 Email newsletters (some clients)
- 🎓 Course platforms (LearnWorlds, Teachable)

---

## 🎯 **Quick Start: Simple Embedding**

### **Method 1: Basic iframe (Easiest)**

```html
<iframe
    src="https://judelaw007.github.io/ADITER/presentation_output/presentation.html"
    width="800px"
    height="600px"
    frameborder="0"
    allowfullscreen
    allow="autoplay">
</iframe>
```

**Use this when:**
- Quick and simple
- You control the page width
- Desktop-first design

---

### **Method 2: Responsive Embed (Recommended)**

```html
<!-- Responsive 16:9 ratio -->
<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
    <iframe
        src="https://judelaw007.github.io/ADITER/presentation_output/presentation.html"
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
        allowfullscreen
        allow="autoplay">
    </iframe>
</div>
```

**Use this when:**
- Mobile-friendly required
- Responsive website
- Unknown screen sizes

---

### **Method 3: Visme-Style Embed (Fanciest)**

```html
<!-- Include the embed script once per page -->
<script src="https://judelaw007.github.io/ADITER/adit-embed.js"></script>

<!-- Use anywhere on the page -->
<div class="adit-presentation"
     data-url="presentation_output/presentation.html"
     data-width="100%"
     data-height="600px"
     data-border="visme"
     data-title="ADIT Tax Presentation">
</div>
```

**Use this when:**
- Want Visme-like experience
- Multiple embeds on same page
- Need loading animations
- Want fullscreen button

---

## 🛠️ **Interactive Embed Code Generator**

**Open this file in your browser:**
```
file:///home/user/ADITER/embed_code_generator.html
```

Or host it and access via:
```
https://judelaw007.github.io/ADITER/embed_code_generator.html
```

**Features:**
- ✅ Visual configuration
- ✅ Live preview
- ✅ One-click copy
- ✅ Multiple embed styles
- ✅ Responsive options

---

## 📋 **Embedding Options Reference**

### **Data Attributes (for Visme-style embed)**

| Attribute | Default | Options | Description |
|-----------|---------|---------|-------------|
| `data-url` | `presentation_output/presentation.html` | Any URL | Presentation URL |
| `data-width` | `100%` | px or % | Width of embed |
| `data-height` | `600px` | px | Height of embed |
| `data-border` | `none` | `none`, `simple`, `rounded`, `shadow`, `visme` | Border style |
| `data-fullscreen` | `true` | `true`, `false` | Allow fullscreen |
| `data-autoplay` | `true` | `true`, `false` | Allow audio autoplay |
| `data-loading` | `lazy` | `lazy`, `eager` | Load timing |
| `data-title` | `ADIT Presentation` | Any text | Accessibility title |

---

## 🎨 **Styling Examples**

### **1. Simple Border**
```html
<iframe
    src="YOUR_URL"
    width="100%"
    height="600px"
    style="border: 1px solid #ddd;">
</iframe>
```

### **2. Rounded with Shadow (Visme-like)**
```html
<iframe
    src="YOUR_URL"
    width="100%"
    height="600px"
    style="border: 2px solid #667eea;
           border-radius: 10px;
           box-shadow: 0 4px 20px rgba(102,126,234,0.2);">
</iframe>
```

### **3. Card Style**
```html
<div style="background: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);">
    <h3 style="margin-bottom: 15px;">ADIT Tax Presentation</h3>
    <iframe
        src="YOUR_URL"
        width="100%"
        height="600px"
        style="border: none; border-radius: 10px;">
    </iframe>
</div>
```

---

## 🌐 **Platform-Specific Embedding**

### **WordPress**

**Method 1: Gutenberg Block**
1. Add "Custom HTML" block
2. Paste iframe code
3. Publish

**Method 2: Shortcode (create in functions.php)**
```php
function adit_presentation_shortcode($atts) {
    $a = shortcode_atts(array(
        'url' => 'https://judelaw007.github.io/ADITER/presentation_output/presentation.html',
        'width' => '100%',
        'height' => '600px'
    ), $atts);

    return '<iframe src="' . $a['url'] . '"
                    width="' . $a['width'] . '"
                    height="' . $a['height'] . '"
                    frameborder="0"
                    allowfullscreen
                    allow="autoplay"></iframe>';
}
add_shortcode('adit_presentation', 'adit_presentation_shortcode');
```

**Usage:**
```
[adit_presentation url="YOUR_URL" width="100%" height="600px"]
```

---

### **Wix**

1. Add "HTML iframe" element
2. Paste URL: `https://judelaw007.github.io/ADITER/presentation_output/presentation.html`
3. Adjust size
4. Publish

---

### **Squarespace**

1. Add "Code" block
2. Paste iframe code
3. Save

---

### **LearnWorlds**

**Option 1: As HTML section**
1. Create new section
2. Choose "HTML" type
3. Paste embed code

**Option 2: As SCORM (better)**
- Upload SCORM package instead
- Gets full tracking

---

### **Moodle**

**Method 1: Label with HTML**
1. Add "Label" activity
2. Click HTML source button
3. Paste iframe code

**Method 2: URL Resource**
1. Add "URL" resource
2. Set to open in "Embed"
3. Paste presentation URL

**Method 3: SCORM (best)**
- Upload SCORM package
- Full tracking integration

---

### **Canvas LMS**

**Method 1: Page Embed**
1. Create/edit page
2. Click HTML editor
3. Paste iframe code

**Method 2: External Tool**
1. Add external tool
2. Set URL
3. Configure display

---

## 💡 **Advanced Embedding**

### **Multiple Presentations on One Page**

```html
<script src="https://judelaw007.github.io/ADITER/adit-embed.js"></script>

<h2>Topic 1: Fundamentals</h2>
<div class="adit-presentation"
     data-url="presentation_output/topic01.html">
</div>

<h2>Topic 2: Tax Regimes</h2>
<div class="adit-presentation"
     data-url="presentation_output/topic02.html">
</div>

<h2>Topic 3: Country Examples</h2>
<div class="adit-presentation"
     data-url="presentation_output/topic03.html">
</div>
```

---

### **Programmatic Embedding (JavaScript)**

```html
<div id="my-presentation"></div>

<script src="https://judelaw007.github.io/ADITER/adit-embed.js"></script>
<script>
    // Embed programmatically
    ADITEmbed.embed('#my-presentation', {
        url: 'presentation_output/presentation.html',
        width: '100%',
        height: '600px',
        border: 'visme',
        title: 'My Custom Title'
    });
</script>
```

---

### **Lazy Loading (Performance)**

```html
<!-- Only loads when scrolled into view -->
<iframe
    src="YOUR_URL"
    width="100%"
    height="600px"
    loading="lazy"
    allowfullscreen>
</iframe>
```

---

## 🔒 **Password-Protected Embeds**

Your encrypted presentations (`index.html`) can also be embedded:

```html
<iframe
    src="https://judelaw007.github.io/ADITER/presentation_output/index.html"
    width="100%"
    height="650px">
</iframe>
```

**User experience:**
1. Iframe loads
2. Shows password prompt
3. User enters password: `ADIT2025`
4. Presentation unlocks

---

## 📱 **Mobile Optimization**

### **Responsive Breakpoints**

```html
<style>
    .presentation-container {
        width: 100%;
        max-width: 1200px;
        margin: 0 auto;
    }

    .presentation-container iframe {
        width: 100%;
        height: 600px;
    }

    @media (max-width: 768px) {
        .presentation-container iframe {
            height: 400px;
        }
    }

    @media (max-width: 480px) {
        .presentation-container iframe {
            height: 300px;
        }
    }
</style>

<div class="presentation-container">
    <iframe src="YOUR_URL" allowfullscreen allow="autoplay"></iframe>
</div>
```

---

## 📊 **Comparison: Your Embed vs Visme**

| Feature | Visme Embed | Your ADIT Embed |
|---------|-------------|-----------------|
| **Embed Code** | ✅ Yes | ✅ Yes (3 methods!) |
| **Responsive** | ✅ Yes | ✅ Yes |
| **Loading Animation** | ✅ Yes | ✅ Yes (with adit-embed.js) |
| **Fullscreen** | ✅ Yes | ✅ Yes |
| **Voice Narration** | ❌ No | ✅ Yes (built-in) |
| **Requires Server** | ✅ Visme servers | ✅ Your GitHub/any host |
| **Customizable** | ⚠️ Limited | ✅ Fully customizable |
| **Offline Capable** | ❌ No | ✅ Yes |
| **Cost** | 💰 $12.25/mo+ | ✅ Free (GitHub Pages) |
| **Branding** | ⚠️ Visme logo | ✅ Your branding |

---

## 🎯 **Embedding Best Practices**

### **1. Choose Right Height**

**Desktop:**
- Standard: `600px`
- Comfortable: `700px`
- Full experience: `800px`

**Mobile:**
- Minimum: `300px`
- Recommended: `400px`
- Maximum: `500px`

### **2. Always Include Attributes**

```html
allowfullscreen    <!-- Let users go fullscreen -->
allow="autoplay"   <!-- Let audio play automatically -->
loading="lazy"     <!-- Improve page load performance -->
```

### **3. Accessibility**

```html
<iframe
    src="YOUR_URL"
    title="ADIT Tax Presentation on Fiscal Regimes"
    aria-label="Interactive tax presentation">
</iframe>
```

### **4. SEO Considerations**

```html
<!-- Add context around embed for SEO -->
<article>
    <h2>ADIT Module 2: Tax and Fiscal Regimes</h2>
    <p>This interactive presentation covers PSCs, concession regimes, and royalty structures.</p>

    <div class="presentation-embed">
        <iframe src="YOUR_URL" ...></iframe>
    </div>

    <p>Use arrow keys to navigate. Audio plays automatically with each slide.</p>
</article>
```

---

## 🔧 **Troubleshooting**

### **Problem: Iframe Not Showing**

**Solutions:**
1. Check URL is correct and accessible
2. Check browser console for errors
3. Verify CORS policy (GitHub Pages should work)
4. Try different browser

### **Problem: Audio Not Playing**

**Solutions:**
1. Add `allow="autoplay"` attribute
2. User may need to click/interact first (browser policy)
3. Check browser's autoplay settings

### **Problem: Not Responsive on Mobile**

**Solutions:**
1. Use responsive embed code (Method 2)
2. Set `width="100%"`
3. Add viewport meta tag to page:
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

### **Problem: Fullscreen Not Working**

**Solutions:**
1. Add `allowfullscreen` attribute
2. Check browser support
3. May need user gesture (click) to trigger

---

## 📦 **Files You Need**

**For Simple Embedding:**
- ✅ Just the iframe code (no files needed)

**For Visme-Style Embedding:**
- ✅ `adit-embed.js` (host on GitHub Pages)
- ✅ Presentation files (already on GitHub Pages)

**For Custom Styling:**
- ✅ Your CSS file
- ✅ Optional: custom embed wrapper

---

## 🚀 **Quick Reference**

### **Most Common Use Cases:**

**1. Blog Post Embed:**
```html
<div style="position: relative; padding-bottom: 56.25%; height: 0;">
    <iframe src="YOUR_URL"
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
            allowfullscreen allow="autoplay">
    </iframe>
</div>
```

**2. Course Page Embed:**
```html
<script src="https://judelaw007.github.io/ADITER/adit-embed.js"></script>
<div class="adit-presentation"
     data-url="presentation_output/presentation.html"
     data-border="visme">
</div>
```

**3. LMS Embed:**
```html
<iframe src="YOUR_URL"
        width="100%"
        height="600px"
        allowfullscreen>
</iframe>
```

---

## ✨ **Summary**

**Your presentations CAN be embedded just like Visme!**

You have **3 embedding methods**:
1. ✅ Simple iframe (easiest)
2. ✅ Responsive embed (best for mobile)
3. ✅ Visme-style with `adit-embed.js` (fanciest)

**Advantages over Visme:**
- ✅ Free (no subscription)
- ✅ Voice narration included
- ✅ Full customization
- ✅ Host anywhere
- ✅ No branding requirements

**Tools provided:**
- ✅ `embed_code_generator.html` - Visual generator
- ✅ `adit-embed.js` - Visme-style embed script
- ✅ Multiple code examples

**Ready to embed anywhere!** 🎉
