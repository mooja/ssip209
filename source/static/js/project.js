/* Project specific Javascript goes here. */

$(document).ready(function () {

    $container = $("#members");

    $container.isotope({
        layoutMode: "masonry",
        itemSelector: ".member-data",
    });

    hobbies_button.click(function () {
        hobbies_button.toggleClass('btn-success');
        hobbies.toggleClass("hidden");
        $container.isotope('layout');
    });

    canhelp_button.click(function () {
        canhelp_button.toggleClass('btn-success');
        canhelp.toggleClass("hidden");
        $container.isotope('layout');
    });

    $(".member-data").hover(function () {
        $(this).toggleClass("bg-warning");
        $(this).find(".detail-data").toggleClass("hidden");
        $container.isotope('layout');
    });
});
