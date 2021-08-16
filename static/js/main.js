//Get tab element
var action_list = document.querySelectorAll(".actions-tab span");

//Set onclick listner for tab buttons
action_list.forEach(function (element) {
  element.onclick = function (e) {
    let tab_id = element.getAttribute("data-target");

    //Show and hide tab contents
    document
      .querySelectorAll("#actions-tab-body div")
      .forEach(function (element) {
        element.style.display = "none";
      });
    action_list.forEach(function (element) {
      element.classList.remove("active");
    });

    document.querySelector(tab_id).style.display = "block";
    element.classList.add("active");
  };
});

//Get form status element for displaying info.
var form_status = document.querySelector("#form-status");

//On form submit event listener
document.querySelector("#student-form").onsubmit = function (event) {
  event.preventDefault();

  // Formdata object whichs contains data to be sent
  let formdata = new FormData(this);
  formdata.append("csrfmiddlewaretoken", csrf_token);
  formdata.append("type", "CS");

  form_status.textContent = "Submitting.";

  //Fetch api http post request
  fetch("processor/", {
    method: "POST",
    body: formdata,
  })
    .then((response) => {
      if (!response.ok) {
        form_status.textContent = "Failed.";
      } else {
        form_status.textContent = "Submitted.";
      }
    })
    .catch(console.error);
};

//Delete button onclick event listener
document.querySelectorAll(".student-delete-btn").forEach(function (element) {
  element.onclick = function (e) {
    let btn = this;
    btn.textContent = "Deleting...";
    let formdata = new FormData();
    formdata.append("csrfmiddlewaretoken", csrf_token);
    formdata.append("type", "DS");
    formdata.append("pk", btn.getAttribute("data-pk"));
    fetch("processor/", {
      method: "POST",
      body: formdata,
    })
      .then((response) => {
        if (!response.ok) {
          btn.textContent = "Failed.";
        } else btn.textContent = "Deleted.";
        btn.disabled = true;
      })
      .catch(console.error);
  };
});

//Create course button onclick event listener
document.querySelector("#create-courses-btn").onclick = function (e) {
  let btn = this;
  let course_title = btn.previousElementSibling.value;
  btn.textContent = "Creating...";
  let formdata = new FormData();
  formdata.append("csrfmiddlewaretoken", csrf_token);
  formdata.append("type", "CC");
  formdata.append("course_title", course_title);
  fetch("processor/", {
    method: "POST",
    body: formdata,
  })
    .then((response) => {
      if (!response.ok) {
        btn.textContent = "Failed.";
      } else {
        btn.textContent = "Created.";
        btn.previousElementSibling.value = "";
      }
    })
    .catch(console.error);
};

//Assign course button onclick event listener
document.querySelector("#assign-courses-btn").onclick = function (e) {
  let btn = this;
  btn.textContent = "Assigning...";
  let student_select_val = document.querySelector("#student-select").value;
  let courses_select_options =
    document.querySelector("#courses-select").selectedOptions;
  let formdata = new FormData();
  formdata.append("csrfmiddlewaretoken", csrf_token);
  formdata.append("type", "AC");
  formdata.append("student", student_select_val);
  for (var i = 0; i < courses_select_options.length; i++) {
    formdata.append("courses", courses_select_options[i].value);
  }
  fetch("processor/", {
    method: "POST",
    body: formdata,
  })
    .then((response) => {
      if (!response.ok) {
        btn.textContent = "Failed.";
      } else {
        btn.textContent = "Assigned.";
        btn.previousElementSibling.value = "";
      }
    })
    .catch(console.error);
};

//Delete course button onclick event listener
document.querySelectorAll(".course-delete-btn").forEach(function (element) {
  element.onclick = function (e) {
    let btn = this;
    btn.textContent = "Deleting...";
    let formdata = new FormData();
    formdata.append("csrfmiddlewaretoken", csrf_token);
    formdata.append("type", "DC");
    formdata.append("pk", btn.getAttribute("data-pk"));
    fetch("processor/", {
      method: "POST",
      body: formdata,
    })
      .then((response) => {
        if (!response.ok) {
          btn.textContent = "Failed.";
        } else btn.textContent = "Deleted.";
        btn.disabled = true;
      })
      .catch(console.error);
  };
});
