$(document).ready(function () {
  //   Menutrigger
  $("#menuToggle").on("click", function (event) {
    var windowWidth = $(window).width();
    if (windowWidth < 1010) {
      $("body").removeClass("open");
      if (windowWidth < 760) {
        $("#left-panel").slideToggle();
      } else {
        $("#left-panel").toggleClass("open-menu");
      }
    } else {
      $("body").toggleClass("open");
      $("#left-panel").removeClass("open-menu");
    }
  });

  // Load Resize
  $(window).on("load resize", function (event) {
    var windowWidth = $(window).width();
    if (windowWidth < 1010) {
      $("body").addClass("small-device");
    } else {
      $("body").removeClass("small-device");
    }
  });
});
