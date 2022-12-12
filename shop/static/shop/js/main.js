(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();


    // Initiate the wowjs
    new WOW().init();


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.sticky-top').css('top', '0px');
        } else {
            $('.sticky-top').css('top', '-100px');
        }
    });


    // Dropdown on mouse hover
    const $dropdown = $(".dropdown");
    const $dropdownToggle = $(".dropdown-toggle");
    const $dropdownMenu = $(".dropdown-menu");
    const showClass = "show";

    $(window).on("load resize", function () {
        if (this.matchMedia("(min-width: 992px)").matches) {
            $dropdown.hover(
                function () {
                    const $this = $(this);
                    $this.addClass(showClass);
                    $this.find($dropdownToggle).attr("aria-expanded", "true");
                    $this.find($dropdownMenu).addClass(showClass);
                },
                function () {
                    const $this = $(this);
                    $this.removeClass(showClass);
                    $this.find($dropdownToggle).attr("aria-expanded", "false");
                    $this.find($dropdownMenu).removeClass(showClass);
                }
            );
        } else {
            $dropdown.off("mouseenter mouseleave");
        }
    });


    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Header carousel
    $(".header-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        items: 1,
        dots: false,
        loop: true,
        nav: true,
        navText: [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ]
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        center: true,
        margin: 24,
        dots: true,
        loop: true,
        nav: false,
        responsive: {
            0: {
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

})(jQuery);

var _URL = window.URL || window.webkitURL;

$("#fileInput").change(function (e) {
    var image, file;
    if ((file = this.files[0])) {
        image = new Image();
        image.onload = function () {
            src = this.src;
            $('#uploadPreview').html('<img src="' + src + '" width="350px" height="230px"></div>');
            $('#uploadAvatar').html('<img src="' + src + '"></div>');
            e.preventDefault();
        }
    }
    ;
    image.src = _URL.createObjectURL(file);
});


const msg = document.getElementById("alert-msg");

setTimeout(function () {
    msg.style.display = 'none';
}, 2000);


$(function () {
    const current = location.pathname;
    $('nav a').each(function () {
        const $this = $(this);
        if ($this.attr('href').indexOf(current) !== -1) {
            $this.addClass('active');
            $this.parent($this).siblings($this).addClass('active');
        }
    })
})


window.onload = function () {
    var theme = localStorage.getItem('data-theme');
    if (theme == 'light') {
        document.documentElement.setAttribute('data-theme', 'light');
    } else if (theme == '') {
        document.documentElement.setAttribute('data-theme', 'light');
    } else if (theme == 'dark') {
        document.documentElement.setAttribute('data-theme', 'dark');
        document.getElementById("checkbox").checked = true;
    }
}

function toggle(a) {
    if (a.checkbox.checked == true) {
        document.documentElement.classList.add('transition');
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('data-theme', 'dark');
    } else if (a.checkbox.checked == false) {
        document.documentElement.classList.add('transition');
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('data-theme', 'light');
    }
}


const cart = document.querySelectorAll(".card-footer");
const qbox = document.querySelectorAll("#quantity-box");

for (let i = 0; i <= cart.length; i++) {
    cart[i].addEventListener('mouseover', () => {
        qbox[i].style.display = "block";
    })

    cart[i].addEventListener('mouseout', () => {
        qbox[i].style.display = "none";
    })
}

