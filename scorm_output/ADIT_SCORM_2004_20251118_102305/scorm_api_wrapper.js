/**
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
