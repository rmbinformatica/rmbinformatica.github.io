/* System preference by default; explicit selection persists when storage is available. */
(function () {
  "use strict";
  var root = document.documentElement;
  var key = "rmb-theme";
  var mode = "system";
  try { var saved = localStorage.getItem(key); if (saved === "light" || saved === "dark") mode = saved; } catch (_) {}
  function apply(value) {
    if (value === "light" || value === "dark") root.setAttribute("data-theme", value);
    else root.removeAttribute("data-theme");
  }
  apply(mode);
  document.addEventListener("DOMContentLoaded", function () {
    var select = document.getElementById("rmb-theme");
    if (!select) return;
    select.value = mode;
    select.addEventListener("change", function () {
      mode = select.value;
      apply(mode);
      try { localStorage.setItem(key, mode); } catch (_) {}
    });
  });
}());
