/* Comportamiento común a todas las páginas: menú, animaciones e índice. */
(function () {
	"use strict";
	document.documentElement.classList.remove("no-js");

	var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

	/* ---------- Menú a pantalla completa ---------- */
	var menu = document.querySelector(".mega-menu");
	var openers = document.querySelectorAll(".menu-toggle");
	var lastFocus = null;

	function openMenu() {
		if (!menu) return;
		lastFocus = document.activeElement;
		menu.classList.add("is-open");
		menu.setAttribute("aria-hidden", "false");
		document.body.classList.add("menu-open");
		openers.forEach(function (b) { b.setAttribute("aria-expanded", "true"); });
		var close = menu.querySelector(".mega-menu__close");
		// esperar a que el menú sea visible para poder darle el foco
		if (close) setTimeout(function () { close.focus(); }, 60);
	}
	function closeMenu() {
		if (!menu || !menu.classList.contains("is-open")) return;
		menu.classList.remove("is-open");
		menu.setAttribute("aria-hidden", "true");
		document.body.classList.remove("menu-open");
		openers.forEach(function (b) { b.setAttribute("aria-expanded", "false"); });
		if (lastFocus) lastFocus.focus();
	}
	openers.forEach(function (b) { b.addEventListener("click", openMenu); });
	if (menu) {
		menu.querySelector(".mega-menu__close").addEventListener("click", closeMenu);
		// Al elegir un ancla de la misma página, cerrar el menú
		menu.querySelectorAll("a").forEach(function (a) { a.addEventListener("click", closeMenu); });
		document.addEventListener("keydown", function (e) {
			if (e.key === "Escape") closeMenu();
			if (e.key === "Tab" && menu.classList.contains("is-open")) {
				var f = menu.querySelectorAll("a, button");
				var first = f[0], last = f[f.length - 1];
				if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
				else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
			}
		});
	}

	/* ---------- Aparición al hacer scroll ---------- */
	var reveals = document.querySelectorAll(".reveal");
	if ("IntersectionObserver" in window && !reduceMotion) {
		var io = new IntersectionObserver(function (entries) {
			entries.forEach(function (en) {
				if (en.isIntersecting) { en.target.classList.add("is-visible"); io.unobserve(en.target); }
			});
		}, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
		reveals.forEach(function (el) { io.observe(el); });
	} else {
		reveals.forEach(function (el) { el.classList.add("is-visible"); });
	}

	/* ---------- Estratos de la portada: leve paralaje ---------- */
	var layers = document.querySelectorAll(".hero__strata .layer");
	if (layers.length && !reduceMotion) {
		var ticking = false;
		window.addEventListener("scroll", function () {
			if (ticking) return;
			ticking = true;
			requestAnimationFrame(function () {
				var y = Math.min(window.scrollY, 900);
				layers.forEach(function (l) {
					var depth = parseFloat(l.getAttribute("data-depth")) || 0;
					l.style.transform = "translateY(" + (y * depth) + "px)";
				});
				ticking = false;
			});
		}, { passive: true });
	}

	/* ---------- Índice de la página: resaltar la sección visible ---------- */
	var indexLinks = document.querySelectorAll(".page-index a[href^='#']");
	if (indexLinks.length && "IntersectionObserver" in window) {
		var map = {};
		indexLinks.forEach(function (a) {
			var t = document.getElementById(a.getAttribute("href").slice(1));
			if (t) map[t.id] = a;
		});
		var spy = new IntersectionObserver(function (entries) {
			entries.forEach(function (en) {
				if (en.isIntersecting && map[en.target.id]) {
					indexLinks.forEach(function (a) { a.classList.remove("is-active"); });
					map[en.target.id].classList.add("is-active");
					// desplazar solo la barra del índice (no la página) para mostrar el ítem activo
					var a = map[en.target.id], ul = a.closest("ul");
					if (ul && ul.scrollWidth > ul.clientWidth) ul.scrollLeft = a.offsetLeft - 20;
				}
			});
		}, { rootMargin: "-40% 0px -55% 0px" });
		Object.keys(map).forEach(function (id) { spy.observe(document.getElementById(id)); });
	}

	/* ---------- Año en el pie ---------- */
	document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
