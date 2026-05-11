// ===============================================
// TALENTSYNC PRODUCTION MAIN JS
// ===============================================

console.log("TalentSync Loaded");


// ===============================================
// DOM READY
// ===============================================

document.addEventListener(
    'DOMContentLoaded',
    function () {

        initializeAlerts();

        initializeDarkMode();

        initializeSearch();

        initializeResumeValidation();

        initializeProfilePreview();

        initializePasswordToggle();

        initializeFormLoading();

        initializeCounters();

        initializeScrollTop();

        initializeScrollAnimations();

        initializeNavbarEffects();

        initializeActiveLinks();

        initializeTooltips();

    }
);


// ===============================================
// AUTO CLOSE ALERTS
// ===============================================

function initializeAlerts() {

    const alerts =
        document.querySelectorAll(
            '.alert'
        );

    if (!alerts.length) return;

    setTimeout(() => {

        alerts.forEach(alert => {

            alert.style.transition =
                '0.4s ease';

            alert.style.opacity = '0';

            alert.style.transform =
                'translateY(-10px)';

            setTimeout(() => {

                alert.remove();

            }, 400);

        });

    }, 3000);

}


// ===============================================
// DARK MODE
// ===============================================

function initializeDarkMode() {

    const darkModeToggle =
        document.getElementById(
            'darkModeToggle'
        );

    if (
        localStorage.getItem(
            'darkMode'
        ) === 'enabled'
    ) {

        document.body.classList.add(
            'dark-mode'
        );

        if (darkModeToggle) {

            darkModeToggle.innerHTML =
                '☀️';
        }
    }

    if (darkModeToggle) {

        darkModeToggle.addEventListener(
            'click',
            () => {

                document.body.classList.toggle(
                    'dark-mode'
                );

                if (
                    document.body.classList.contains(
                        'dark-mode'
                    )
                ) {

                    localStorage.setItem(
                        'darkMode',
                        'enabled'
                    );

                    darkModeToggle.innerHTML =
                        '☀️';

                } else {

                    localStorage.setItem(
                        'darkMode',
                        'disabled'
                    );

                    darkModeToggle.innerHTML =
                        '🌙';
                }

            }
        );

    }

}


// ===============================================
// JOB SEARCH
// ===============================================

function initializeSearch() {

    const searchInput =
        document.querySelector(
            '#searchInput'
        );

    if (!searchInput) return;

    searchInput.addEventListener(
        'keyup',
        () => {

            const filter =
                searchInput.value.toLowerCase();

            const cards =
                document.querySelectorAll(
                    '.job-card'
                );

            cards.forEach(card => {

                const text =
                    card.innerText.toLowerCase();

                card.style.display =
                    text.includes(filter)
                    ? 'block'
                    : 'none';

            });

        }
    );

}


// ===============================================
// RESUME VALIDATION
// ===============================================

