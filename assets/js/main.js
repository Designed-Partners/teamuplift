(function () {
  document.documentElement.classList.remove("no-js");

  // Header shadow on scroll
  var header = document.querySelector(".site-header");
  var onScroll = function () {
    if (header) header.classList.toggle("is-scrolled", window.scrollY > 8);
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // Mobile nav
  var toggle = document.querySelector(".nav-toggle");
  if (toggle) {
    var setOpen = function (open) {
      document.body.classList.toggle("nav-open", open);
      toggle.setAttribute("aria-expanded", String(open));
      toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    };
    toggle.addEventListener("click", function () {
      setOpen(!document.body.classList.contains("nav-open"));
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") setOpen(false);
    });
    document.querySelectorAll(".nav-links a").forEach(function (a) {
      a.addEventListener("click", function () { setOpen(false); });
    });
  }

  // Reveal on scroll
  var items = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add("is-visible"); });
  }

  // Footer year
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  // Contact form (Formspree)
  var form = document.querySelector("[data-formspree]");
  if (form) {
    var params = new URLSearchParams(window.location.search);
    var interest = params.get("interest");
    var select = form.querySelector("select[name='interest']");
    if (interest && select) {
      Array.prototype.forEach.call(select.options, function (opt) {
        if (opt.value.toLowerCase() === interest.toLowerCase()) select.value = opt.value;
      });
    }

    var status = form.querySelector(".form-status");
    var button = form.querySelector("button[type='submit']");
    var label = button ? button.innerHTML : "";

    var show = function (type, msg) {
      status.className = "form-status is-" + type;
      status.textContent = msg;
    };

    form.addEventListener("submit", function (e) {
      if (!window.fetch) return; // fall back to a normal POST
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      button.disabled = true;
      button.textContent = "Sending…";
      status.className = "form-status";

      fetch(form.action, {
        method: "POST",
        body: new FormData(form),
        headers: { Accept: "application/json" }
      })
        .then(function (res) {
          return res.json().catch(function () { return {}; }).then(function (data) {
            if (res.ok) {
              form.reset();
              show("success", "Thank you! Your message has been sent. A member of our team will be in touch soon.");
            } else {
              var msg = data && data.errors
                ? data.errors.map(function (x) { return x.message; }).join(" ")
                : "Something went wrong sending your message. Please try again or email info@teamuplift.org.";
              show("error", msg);
            }
          });
        })
        .catch(function () {
          show("error", "We couldn't reach the server. Please check your connection or email info@teamuplift.org.");
        })
        .finally(function () {
          button.disabled = false;
          button.innerHTML = label;
        });
    });
  }
})();

// When opened straight from disk (file://), point folder links at their index.html
if (window.location.protocol === "file:") {
  document.querySelectorAll("a[href]").forEach(function (a) {
    var href = a.getAttribute("href");
    if (/^(?!https?:|mailto:|#)[^?#]*\/(\?[^#]*)?(#.*)?$/.test(href)) {
      a.setAttribute("href", href.replace(/\/(?=[?#]|$)/, "/index.html"));
    }
  });
}
