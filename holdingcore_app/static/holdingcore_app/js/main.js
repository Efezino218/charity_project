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
    document.getElementById("contactForm").addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent default form submission

        // Get the input values
        const name = document.getElementById("name").value.trim();
        const email = document.getElementById("email").value.trim();
        const subject = document.getElementById("subject").value.trim();
        const message = document.getElementById("message").value.trim();
        const submitButton = document.getElementById("sendMessageButton");

        // Validate each field and show an error if any are empty
        if (!name || !email || !subject || !message) {
            Swal.fire({
                icon: 'error',
                title: 'Incomplete Form',
                text: 'Please fill in all fields before submitting the form.'
            });
            return; // Stop the function here if any field is empty
        }

        // Start the loading animation
        let dotCount = 0;
        submitButton.innerHTML = "Sending"; // Initial text
        submitButton.disabled = true; // Disable the button while loading
        const loadingInterval = setInterval(() => {
            dotCount = (dotCount + 1) % 4; // Cycle between 0, 1, 2, 3
            submitButton.innerHTML = "Sending" + ".".repeat(dotCount);
        }, 500);

        // Send the email if all fields are filled
        emailjs.send("service_lpbv6tq", "template_fvcskwb", {
            name: name,
            email: email,
            subject: subject,
            message: message
        }).then(function (response) {
            clearInterval(loadingInterval); // Stop the loading animation
            submitButton.innerHTML = "Send Message"; // Reset button text
            submitButton.disabled = false; // Re-enable the button

            // Success message
            Swal.fire({
                icon: 'success',
                title: 'Message Sent!',
                text: 'Thank you for contacting us. We will get back to you shortly.'
            }).then(() => {
                // Clear the form fields only after showing the success message
                document.getElementById("contactForm").reset();
            });
        }, function (error) {
            clearInterval(loadingInterval); // Stop the loading animation
            submitButton.innerHTML = "Send Message"; // Reset button text
            submitButton.disabled = false; // Re-enable the button

            // Error message
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Something went wrong. Please try again later.'
            });
        });
    });
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


