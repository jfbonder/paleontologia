/* =========================================================================
   Plan de estudios de la Licenciatura en Paleontología
   -------------------------------------------------------------------------
   Para actualizar el plan, editar SOLO el bloque de datos de abajo.
   Con estos datos se dibujan el diagrama de correlatividades y la tabla.

   Campos de cada materia:
     id        identificador corto (sin espacios)
     nombre    nombre de la materia
     horas     carga horaria total
     anio      año de la carrera (2 a 6: el 1.º año es el CBC)
     cuatri    1 o 2 (primer o segundo cuatrimestre)
     area      paleo | geo | bio | basicas | atm   (define el color)
     correl    lista de ids de las correlativas ("cbc" = Ciclo Básico Común)
     programa  (opcional) ruta al PDF del programa
     nota      (opcional) equivalencias u observaciones
   ========================================================================= */
var PLAN = {
	areas: {
		paleo:   { nombre: "Paleontología", color: "#b4532a" },
		geo:     { nombre: "Geología", color: "#c68b2c" },
		bio:     { nombre: "Biología", color: "#5f7a3a" },
		basicas: { nombre: "Química, física y matemática", color: "#2f4a52" },
		atm:     { nombre: "Ciencias de la atmósfera y los océanos", color: "#3c7aa0" }
	},
	materias: [
		// ---- Primer año ----
		{ id: "ibm", nombre: "Introducción a la Biología Molecular para Paleontólogos", corto: "Int. a la Biología Molecular", horas: 160, anio: 2, cuatri: 1, area: "bio", correl: ["cbc"],
			programa: "archivos/programas/introduccion-biologia-molecular.pdf", nota: "Quienes aprueben Introducción a la Biología Molecular y Celular (IBMC) de la carrera de Biología obtienen la equivalencia." },
		{ id: "icao", nombre: "Introducción a las Ciencias de la Atmósfera y los Océanos", corto: "Cs. de la Atmósfera y los Océanos", horas: 128, anio: 2, cuatri: 1, area: "atm", correl: ["cbc"],
			programa: "archivos/programas/introduccion-ciencias-atmosfera-oceanos.pdf" },
		{ id: "bv", nombre: "Biodiversidad de Vegetales", horas: 160, anio: 2, cuatri: 1, area: "bio", correl: ["cbc"],
			programa: "archivos/programas/biodiversidad-de-vegetales.pdf", nota: "Quienes aprueben Introducción a la Botánica de la carrera de Biología obtienen la equivalencia." },
		{ id: "ba", nombre: "Biodiversidad de Animales", horas: 160, anio: 2, cuatri: 2, area: "bio", correl: ["cbc"],
			programa: "archivos/programas/biodiversidad-de-animales.pdf", nota: "Quienes aprueben Introducción a la Zoología de la carrera de Biología obtienen la equivalencia." },
		{ id: "gg", nombre: "Geología General", horas: 128, anio: 2, cuatri: 2, area: "geo", correl: ["cbc"] },
		{ id: "fis", nombre: "Física para Paleontólogos", corto: "Física para Paleontólogos", horas: 160, anio: 2, cuatri: 2, area: "basicas", correl: ["cbc"],
			programa: "archivos/programas/fisica-para-paleontologos.pdf",
			nota: "Actualmente reemplazada por la asignatura «Electromagnetismo y Óptica» del plan de Biología (Res. CD 1911/2023).",
			resolucion: "archivos/resoluciones/res-cd-1911-2023.pdf" },

		// ---- Segundo año ----
		{ id: "biom", nombre: "Biometría", horas: 120, anio: 3, cuatri: 1, area: "basicas", correl: ["ba", "bv"],
			programa: "archivos/programas/biometria.pdf" },
		{ id: "paleo", nombre: "Paleontología", horas: 160, anio: 3, cuatri: 1, area: "paleo", correl: ["ba", "bv", "gg"],
			programa: "archivos/programas/paleontologia.pdf" },
		{ id: "pbot", nombre: "Paleobotánica", horas: 160, anio: 3, cuatri: 2, area: "paleo", correl: ["paleo"],
			programa: "archivos/programas/paleobotanica.pdf" },
		{ id: "fse", nombre: "Fundamentos de Sedimentología y Estratigrafía", corto: "Fund. Sedimentología y Estratigrafía", horas: 90, anio: 3, cuatri: 2, area: "geo", correl: ["gg"] },
		{ id: "qg", nombre: "Química General e Inorgánica para Paleontólogos", corto: "Química General e Inorgánica", horas: 192, anio: 3, cuatri: 2, area: "basicas", correl: ["cbc"],
			programa: "archivos/programas/quimica-general-e-inorganica.pdf",
			nota: "Se otorga equivalencia a quienes aprueben Química General e Inorgánica I del plan de Biología (Res. CD 2510/2017).",
			resolucion: "archivos/resoluciones/res-cd-2510-2017.pdf" },

		// ---- Tercer año ----
		{ id: "qo", nombre: "Química Orgánica para Paleontólogos", corto: "Química Orgánica", horas: 160, anio: 4, cuatri: 1, area: "basicas", correl: ["qg"],
			programa: "archivos/programas/quimica-organica.pdf", nota: "Quienes aprueben Química Orgánica de la carrera de Biología obtienen la equivalencia." },
		{ id: "as", nombre: "Ambientes Sedimentarios", horas: 128, anio: 4, cuatri: 1, area: "geo", correl: ["fse"] },
		{ id: "pinv", nombre: "Paleontología de Invertebrados", horas: 160, anio: 4, cuatri: 1, area: "paleo", correl: ["paleo"],
			programa: "archivos/programas/paleontologia-de-invertebrados.pdf" },
		{ id: "micro", nombre: "Fundamentos de Micropaleontología", corto: "Fund. de Micropaleontología", horas: 160, anio: 4, cuatri: 2, area: "paleo", correl: ["paleo"] },
		{ id: "vert", nombre: "Vertebrados", horas: 160, anio: 4, cuatri: 2, area: "bio", correl: ["ba"],
			programa: "archivos/programas/vertebrados.pdf" },
		{ id: "gen", nombre: "Genética General para Paleontólogos", corto: "Genética General", horas: 110, anio: 4, cuatri: 2, area: "bio", correl: ["ibm", "biom"],
			programa: "archivos/programas/genetica-general.pdf", nota: "Se otorga por equivalencia a quienes aprueben Genética I del plan de Biología (Res. CD 114/2006)." },

		// ---- Cuarto año ----
		{ id: "evo", nombre: "Evolución para Paleontólogos", corto: "Evolución", horas: 90, anio: 5, cuatri: 1, area: "bio", correl: ["gen"],
			programa: "archivos/programas/evolucion.pdf", nota: "Quienes aprueben Evolución de la carrera de Biología obtienen la equivalencia." },
		{ id: "pvert", nombre: "Paleontología de Vertebrados", horas: 160, anio: 5, cuatri: 2, area: "paleo", correl: ["paleo", "vert"],
			programa: "archivos/programas/paleontologia-de-vertebrados.pdf" },
		{ id: "bioest", nombre: "Bioestratigrafía", horas: 128, anio: 5, cuatri: 2, area: "paleo", correl: ["paleo"] }
	],
	// Bloques que no son materias puntuales (se muestran en el diagrama con otro estilo)
	bloques: [
		{ id: "opt4", nombre: "Optativas y electivas", anio: 5, cuatri: 1, texto: "Ciclo de orientación: 800 créditos en total entre 5.º y 6.º año." },
		{ id: "opt5", nombre: "Optativas y electivas", anio: 6, cuatri: 1, texto: "Ciclo de orientación: 800 créditos en total entre 5.º y 6.º año." },
		{ id: "tesis", nombre: "Tesis de Licenciatura", horas: 160, anio: 6, cuatri: 2, texto: "Se puede iniciar con los trabajos prácticos de todas las materias del ciclo obligatorio aprobados." }
	],
	// Orden de las materias dentro de cada cuatrimestre en el diagrama (izquierda a derecha)
	layout: {
		"2-1": ["ibm", "icao", "bv"], "2-2": ["ba", "gg", "fis"],
		"3-1": ["biom", "paleo"],     "3-2": ["pbot", "fse", "qg"],
		"4-1": ["qo", "as", "pinv"],  "4-2": ["micro", "vert", "gen"],
		"5-1": ["opt4", "evo"],       "5-2": ["pvert", "bioest"],
		"6-1": ["opt5"],              "6-2": ["tesis"]
	}
};

