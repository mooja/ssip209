/* Project specific Javascript goes here. */

$(document).ready(function () {

    $container = $("#members");

    $container.isotope({
        layoutMode: "masonry",
        itemSelector: ".member-data",
    });

    function filter_by_name() {
        $container.isotope({
            filter: function () {
                var re = new RegExp($("#search-name").val(), "ig");
                var name = $(this).find('.name').text().trim();
                return name.match(re);
        }});
    }

    // show details on hover
    // $(".member-data").hover(function () {
    //     $(this).toggleClass("well");
    //     $(this).find(".detail-data").toggleClass("hidden");
    //     $container.isotope('layout');
    // });

    $("#show-details").change(function () {
        $(".detail-data").toggleClass("hidden");
        $container.isotope('layout');
    });

    $("#search-name").keyup(filter_by_name);

});
