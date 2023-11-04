var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
var popoverList = popoverTriggerList.map(function(popoverTriggerEl) {
  return new bootstrap.Popover(popoverTriggerEl)
})

var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function(tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})

function setAttributes(el, options) {
  Object.keys(options).forEach(function(attr) {
    el.setAttribute(attr, options[attr]);
  })
}

var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-toggle="popover"]'))
var popoverList = popoverTriggerList.map(function(popoverTriggerEl) {
  return new bootstrap.Popover(popoverTriggerEl)
})

var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function(tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})


function copyCode(el) {
  const selection = window.getSelection();
  const range = document.createRange();
  const textToCopy = el.nextElementSibling;
  range.selectNodeContents(textToCopy);
  selection.removeAllRanges();
  selection.addRange(range);
  const successful = document.execCommand('copy');
  window.getSelection().removeAllRanges()
  if (!el.parentElement.querySelector('.alert')) {
    var alert = document.createElement('div');
    alert.classList.add('alert', 'alert-success', 'position-absolute', 'top-0', 'border-0', 'text-white', 'w-25', 'end-0', 'start-0', 'mt-2', 'mx-auto', 'py-2');
    alert.style.transform = 'translate3d(0px, 0px, 0px)'
    alert.style.opacity = '0';
    alert.style.transition = '.35s ease';
    setTimeout(function() {
      alert.style.transform = 'translate3d(0px, 20px, 0px)';
      alert.style.setProperty("opacity", "1", "important");
    }, 100);
    alert.innerHTML = "Code successfully copied!";
    el.parentElement.appendChild(alert);
    setTimeout(function() {
      alert.style.transform = 'translate3d(0px, 0px, 0px)'
      alert.style.setProperty("opacity", "0", "important");
    }, 2000);
    setTimeout(function() {
      el.parentElement.querySelector('.alert').remove();
    }, 2500);
  }
}

function debounce(func, wait, immediate) {
  var timeout;
  return function() {
    var context = this,
      args = arguments;
    clearTimeout(timeout);
    timeout = setTimeout(function() {
      timeout = null;
      if (!immediate) func.apply(context, args);
    }, wait);
    if (immediate && !timeout) func.apply(context, args);
  };
};