function initializeResumeValidation() {

    const resumeInput =
        document.querySelector(
            'input[name="resume"]'
        );

    if (!resumeInput) return;

    resumeInput.addEventListener(
        'change',
        function () {

            const file = this.files[0];

            if (!file) return;

            const allowedTypes = [

                'application/pdf',

                'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            ];

            if (
                !allowedTypes.includes(
                    file.type
                )
            ) {

                alert(
                    'Only PDF and DOCX files allowed.'
                );

                this.value = '';

                return;
            }

            if (
                file.size >
                5 * 1024 * 1024
            ) {

                alert(
                    'Resume must be under 5MB.'
                );

                this.value = '';
            }

        }
    );

}


// ===============================================
// PROFILE IMAGE PREVIEW
// ===============================================

function initializeProfilePreview() {

    const imageInput =
        document.querySelector(
            'input[name="profile_pic"]'
        );

    if (!imageInput) return;

    imageInput.addEventListener(
        'change',
        function () {

            const file = this.files[0];

            if (!file) return;

            const allowedTypes = [

                'image/jpeg',

                'image/jpg',

                'image/png',

                'image/webp'
            ];

            if (
                !allowedTypes.includes(
                    file.type
                )
            ) {

                alert(
                    'Only JPG, PNG and WEBP allowed.'
                );

                this.value = '';

                return;
            }

            if (
                file.size >
                5 * 1024 * 1024
            ) {

                alert(
                    'Image must be under 5MB.'
                );

                this.value = '';

                return;
            }

            const reader =
                new FileReader();

            reader.onload = function (e) {

                const preview =
                    document.querySelector(
                        '#profilePreview'
                    );

                if (preview) {

                    preview.src =
                        e.target.result;
                }

            };

            reader.readAsDataURL(file);

        }
    );

}


// ===============================================
// PASSWORD TOGGLE
// ===============================================

function initializePasswordToggle() {

    const passwordFields =
        document.querySelectorAll(
            'input[type="password"]'
        );

    passwordFields.forEach(field => {

        if (
            field.dataset.processed
        ) return;

        field.dataset.processed = true;

        const wrapper =
            document.createElement('div');

        wrapper.style.position =
            'relative';

        field.parentNode.insertBefore(
            wrapper,
            field
        );

        wrapper.appendChild(field);

        const button =
            document.createElement('button');

        button.type = 'button';

        button.innerHTML = 'Show';

        button.classList.add(
            'password-toggle-btn'
        );

        wrapper.appendChild(button);

        button.addEventListener(
            'click',
            () => {

                if (
                    field.type === 'password'
                ) {

                    field.type = 'text';

                    button.innerHTML = 'Hide';

                } else {

                    field.type = 'password';

                    button.innerHTML = 'Show';
                }

            }
        );

    });

}


// ===============================================
// FORM LOADING
// ===============================================

function initializeFormLoading() {

    const forms =
        document.querySelectorAll(
            'form'
        );

    forms.forEach(form => {

        form.addEventListener(
            'submit',
            () => {

                const button =
                    form.querySelector(
                        'button[type="submit"]'
                    );

                if (button) {

                    button.disabled = true;

                    button.innerHTML =
                        `
                        <span class="spinner-border spinner-border-sm me-2"></span>
                        Please Wait...
                        `;
                }

            }
        );

    });

}


// ===============================================
// COUNTER ANIMATION
// ===============================================

function initializeCounters() {

    const counters =
        document.querySelectorAll(
            '.counter'
        );

    counters.forEach(counter => {

        counter.innerText = '0';

        const updateCounter = () => {

            const target =
                +counter.dataset.target;

            const current =
                +counter.innerText;

            const increment =
                target / 40;

            if (current < target) {

                counter.innerText =
                    `${Math.ceil(
                        current + increment
                    )}`;

                setTimeout(
                    updateCounter,
                    25
                );

            } else {

                counter.innerText =
                    target;
            }

        };

        updateCounter();

    });

}


// ===============================================
// SCROLL TOP BUTTON
// ===============================================

function initializeScrollTop() {

    const scrollBtn =
        document.createElement(
            'button'
        );

    scrollBtn.innerHTML =
        '<i class="bi bi-arrow-up"></i>';

    scrollBtn.classList.add(
        'scroll-top-btn'
    );

    document.body.appendChild(
        scrollBtn
    );

    window.addEventListener(
        'scroll',
        () => {

            scrollBtn.style.display =
                window.scrollY > 300
                ? 'flex'
                : 'none';

        }
    );

    scrollBtn.addEventListener(
        'click',
        () => {

            window.scrollTo({

                top: 0,

                behavior: 'smooth'
            });

        }
    );

}


// ===============================================
// SCROLL ANIMATION
// ===============================================

function initializeScrollAnimations() {

    const elements =
        document.querySelectorAll(
            '.card, .job-card'
        );

    const observer =
        new IntersectionObserver(
            entries => {

                entries.forEach(entry => {

                    if (
                        entry.isIntersecting
                    ) {

                        entry.target.classList.add(
                            'fade-up'
                        );

                    }

                });

            },
            {
                threshold: 0.1
            }
        );

    elements.forEach(el => {

        observer.observe(el);

    });

}


// ===============================================
// NAVBAR EFFECTS
// ===============================================

function initializeNavbarEffects() {

    const navbar =
        document.querySelector(
            '.premium-navbar'
        );

    if (!navbar) return;

    window.addEventListener(
        'scroll',
        () => {

            if (
                window.scrollY > 40
            ) {

                navbar.style.boxShadow =
                    '0 10px 30px rgba(0,0,0,0.08)';

            } else {

                navbar.style.boxShadow =
                    'none';
            }

        }
    );

}


// ===============================================
// ACTIVE NAV LINKS
// ===============================================

function initializeActiveLinks() {

    const currentLocation =
        window.location.pathname;

    const navLinks =
        document.querySelectorAll(
            '.nav-link'
        );

    navLinks.forEach(link => {

        if (
            link.getAttribute('href') ===
            currentLocation
        ) {

            link.classList.add(
                'active'
            );

        }

    });

}


// ===============================================
// BOOTSTRAP TOOLTIPS
// ===============================================

function initializeTooltips() {

    const tooltipTriggerList =
        [].slice.call(
            document.querySelectorAll(
                '[data-bs-toggle="tooltip"]'
            )
        );

    tooltipTriggerList.map(
        tooltipTriggerEl =>
        new bootstrap.Tooltip(
            tooltipTriggerEl
        )
    );

}


// ===============================================
// CONFIRM DELETE
// ===============================================

function confirmDelete() {

    return confirm(
        'Are you sure you want to delete this item?'
    );

}