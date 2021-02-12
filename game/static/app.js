let curs = document.querySelector('.cursor');

document.addEventListener('mousemove', (e) => {
  let x = e.pageX;
  let y = e.pageY;
  curs.style.left = (x - 15) + 'px';
  curs.style.top = (y - 15) + 'px';
});

document.addEventListener('click', (e) => {
  let x = e.pageX;
  let y = e.pageY;

  curs.classList.add('explosion');
  setTimeout(function() {
    curs.classList.remove('explosion');
  }, 900);

  let blackhole = document.createElement('blackhole');
  blackhole.style.left = x + 'px';
  blackhole.style.top = y + 'px';
  document.body.appendChild(blackhole);
  let size = Math.random() * 40;
  blackhole.style.width = 1 + size + 'px';
  blackhole.style.height = 1 + size + 'px';

  setTimeout(function() {
    blackhole.remove();
  }, 2000);
});

<!-- Start of Async Drift Code -->
<script>
"use strict";

!function() {
  var t = window.driftt = window.drift = window.driftt || [];
  if (!t.init) {
    if (t.invoked) return void (window.console && console.error && console.error("Drift snippet included twice."));
    t.invoked = !0, t.methods = [ "identify", "config", "track", "reset", "debug", "show", "ping", "page", "hide", "off", "on" ],
    t.factory = function(e) {
      return function() {
        var n = Array.prototype.slice.call(arguments);
        return n.unshift(e), t.push(n), t;
      };
    }, t.methods.forEach(function(e) {
      t[e] = t.factory(e);
    }), t.load = function(t) {
      var e = 3e5, n = Math.ceil(new Date() / e) * e, o = document.createElement("script");
      o.type = "text/javascript", o.async = !0, o.crossorigin = "anonymous", o.src = "https://js.driftt.com/include/" + n + "/" + t + ".js";
      var i = document.getElementsByTagName("script")[0];
      i.parentNode.insertBefore(o, i);
    };
  }
}();
drift.SNIPPET_VERSION = '0.3.1';
drift.load('damh9drxfat6');
</script>
<!-- End of Async Drift Code -->