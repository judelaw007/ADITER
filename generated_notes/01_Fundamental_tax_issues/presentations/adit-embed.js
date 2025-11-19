/**
 * ADIT Presentation Embed System
 * Visme-style embeddable presentations with TTS audio
 * Version 1.0
 */

(function() {
    'use strict';

    // Configuration
    const ADIT_CONFIG = {
        baseURL: './presentations/', // Relative path to presentations folder
        version: '1.0.0'
    };

    // Presentation data structure
    const PRESENTATIONS = {
        'fundamental-tax-issues': {
            title: 'Fundamental Tax Issues',
            chapters: {
                1: {
                    title: 'International Income Flows',
                    slug: 'income-flows-tax-considerations-in-energy-resource',
                    sections: 6
                },
                2: {
                    title: 'International Investment',
                    slug: 'investment-tax-considerations-in-energy-resources',
                    sections: 5
                },
                3: {
                    title: 'Tax Treaties',
                    slug: 'treaties-in-energy-resources',
                    sections: 6
                },
                4: {
                    title: 'Transfer Pricing',
                    slug: 'pricing-in-energy-resources',
                    sections: 6
                }
            }
        }
    };

    class ADITPresentationPlayer {
        constructor(container, options) {
            this.container = container;
            this.options = options;
            this.currentSlide = 0;
            this.audio = null;
            this.slides = [];

            this.init();
        }

        init() {
            this.container.classList.add('adit-player-initialized');
            this.createPlayer();
            this.loadPresentation();
        }

        createPlayer() {
            const width = this.options.width || '100%';
            const height = this.options.height || '768px';

            const playerHTML = `
                <div class="adit-presentation-player" style="width: ${width}; max-width: 100%; margin: 0 auto; position: relative; background: #1a1a2e; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 40px rgba(0,0,0,0.3);">
                    <!-- Header -->
                    <div class="adit-header" style="background: linear-gradient(135deg, #003F87 0%, #0066CC 100%); padding: 1rem 2rem; display: flex; justify-content: space-between; align-items: center;">
                        <div class="adit-title" style="color: white; font-size: 1.2rem; font-weight: bold;">
                            <span class="subject-title"></span>
                        </div>
                        <div class="adit-controls" style="display: flex; gap: 1rem;">
                            <button class="adit-btn adit-fullscreen" style="background: rgba(255,255,255,0.2); border: none; color: white; padding: 0.5rem 1rem; border-radius: 6px; cursor: pointer; font-weight: bold;">
                                ⛶ Fullscreen
                            </button>
                        </div>
                    </div>

                    <!-- Slide Container -->
                    <div class="adit-slide-container" style="height: ${height}; background: white; position: relative; overflow: hidden;">
                        <iframe class="adit-slide-frame" style="width: 100%; height: 100%; border: none;" frameborder="0"></iframe>
                    </div>

                    <!-- Navigation -->
                    <div class="adit-navigation" style="background: #16213e; padding: 1rem 2rem; display: flex; justify-content: space-between; align-items: center;">
                        <button class="adit-btn adit-prev" style="background: #0066CC; border: none; color: white; padding: 0.75rem 1.5rem; border-radius: 6px; cursor: pointer; font-weight: bold;" disabled>
                            ← Previous
                        </button>

                        <div class="adit-progress" style="flex: 1; margin: 0 2rem;">
                            <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                                <span class="adit-slide-info" style="color: white; font-size: 0.9rem;"></span>
                                <span class="adit-chapter-info" style="color: rgba(255,255,255,0.7); font-size: 0.9rem;"></span>
                            </div>
                            <div style="background: rgba(255,255,255,0.2); height: 6px; border-radius: 3px; overflow: hidden;">
                                <div class="adit-progress-bar" style="background: #FF6B35; height: 100%; width: 0%; transition: width 0.3s;"></div>
                            </div>
                        </div>

                        <button class="adit-btn adit-next" style="background: #FF6B35; border: none; color: white; padding: 0.75rem 1.5rem; border-radius: 6px; cursor: pointer; font-weight: bold;">
                            Next →
                        </button>
                    </div>

                    <!-- Loading Indicator -->
                    <div class="adit-loading" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; font-size: 1.2rem; display: none;">
                        <div style="text-align: center;">
                            <div style="border: 4px solid rgba(255,255,255,0.3); border-top: 4px solid white; border-radius: 50%; width: 40px; height: 40px; animation: spin 1s linear infinite; margin: 0 auto 1rem;"></div>
                            Loading presentation...
                        </div>
                    </div>
                </div>

                <style>
                    @keyframes spin {
                        0% { transform: rotate(0deg); }
                        100% { transform: rotate(360deg); }
                    }
                    .adit-btn:hover {
                        opacity: 0.9;
                        transform: translateY(-1px);
                    }
                    .adit-btn:active {
                        transform: translateY(0);
                    }
                    .adit-btn:disabled {
                        opacity: 0.5;
                        cursor: not-allowed;
                    }
                </style>
            `;

            this.container.innerHTML = playerHTML;
            this.attachEventListeners();
        }

        attachEventListeners() {
            const prevBtn = this.container.querySelector('.adit-prev');
            const nextBtn = this.container.querySelector('.adit-next');
            const fullscreenBtn = this.container.querySelector('.adit-fullscreen');

            prevBtn.addEventListener('click', () => this.previousSlide());
            nextBtn.addEventListener('click', () => this.nextSlide());
            fullscreenBtn.addEventListener('click', () => this.toggleFullscreen());

            // Keyboard navigation
            document.addEventListener('keydown', (e) => {
                if (e.key === 'ArrowLeft') this.previousSlide();
                if (e.key === 'ArrowRight') this.nextSlide();
                if (e.key === 'f' || e.key === 'F') this.toggleFullscreen();
            });
        }

        loadPresentation() {
            const subject = this.options.subject || 'fundamental-tax-issues';
            const chapter = parseInt(this.options.chapter) || 1;
            const startSection = parseInt(this.options.section) || 1;

            const presentation = PRESENTATIONS[subject];
            if (!presentation) {
                this.showError('Presentation not found');
                return;
            }

            const chapterData = presentation.chapters[chapter];
            if (!chapterData) {
                this.showError('Chapter not found');
                return;
            }

            // Build slide list
            this.slides = [];

            // Add topic page
            this.slides.push({
                type: 'topic',
                url: `${String(chapter).padStart(2, '0')}-${chapterData.slug}-topic.html`,
                title: `${chapterData.title} - Topic`,
                chapter: chapter
            });

            // Add content pages
            for (let i = 1; i <= chapterData.sections; i++) {
                this.slides.push({
                    type: 'content',
                    url: `${String(chapter).padStart(2, '0')}-${chapterData.slug}-${i}-content.html`,
                    title: `${chapterData.title} - Section ${i}`,
                    chapter: chapter,
                    section: i
                });
            }

            // Add assessment
            this.slides.push({
                type: 'assessment',
                url: `${String(chapter).padStart(2, '0')}-${chapterData.slug}-assessment.html`,
                title: `${chapterData.title} - Assessment`,
                chapter: chapter
            });

            // Add completion
            this.slides.push({
                type: 'completion',
                url: `${String(chapter).padStart(2, '0')}-${chapterData.slug}-completion.html`,
                title: `${chapterData.title} - Completion`,
                chapter: chapter
            });

            // Set subject title
            this.container.querySelector('.subject-title').textContent =
                `${presentation.title} - Chapter ${chapter}: ${chapterData.title}`;

            // Load first slide (or specified section)
            const slideIndex = startSection > 0 ? startSection : 0;
            this.loadSlide(slideIndex);
        }

        loadSlide(index) {
            if (index < 0 || index >= this.slides.length) return;

            this.currentSlide = index;
            const slide = this.slides[index];

            // Show loading
            this.showLoading(true);

            // Load slide in iframe
            const iframe = this.container.querySelector('.adit-slide-frame');
            const slideURL = ADIT_CONFIG.baseURL + slide.url;

            iframe.onload = () => {
                this.showLoading(false);
                this.updateUI();
            };

            iframe.src = slideURL;
        }

        updateUI() {
            const slide = this.slides[this.currentSlide];

            // Update progress
            const progress = ((this.currentSlide + 1) / this.slides.length) * 100;
            this.container.querySelector('.adit-progress-bar').style.width = `${progress}%`;

            // Update slide info
            this.container.querySelector('.adit-slide-info').textContent =
                `Slide ${this.currentSlide + 1} of ${this.slides.length}`;

            this.container.querySelector('.adit-chapter-info').textContent = slide.title;

            // Update button states
            const prevBtn = this.container.querySelector('.adit-prev');
            const nextBtn = this.container.querySelector('.adit-next');

            prevBtn.disabled = this.currentSlide === 0;
            nextBtn.disabled = this.currentSlide === this.slides.length - 1;

            if (this.currentSlide === this.slides.length - 1) {
                nextBtn.textContent = '✓ Complete';
            } else {
                nextBtn.textContent = 'Next →';
            }
        }

        previousSlide() {
            if (this.currentSlide > 0) {
                this.loadSlide(this.currentSlide - 1);
            }
        }

        nextSlide() {
            if (this.currentSlide < this.slides.length - 1) {
                this.loadSlide(this.currentSlide + 1);
            }
        }

        toggleFullscreen() {
            const player = this.container.querySelector('.adit-presentation-player');

            if (!document.fullscreenElement) {
                player.requestFullscreen().catch(err => {
                    console.error('Fullscreen error:', err);
                });
            } else {
                document.exitFullscreen();
            }
        }

        showLoading(show) {
            const loading = this.container.querySelector('.adit-loading');
            loading.style.display = show ? 'block' : 'none';
        }

        showError(message) {
            this.container.innerHTML = `
                <div style="padding: 2rem; text-align: center; color: #ff4444;">
                    <h2>Error Loading Presentation</h2>
                    <p>${message}</p>
                </div>
            `;
        }
    }

    // Auto-initialize presentations on page load
    function initADITPresentations() {
        const containers = document.querySelectorAll('.adit-presentation:not(.adit-player-initialized)');

        containers.forEach(container => {
            const options = {
                subject: container.dataset.subject || 'fundamental-tax-issues',
                chapter: container.dataset.chapter || '1',
                section: container.dataset.section || '0',
                width: container.dataset.width || '100%',
                height: container.dataset.height || '768px',
                autoplay: container.dataset.autoplay === 'true'
            };

            new ADITPresentationPlayer(container, options);
        });
    }

    // Initialize on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initADITPresentations);
    } else {
        initADITPresentations();
    }

    // Export for manual initialization
    window.ADITPresentationPlayer = ADITPresentationPlayer;
    window.initADITPresentations = initADITPresentations;

})();
