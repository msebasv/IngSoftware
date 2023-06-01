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
        .css({ opacity: 1, top: "112px", height: "auto" });
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

// document.addEventListener("DOMContentLoaded", function () {
//   var calendarEl = document.getElementById("calendar");

//   var calendar = new FullCalendar.Calendar(calendarEl, {
//     headerToolbar: {
//       left: "prev,next today",
//       center: "title",
//       right: "dayGridMonth,timeGridWeek,timeGridDay,listMonth",
//     },
//     initialDate: "2023-01-12",
//     navLinks: true, // can click day/week names to navigate views
//     businessHours: true, // display business hours
//     editable: true,
//     selectable: true,
//     events: [
//       {
//         title: "Business Lunch",
//         start: "2023-01-03T13:00:00",
//         constraint: "businessHours",
//       },
//       {
//         title: "Meeting",
//         start: "2023-01-13T11:00:00",
//         constraint: "availableForMeeting", // defined below
//         color: "#257e4a",
//       },
//       {
//         title: "Conference",
//         start: "2023-01-18",
//         end: "2023-01-20",
//       },
//       {
//         title: "Party",
//         start: "2023-01-29T20:00:00",
//       },

//       // areas where "Meeting" must be dropped
//       {
//         groupId: "availableForMeeting",
//         start: "2023-01-11T10:00:00",
//         end: "2023-01-11T16:00:00",
//         display: "background",
//       },
//       {
//         groupId: "availableForMeeting",
//         start: "2023-01-13T10:00:00",
//         end: "2023-01-13T16:00:00",
//         display: "background",
//       },

//       // red areas where no events can be dropped
//       {
//         start: "2023-01-24",
//         end: "2023-01-28",
//         overlap: false,
//         display: "background",
//         color: "#ff9f89",
//       },
//       {
//         start: "2023-01-06",
//         end: "2023-01-08",
//         overlap: false,
//         display: "background",
//         color: "#ff9f89",
//       },
//     ],
//   });

//   calendar.render();
// });
