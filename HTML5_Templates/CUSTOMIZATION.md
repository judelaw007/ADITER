# MojiTax Templates - Customization Examples

This guide shows real-world examples of how to customize the templates for different courses and organizations.

## 🎯 Example 1: CPE Credit Course

### Scenario
You're hosting a CPA continuing education course on Tax Planning Strategies.

### Key Changes

#### 1. Header and Branding (all templates)
**Find:**
```html
<h1>MojiTax Presentation Templates</h1>
<p>Professional HTML5 Educational Content System</p>
```

**Replace with:**
```html
<h1>Tax Planning Strategies 2024</h1>
<p>NASBA-Approved CPA Continuing Education - 4 CPE Credits</p>
```

#### 2. Welcome Page (01-welcome.html)
**Find:**
```html
<h1>Welcome to MojiTax</h1>
<p class="tagline">Professional Tax Education & Training</p>
<p class="welcome-description">
    Master modern tax strategy, compliance, and planning with our comprehensive, expert-led curriculum designed for financial professionals and tax practitioners.
</p>
```

**Replace with:**
```html
<h1>Welcome to Tax Planning Strategies</h1>
<p class="tagline">Advanced Strategies for 2024 Tax Year</p>
<p class="welcome-description">
    Discover cutting-edge tax planning techniques, emerging legislative changes, and strategic approaches to maximize client outcomes. This course is approved for 4 hours of NASBA continuing professional education credits.
</p>
```

#### 3. Curriculum Page (02-curriculum.html)
**Update module titles:**
```html
<div class="module-number">1</div>
<div class="module-title">Tax Law Updates 2024</div>
```

**Update descriptions:**
```html
<p class="module-description">
    Comprehensive review of recent legislative changes, IRS guidance, and their implications for tax planning strategies.
</p>
```

#### 4. Color Scheme for CPE
In `<style>` section, update colors to professional accounting standards:
```css
:root {
    --primary: #1B3A57;      /* Dark navy - professional */
    --secondary: #2E5090;    /* Blue - trust & stability */
    --accent: #D4AF37;       /* Gold - achievement */
    --success: #1E7E34;      /* Green - compliance */
}
```

---

## 💼 Example 2: Corporate Tax Training

### Scenario
You're training new hires at a Fortune 500 corporation on tax compliance procedures.

### Key Changes

#### 1. Company Branding
**Update logo emoji:**
```html
<!-- Replace 🦅 with your company logo -->
<div class="logo-circle" style="background-image: url('company-logo.png'); background-size: contain;">
</div>
```

**Or use company initials:**
```html
<div class="logo-circle">
    <span style="font-size: 60px; font-weight: bold;">ABC</span>
</div>
```

#### 2. Welcome Page Customization
```html
<h1>Tax Compliance Training Program</h1>
<p class="tagline">ABC Corporation - New Employee Onboarding</p>
<p class="welcome-description">
    Learn ABC Corporation's tax compliance procedures, internal controls, and best practices for managing corporate tax obligations.
</p>
<button class="cta-button">Start Training Module</button>
```

#### 3. Curriculum - Real Training Modules
```html
<div class="module-number">1</div>
<div class="module-title">Tax Compliance Framework</div>
<p class="module-description">
    Overview of ABC's tax governance structure, key tax compliance responsibilities, and regulatory requirements.
</p>
<div class="module-meta">
    <span>📚 8 lessons</span>
    <span>⏱ 3.5 hours</span>
</div>
```

#### 4. Content Page - Specific Topics
```html
<h2 class="section-title">ABC Corporation Tax Filing Procedures</h2>

<ul class="bullet-points">
    <li>Federal income tax return filing requirements and deadlines</li>
    <li>State and local tax compliance checklist</li>
    <li>Documentation standards and record retention policies</li>
    <li>Approval workflows for tax positions and valuations</li>
    <li>Internal reporting and compliance monitoring</li>
</ul>
```

#### 5. Assessment - Real Scenarios
```html
<div class="question-card">
    <div class="question-number">Question 1</div>
    <div class="question-text">
        According to ABC's tax compliance policy, what is the required retention period for supporting tax documentation?
    </div>
    
    <ul class="options">
        <li class="option">
            <input type="radio" id="q1a" name="question1">
            <label for="q1a">
                <span class="custom-radio"></span>
                3 years
            </label>
        </li>
        <!-- Additional options -->
    </ul>
</div>
```

#### 6. Company Colors
```css
:root {
    --primary: #003366;      /* Your company blue */
    --secondary: #0052CC;    /* Your secondary color */
    --accent: #FF6600;       /* Your accent color */
}
```

---

## 🏦 Example 3: Financial Advisory Firm Course

### Scenario
You're running an intensive course on Advanced Tax Strategies for your advisory team.

### Key Changes

#### 1. Branding (Logo Container)
```html
<div class="logo-container">
    <img src="firm-logo.svg" alt="Firm Logo" style="width: 80px; height: auto;">
</div>
```

#### 2. Welcome Page
```html
<h1>Advanced Tax Strategies Intensive</h1>
<p class="tagline">Expert Development Program for Advisors</p>
<p class="welcome-description">
    Enhance your expertise in sophisticated tax planning, estate strategies, and wealth optimization. This intensive program covers advanced techniques to elevate your advisory capabilities and client value delivery.
</p>
<button class="cta-button" onclick="alert('Ready to begin your intensive program?')">
    Begin Intensive Program
</button>
```

