/**
 * ADIT Presentation Embed Script
 * Similar to Visme's embed functionality
 *
 * Usage:
 * <script src="https://judelaw007.github.io/ADITER/adit-embed.js"></script>
 * <div class="adit-presentation"
 *      data-url="presentation_output/presentation.html"
 *      data-width="100%"
 *      data-height="600px"
 *      data-border="rounded">
 * </div>
 */

(function() {
    'use strict';

    // Configuration
    const BASE_URL = 'https://judelaw007.github.io/ADITER/';

    // Initialize on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    function init() {
        // Find all ADIT presentation containers
        const containers = document.querySelectorAll('.adit-presentation, .adit-embed');

        containers.forEach(container => {
            embedPresentation(container);
        });
    }

    function embedPresentation(container) {
        // Get configuration from data attributes
        const config = {
            url: container.getAttribute('data-url') || 'presentation_output/presentation.html',
            width: container.getAttribute('data-width') || '100%',
            height: container.getAttribute('data-height') || '600px',
            border: container.getAttribute('data-border') || 'none',
            fullscreen: container.getAttribute('data-fullscreen') !== 'false',
            autoplay: container.getAttribute('data-autoplay') !== 'false',
            loading: container.getAttribute('data-loading') || 'lazy',
            title: container.getAttribute('data-title') || 'ADIT Presentation'
        };

        // Build full URL
        const fullUrl = config.url.startsWith('http') ?
            config.url :
            BASE_URL + config.url;

        // Create wrapper for responsive sizing
        const wrapper = document.createElement('div');
        wrapper.className = 'adit-embed-wrapper';
        wrapper.style.cssText = `
            position: relative;
            width: ${config.width};
            height: ${config.height};
            margin: 0 auto;
        `;

        // Apply border styling
        let borderStyle = '';
        switch(config.border) {
            case 'simple':
                borderStyle = 'border: 1px solid #ddd;';
                break;
            case 'rounded':
                borderStyle = 'border: 2px solid #667eea; border-radius: 10px; overflow: hidden;';
                break;
            case 'shadow':
                borderStyle = 'box-shadow: 0 10px 40px rgba(0,0,0,0.1); border-radius: 10px; overflow: hidden;';
                break;
            case 'visme':
                borderStyle = 'border: 2px solid #667eea; border-radius: 15px; overflow: hidden; box-shadow: 0 4px 20px rgba(102, 126, 234, 0.2);';
                break;
        }

        wrapper.style.cssText += borderStyle;

        // Create loading indicator
        const loader = document.createElement('div');
        loader.className = 'adit-loader';
        loader.innerHTML = `
            <div style="
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                text-align: center;
                color: #667eea;
                font-family: 'Segoe UI', sans-serif;
            ">
                <div style="
                    width: 50px;
                    height: 50px;
                    border: 4px solid #f3f3f3;
                    border-top: 4px solid #667eea;
                    border-radius: 50%;
                    animation: adit-spin 1s linear infinite;
                    margin: 0 auto 15px;
                "></div>
                <div>Loading presentation...</div>
            </div>
        `;

        // Add spinner animation
        if (!document.getElementById('adit-embed-styles')) {
            const style = document.createElement('style');
            style.id = 'adit-embed-styles';
            style.textContent = `
                @keyframes adit-spin {
                    0% { transform: rotate(0deg); }
                    100% { transform: rotate(360deg); }
                }

                .adit-embed-wrapper {
                    transition: all 0.3s ease;
                }

                .adit-embed-wrapper:hover {
                    transform: translateY(-2px);
                }

                .adit-fullscreen-btn {
                    position: absolute;
                    top: 10px;
                    right: 10px;
                    background: rgba(255,255,255,0.9);
                    border: none;
                    padding: 8px 12px;
                    border-radius: 5px;
                    cursor: pointer;
                    z-index: 1000;
                    font-size: 14px;
                    transition: all 0.3s;
                }

                .adit-fullscreen-btn:hover {
                    background: white;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
                }
            `;
            document.head.appendChild(style);
        }

        wrapper.appendChild(loader);

        // Create iframe
        const iframe = document.createElement('iframe');
        iframe.src = fullUrl;
        iframe.title = config.title;
        iframe.style.cssText = `
            width: 100%;
            height: 100%;
            border: none;
            display: none;
        `;

        if (config.fullscreen) {
            iframe.setAttribute('allowfullscreen', '');
        }

        if (config.autoplay) {
            iframe.setAttribute('allow', 'autoplay');
        }

        if (config.loading) {
            iframe.setAttribute('loading', config.loading);
        }

        // Handle iframe load
        iframe.addEventListener('load', function() {
            loader.style.display = 'none';
            iframe.style.display = 'block';
        });

        wrapper.appendChild(iframe);

        // Add fullscreen button if enabled
        if (config.fullscreen) {
            const fullscreenBtn = document.createElement('button');
            fullscreenBtn.className = 'adit-fullscreen-btn';
            fullscreenBtn.innerHTML = '⛶ Fullscreen';
            fullscreenBtn.onclick = function() {
                if (wrapper.requestFullscreen) {
                    wrapper.requestFullscreen();
                } else if (wrapper.webkitRequestFullscreen) {
                    wrapper.webkitRequestFullscreen();
                } else if (wrapper.msRequestFullscreen) {
                    wrapper.msRequestFullscreen();
                }
            };
            wrapper.appendChild(fullscreenBtn);
        }

        // Replace container content with embed
        container.innerHTML = '';
        container.appendChild(wrapper);

        // Add responsive handling for mobile
        handleResponsive(wrapper, config);
    }

    function handleResponsive(wrapper, config) {
        function adjustSize() {
            const containerWidth = wrapper.parentElement.offsetWidth;

            // If width is percentage, make it responsive
            if (config.width.includes('%')) {
                // Adjust height proportionally if needed
                if (containerWidth < 768) { // Mobile
                    wrapper.style.height = Math.min(500, containerWidth * 0.75) + 'px';
                }
            }
        }

        // Initial adjustment
        adjustSize();

        // Adjust on window resize
        window.addEventListener('resize', adjustSize);
    }

    // Expose global function for programmatic embedding
    window.ADITEmbed = {
        embed: function(selector, options) {
            const container = document.querySelector(selector);
            if (container) {
                // Set data attributes from options
                Object.keys(options).forEach(key => {
                    container.setAttribute('data-' + key, options[key]);
                });
                embedPresentation(container);
            }
        }
    };

})();
