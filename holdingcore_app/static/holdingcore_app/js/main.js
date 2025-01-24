(function ($) {
    "use strict";

    // loader
    var loader = function () {
        setTimeout(function () {
            if ($('#loader').length > 0) {
                $('#loader').removeClass('show');
            }
        }, 1);
    };
    loader();

    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 200) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({ scrollTop: 0 }, 1500, 'easeInOutExpo');
        return false;
    });


    // Sticky Navbar
    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 0) {
            $('.navbar').addClass('nav-sticky');
        } else {
            $('.navbar').removeClass('nav-sticky');
        }
    });



    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
    });


    // Main carousel
    $(".carousel .owl-carousel").owlCarousel({
        autoplay: true,
        animateOut: 'fadeOut',
        animateIn: 'fadeIn',
        items: 1,
        smartSpeed: 300,
        dots: false,
        loop: true,
        nav: true,
        navText: [
            '<i class="fa fa-angle-left" aria-hidden="true"></i>',
            '<i class="fa fa-angle-right" aria-hidden="true"></i>'
        ]
    });


    // Modal Video
    $(document).ready(function () {
        var $videoSrc;
        $('.btn-play').click(function () {
            $videoSrc = $(this).data("src");
        });
        console.log($videoSrc);

        $('#videoModal').on('shown.bs.modal', function (e) {
            $("#video").attr('src', $videoSrc + "?autoplay=1&amp;modestbranding=1&amp;showinfo=0");
        })

        $('#videoModal').on('hide.bs.modal', function (e) {
            $("#video").attr('src', $videoSrc);
        })
    });


    // Causes carousel
    $(".causes-carousel").owlCarousel({
        autoplay: true,
        animateIn: 'slideInDown',
        animateOut: 'slideOutDown',
        items: 1,
        smartSpeed: 450,
        dots: false,
        loop: true,
        responsive: {
            0: {
                items: 1
            },
            576: {
                items: 1
            },
            768: {
                items: 2
            },
            992: {
                items: 3
            }
        }
    });


    // Causes progress
    $('.causes-progress').waypoint(function () {
        $('.progress .progress-bar').each(function () {
            $(this).css("width", $(this).attr("aria-valuenow") + '%');
        });
    }, { offset: '80%' });


    // Facts counter
    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 2000
    });


    // Testimonials carousel
    $(".testimonials-carousel").owlCarousel({
        center: true,
        autoplay: true,
        dots: true,
        loop: true,
        responsive: {
            0: {
                items: 1
            },
            576: {
                items: 1
            },
            768: {
                items: 2
            },
            992: {
                items: 3
            }
        }
    });


    // Related post carousel
    $(".related-slider").owlCarousel({
        autoplay: true,
        dots: false,
        loop: true,
        nav: true,
        navText: [
            '<i class="fa fa-angle-left" aria-hidden="true"></i>',
            '<i class="fa fa-angle-right" aria-hidden="true"></i>'
        ],
        responsive: {
            0: {
                items: 1
            },
            576: {
                items: 1
            },
            768: {
                items: 2
            }
        }
    });

})(jQuery);


function toggleContent(link) {
    var content = link.previousElementSibling;  // Get the <p> with the class 'hidden-content'

    if (content.style.display === "none") {
        content.style.display = "block";  // Show the content
        link.innerHTML = "Show Less ▲";     // Change link text
    } else {
        content.style.display = "none";   // Hide the content
        link.innerHTML = "Show More ▼";     // Reset link text
    }
}



//___________________________________
//  Contact Form  //
// ___________________________________
function initializeContactForm() {

}



/*___________________________
***Hero Counter JS***
____________________________*/
document.addEventListener('DOMContentLoaded', function () {
    const counters = document.querySelectorAll('.counter');

    counters.forEach(counter => {
        const updateCounter = () => {
            const target = +counter.getAttribute('data-target'); // Convert target value to number
            const count = +counter.innerText.replace('+', ''); // Remove '+' before updating

            const increment = target / 100; // Adjust speed (higher divisor = slower)

            if (count < target) {
                counter.innerText = Math.ceil(count + increment) + "+"; // Add "+" after the number
                setTimeout(updateCounter, 20); // Adjust delay for smoother animation
            } else {
                counter.innerText = target + "+"; // Ensure final value has "+"
            }
        };

        updateCounter();
    });
});




/*___________________________
***About Founder Message JS***
____________________________*/

function founderToggleText() {
    document.getElementById('toggle-message').addEventListener('click', function () {
        const fullMessage = document.getElementById('full-message');
        const toggleText = document.getElementById('toggle-text');
        const toggleIcon = document.getElementById('toggle-icon');

        // Toggle visibility
        if (fullMessage.classList.contains('d-none')) {
            fullMessage.classList.remove('d-none');
            toggleText.textContent = 'Read Less...';
            toggleIcon.classList.replace('fa-chevron-down', 'fa-chevron-up');
        } else {
            fullMessage.classList.add('d-none');
            toggleText.textContent = 'Read More...';
            toggleIcon.classList.replace('fa-chevron-up', 'fa-chevron-down');
        }
    });

}

// Wait for the DOM content to be loaded before running the function
document.addEventListener('DOMContentLoaded', founderToggleText);




/*___________________________
***Our Program Post***
____________________________*/

function handleReadMoreButtons() {
    const maxLength = 280; // Set the maximum character length before truncation
    const readMoreButtons = document.querySelectorAll(".read-more-btn");

    readMoreButtons.forEach((button) => {
        // Get the associated content span for this button
        const contentSpan = button.previousElementSibling;

        if (contentSpan && contentSpan.textContent.length > maxLength) {
            const fullText = contentSpan.textContent.trim(); // Ensure trimmed text
            const truncatedText = fullText.slice(0, maxLength) + "...";

            // Initially set the truncated text
            contentSpan.textContent = truncatedText;

            button.style.display = "inline"; // Show the button

            // Toggle functionality
            button.addEventListener("click", () => {
                if (contentSpan.textContent === truncatedText) {
                    contentSpan.textContent = fullText; // Show full text
                    button.textContent = "Show Less"; // Update button text
                } else {
                    contentSpan.textContent = truncatedText; // Show truncated text
                    button.textContent = "Read More..."; // Reset button text
                }
            });
        } else {
            button.style.display = "none"; // Hide the button if text is short
        }
    });
}

// Run the function once the DOM is fully loaded
document.addEventListener("DOMContentLoaded", handleReadMoreButtons);


// Model For Program Img
function initImageModalPop() {
    const images = document.querySelectorAll(".clickable-image");
    const modal = document.getElementById("imageModalPop");
    const modalImage = document.getElementById("modalImage");
    const closeModal = document.querySelector(".modal-close");

    images.forEach((image) => {
        image.addEventListener("click", () => {
            modal.style.display = "flex";
            modalImage.src = image.src;
        });
    });

    closeModal.addEventListener("click", () => {
        modal.style.display = "none";
    });

    // Close modal on click outside the image
    modal.addEventListener("click", (event) => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
}

// Wait for DOM to load before initializing modal functionality
document.addEventListener("DOMContentLoaded", initImageModalPop);




/*___________________________
**Blog Section***
____________________________*/





