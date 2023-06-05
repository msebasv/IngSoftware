// document.addEventListener("DOMContentLoaded", function () {
//   var calendarUI = document.getElementById("calendar");
//   var calendar = new FullCalendar.Calendar(calendarUI, {
//     events :[
//       {% for eventos in object_list %}
//           {
//             title: "{{ eventos.subject }}",
//             start: "{{ eventos.date_init}}",
//             end: "{{ eventos.date_finish }}"
//           },
//       {% endfor %}
//     ],
//   });
//   calendar.render();
// });
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