(function () {
	"use strict";
	var SVGNS = "http://www.w3.org/2000/svg";
	var ORD = ["", "Primer", "Segundo", "Tercer", "Cuarto", "Quinto", "Sexto"];
	var byId = {};
	PLAN.materias.forEach(function (m) { byId[m.id] = m; });
	PLAN.bloques.forEach(function (b) { byId[b.id] = b; b.bloque = true; });

	// Relaciones directas: quién habilita a quién
	var habilita = {};
	PLAN.materias.forEach(function (m) {
		m.correl.forEach(function (c) { (habilita[c] = habilita[c] || []).push(m.id); });
	});

	function nombreDe(id) { return id === "cbc" ? "CBC" : (byId[id] ? byId[id].nombre : id); }
	function cuatriTxt(m) { return ORD[m.anio] + " año, " + (m.cuatri === 1 ? "primer" : "segundo") + " cuatrimestre"; }
	function el(tag, attrs, parent) {
		var e = document.createElementNS(SVGNS, tag);
		for (var k in attrs) e.setAttribute(k, attrs[k]);
		if (parent) parent.appendChild(e);
		return e;
	}

	/* ------------------------------------------------------------------
	   Diagrama de correlatividades
	   ------------------------------------------------------------------ */
	var svg = document.getElementById("plan-diagram");
	if (svg) {
		var NW = 156, NH = 54, SLOT = 168, LABEL_W = 96, HALF_GAP = 34;
		var ROW_H = 118, TOP = 70;
		var halfW = SLOT * 3;
		var W = LABEL_W + halfW * 2 + HALF_GAP + 10;
		var H = TOP + ROW_H * 5 + 40;
		svg.setAttribute("viewBox", "0 0 " + W + " " + H);
		var pos = {};

		// Bandas por año y rótulos
		var gBands = el("g", {}, svg);
		for (var a = 0; a <= 5; a++) {
			var y = a === 0 ? 0 : TOP + (a - 1) * ROW_H + 20;
			if (a > 0) {
				if (a % 2 === 1) el("rect", { x: 0, y: y - 16, width: W, height: ROW_H, rx: 12, "class": "row-band" }, gBands);
				var t = el("text", { x: 6, y: y + NH / 2 + 5, "class": "row-label" }, gBands);
				t.textContent = (a + 1) + ".º año";
			}
		}
		[["1.º cuatrimestre", LABEL_W + halfW / 2], ["2.º cuatrimestre", LABEL_W + halfW + HALF_GAP + halfW / 2]].forEach(function (c) {
			var t = el("text", { x: c[1], y: TOP - 6, "text-anchor": "middle", "class": "col-label" }, gBands);
			t.textContent = c[0];
		});

		// Posición de cada nodo
		Object.keys(PLAN.layout).forEach(function (key) {
			var p = key.split("-"), anio = +p[0], cu = +p[1], ids = PLAN.layout[key];
			var x0 = LABEL_W + (cu === 2 ? halfW + HALF_GAP : 0);
			var offset = (3 - ids.length) * SLOT / 2; // centrar si hay menos de 3
			ids.forEach(function (id, i) {
				pos[id] = { x: x0 + offset + i * SLOT + (SLOT - NW) / 2, y: TOP + (anio - 2) * ROW_H + 20, anio: anio, cuatri: cu };
			});
		});
		pos.cbc = { x: W / 2 - 50, y: 6, w: 100, h: 34 };
		var tc = el("text", { x: 6, y: 6 + 34 / 2 + 5, "class": "row-label" }, gBands);
		tc.textContent = "1.º año";

		// Aristas
		var gEdges = el("g", {}, svg);
		var edges = [];
		function addEdge(from, to) {
			var a = pos[from], b = pos[to];
			var d, cls = "edge" + (from === "cbc" ? " cbc" : "");
			var aw = a.w || NW, ah = a.h || NH;
			if (from !== "cbc" && a.anio === b.anio) {
				// mismo año: de lado a lado
				var x1 = a.x + aw, y1 = a.y + ah / 2, x2 = b.x, y2 = b.y + NH / 2;
				d = "M" + x1 + " " + y1 + " C" + (x1 + 30) + " " + y1 + " " + (x2 - 30) + " " + y2 + " " + x2 + " " + y2;
			} else {
				var sx = a.x + aw / 2, sy = a.y + ah, tx = b.x + NW / 2, ty = b.y;
				var dy = Math.max(40, (ty - sy) * 0.5);
				d = "M" + sx + " " + sy + " C" + sx + " " + (sy + dy) + " " + tx + " " + (ty - dy) + " " + tx + " " + ty;
			}
			var p = el("path", { d: d, "class": cls, "marker-end": "url(#arrow)" }, gEdges);
			edges.push({ from: from, to: to, node: p });
		}
		var defs = el("defs", {}, svg);
		var mk = el("marker", { id: "arrow", viewBox: "0 0 10 10", refX: 9, refY: 5, markerWidth: 6, markerHeight: 6, orient: "auto-start-reverse" }, defs);
		el("path", { d: "M0 0 L10 5 L0 10 z", fill: "#b9ab95" }, mk);
		PLAN.materias.forEach(function (m) { m.correl.forEach(function (c) { if (pos[c] && pos[m.id]) addEdge(c, m.id); }); });

		// Nodos
		var gNodes = el("g", {}, svg);
		var nodes = {};
		function wrap(text, max) {
			var words = text.split(" "), lines = [""];
			words.forEach(function (w) {
				var cur = lines[lines.length - 1];
				if ((cur + " " + w).trim().length > max && cur) lines.push(w); else lines[lines.length - 1] = (cur + " " + w).trim();
			});
			return lines;
		}
		function drawNode(id, label, horas, fill, placeholder, w, h) {
			var p = pos[id]; w = w || NW; h = h || NH;
			var g = el("g", { "class": "node" + (placeholder ? " is-placeholder" : ""), tabindex: 0, role: "button", "data-id": id,
				"aria-label": label + (horas ? ", " + horas + " horas" : "") }, gNodes);
			el("rect", { "class": "box", x: p.x, y: p.y, width: w, height: h, rx: 7, fill: fill,
				stroke: placeholder ? "#b4532a" : "none", "stroke-dasharray": placeholder ? "4 4" : "none" }, g);
			var lines = wrap(label, 22).slice(0, 3);
			var lh = 13.5, total = lines.length * lh + (horas ? 12 : 0);
			var ty = p.y + h / 2 - total / 2 + 10;
			lines.forEach(function (ln, i) {
				var t = el("text", { x: p.x + w / 2, y: ty + i * lh, "text-anchor": "middle" }, g);
				t.textContent = ln;
			});
			if (horas) {
				var th = el("text", { x: p.x + w / 2, y: ty + lines.length * lh + 1, "text-anchor": "middle", "class": "hours" }, g);
				th.textContent = horas + " h";
			}
			nodes[id] = g;
			return g;
		}
		drawNode("cbc", "CBC", null, "#2a211c", false, 100, 34);
		PLAN.materias.forEach(function (m) {
			drawNode(m.id, m.corto || m.nombre, m.horas, PLAN.areas[m.area].color, false);
		});
		PLAN.bloques.forEach(function (b) {
			drawNode(b.id, b.nombre, b.horas, b.id === "tesis" ? "#1f343a" : "#efe5d3", b.id !== "tesis");
		});

		// Interacción: resaltar cadena de correlativas
		var panel = document.getElementById("plan-panel");
		var panelEmpty = panel ? panel.innerHTML : "";
		function collect(id, dir, acc) {
			var next = dir === "up" ? ((byId[id] && byId[id].correl) || []) : (habilita[id] || []);
			next.forEach(function (n) { if (!acc[n]) { acc[n] = true; collect(n, dir, acc); } });
			return acc;
		}
		var current = null;
		function select(id) {
			current = id;
			svg.classList.toggle("has-focus", !!id);
			Object.keys(nodes).forEach(function (k) { nodes[k].classList.remove("is-related", "is-current"); });
			edges.forEach(function (e) { e.node.classList.remove("is-related"); });
			if (!id) { if (panel) panel.innerHTML = panelEmpty; return; }
			var up = collect(id, "up", {}), down = collect(id, "down", {});
			nodes[id].classList.add("is-current");
			Object.keys(up).concat(Object.keys(down)).forEach(function (k) { if (nodes[k]) nodes[k].classList.add("is-related"); });
			edges.forEach(function (e) {
				var upEdge = (e.to === id || up[e.to]) && (up[e.from]);
				var downEdge = (e.from === id || down[e.from]) && down[e.to];
				if (upEdge || downEdge) e.node.classList.add("is-related");
			});
			if (panel) panel.innerHTML = panelHTML(id);
		}
		function item(t, d) { return "<div><dt>" + t + "</dt><dd>" + d + "</dd></div>"; }
		function panelHTML(id) {
			if (id === "cbc") {
				return "<h3>Ciclo Básico Común</h3><p>Primer año de todas las carreras de la UBA. Es la correlativa de las materias marcadas con línea punteada.</p>";
			}
			var m = byId[id], h = "<h3>" + m.nombre + "</h3><dl>";
			if (m.bloque) {
				h += item("Cuándo", ORD[m.anio] + " año");
				if (m.horas) h += item("Carga horaria", m.horas + " horas");
				h += item("Detalle", m.texto) + "</dl>";
				return h;
			}
			var ar = PLAN.areas[m.area];
			h += item("Área", "<span class='area-dot' style='background:" + ar.color + "'></span>" + ar.nombre);
			h += item("Cuándo", cuatriTxt(m) + " · " + m.horas + " horas");
			h += item("Correlativas", m.correl.map(nombreDe).join(", "));
			var hab = habilita[id] || [];
			h += item("Habilita", hab.length ? hab.map(nombreDe).join(", ") : "—");
			if (m.nota) h += item("Equivalencias y notas", m.nota);
			if (m.programa) h += item("Programa", "<a href='" + m.programa + "'>Descargar programa</a>");
			return h + "</dl>";
		}
		Object.keys(nodes).forEach(function (id) {
			var g = nodes[id];
			g.addEventListener("mouseenter", function () { if (window.matchMedia("(hover: hover)").matches) select(id); });
			g.addEventListener("focus", function () { select(id); });
			g.addEventListener("click", function (e) { e.stopPropagation(); select(id); });
			g.addEventListener("keydown", function (e) {
				if (e.key === "Enter" || e.key === " ") { e.preventDefault(); select(id); }
				if (e.key === "Escape") { select(null); g.blur(); }
			});
		});
		document.addEventListener("click", function (e) { if (!e.target.closest("#plan-diagram") && !e.target.closest("#plan-panel")) select(null); });
	}

	/* ------------------------------------------------------------------
	   Tabla de materias por año (con detalle desplegable)
	   ------------------------------------------------------------------ */
	var table = document.getElementById("plan-table");
	if (table) {
		var html = "";
		for (var anio = 2; anio <= 6; anio++) {
			var delAnio = PLAN.materias.filter(function (m) { return m.anio === anio; });
			var horas = delAnio.reduce(function (s, m) { return s + m.horas; }, 0);
			html += "<div class='year-block reveal'><h3>" + ORD[anio] + " año" + (horas ? " <small>" + horas + " horas de materias obligatorias</small>" : "") + "</h3>";
			html += "<div class='table-wrap'><table class='subject-table'><thead><tr><th scope='col'>Materia</th><th scope='col' class='num'>Horas</th><th scope='col'>Correlativas</th></tr></thead><tbody>";
			[1, 2].forEach(function (cu) {
				var lista = delAnio.filter(function (m) { return m.cuatri === cu; });
				var bloques = PLAN.bloques.filter(function (b) { return b.anio === anio && b.cuatri === cu; });
				if (!lista.length && !bloques.length) return;
				html += "<tr class='cuatri-label'><td colspan='3'>" + (cu === 1 ? "Primer" : "Segundo") + " cuatrimestre</td></tr>";
				lista.forEach(function (m) {
					var did = "det-" + m.id;
					html += "<tr class='subject-row' tabindex='0' role='button' aria-expanded='false' aria-controls='" + did + "'>" +
						"<td><span class='area-dot' style='background:" + PLAN.areas[m.area].color + "'></span>" + m.nombre + "</td>" +
						"<td class='num'>" + m.horas + "</td><td>" + m.correl.map(nombreDe).join(", ") + "</td></tr>";
					var det = [];
					det.push("Área: " + PLAN.areas[m.area].nombre + ".");
					var hab = habilita[m.id] || [];
					if (hab.length) det.push("Es correlativa de: " + hab.map(nombreDe).join(", ") + ".");
					if (m.nota) det.push(m.nota + (m.resolucion ? " <a href='" + m.resolucion + "'>Ver resolución</a>" : ""));
					if (m.programa) det.push("<a href='" + m.programa + "'><svg aria-hidden='true'><use href='imgs/fosiles.svg#descarga'/></svg>Programa de la materia</a>");
					html += "<tr class='subject-detail' id='" + did + "' hidden><td colspan='3'>" + det.join("<br>") + "</td></tr>";
				});
				bloques.forEach(function (b) {
					html += "<tr><td><em>" + b.nombre + "</em></td><td class='num'>" + (b.horas || "—") + "</td><td>" + b.texto + "</td></tr>";
				});
			});
			html += "</tbody></table></div></div>";
		}
		table.innerHTML = html;
		table.querySelectorAll(".subject-row").forEach(function (row) {
			function toggle() {
				var det = document.getElementById(row.getAttribute("aria-controls"));
				var open = row.getAttribute("aria-expanded") === "true";
				row.setAttribute("aria-expanded", open ? "false" : "true");
				det.hidden = open;
			}
			row.addEventListener("click", function (e) { if (!e.target.closest("a")) toggle(); });
			row.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); toggle(); } });
		});
		// Las filas se crean después de que main.js activó las animaciones: mostrarlas
		table.querySelectorAll(".reveal").forEach(function (b) { b.classList.add("is-visible"); });
	}

	/* Totales calculados a partir de los datos */
	var tot = PLAN.materias.reduce(function (s, m) { return s + m.horas; }, 0);
	document.querySelectorAll("[data-total-obligatorias]").forEach(function (e) { e.textContent = tot.toLocaleString("es-AR"); });
	document.querySelectorAll("[data-cant-obligatorias]").forEach(function (e) { e.textContent = PLAN.materias.length; });
})();
