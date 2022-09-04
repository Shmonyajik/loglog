var buttonAddSelect = document.getElementById("addSelect");
var buttonRemoveSelect = document.getElementById("removeSelect");
var buttonAddSelect1 = document.getElementById("addSelect1");
var buttonRemoveSelect1 = document.getElementById("removeSelect1");
var buttonAddSelect2 = document.getElementById("addSelect2");
var buttonRemoveSelect2 = document.getElementById("removeSelect2");
var buttonAddSelect3 = document.getElementById("addSelect3");
var buttonRemoveSelect3 = document.getElementById("removeSelect3");
var buttonAddSelect4 = document.getElementById("addSelect4");
var buttonRemoveSelect4 = document.getElementById("removeSelect4");

var checkboxes = document.getElementById("checkboxes");
var checkboxes1 = document.getElementById("checkboxes1");
var checkboxes2 = document.getElementById("checkboxes2");
var checkboxes3 = document.getElementById("checkboxes3");
var checkboxes4 = document.getElementById("checkboxes4");

var checkboxes_list = checkboxes.querySelectorAll("input[type=checkbox]")
var checkboxes_list1 = checkboxes1.querySelectorAll("input[type=checkbox]")
var checkboxes_list2 = checkboxes2.querySelectorAll("input[type=checkbox]")
var checkboxes_list3 = checkboxes3.querySelectorAll("input[type=checkbox]")
var checkboxes_list4 = checkboxes4.querySelectorAll("input[type=checkbox]")

var expanded = false;
var expanded1 = false;
var expanded2 = false;
var expanded3 = false;
var expanded4 = false;

function showCheckboxes() {
  if (!expanded) {
    checkboxes.style.display = "block";
    expanded = true;
  } else {
    checkboxes.style.display = "none";
    expanded = false;
  }
}

function showCheckboxes1() {
  if (!expanded1) {
    checkboxes1.style.display = "block";
    expanded1 = true;
  } else {
    checkboxes1.style.display = "none";
    expanded1 = false;
  }
}
function showCheckboxes2() {
  if (!expanded2) {
    checkboxes2.style.display = "block";
    expanded2 = true;
  } else {
    checkboxes2.style.display = "none";
    expanded2 = false;
  }
}
function showCheckboxes3() {
  if (!expanded3) {
    checkboxes3.style.display = "block";
    expanded3 = true;
  } else {
    checkboxes3.style.display = "none";
    expanded3 = false;
  }
}
function showCheckboxes4() {
  if (!expanded4) {
    checkboxes4.style.display = "block";
    expanded4 = true;
  } else {
    checkboxes4.style.display = "none";
    expanded4 = false;
  }
}


buttonAddSelect.addEventListener("click", function() {

    checkboxes_list.forEach(item => {
      if (!item.checked) {
        item.checked = 1;
      }
    });
});
buttonAddSelect1.addEventListener("click", function() {

  checkboxes_list1.forEach(item => {
    if (!item.checked) {
      item.checked = 1;
    }
  });
});
buttonAddSelect2.addEventListener("click", function() {

  checkboxes_list2.forEach(item => {
    if (!item.checked) {
      item.checked = 1;
    }
  });
});
buttonAddSelect3.addEventListener("click", function() {

  checkboxes_list3.forEach(item => {
    if (!item.checked) {
      item.checked = 1;
    }
  });
});
buttonAddSelect4.addEventListener("click", function() {

  checkboxes_list4.forEach(item => {
    if (!item.checked) {
      item.checked = 1;
    }
  });
});

buttonRemoveSelect.addEventListener("click", function() {
  checkboxes_list.forEach(item => {
    if (item.checked) {
      item.checked = 0;
    }
  });
});
buttonRemoveSelect1.addEventListener("click", function() {
  checkboxes_list1.forEach(item => {
    if (item.checked) {
      item.checked = 0;
    }
  });
});
buttonRemoveSelect2.addEventListener("click", function() {
  checkboxes_list2.forEach(item => {
    if (item.checked) {
      item.checked = 0;
    }
  });
});
buttonRemoveSelect3.addEventListener("click", function() {
  checkboxes_list3.forEach(item => {
    if (item.checked) {
      item.checked = 0;
    }
  });
});
buttonRemoveSelect4.addEventListener("click", function() {
  checkboxes_list4.forEach(item => {
    if (item.checked) {
      item.checked = 0;
    }
  });
});