#### 3. Curriculum - Specialized Modules
```html
<div class="module-card">
    <div class="module-header">
        <div class="module-number">1</div>
        <div class="module-title">High-Net-Worth Planning</div>
    </div>
    <div class="module-body">
        <p class="module-description">
            Advanced strategies for ultra-high-net-worth clients including succession planning, charitable giving, and generational wealth transfer optimization.
        </p>
        <div class="module-meta">
            <span>📚 12 lessons</span>
            <span>⏱ 6 hours</span>
        </div>
        <a href="03-topic.html" class="module-link">Start Module</a>
    </div>
</div>
```

#### 4. Assessment with Firm-Specific Scenarios
```html
<div class="question-card">
    <div class="question-number">Question 1</div>
    <div class="question-text">
        Your client, a successful tech entrepreneur with $50M in concentrated stock, is concerned about tax efficiency and diversification. What is the most appropriate strategy to discuss?
    </div>
    
    <ul class="options">
        <li class="option">
            <input type="radio" id="q1a" name="question1">
            <label for="q1a">
                <span class="custom-radio"></span>
                Charitable Remainder Trust for tax-free diversification
            </label>
        </li>
        <li class="option">
            <input type="radio" id="q1b" name="question1">
            <label for="q1b">
                <span class="custom-radio"></span>
                Variable Prepaid Forward Contract for tax deferral
            </label>
        </li>
        <!-- More options -->
    </ul>
</div>
```

#### 5. Completion Page - Specialized Certificate
```html
<div class="certificate-notice">
    <strong>✓ Certificate of Completion Earned</strong>
    <p>You've completed the Advanced Tax Strategies Intensive. Share your achievement with your professional network. Access your certificate in your profile.</p>
</div>

<div class="next-steps">
    <h3>📚 Continue Your Development</h3>
    <ul class="steps-list">
        <li>Schedule a mentoring session with a senior advisor</li>
        <li>Review case studies of successful client implementations</li>
        <li>Attend the monthly advanced planning webinar series</li>
        <li>Access the exclusive advisor resource library</li>
    </ul>
</div>
```

---

## 🎨 Color Scheme Examples

### Professional Blue (Default)
```css
--primary: #003F87;
--secondary: #0066CC;
--accent: #FF6B35;
```

### Accounting Firm (Dark Green)
```css
--primary: #1B5E3F;
--secondary: #2E8B57;
--accent: #CD853F;
```

### Tech-Forward (Purple)
```css
--primary: #6F42C1;
--secondary: #7952B3;
--accent: #FF6B9D;
```

### Financial Services (Navy Gold)
```css
--primary: #0A1E3F;
--secondary: #142D5F;
--accent: #D4AF37;
```

### Government/Regulatory (Formal Gray)
```css
--primary: #333333;
--secondary: #666666;
--accent: #E74C3C;
```

---

## 🔄 Quick Find & Replace Guide

Use your editor's Find & Replace (Ctrl+H or Cmd+H) to make bulk changes:

### Global Content Updates
```
Find: "MojiTax"
Replace: "Your Organization Name"

Find: "tax"
Replace: "your topic"

Find: "tax professionals"
Replace: "your audience"

Find: "🦅"
Replace: "your emoji or logo"
```

### Global Color Updates
```
Find: "#003F87"
Replace: "your-primary-hex"

Find: "#0066CC"
Replace: "your-secondary-hex"

Find: "#FF6B35"
Replace: "your-accent-hex"
```

### Navigation Link Updates
```
Find: "03-topic.html"
Replace: "lessons/lesson-1.html"

Find: "04-content.html"
Replace: "courses/course-1/content.html"
```

---

## 📋 Content Customization Checklist

For each template, update:

- [ ] Page title (in `<title>` tag)
- [ ] Main heading (`<h1>`)
- [ ] Subheading/tagline (`<h2>`, `.tagline`)
- [ ] Description text (`<p>`)
- [ ] All button text and links
- [ ] Module/lesson names
- [ ] Learning objectives
- [ ] Example content
- [ ] Assessment questions and answers
- [ ] Completion message and next steps
- [ ] Logo/emoji representation
- [ ] Color scheme (CSS variables)

---

## 🚀 Deployment Checklist

Before going live with your customized templates:

- [ ] All content is accurate and proofread
- [ ] All links point to correct destinations
- [ ] Color palette is finalized and consistent
- [ ] Logo/branding is in place
- [ ] Mobile responsive on all templates
- [ ] Links work across all pages
- [ ] Assessment questions make sense
- [ ] Completion messages are appropriate
- [ ] Forms and buttons are functional
- [ ] Page load time is acceptable
- [ ] Browser compatibility tested
- [ ] Accessibility checked (keyboard navigation, color contrast)

---

## 💡 Pro Tips

1. **Start Small**: Customize one template completely, then use it as a template for others
2. **Consistent Branding**: Use the same colors, fonts, and logo across all templates
3. **Clear CTAs**: Make buttons and calls-to-action obvious and action-oriented
4. **Mobile First**: Always test mobile view as you customize
5. **Keep It Simple**: More content isn't always better; prioritize clarity
6. **Test Thoroughly**: Click every link and button before deployment
7. **Get Feedback**: Have colleagues review for accuracy and clarity
8. **Document Changes**: Keep notes on what you changed for future updates

---

These templates are designed for flexibility. Don't hesitate to experiment with different layouts, colors, and content structures to find what works best for your audience!
