/* Project specific Javascript goes here. */

$(document).ready(function () {
    hobbies = $(".hobbies");
    canhelp = $(".canhelp");

    hobbies_button = $("#hobbies-toggle");
    canhelp_button = $("#canhelp-toggle");

    hobbies_button.click(function () {
        hobbies_button.toggleClass('btn-success');
        hobbies.toggle();
    });

    canhelp_button.click(function () {
        canhelp_button.toggleClass('btn-success');
        canhelp.toggle();
    });
})
