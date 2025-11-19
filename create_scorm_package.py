#!/usr/bin/env python3
"""
Create SCORM 1.2 Package for ADIT Presentations
Compatible with LearnWorlds and other LMS platforms
"""

import os
import shutil
import zipfile
from pathlib import Path
from datetime import datetime


def create_scorm_manifest(output_dir):
    """Create imsmanifest.xml for SCORM 1.2"""

    manifest_content = '''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="ADIT_FundamentalTaxIssues_SCORM12" version="1.0"
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

    <organizations default="ADIT_ORG">
        <organization identifier="ADIT_ORG">
            <title>ADIT Fundamental Tax Issues</title>

            <!-- Chapter 1: International Income Flows -->
            <item identifier="chapter1" identifierref="chapter1_resource">
                <title>Chapter 1: International Income Flows</title>
            </item>

            <!-- Chapter 2: International Investment -->
            <item identifier="chapter2" identifierref="chapter2_resource">
                <title>Chapter 2: International Investment</title>
            </item>

            <!-- Chapter 3: Tax Treaties -->
            <item identifier="chapter3" identifierref="chapter3_resource">
                <title>Chapter 3: Tax Treaties</title>
            </item>

            <!-- Chapter 4: Transfer Pricing -->
            <item identifier="chapter4" identifierref="chapter4_resource">
                <title>Chapter 4: Transfer Pricing</title>
            </item>
        </organization>
    </organizations>

    <resources>
        <resource identifier="chapter1_resource" type="webcontent" adlcp:scormtype="sco" href="index.html?chapter=1">
            <file href="index.html"/>
            <file href="scorm-api.js"/>
        </resource>

        <resource identifier="chapter2_resource" type="webcontent" adlcp:scormtype="sco" href="index.html?chapter=2">
            <file href="index.html"/>
            <file href="scorm-api.js"/>
        </resource>

        <resource identifier="chapter3_resource" type="webcontent" adlcp:scormtype="sco" href="index.html?chapter=3">
            <file href="index.html"/>
            <file href="scorm-api.js"/>
        </resource>

        <resource identifier="chapter4_resource" type="webcontent" adlcp:scormtype="sco" href="index.html?chapter=4">
            <file href="index.html"/>
            <file href="scorm-api.js"/>
        </resource>
    </resources>
</manifest>'''

    manifest_file = output_dir / "imsmanifest.xml"
    with open(manifest_file, 'w', encoding='utf-8') as f:
        f.write(manifest_content)
    print(f"✓ Created: {manifest_file}")


def create_scorm_api_wrapper(output_dir):
    """Create SCORM API wrapper for LMS communication"""

    api_content = '''/**
 * SCORM 1.2 API Wrapper for ADIT Presentations
 */

var scormAPI = (function() {
    var API = null;
    var isInitialized = false;

    function findAPI(win) {
        var findAttempts = 0;
        var maxAttempts = 500;

        while ((win.API == null) && (win.parent != null) && (win.parent != win)) {
            findAttempts++;
            if (findAttempts > maxAttempts) {
                return null;
            }
            win = win.parent;
        }
        return win.API;
    }

    function initialize() {
        if (isInitialized) return true;
        API = findAPI(window);
        if (API != null) {
            var result = API.LMSInitialize("");
            if (result == "true") {
                isInitialized = true;
                console.log("SCORM API initialized");
                return true;
            }
        } else {
            console.warn("SCORM API not found");
            return false;
        }
        return false;
    }

    function setValue(element, value) {
        if (API != null && isInitialized) {
            return API.LMSSetValue(element, value);
        }
        return "false";
    }

    function getValue(element) {
        if (API != null && isInitialized) {
            return API.LMSGetValue(element);
        }
        return "";
    }

    function commit() {
        if (API != null && isInitialized) {
            return API.LMSCommit("");
        }
        return "false";
    }

    function setCompleted() {
        setValue("cmi.core.lesson_status", "completed");
        setValue("cmi.core.score.raw", "100");
        commit();
    }

    function setIncomplete() {
        setValue("cmi.core.lesson_status", "incomplete");
        commit();
    }

    function setProgress(percent) {
        setValue("cmi.core.score.raw", String(percent));
        commit();
    }

    function finish() {
        if (API != null && isInitialized) {
            API.LMSFinish("");
            isInitialized = false;
        }
    }

    return {
        initialize: initialize,
        setValue: setValue,
        getValue: getValue,
        commit: commit,
        setCompleted: setCompleted,
        setIncomplete: setIncomplete,
        setProgress: setProgress,
        finish: finish
    };
})();

window.addEventListener('load', function() {
    scormAPI.initialize();
    scormAPI.setIncomplete();
});

window.addEventListener('beforeunload', function() {
    scormAPI.finish();
});
'''

    api_file = output_dir / "scorm-api.js"
    with open(api_file, 'w', encoding='utf-8') as f:
        f.write(api_content)
    print(f"✓ Created: {api_file}")


def create_scorm_index(output_dir):
    """Create SCORM entry point"""

    index_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ADIT Fundamental Tax Issues</title>
    <script src="scorm-api.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
    </style>
</head>
<body>
    <script src="presentations/adit-embed.js"></script>
    <div class="adit-presentation"
         data-subject="fundamental-tax-issues"
         data-chapter="1"
         data-width="100%"
         data-height="100vh">
    </div>
    <script>
        const urlParams = new URLSearchParams(window.location.search);
        const chapter = urlParams.get('chapter') || '1';
        document.querySelector('.adit-presentation').setAttribute('data-chapter', chapter);
        if (window.initADITPresentations) {
            window.initADITPresentations();
        }
    </script>
</body>
</html>'''

    index_file = output_dir / "index.html"
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(index_content)
    print(f"✓ Created: {index_file}")


def create_scorm_package():
    """Create complete SCORM package"""

    print("\n📦 Creating SCORM 1.2 Package for LearnWorlds")
    print("=" * 70)

    from pathlib import Path
    presentations_dir = Path("generated_notes/01_Fundamental_tax_issues/presentations")
    scorm_dir = Path("scorm_package")

    if scorm_dir.exists():
        shutil.rmtree(scorm_dir)
    scorm_dir.mkdir()

    print("\n1. Creating SCORM files...")
    create_scorm_manifest(scorm_dir)
    create_scorm_api_wrapper(scorm_dir)
    create_scorm_index(scorm_dir)

    print("\n2. Copying presentations...")
    presentations_dest = scorm_dir / "presentations"
    shutil.copytree(presentations_dir, presentations_dest)
    print(f"✓ Copied presentations")

    print("\n3. Creating ZIP...")
    zip_file = Path("ADIT_FundamentalTaxIssues_SCORM12.zip")

    with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(scorm_dir):
            for file in files:
                file_path = Path(root) / file
                arcname = file_path.relative_to(scorm_dir)
                zipf.write(file_path, arcname)

    file_size_mb = zip_file.stat().st_size / (1024 * 1024)

    print(f"\n✅ SCORM package created!")
    print(f"   File: {zip_file}")
    print(f"   Size: {file_size_mb:.1f} MB")
    print(f"\n📤 Upload to LearnWorlds:")
    print(f"   1. Course Builder → Add Learning Activity")
    print(f"   2. Select 'SCORM/HTML5 Package'")
    print(f"   3. Upload: {zip_file.absolute()}")
    print()


if __name__ == "__main__":
    create_scorm_package()
