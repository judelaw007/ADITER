#!/usr/bin/env python3
"""
Convert ADIT Presentations to SCORM Package
Creates SCORM 1.2 and SCORM 2004 compatible packages for LMS
"""

import os
import shutil
import zipfile
from pathlib import Path
from datetime import datetime
import xml.etree.ElementTree as ET


class SCORMPackager:
    """Convert HTML5 presentations to SCORM packages"""

    def __init__(self, presentation_dir: str = "presentation_output"):
        self.presentation_dir = Path(presentation_dir)
        self.scorm_dir = Path("scorm_output")
        self.scorm_dir.mkdir(exist_ok=True)

    def create_scorm_12_manifest(self, title: str, identifier: str) -> str:
        """Create SCORM 1.2 imsmanifest.xml"""

        manifest = f'''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="{identifier}" version="1.0"
    xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2"
    xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.imsproject.org/xsd/imscp_rootv1p1p2 imscp_rootv1p1p2.xsd
                        http://www.imsglobal.org/xsd/imsmd_rootv1p2p1 imsmd_rootv1p2p1.xsd
                        http://www.adlnet.org/xsd/adlcp_rootv1p2 adlcp_rootv1p2.xsd">

    <metadata>
        <schema>ADL SCORM</schema>
        <schemaversion>1.2</schemaversion>
    </metadata>

    <organizations default="ORG-{identifier}">
        <organization identifier="ORG-{identifier}">
            <title>{title}</title>
            <item identifier="ITEM-{identifier}" identifierref="RES-{identifier}">
                <title>{title}</title>
                <adlcp:masteryscore>80</adlcp:masteryscore>
            </item>
        </organization>
    </organizations>

    <resources>
        <resource identifier="RES-{identifier}" type="webcontent" adlcp:scormtype="sco" href="presentation.html">
            <file href="presentation.html"/>
            <file href="scorm_api_wrapper.js"/>
            <!-- Audio files -->
            <file href="audio/slide_000.mp3"/>
            <file href="audio/slide_001.mp3"/>
            <file href="audio/slide_002.mp3"/>
            <file href="audio/slide_003.mp3"/>
            <file href="audio/slide_004.mp3"/>
            <file href="audio/slide_005.mp3"/>
            <file href="audio/slide_006.mp3"/>
            <file href="audio/slide_007.mp3"/>
        </resource>
    </resources>
</manifest>'''
        return manifest

    def create_scorm_2004_manifest(self, title: str, identifier: str) -> str:
        """Create SCORM 2004 (4th Edition) imsmanifest.xml"""

        manifest = f'''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="{identifier}" version="1.0"
    xmlns="http://www.imsglobal.org/xsd/imscp_v1p1"
    xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_v1p3"
    xmlns:adlseq="http://www.adlnet.org/xsd/adlseq_v1p3"
    xmlns:adlnav="http://www.adlnet.org/xsd/adlnav_v1p3"
    xmlns:imsss="http://www.imsglobal.org/xsd/imsss"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.imsglobal.org/xsd/imscp_v1p1 imscp_v1p1.xsd
                        http://www.adlnet.org/xsd/adlcp_v1p3 adlcp_v1p3.xsd
                        http://www.adlnet.org/xsd/adlseq_v1p3 adlseq_v1p3.xsd
                        http://www.adlnet.org/xsd/adlnav_v1p3 adlnav_v1p3.xsd
                        http://www.imsglobal.org/xsd/imsss imsss_v1p0.xsd">

    <metadata>
        <schema>ADL SCORM</schema>
        <schemaversion>2004 4th Edition</schemaversion>
    </metadata>

    <organizations default="ORG-{identifier}">
        <organization identifier="ORG-{identifier}">
            <title>{title}</title>
            <item identifier="ITEM-{identifier}" identifierref="RES-{identifier}">
                <title>{title}</title>
            </item>
        </organization>
    </organizations>

    <resources>
        <resource identifier="RES-{identifier}" type="webcontent" adlcp:scormType="sco" href="presentation.html">
            <file href="presentation.html"/>
            <file href="scorm_api_wrapper.js"/>
            <!-- Audio files -->
            <file href="audio/slide_000.mp3"/>
            <file href="audio/slide_001.mp3"/>
            <file href="audio/slide_002.mp3"/>
            <file href="audio/slide_003.mp3"/>
            <file href="audio/slide_004.mp3"/>
            <file href="audio/slide_005.mp3"/>
            <file href="audio/slide_006.mp3"/>
            <file href="audio/slide_007.mp3"/>
        </resource>
    </resources>
</manifest>'''
        return manifest

    def create_scorm_api_wrapper(self) -> str:
        """Create SCORM API JavaScript wrapper for LMS communication"""

        wrapper = '''/**
 * SCORM API Wrapper
 * Handles communication with LMS (Learning Management System)
 */

var SCORM_API = (function() {
    var API = null;
    var isInitialized = false;

    // Find SCORM API
    function findAPI(win) {
        var attempts = 0;
        var maxAttempts = 500;

        while ((win.API == null || win.API_1484_11 == null) && win.parent != null && win.parent != win && attempts < maxAttempts) {
            attempts++;
            win = win.parent;
        }

        // SCORM 1.2
        if (win.API != null) {
            return win.API;
        }
        // SCORM 2004
        if (win.API_1484_11 != null) {
            return win.API_1484_11;
        }

        return null;
    }

    // Initialize SCORM
    function initialize() {
        if (isInitialized) return true;

        API = findAPI(window);

        if (API == null) {
            console.log('SCORM API not found - running in standalone mode');
            return false;
        }

        var result = API.LMSInitialize ? API.LMSInitialize("") : API.Initialize("");

        if (result == "true" || result == true) {
            isInitialized = true;
            console.log('SCORM API initialized successfully');

            // Set initial status
            setValue('cmi.core.lesson_status', 'incomplete');
            setValue('cmi.core.score.min', '0');
            setValue('cmi.core.score.max', '100');

            return true;
        }

        return false;
    }

    // Set value in LMS
    function setValue(key, value) {
        if (!API) return false;

        var result = API.LMSSetValue ? API.LMSSetValue(key, value) : API.SetValue(key, value);
        return result == "true" || result == true;
    }

    // Get value from LMS
    function getValue(key) {
        if (!API) return "";

        return API.LMSGetValue ? API.LMSGetValue(key) : API.GetValue(key);
    }

    // Commit data to LMS
    function commit() {
        if (!API) return false;

        var result = API.LMSCommit ? API.LMSCommit("") : API.Commit("");
        return result == "true" || result == true;
    }

    // Finish/terminate SCORM session
    function finish() {
        if (!API || !isInitialized) return false;

        var result = API.LMSFinish ? API.LMSFinish("") : API.Terminate("");

        if (result == "true" || result == true) {
            isInitialized = false;
            console.log('SCORM session terminated');
            return true;
        }

        return false;
    }

    // Set completion status
    function setCompleted() {
        setValue('cmi.core.lesson_status', 'completed');
        commit();
    }

    // Set score
    function setScore(score) {
        setValue('cmi.core.score.raw', score.toString());
        commit();
    }

    // Track slide view
    function trackSlideView(slideNumber, totalSlides) {
        var progress = Math.round((slideNumber / totalSlides) * 100);
        setValue('cmi.core.lesson_location', slideNumber.toString());
        setValue('cmi.core.score.raw', progress.toString());
        commit();

        // Mark as completed if viewed all slides
        if (slideNumber >= totalSlides) {
            setCompleted();
        }
    }

    // Public API
    return {
        initialize: initialize,
        setValue: setValue,
        getValue: getValue,
        commit: commit,
        finish: finish,
        setCompleted: setCompleted,
        setScore: setScore,
        trackSlideView: trackSlideView,
        isAvailable: function() { return API != null; }
    };
})();

// Auto-initialize on page load
window.addEventListener('load', function() {
    SCORM_API.initialize();
});

// Auto-finish on page unload
window.addEventListener('beforeunload', function() {
    SCORM_API.finish();
});
'''
        return wrapper

    def inject_scorm_tracking(self, html_content: str) -> str:
        """Inject SCORM tracking into presentation HTML"""

        # Add SCORM script reference
        scorm_script = '<script src="scorm_api_wrapper.js"></script>'
        html_content = html_content.replace('</head>', f'{scorm_script}\n</head>')

        # Add SCORM tracking to navigation
        tracking_code = '''
        // SCORM Tracking
        if (typeof SCORM_API !== 'undefined' && SCORM_API.isAvailable()) {
            console.log('SCORM tracking enabled');

            // Track slide views
            const originalShowSlide = showSlide;
            showSlide = function(index) {
                originalShowSlide(index);
                SCORM_API.trackSlideView(index + 1, totalSlides);
            };
        }
        '''

        # Inject before closing script tag
        html_content = html_content.replace('// Initialize\n        showSlide(0);',
                                           '// Initialize\n        showSlide(0);\n' + tracking_code)

        return html_content

    def create_scorm_package(self, title: str, version: str = "1.2") -> str:
        """Create complete SCORM package"""

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        identifier = f"ADIT_{timestamp}"
        package_name = f"ADIT_SCORM_{version.replace('.', '_')}_{timestamp}"
        package_dir = self.scorm_dir / package_name

        # Create package directory
        package_dir.mkdir(exist_ok=True)

        print(f"\n{'='*60}")
        print(f"Creating SCORM {version} Package")
        print(f"{'='*60}\n")

        # Step 1: Copy presentation files
        print("Step 1: Copying presentation files...")

        # Copy presentation.html
        presentation_file = self.presentation_dir / "presentation.html"
        if presentation_file.exists():
            with open(presentation_file, 'r', encoding='utf-8') as f:
                html_content = f.read()

            # Inject SCORM tracking
            html_content = self.inject_scorm_tracking(html_content)

            with open(package_dir / "presentation.html", 'w', encoding='utf-8') as f:
                f.write(html_content)
            print("  ✓ Presentation HTML copied and enhanced")
        else:
            print("  ✗ Presentation file not found!")
            return None

        # Copy audio files
        audio_dir = self.presentation_dir / "audio"
        if audio_dir.exists():
            package_audio_dir = package_dir / "audio"
            package_audio_dir.mkdir(exist_ok=True)

            audio_count = 0
            for audio_file in audio_dir.glob("*.mp3"):
                shutil.copy2(audio_file, package_audio_dir / audio_file.name)
                audio_count += 1

            print(f"  ✓ {audio_count} audio files copied")

        # Step 2: Create SCORM files
        print("\nStep 2: Creating SCORM files...")

        # Create manifest
        if version == "1.2":
            manifest_content = self.create_scorm_12_manifest(title, identifier)
        else:  # SCORM 2004
            manifest_content = self.create_scorm_2004_manifest(title, identifier)

        with open(package_dir / "imsmanifest.xml", 'w', encoding='utf-8') as f:
            f.write(manifest_content)
        print(f"  ✓ imsmanifest.xml created (SCORM {version})")

        # Create SCORM API wrapper
        wrapper_content = self.create_scorm_api_wrapper()
        with open(package_dir / "scorm_api_wrapper.js", 'w', encoding='utf-8') as f:
            f.write(wrapper_content)
        print("  ✓ SCORM API wrapper created")

        # Step 3: Create ZIP package
        print("\nStep 3: Creating ZIP package...")

        zip_file = self.scorm_dir / f"{package_name}.zip"
        with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(package_dir):
                for file in files:
                    file_path = Path(root) / file
                    arcname = file_path.relative_to(package_dir)
                    zipf.write(file_path, arcname)

        print(f"  ✓ ZIP package created")

        # Calculate sizes
        zip_size = os.path.getsize(zip_file) / (1024 * 1024)  # MB

        print(f"\n{'='*60}")
        print(f"✅ SCORM {version} Package Created!")
        print(f"{'='*60}")
        print(f"\nPackage: {zip_file}")
        print(f"Size: {zip_size:.2f} MB")
        print(f"\nContents:")
        print(f"  - imsmanifest.xml (SCORM {version} manifest)")
        print(f"  - presentation.html (your presentation with SCORM tracking)")
        print(f"  - scorm_api_wrapper.js (LMS communication)")
        print(f"  - audio/ folder ({audio_count} MP3 files)")
        print(f"\nUpload to LMS:")
        print(f"  - Moodle, Blackboard, Canvas, Totara, etc.")
        print(f"  - Look for 'Upload SCORM package' or 'Add activity'")
        print(f"  - Select the ZIP file")
        print(f"\nFeatures:")
        print(f"  ✓ Tracks slide progress")
        print(f"  ✓ Records completion status")
        print(f"  ✓ Saves last viewed slide")
        print(f"  ✓ Reports score based on progress")
        print(f"  ✓ Full voice narration preserved")
        print(f"  ✓ Interactive navigation works")

        return str(zip_file)

    def create_both_versions(self, title: str):
        """Create both SCORM 1.2 and SCORM 2004 packages"""

        print(f"\n{'='*70}")
        print(f"SCORM Package Creator")
        print(f"{'='*70}")
        print(f"\nTitle: {title}")
        print(f"Creating both SCORM 1.2 and SCORM 2004 packages...")

        # Create SCORM 1.2
        scorm_12 = self.create_scorm_package(title, "1.2")

        # Create SCORM 2004
        scorm_2004 = self.create_scorm_package(title, "2004")

        print(f"\n{'='*70}")
        print(f"✅ Both SCORM Packages Created!")
        print(f"{'='*70}")
        print(f"\nSCORM 1.2: {scorm_12}")
        print(f"SCORM 2004: {scorm_2004}")
        print(f"\nUse SCORM 1.2 for:")
        print(f"  - Older LMS systems")
        print(f"  - Maximum compatibility")
        print(f"\nUse SCORM 2004 for:")
        print(f"  - Modern LMS systems")
        print(f"  - Advanced tracking features")
        print(f"  - Better sequencing control")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Convert presentation to SCORM package')
    parser.add_argument('--title', default='ADIT Tax Presentation',
                       help='Presentation title for SCORM manifest')
    parser.add_argument('--version', choices=['1.2', '2004', 'both'], default='both',
                       help='SCORM version to create')
    parser.add_argument('--presentation-dir', default='presentation_output',
                       help='Directory containing presentation files')

    args = parser.parse_args()

    packager = SCORMPackager(args.presentation_dir)

    if args.version == 'both':
        packager.create_both_versions(args.title)
    else:
        packager.create_scorm_package(args.title, args.version)

    print(f"\n{'='*70}")
    print("Ready to upload to your LMS!")
    print(f"{'='*70}\n")
