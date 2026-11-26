/* Mrsam page background: a lab sheet. A measuring grid that drifts with the scroll, slow nodes joined by hairlines, and a probe that follows the pointer.
   Drawn in the page's ink token. Paused when the tab is hidden; one still frame under reduced motion. */
(function () {
  var c = document.getElementById("bg"); if (!c || !c.getContext) return;
  var x = c.getContext("2d"), cs = getComputedStyle(document.documentElement);
  var ink = cs.getPropertyValue("--color-ink").trim() || "#e8e5df";
  var font = cs.getPropertyValue("--font-body").trim() || "sans-serif";
  var reduce = matchMedia("(prefers-reduced-motion: reduce)").matches, hover = matchMedia("(hover: hover)").matches;
  var W = 0, H = 0, D = 1, CELL = 48, nodes = [], px = -1, py = -1, tick = 0, SY = 0;
  function color(a) { x.globalAlpha = a; }
  function size() {
    D = Math.min(devicePixelRatio || 1, 1.5); W = innerWidth; H = innerHeight;
    c.width = Math.round(W * D); c.height = Math.round(H * D); x.setTransform(D, 0, 0, D, 0, 0);
    x.strokeStyle = ink; x.fillStyle = ink; if (x.strokeStyle === "#000000") { x.strokeStyle = "#e8e5df"; x.fillStyle = "#e8e5df"; }
    var n = Math.max(36, Math.min(100, Math.round(W * H / 20000)));
    while (nodes.length < n) nodes.push({ x: Math.random() * W, y: Math.random() * H, vx: (Math.random() - .5) * .22, vy: (Math.random() - .5) * .22 });
    nodes.length = n;
  }
  function grid() {
    var off = (SY * .12) % (CELL * 4);
    x.lineWidth = 1;
    for (var gx = 0, i = 0; gx <= W + CELL; gx += CELL, i++) { color(i % 4 === 0 ? .11 : .05); x.beginPath(); x.moveTo(gx + .5, 0); x.lineTo(gx + .5, H); x.stroke(); }
    for (var gy = -CELL * 4, j = 0; gy <= H + CELL; gy += CELL, j++) { var yy = gy + off; color(((j % 4) === 0) ? .11 : .05); x.beginPath(); x.moveTo(0, yy + .5); x.lineTo(W, yy + .5); x.stroke(); }
  }
  function draw() {
    x.clearRect(0, 0, W, H); grid();
    var i, j, a, b, d, link = 150;
    for (i = 0; i < nodes.length; i++) {
      a = nodes[i];
      if (!reduce) { a.x += a.vx; a.y += a.vy; if (a.x < -10) a.x = W + 10; if (a.x > W + 10) a.x = -10; if (a.y < -10) a.y = H + 10; if (a.y > H + 10) a.y = -10; }
      for (j = i + 1; j < nodes.length; j++) { b = nodes[j]; d = Math.hypot(a.x - b.x, a.y - b.y); if (d < link) { color((1 - d / link) * .3); x.beginPath(); x.moveTo(a.x, a.y); x.lineTo(b.x, b.y); x.stroke(); } }
    }
    for (i = 0; i < nodes.length; i++) { a = nodes[i]; color(.65); x.fillRect(a.x - 1, a.y - 1, 2, 2); }
    if (px >= 0) {
      for (i = 0; i < nodes.length; i++) { a = nodes[i]; d = Math.hypot(a.x - px, a.y - py); if (d < 190) { color((1 - d / 190) * .4); x.beginPath(); x.moveTo(px, py); x.lineTo(a.x, a.y); x.stroke(); } }
      color(.6); x.beginPath(); x.moveTo(px - 9, py + .5); x.lineTo(px + 10, py + .5); x.moveTo(px + .5, py - 9); x.lineTo(px + .5, py + 10); x.stroke();
      x.font = "12px " + font; x.fillText((px / CELL).toFixed(1) + ", " + ((py + SY * .12) / CELL).toFixed(1), px + 14, py - 10);
    }
    color(1);
  }
  function loop() { if (!document.hidden) { tick++; draw(); } requestAnimationFrame(loop); }
  size(); draw();
  addEventListener("resize", function () { size(); draw(); });
  addEventListener("scroll", function () { SY = scrollY; if (reduce) draw(); }, { passive: true });
  if (!reduce) { if (hover) addEventListener("pointermove", function (e) { px = e.clientX; py = e.clientY; }, { passive: true }); document.addEventListener("pointerleave", function () { px = -1; py = -1; }); requestAnimationFrame(loop); }
})();
