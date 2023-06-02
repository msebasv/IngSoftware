$(document).ready(function () {
  var isSidebarReduced = false; // Variable to track if the sidebar is reduced or not
  var isLogReduced = true; // Variable to track if the log is reduced or not
  var originalSidebarWidth = $(".sidebar").width(); // Store the original width of the sidebar
  var originalLogheight = $(".log_out").height(); // Store the original height of the log
  var sidebarNav = $(".sidebar .sidebar__nav"); // Sidebar navigation element
  var sidebarItems = $(".sidebar .sidebar__nav .sidebar__list .sidebar__item"); // Sidebar item elements
  var sidebarButton = $(".header_list_first_button"); // Sidebar button element
  var profileButton = $(".header_list_second_button"); // Profile button element

  sidebarButton.click(function () {
    if (isSidebarReduced) {
      sidebarButton.prop("disabled", true); // Disable the button during the animation
      $(".sidebar").animate({ width: originalSidebarWidth }); // Animate the sidebar width to its original width
      sidebarNav.find("h3").fadeIn(); // Fade in the sidebar navigation headings
      sidebarItems.find("a p, a .fa-caret-right").fadeIn(); // Fade in the sidebar item content
      sidebarItems.find("a").animate({ marginLeft: "0" }); // Animate the left margin of the sidebar items
      isSidebarReduced = false; // Set the flag to indicate that the sidebar is not reduced
    } else {
      sidebarButton.prop("disabled", true); // Disable the button during the animation
      $(".sidebar").animate({ width: "50px" }); // Animate the sidebar width to a reduced size
      sidebarNav.find("h3").fadeOut(); // Fade out the sidebar navigation headings
      sidebarItems.find("a p, a .fa-caret-right").fadeOut(); // Fade out the sidebar item content
      sidebarItems.find("a").animate(); // Animate the left margin of the sidebar items
      isSidebarReduced = true; // Set the flag to indicate that the sidebar is reduced
    }
  });

  profileButton.click(function () {
    if (isLogReduced) {
      $(".log_out")
        .css({ opacity: 0, height: "auto" })
        .show()
        .css({ opacity: 1, top: "90px", height: "120px" });
      // Make the log section visible and adjust its position and opacity
      $(".log_out .log_out_menu").fadeIn(); // Fade in the log menu
      isLogReduced = false; // Set the flag to indicate that the log is not reduced
    } else {
      $(".log_out").css({ opacity: 0, height: "0px" }, function () {
        $(this).hide(); // Set the log section to be hidden and adjust its height and opacity
      });
      $(".log_out .log_out_menu").fadeOut(); // Fade out the log menu
      isLogReduced = true; // Set the flag to indicate that the log is reduced
    }
  });
});
