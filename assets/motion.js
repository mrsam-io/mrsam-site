/* Mrsam page motion: headline words rise out of a mask, section words and rows rise in as they enter the screen, the headline drifts a little on scroll.
   Content is visible without script; nothing moves under prefers-reduced-motion. Transform and opacity only. */
(function () {
  var reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  function words(el) {
    var txt = el.textContent.trim(); if (!txt || el.querySelector("img")) return false;
    el.setAttribute("aria-label", txt); el.textContent = "";
    txt.split(/\s+/).forEach(function (w, i) {
      var o = document.createElement("span"), n = document.createElement("span");
      o.className = "w"; o.setAttribute("aria-hidden", "true"); n.textContent = w; n.style.setProperty("--i", i); o.appendChild(n);
      el.appendChild(o); el.appendChild(document.createTextNode(" "));
    });
    return true;
  }
  var h1 = document.querySelector(".hero h1"); if (h1) words(h1);
  document.querySelectorAll("main h2").forEach(function (h) { if (words(h)) h.classList.add("rise-words"); });
  var groups = [".section__head > p", ".section__head > div:not(.work__brand)", ".sheet li", ".link-line", ".cells > div", ".steps > div", ".about .lead", ".contact .lead", ".contact__mail"];
  groups.forEach(function (sel) { document.querySelectorAll(sel).forEach(function (el, i) { el.classList.add("rise"); el.style.setProperty("--d", (i % 6) * 90 + "ms"); }); });
  var targets = document.querySelectorAll(".rise, .rise-words");
  if (reduce || !("IntersectionObserver" in window)) { targets.forEach(function (el) { el.classList.add("in"); }); return; }
  var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }); }, { threshold: .15, rootMargin: "0px 0px -6% 0px" });
  targets.forEach(function (el) { io.observe(el); });
  var lead = document.querySelector(".hero .lead"), busy = false;
  function drift() { busy = false; var y = Math.min(scrollY, 700); if (h1) h1.style.transform = "translate3d(0," + (y * .1).toFixed(1) + "px,0)"; if (lead) lead.style.transform = "translate3d(0," + (y * .05).toFixed(1) + "px,0)"; }
  addEventListener("scroll", function () { if (!busy) { busy = true; requestAnimationFrame(drift); } }, { passive: true });
})();
