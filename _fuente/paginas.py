# Contenido de cada página. Cada "body" recibe ctx con helpers.
import math, random

def strata_svg():
    """Ilustración de estratos con fósiles para la portada."""
    random.seed(7)
    W, H = 1440, 720
    colores = ['#3a2a22', '#4a3226', '#5d3b27', '#6e4428', '#7e4a26', '#5a3a2a', '#3d2c24']
    tops = [300, 365, 430, 500, 565, 625, 680]
    depth = [0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16]
    s = [f'<svg class="hero__strata" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice" aria-hidden="true">',
         '<defs><linearGradient id="cielo" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1f343a"/><stop offset="1" stop-color="#2f4a52"/></linearGradient>',
         '<radialGradient id="velo" cx="50%" cy="45%" r="60%"><stop offset="0" stop-color="#1b1411" stop-opacity=".55"/><stop offset="1" stop-color="#1b1411" stop-opacity="0"/></radialGradient></defs>',
         f'<rect width="{W}" height="{H}" fill="url(#cielo)"/>']
    fosiles = {1: [('amonite', 180, 18, 70, 20)], 2: [('helecho', 1180, 8, 60, -12)], 3: [('trilobite', 420, 14, 56, 18), ('pez', 960, 20, 120, -6)],
               4: [('amonite', 1300, 10, 52, 40)], 5: [('columna', 640, 16, 110, 8)], 6: [('trilobite', 90, 6, 40, -20)]}
    for i, (top, col) in enumerate(zip(tops, colores)):
        amp = 10 + i * 3
        pts = []
        for x in range(-40, W + 81, 80):
            pts.append((x, top + amp * math.sin(x / 210 + i * 1.3) + random.uniform(-5, 5)))
        d = f'M{pts[0][0]} {pts[0][1]:.1f} ' + ' '.join(f'Q{x - 40} {y + random.uniform(-8, 8):.1f} {x} {y:.1f}' for x, y in pts[1:])
        d += f' L{W + 60} {H + 200} L-60 {H + 200} Z'
        g = f'<g class="layer" data-depth="{-depth[i]:.2f}"><path d="{d}" fill="{col}"/>'
        # vetas finas dentro de la capa
        g += f'<path d="{d.split(" L")[0]}" fill="none" stroke="#f6d9a8" stroke-opacity=".10" stroke-width="1.2" transform="translate(0 {14 + i})"/>'
        for (sym, x, dy, size, rot) in fosiles.get(i, []):
            y = top + dy + 10
            g += f'<use href="imgs/fosiles.svg#{sym}" x="{x}" y="{y}" width="{size}" height="{size}" color="#f6d9a8" opacity=".32" transform="rotate({rot} {x + size / 2} {y + size / 2})"/>'
        s.append(g + '</g>')
    s.append(f'<rect width="{W}" height="{H}" fill="url(#velo)"/></svg>')
    return '\n'.join(s)


FOTOS = {
    'hero-ischigualasto': ('Barrancas del Valle de la Luna, Parque Provincial Ischigualasto, San Juan', 'Paulakindsvater', 'CC BY-SA 4.0', 'https://commons.wikimedia.org/wiki/File:Vista_del_valle_de_la_luna.jpg', 2400, 1600),
    'campo-embochonando': ('Paleontólogos protegiendo un fósil con un bochón de yeso durante una excavación', 'Nicolás D. Farroni', 'CC BY-SA 4.0', 'https://commons.wikimedia.org/wiki/File:Embochonando.jpg', 960, 640),
    'campo-acarreando': ('Paleontólogos transportando un hueso de dinosaurio protegido con yeso', 'Paleoninja', 'CC BY 4.0', 'https://commons.wikimedia.org/wiki/File:Acarreando_huesos_de_dinosaurio.jpg', 1200, 801),
    'doctorado-laboratorio-campo': ('Paleontólogos observando microfósiles con una lupa en un laboratorio de campo, Patagonia norte', 'Paleoninja', 'CC BY 4.0', 'https://commons.wikimedia.org/wiki/File:Laboratorio_port%C3%A1til.jpg', 1200, 801),
    'estudiantes-laboratorio': ('Estudiantes trabajando con restos fósiles en un laboratorio universitario de paleontología', 'Е. С. Поданёва', 'CC BY-SA 4.0', 'https://commons.wikimedia.org/wiki/File:%D0%9B%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%B8%D1%8F_%D0%BA%D0%BE%D0%BD%D1%82%D0%B8%D0%BD%D0%B5%D0%BD%D1%82%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D1%85_%D1%8D%D0%BA%D0%BE%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC_%D0%BC%D0%B5%D0%B7%D0%BE%D0%B7%D0%BE%D1%8F_%D0%B8_%D0%BA%D0%B0%D0%B9%D0%BD%D0%BE%D0%B7%D0%BE%D1%8F_%D0%9D%D0%98_%D0%A2%D0%93%D0%A3_(%D0%A2%D0%BE%D0%BC%D1%81%D0%BA)_07.JPG', 1800, 1200),
    'fosil-bagualia': ('Diente fósil de Bagualia hallado en la excavación del holotipo', 'Sreuil', 'CC BY-SA 4.0', 'https://commons.wikimedia.org/wiki/File:Bagualia_teeth_at_the_excavation_site.jpg', 1200, 900),
}

def credito(n):
    alt, autor, lic, url, w, h = FOTOS[n]
    return f'Foto: <a href="{url}">{autor}</a>, {lic}'

def foto(n):
    """Foto provisoria (Wikimedia Commons) con su crédito, que exige la licencia."""
    alt, autor, lic, url, w, h = FOTOS[n]
    return f'<figure class="figure-photo"><img src="imgs/fotos/{n}.jpg" alt="{alt}" width="{w}" height="{h}" loading="lazy"><figcaption>{credito(n)}</figcaption></figure>'

def banner(n, pos=''):
    alt, autor, lic, url, w, h = FOTOS[n]
    st = f' style="object-position:{pos}"' if pos else ''
    return f'<figure class="figure-banner"><img src="imgs/fotos/{n}.jpg" alt="{alt}" width="{w}" height="{h}"{st}><figcaption>{credito(n)}</figcaption></figure>'

def ph(sym, caption, variant=''):
    v = f' figure-placeholder--{variant}' if variant else ''
    return f'<figure class="figure-placeholder{v}"><svg aria-hidden="true"><use href="imgs/fosiles.svg#{sym}"/></svg><figcaption>{caption}</figcaption></figure>'


# ---------------------------------------------------------------- INICIO
def inicio(c):
    ico = c['ico']
    return f'''<section class="hero">
	<div class="container">
		<div class="hero__frame">
			<img class="hero__photo" src="imgs/fotos/hero-ischigualasto.jpg" alt="" width="2400" height="1600" fetchpriority="high">
			<div class="hero__content">
				<h1>Estudiá <em>Paleontología</em></h1>
				<p>Para develar el pasado de la vida en la larga historia de la Tierra hay que conocer sobre biología y también sobre geología. La Licenciatura en Paleontología de Exactas UBA integra las dos.</p>
				<div class="hero__cta">
					<a class="btn btn--primary" href="ingresantes.html">Quiero estudiar {ico('flecha')}</a>
					<a class="btn btn--light" href="carrera.html">Ver el plan de estudios</a>
				</div>
			</div>
			<a class="hero__scroll" href="#intro">Descubrí más</a>
			<p class="hero__credit">Valle de la Luna, Ischigualasto. {credito('hero-ischigualasto')}</p>
		</div>
	</div>
</section>

<section class="section" id="intro">
	<div class="container">
		<p class="quote reveal">La <b>Paleontología</b> da entrada al mundo de los restos fósiles: <em>los primeros organismos unicelulares, los metazoos, los grandes dinosaurios, las plantas</em> y las estructuras geológicas que cuentan sobre el ambiente en el que vivió cada organismo.</p>
	</div>
</section>

<section class="section section--tight">
	<div class="container">
		<div class="split">
			<div class="reveal offset-frame">{foto('campo-embochonando')}</div>
			<div class="reveal">
				<h2 class="title-duo"><span>¿Qué hace un/a</span><strong>paleontólogo/a?</strong></h2>
				<p>La paleontología es una ciencia que integra aspectos de índole geológica y biológica. Quienes egresan de la carrera estudian la historia de la vida sobre la Tierra a partir del registro fósil: desde debates actuales de biología evolutiva, sistemática y paleobiología hasta los procesos geológicos que actuaban cuando el fósil era aún un organismo vivo y las posibles causas de eventos mayores como las extinciones masivas.</p>
				<p>La formación es interdisciplinaria y permite desempeñarse en investigación, en la industria del petróleo, en museos, en la protección del patrimonio paleontológico y en la divulgación científica.</p>
				<a class="btn btn--primary" href="ingresantes.html#que-es">Leer más {ico('flecha')}</a>
			</div>
		</div>
	</div>
</section>

<section class="section section--slate">
	<div class="container">
		<div class="stats reveal">
			<div class="stat"><span class="stat__num">2001</span><span class="stat__label">año de creación de la carrera</span></div>
			<div class="stat"><span class="stat__num">20</span><span class="stat__label">materias obligatorias</span></div>
			<div class="stat"><span class="stat__num">800</span><span class="stat__label">créditos de optativas para orientar tu formación</span></div>
			<div class="stat"><span class="stat__num">4</span><span class="stat__label">departamentos de Exactas ofrecen materias</span></div>
		</div>
	</div>
</section>

<section class="section">
	<div class="container">
		<div class="split split--reverse split--top">
			<div class="reveal offset-frame">{foto('campo-acarreando')}</div>
			<div class="reveal">
				<h2 class="title-duo"><span>¿Por qué estudiar</span><strong>paleontología?</strong></h2>
				<h3 class="c-terracotta" style="font-size:1.05rem">Campo laboral</h3>
				<p>Los egresados y las egresadas se pueden dedicar a la investigación dentro de la Facultad y en institutos de investigación de todo el país. El título tiene validez nacional y, en el marco de la Ley 25.743 de Protección del Patrimonio Arqueológico y Paleontológico, habilita para:</p>
				<ul class="arrow-list">
					<li>Asesorar a los organismos encargados de la preservación y tutela del patrimonio paleontológico.</li>
					<li>Integrar las autoridades de aplicación y los registros oficiales de yacimientos, colecciones y restos paleontológicos.</li>
					<li>Determinar fósiles con fines bioestratigráficos, con amplia aplicación en la industria petrolera.</li>
					<li>Actuar como perito judicial en la determinación, valoración y origen de fósiles.</li>
					<li>Trabajar en museos, en extensión científica y en medios de comunicación.</li>
				</ul>
				<a class="btn btn--primary" href="ingresantes.html#campo-laboral">Leer más {ico('flecha')}</a>
			</div>
		</div>
	</div>
</section>

<section class="section section--sand">
	<div class="container">
		<span class="eyebrow">Áreas de estudio</span>
		<h2 class="title-duo reveal"><span>Un abanico de</span><strong>especialidades</strong></h2>
		<div class="cards cards--compact">
			<div class="card reveal">{ico('columna', 'card__icon card__icon--wide')}<h3>Paleontología de Vertebrados</h3><p>Peces, anfibios, reptiles, dinosaurios, aves y mamíferos del pasado.</p></div>
			<div class="card reveal">{ico('trilobite', 'card__icon')}<h3>Paleontología de Invertebrados</h3><p>Trilobites, amonites, braquiópodos y otros grupos que dominaron los mares antiguos.</p></div>
			<div class="card reveal">{ico('helecho', 'card__icon')}<h3>Paleobotánica y Palinología</h3><p>Plantas fósiles, polen y esporas para reconstruir la vegetación y el clima del pasado.</p></div>
			<div class="card reveal">{ico('amonite', 'card__icon')}<h3>Micropaleontología y Bioestratigrafía</h3><p>Microfósiles para datar las rocas y reconstruir ambientes, clave en la industria del petróleo.</p></div>
			<div class="card reveal">{ico('pez', 'card__icon card__icon--wide')}<h3>Paleoecología y Tafonomía</h3><p>Cómo vivían los organismos, cómo se fosilizaron y qué nos cuentan sobre el ambiente.</p></div>
		</div>
	</div>
</section>

<section class="section">
	<div class="container">
		<div class="quick-links reveal">
			<ul>
				<li><a href="ingresantes.html#como-ingresar">Requisitos para ingresar <span class="box">{ico('flecha')}</span></a></li>
				<li><a href="carrera.html">Plan de estudios <span class="box">{ico('flecha')}</span></a></li>
				<li><a href="carrera.html#correlatividades">Correlatividades <span class="box">{ico('flecha')}</span></a></li>
				<li><a href="tesis.html">Tesis de licenciatura <span class="box">{ico('flecha')}</span></a></li>
				<li><a href="mailto:{c['MAIL']}">Contactanos <span class="box">{ico('flecha')}</span></a></li>
			</ul>
		</div>
	</div>
</section>

<section class="section section--tight">
	<div class="container">
		<div class="split">
			<div class="reveal">
				<h2 class="title-duo"><span>Un ámbito natural</span><strong>para la paleontología</strong></h2>
				<p>Exactas UBA, con sus departamentos de Ciencias Geológicas, Ciencias Biológicas y Ciencias de la Atmósfera y los Océanos, cuenta con un importante caudal de recursos humanos en todos los niveles de la carrera docente.</p>
				<p>En el área de Paleontología del Departamento de Ciencias Geológicas se atesoran numerosas <strong>colecciones de fósiles</strong>, muchas de ellas con fines didácticos, una amplia y actualizada <strong>biblioteca</strong> especializada y <strong>equipamiento de campo y laboratorio</strong>. Esto permite enseñar la paleontología con su enfoque clásico y, a la vez, con un uso creciente de la tecnología en proyectos de laboratorio.</p>
			</div>
			<div class="reveal offset-frame">{foto('fosil-bagualia')}</div>
		</div>
	</div>
</section>

<section class="section">
	<div class="container">
		<p class="quote reveal" style="text-align:center">¿Tenés dudas sobre la cursada? <b>Escribinos.</b></p>
		<p style="text-align:center;margin-top:24px" class="reveal"><a class="btn btn--outline" href="mailto:{c['MAIL']}">{ico('mail')}{c['MAIL']}</a></p>
	</div>
</section>
'''


# ---------------------------------------------------------------- INGRESANTES
def ingresantes(c):
    ico, ph_ = c['ico'], ph
    return c['page_hero']('Ingresantes', 'Todo lo que necesitás saber para empezar la Licenciatura en Paleontología: qué es, qué se estudia, para qué te habilita el título y cómo inscribirte.', 'piqueta', 'Licenciatura en Paleontología') + c['page_index']([
        ('que-es', '¿Qué es la paleontología?'), ('perfil', 'Perfil del egresado'), ('por-que', '¿Por qué estudiarla?'),
        ('campo-laboral', 'Campo laboral e incumbencias'), ('como-ingresar', 'Cómo ingresar'), ('contacto', 'Contacto')]) + f'''
<section class="section" id="que-es">
	<div class="container">
		<div class="split split--top">
			<div class="reveal">
				<h2 class="title-duo"><span>¿Qué es la</span><strong>paleontología?</strong></h2>
				<p>Para develar el pasado de la vida en la larga historia de la Tierra hay que conocer sobre biología y también sobre geología. La Licenciatura en Paleontología es una amalgama de ambas, pero con características únicas: concentra los conocimientos más específicos de esas dos áreas y da entrada al mundo de los restos fósiles, tales como los primeros organismos unicelulares, los metazoos, los grandes dinosaurios, las plantas y las estructuras geológicas que cuentan sobre el ambiente en el que vivió cada organismo.</p>
				<p>Por eso la carrera exige cursar materias tanto en los departamentos de Ciencias Biológicas como en el de Ciencias Geológicas, y reconoce formalmente esta dualidad de la disciplina.</p>
			</div>
			<div class="reveal"><figure class="collage"><div class="collage__grid"><div class="collage__tile"><img src="imgs/fotos/collage-microfosiles.jpg" alt="Microfósiles en roca" width="640" height="480" loading="lazy"><span>Microfósiles</span></div><div class="collage__tile"><img src="imgs/fotos/collage-amonite.jpg" alt="Amonite de la Formación Agrio, Neuquén" width="640" height="480" loading="lazy"><span>Invertebrados</span></div><div class="collage__tile"><img src="imgs/fotos/collage-giganotosaurus.jpg" alt="Cráneo de Giganotosaurus carolinii" width="640" height="480" loading="lazy"><span>Dinosaurios</span></div><div class="collage__tile"><img src="imgs/fotos/collage-helecho.jpg" alt="Helecho fósil" width="640" height="480" loading="lazy"><span>Plantas</span></div></div><figcaption>Fotos: <a href="https://commons.wikimedia.org/wiki/File:Microfossils.JPG">ZooFari</a> (CC BY 3.0), <a href="https://commons.wikimedia.org/wiki/File:Ammonite_de_la_Formaci%C3%B3n_Agrio.jpg">Fernando Archuby</a> (CC BY-SA 4.0), <a href="https://commons.wikimedia.org/wiki/File:Esqueleto_articulado,_Giganotosaurus_carolinii.jpg">Rjcastillo</a> (CC BY-SA 4.0), <a href="https://commons.wikimedia.org/wiki/File:Dennstaedtia_americana_(fossil_fern)_(Fort_Union_Formation,_Paleocene;_Yellowstone_County,_Montana,_USA).jpg">James St. John</a> (CC BY 2.0)</figcaption></figure></div>
		</div>
	</div>
</section>

<section class="section section--sand" id="perfil">
	<div class="container">
		<div class="prose reveal">
			<h2>Perfil del egresado</h2>
			<p>La carrera brinda una robusta preparación teórica y práctica, acorde con las exigencias actuales de una disciplina que abarca campos tan disímiles como la bioestratigrafía y la indagación teórica sobre problemas evolutivos.</p>
			<p>Los y las estudiantes aprenden sobre debates actuales en biología evolutiva, sistemática y paleobiología, a analizar problemas desde un punto de vista cuantitativo y a diseñar experimentos que permitan resolver problemas de macroevolución y del estudio de los organismos fósiles. Los conocimientos en geología permiten comprender tanto el ambiente local donde se depositó el organismo fosilizado como los procesos geológicos generales que actuaban cuando el fósil era aún un organismo vivo, y las posibles causas de eventos mayores como las extinciones masivas.</p>
			<p>La formación interdisciplinaria permite desempeñarse en tareas aplicadas, como la industria del petróleo, museos, extensión científica o la relación con los medios, y acceder a estudios de posgrado, incluido el <a href="doctorado.html">Doctorado de la UBA en el área Paleontología</a>.</p>
		</div>
	</div>
</section>

<section class="section" id="por-que">
	<div class="container">
		<h2 class="title-duo reveal"><span>Objetivos</span><strong>de la carrera</strong></h2>
		<div class="cards">
			<div class="card reveal"><span class="card__num">1</span><p>Preparar profesionales idóneos para realizar todos los trabajos específicos relacionados con la actividad paleontológica, en el contexto de una formación de excelencia.</p></div>
			<div class="card reveal"><span class="card__num">2</span><p>Promover el análisis, la comprensión y la fijación de conocimientos teóricos sólidos, complementados con un entrenamiento práctico intensivo desde el comienzo de la carrera.</p></div>
			<div class="card reveal"><span class="card__num">3</span><p>Contribuir a la profundización de los conocimientos de las ciencias básicas que constituyen los cimientos del quehacer paleontológico.</p></div>
			<div class="card reveal"><span class="card__num">4</span><p>Dotar a cada estudiante de los conocimientos necesarios para realizar actividades de investigación, o ligadas más directamente a aspectos productivos y de extensión.</p></div>
		</div>
	</div>
</section>

<section class="section section--slate" id="campo-laboral">
	<div class="container">
		<div class="prose reveal" style="max-width:none">
			<h2 style="color:#fff">Campo laboral e incumbencias</h2>
			<p style="max-width:820px">El título de Licenciado/a en Paleontología tiene <strong>reconocimiento oficial y validez nacional</strong> (Resolución N.º 922/2014 del Ministerio de Educación de la Nación). La Ley Nacional 25.743 de Protección del Patrimonio Arqueológico y Paleontológico establece que los yacimientos paleontológicos son del dominio del Estado y que su defensa, estudio y conservación son de interés público. En ese marco, quienes egresan tienen incumbencias para:</p>
		</div>
		<div class="cards cards--3" style="margin-top:30px">
			<div class="card reveal"><span class="card__num">1</span><h3>Asesoramiento</h3><p>Asesorar a los organismos competentes encargados de la preservación, protección y tutela del patrimonio paleontológico como parte del patrimonio cultural de la Nación.</p></div>
			<div class="card reveal"><span class="card__num">2</span><h3>Autoridades de aplicación</h3><p>Integrar las autoridades competentes, nacionales, provinciales o de la Ciudad de Buenos Aires, en el cumplimiento de las leyes de protección del patrimonio paleontológico.</p></div>
			<div class="card reveal"><span class="card__num">3</span><h3>Registros oficiales</h3><p>Actuar en los registros oficiales de yacimientos, colecciones y restos paleontológicos.</p></div>
			<div class="card reveal"><span class="card__num">4</span><h3>Conservación del patrimonio</h3><p>Trabajar en los departamentos de conservación del patrimonio y en el relevamiento de yacimientos y de lugares con potencial paleontológico.</p></div>
			<div class="card reveal"><span class="card__num">5</span><h3>Bioestratigrafía e industria</h3><p>Asesorar en la determinación de fósiles con fines bioestratigráficos (micropaleontología, palinología, megafósiles) para establecer la edad y el ambiente de sedimentación, con amplia aplicación en la industria petrolera.</p></div>
			<div class="card reveal"><span class="card__num">6</span><h3>Peritajes</h3><p>Actuar como perito judicial, de parte o de oficio, en la determinación, valoración y origen de fósiles.</p></div>
		</div>
	</div>
</section>

<section class="section" id="como-ingresar">
	<div class="container">
		<h2 class="title-duo reveal"><span>Cómo</span><strong>ingresar</strong></h2>
		<div class="split split--top">
			<ol class="steps reveal">
				<li><h3>Inscribite en el CBC</h3><p>Como todas las carreras de la UBA, la licenciatura empieza con el Ciclo Básico Común. Las inscripciones se hacen en <a href="https://www.cbc.uba.ar/">cbc.uba.ar</a>.</p></li>
				<li><h3>Cursá las materias del CBC</h3><p>Análisis Matemático, Biología, Física, Química, Introducción al Pensamiento Científico e Introducción al Conocimiento de la Sociedad y el Estado.</p></li>
				<li><h3>Seguí en Exactas</h3><p>Con el CBC aprobado continuás con el ciclo obligatorio de la carrera en la Facultad de Ciencias Exactas y Naturales. Mirá el <a href="carrera.html">plan de estudios</a>.</p></li>
			</ol>
			<div class="reveal">
				<div class="note"><strong>¿Todavía estás eligiendo carrera?</strong><br>La Dirección de Orientación Vocacional de Exactas te ayuda a conocer todas las carreras de la Facultad: <a href="https://exactas.uba.ar/extension/ov/">exactas.uba.ar/extension/ov</a>.</div>
				<ul class="doc-list">
					<li><a href="archivos/folleto-paleontologia.pdf">{ico('descarga')}<span>Folleto informativo de la Licenciatura<small>PDF</small></span></a></li>
					<li><a href="carrera.html">{ico('flecha')}<span>Plan de estudios y correlatividades<small>Materias, horas y recorrido</small></span></a></li>
					<li><a href="https://exactas.uba.ar/ensenanza/carreras-de-grado/paleontologia/">{ico('externo')}<span>La carrera en el sitio de Exactas<small>exactas.uba.ar</small></span></a></li>
				</ul>
			</div>
		</div>
	</div>
</section>

<section class="section section--sand" id="contacto">
	<div class="container">
		<div class="prose reveal">
			<h2>Contacto</h2>
			<ul class="arrow-list">
				<li>Dudas sobre cómo inscribirte en el CBC o en las carreras de la Facultad: <a href="https://www.cbc.uba.ar/">www.cbc.uba.ar</a> y <a href="https://exactas.uba.ar/">exactas.uba.ar</a>.</li>
				<li>Dudas sobre qué carreras se dictan en la Facultad: <a href="https://exactas.uba.ar/extension/ov/">Orientación Vocacional</a>.</li>
				<li>Dudas específicas sobre la cursada de Paleontología: escribinos a <a href="mailto:{c['MAIL']}">{c['MAIL']}</a>.</li>
			</ul>
		</div>
	</div>
</section>
'''


# ---------------------------------------------------------------- PLAN DE ESTUDIOS
ELECTIVAS = [
    ('Departamento de Ciencias Geológicas', [('Análisis de Ambientes Continentales', 128, 128), ('Cuencas Sedimentarias', 160, 160), ('Escuela de Campo', 50, 50),
        ('Estratigrafía', 80, 80), ('Geología Ambiental', 160, 160), ('Geología Histórica', 160, 160), ('Geología Marina', 160, 160), ('Geología Regional', 160, 160),
        ('Geología y Ecología de Ambientes Costeros', 128, 128), ('Geomorfología', 160, 160), ('Geoquímica', 128, 128), ('Geotectónica', 160, 160),
        ('Levantamiento Geológico', 160, 160), ('Fotointerpretación', 160, 160), ('Palinoestratigrafía', 160, 160), ('Paleoecología', 128, 128),
        ('Sedimentología', 160, 160), ('Rocas Carbonáticas: Ambientes Depositacionales y Petrología', 80, 96)]),
    ('Departamento de Ecología, Genética y Evolución', [('Biometría II', 160, 160), ('Ecología Ambiental', 192, 160), ('Ecología de Comunidades y Ecosistemas', 192, 160),
        ('Ecología de Poblaciones', 192, 160), ('Ecología General', 208, 192), ('Ecología Regional', 192, 160), ('Ecología y Comportamiento Animal', 208, 160),
        ('Limnología', 288, 160), ('Sistemática Teórica', 160, 160)]),
    ('Departamento de Biodiversidad y Biología Experimental', [('Anatomía Vegetal', 128, 160), ('Biología Celular', 288, 160), ('Biología Comparada de Protistas', 192, 160),
        ('Biología de Cyanobacterias', 192, 192), ('Botánica Económica', 100, 120), ('Elementos de Biología Floral', 210, 160), ('Fisiología Animal Comparada', 224, 160),
        ('Fisiología Vegetal', 192, 160), ('Histología Animal', 256, 160), ('Invertebrados I', 256, 160), ('Invertebrados II', 240, 240),
        ('Morfología de Criptógamas', 224, 160), ('Sistemática de Plantas Vasculares', 180, 160)]),
    ('Departamento de Ciencias de la Atmósfera y los Océanos', [('Oceanografía General', 128, 160), ('Paleo y Neoclima', 128, 128)]),
]
OPTATIVAS = [('Actuopaleontología', 128, 128), ('Biología de la Reproducción y el Desarrollo', 160, 160), ('Geología del Cuaternario', 64, 64),
             ('Paleobiología', 128, 160), ('Paleontología Cuantitativa', 80, 80), ('Tafonomía aplicada al análisis del registro sedimentario', 64, 64)]

def tabla_electivas(rows):
    t = '<div class="table-wrap"><table><thead><tr><th scope="col">Materia</th><th scope="col" class="num">Créditos según plan</th><th scope="col" class="num">Carga horaria (2019)</th></tr></thead><tbody>'
    for n, cr, hs in rows:
        t += f'<tr><td>{n}</td><td class="num">{cr}</td><td class="num">{hs}</td></tr>'
    return t + '</tbody></table></div>'

def carrera(c):
    areas = [('#b4532a', 'Paleontología'), ('#c68b2c', 'Geología'), ('#5f7a3a', 'Biología'), ('#2f4a52', 'Química, física y matemática'), ('#3c7aa0', 'Ciencias de la atmósfera y los océanos')]
    legend = ''.join(f'<li><i style="background:{col}"></i>{n}</li>' for col, n in areas)
    acc = ''
    for dep, rows in ELECTIVAS:
        acc += f'<details><summary>Electivas · {dep.replace("Departamento de ", "")} <small>{len(rows)} materias</small></summary><div class="accordion__body">{tabla_electivas(rows)}</div></details>'
    acc += f'<details><summary>Optativas <small>{len(OPTATIVAS)} materias</small></summary><div class="accordion__body">{tabla_electivas(OPTATIVAS)}</div></details>'
    return c['page_hero']('Plan de <em>estudios</em>', 'La Licenciatura en Paleontología combina materias de los departamentos de Ciencias Geológicas, Biodiversidad y Biología Experimental, Ecología, Genética y Evolución, y Ciencias de la Atmósfera y los Océanos.', 'estratos', 'Carrera presencial') + c['page_index']([
        ('recorrido', 'Recorrido'), ('cbc', 'CBC'), ('correlatividades', 'Correlatividades'), ('obligatorias', 'Materias obligatorias'),
        ('orientacion', 'Optativas y electivas'), ('totales', 'Carga horaria')]) + f'''
<section class="section section--tight" id="recorrido">
	<div class="container">
		<h2 class="title-duo reveal"><span>Recorrido</span><strong>académico</strong></h2>
		<div class="journey reveal">
			<div class="journey__step"><div class="journey__circle">CBC</div><p>Primer año: Ciclo Básico Común de la UBA, con seis materias.</p></div>
			<div class="journey__step"><div class="journey__circle">Ciclo obligatorio</div><span class="journey__hours"><span data-total-obligatorias>2.874</span> h</span><p><span data-cant-obligatorias>20</span> materias obligatorias de 2.º a 5.º año.</p></div>
			<div class="journey__step"><div class="journey__circle">Ciclo de orientación</div><span class="journey__hours">800 créditos</span><p>Optativas y electivas elegidas con tu tutor/a según tu orientación.</p></div>
			<div class="journey__step"><div class="journey__circle">Tesis de Licenciatura</div><span class="journey__hours">160 h</span><p>Un trabajo de investigación original con defensa oral y pública.</p></div>
		</div>
	</div>
</section>

<section class="section section--tight" id="cbc">
	<div class="container">
		<div class="prose reveal">
			<h2>Ciclo Básico Común</h2>
			<p>El primer año de la carrera es el Ciclo Básico Común. Sus materias para la Licenciatura en Paleontología son:</p>
			<ol>
				<li>Análisis Matemático</li>
				<li>Biología</li>
				<li>Física</li>
				<li>Química</li>
				<li>Introducción al Pensamiento Científico</li>
				<li>Introducción al Conocimiento de la Sociedad y el Estado</li>
			</ol>
		</div>
	</div>
</section>

<section class="section section--tight" id="correlatividades">
	<div class="container">
		<h2 class="title-duo reveal"><span>Mapa de</span><strong>correlatividades</strong></h2>
		<p class="lead reveal" style="max-width:780px">Pasá el cursor (o tocá) cualquier materia para ver qué necesitás aprobar antes y qué materias habilita.</p>
		<ul class="legend reveal">{legend}<li><i style="background:#efe5d3;border:1px dashed #b4532a"></i>Optativas y electivas</li></ul>
		<div class="diagram-layout">
			<div class="diagram-wrap">
				<p class="diagram-hint">En pantallas chicas, deslizá el diagrama hacia los costados.</p>
				<svg id="plan-diagram" role="group" aria-label="Diagrama de correlatividades del plan de estudios"></svg>
			</div>
			<aside class="plan-panel" id="plan-panel" aria-live="polite">
				<h3>Elegí una materia en el diagrama</h3>
				<p class="empty">Acá vas a ver sus correlativas, las materias que habilita, la carga horaria y el enlace al programa.</p>
			</aside>
		</div>
	</div>
</section>

<section class="section" id="obligatorias">
	<div class="container">
		<h2 class="title-duo reveal"><span>Materias</span><strong>obligatorias</strong></h2>
		<p class="lead reveal" style="max-width:780px">Organización sugerida por año y cuatrimestre. Tocá una materia para ver sus equivalencias y descargar el programa.</p>
		<div id="plan-table"><noscript><p>Para ver la tabla de materias es necesario activar JavaScript.</p></noscript></div>
	</div>
</section>

<section class="section section--sand" id="orientacion">
	<div class="container">
		<div class="split split--top">
			<div class="reveal">
				<h2 class="title-duo"><span>Ciclo de</span><strong>orientación</strong></h2>
				<p>El ciclo de orientación está formado por materias <strong>optativas y electivas</strong> que otorgan créditos según su carga horaria. Para completarlo hay que acreditar <strong>800 créditos</strong>.</p>
				<p>Cada estudiante arma su plan de materias junto con un tutor o una tutora, de acuerdo con la orientación que quiera seguir (por ejemplo, paleovertebrados, paleobotánica o bioestratigrafía). Más información en <a href="estudiantes.html#tutor">Plan de materias y tutor</a>.</p>
				<div class="note">Listado de electivas actualizado en 2025. La columna «Créditos según plan» es la que se usa para acreditar el ciclo.</div>
			</div>
			<div class="accordion reveal">{acc}</div>
		</div>
	</div>
</section>

<section class="section" id="totales">
	<div class="container">
		<h2 class="title-duo reveal"><span>Carga horaria</span><strong>de la carrera</strong></h2>
		<div class="totals reveal">
			<div class="total"><b><span data-total-obligatorias>2.874</span> h</b><span>Materias obligatorias del ciclo superior</span></div>
			<div class="total"><b>800</b><span>Créditos del ciclo de orientación (optativas y electivas)</span></div>
			<div class="total"><b>160 h</b><span>Tesis de Licenciatura</span></div>
		</div>
		<p class="reveal" style="margin-top:24px;color:var(--ink-soft)">A esto se suma el Ciclo Básico Común. Fuente: plan de estudios publicado por la Comisión de Carrera.</p>
	</div>
</section>
'''


# ---------------------------------------------------------------- ESTUDIANTES
EQUIV = [('Biodiversidad de Animales', 'Introducción a la Zoología', ''), ('Biodiversidad de Vegetales', 'Introducción a la Botánica', ''),
         ('Evolución para Paleontólogos', 'Evolución', ''), ('Física para Paleontólogos', 'Electromagnetismo y Óptica (la reemplaza)', 'Res. CD 1911/2023'),
         ('Genética General para Paleontólogos', 'Genética I', 'Res. CD 114/2006'), ('Int. a la Biología Molecular para Paleontólogos', 'Introducción a la Biología Molecular y Celular', ''),
         ('Química General e Inorgánica para Paleontólogos', 'Química General e Inorgánica I', 'Res. CD 2510/2017'), ('Química Orgánica para Paleontólogos', 'Química Orgánica', '')]

def estudiantes(c):
    ico = c['ico']
    progs = sorted(A_PROG(c), key=lambda x: x[1])
    grid = ''.join(f'<li><a href="archivos/programas/{n}.pdf">{ico("descarga")}{d}</a></li>' for n, d in progs)
    eq = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{r}</td></tr>' for a, b, r in EQUIV)
    return c['page_hero']('Estudiantes', 'Trámites, tutorías, programas de las materias y equivalencias para quienes ya cursan la carrera.', 'microscopio', 'Información para la cursada') + f'''<section class="photo-banner reveal"><div class="container">{banner('estudiantes-laboratorio', 'center 35%')}</div></section>
''' + c['page_index']([
        ('tutor', 'Plan de materias y tutor'), ('programas', 'Programas'), ('equivalencias', 'Equivalencias'), ('tesis', 'Tesis'), ('documentos', 'Documentos')]) + f'''
<section class="section" id="tutor">
	<div class="container">
		<div class="split split--top">
			<div class="prose reveal">
				<h2>Plan de materias y tutor</h2>
				<p>Para el ciclo de orientación, cada estudiante presenta a la Comisión de Carrera un <strong>plan de materias optativas y electivas</strong> avalado por un tutor o una tutora. Es <strong>imprescindible</strong> leer el reglamento que corresponda según el trámite a realizar.</p>
				<h3>Qué tiene que incluir la carta de presentación del plan</h3>
				<ul class="arrow-list">
					<li>La orientación general que piensa seguir el/la estudiante (por ejemplo, paleovertebrados, paleobotánica o bioestratigrafía).</li>
					<li>El cuatrimestre y el año en que se cursará cada materia.</li>
					<li>Una justificación de cada una de las materias seleccionadas.</li>
				</ul>
				<h3>Qué tiene que indicar el tutor o la tutora</h3>
				<ul class="arrow-list">
					<li>Que el/la estudiante no cursó más de 2 materias o 400 créditos de optativas al momento de presentar el plan (Art. I.e del reglamento).</li>
					<li>Si considera que el/la estudiante está lo suficientemente avanzado/a en las materias obligatorias como para comenzar con las optativas.</li>
				</ul>
			</div>
			<div class="reveal">
				<ul class="doc-list">
					<li><a href="archivos/modelos/carta-plan-de-estudios-2026.docx">{ico('descarga')}<span>Modelo de carta para plan de estudios (2026)<small>Para presentar el plan de optativas · Word</small></span></a></li>
					<li><a href="archivos/reglamentos/reglamento-tutores-y-planes-de-estudio.pdf">{ico('descarga')}<span>Reglamento de tutores y planes de estudio</span></a></li>
					<li><a href="carrera.html#orientacion">{ico('flecha')}<span>Listado de optativas y electivas<small>Con créditos de cada materia</small></span></a></li>
				</ul>
			</div>
		</div>
	</div>
</section>

<section class="section section--sand" id="programas">
	<div class="container">
		<h2 class="title-duo reveal"><span>Programas de</span><strong>materias obligatorias</strong></h2>
		<p class="reveal" style="max-width:780px">Las materias Ambientes Sedimentarios, Bioestratigrafía, Fundamentos de Micropaleontología, Fundamentos de Sedimentología y Estratigrafía y Geología General todavía no tienen programa publicado.</p>
		<ul class="doc-grid reveal">{grid}</ul>
	</div>
</section>

<section class="section" id="equivalencias">
	<div class="container">
		<h2 class="title-duo reveal"><span>Equivalencias con</span><strong>Ciencias Biológicas</strong></h2>
		<p class="reveal" style="max-width:780px">Varias materias obligatorias se reconocen por equivalencia a quienes aprobaron la materia correspondiente de la Licenciatura en Ciencias Biológicas.</p>
		<div class="table-wrap reveal"><table><thead><tr><th scope="col">Materia de Paleontología</th><th scope="col">Materia de Biología equivalente</th><th scope="col">Resolución</th></tr></thead><tbody>{eq}</tbody></table></div>
	</div>
</section>

<section class="section section--slate" id="tesis">
	<div class="container">
		<div class="split">
			<div class="reveal">
				<h2 class="title-duo"><span style="color:#f6d9a8">Tesis de</span><strong style="color:#fff">Licenciatura</strong></h2>
				<p>La tesis es una materia obligatoria que te inicia en la investigación científica. Conocé los requisitos, los pasos y los formularios.</p>
				<a class="btn btn--light" href="tesis.html">Ver todo sobre la tesis {ico('flecha')}</a>
			</div>
			<ul class="doc-list reveal">
				<li><a href="archivos/modelos/carta-plan-de-tesis-2026.doc">{ico('descarga')}<span>Modelo de carta para presentar plan de tesis (2026)<small>Word</small></span></a></li>
				<li><a href="archivos/modelos/carta-presentar-tesis-2026.doc">{ico('descarga')}<span>Modelo de carta para presentar la tesis (2026)<small>Word</small></span></a></li>
			</ul>
		</div>
	</div>
</section>

<section class="section" id="documentos">
	<div class="container">
		<div class="quick-links reveal">
			<ul>
				<li><a href="documentos.html">Resoluciones y reglamentos <span class="box">{ico('flecha')}</span></a></li>
				<li><a href="comision.html">Comisión de Carrera <span class="box">{ico('flecha')}</span></a></li>
				<li><a href="mailto:{c['MAIL']}">Consultas a la Comisión <span class="box">{ico('flecha')}</span></a></li>
			</ul>
		</div>
	</div>
</section>
'''

def A_PROG(c):
    # electromagnetismo-y-optica era en realidad la Res. CD 1911/2023 (duplicada): no es un programa
    return [(n.split('/')[-1], d.replace('Programa: ', '')) for (i, u, n, d, s, nota) in c['A'].rows if n.startswith('programas/') and 'electromagnetismo' not in n]


# ---------------------------------------------------------------- TESIS
REGLAMENTO = [
    ('Sobre el o los directores', [
        'La Tesis de Licenciatura podrá tener uno o dos Directores.',
        'Podrán ser Directores los docentes (Profesor o Docente Auxiliar con título máximo) de los Departamentos de Biodiversidad y Biología Experimental; Ciencias Geológicas; Ecología, Genética y Evolución; y Fisiología, Biología Molecular y Celular, FCEN-UBA. También podrán serlo investigadores de la FCEN-UBA o de otras instituciones con título máximo (Doctor o equivalente), quienes serán evaluados sin excepción por la Comisión de Carrera. Si hay un único Director, deberá ser docente de la FCEN-UBA; si hay dos, al menos uno deberá serlo.',
        'El/los Director/es será/n responsable/s de garantizar la financiación de las actividades de investigación que demande la tesis.']),
    ('Requisitos para iniciar la tesis', [
        'Los alumnos estarán en condiciones de comenzar oficialmente su Tesis cuando hayan aprobado los trabajos prácticos de todas las materias del Ciclo Obligatorio.',
        'El estudiante presentará una solicitud de inscripción ante la Comisión de Carrera, firmada por el/los Director/es y por el Tutor de su Plan de Estudios (si es otra persona), con el lugar de trabajo propuesto (que deberá coincidir con el de al menos uno de los directores) y el Plan de Tesis. Se adjuntará el CV del Director que no sea docente de la FCEN-UBA y, si la tesis no se desarrolla en la FCEN-UBA, la autorización del responsable de la unidad.']),
    ('Desarrollo de la tesis', [
        'El Plan de Tesis incluirá: título; introducción (antecedentes, hipótesis y objetivos); materiales y métodos; aporte de la investigación; facilidades disponibles (lugar, equipos, financiamiento); referencias bibliográficas; y firmas del/los Director/es.',
        'La Comisión de Carrera evaluará el plan propuesto, y podrá consultar a un especialista. Si lo considera deficiente o inapropiado, pedirá su revisión.']),
    ('Duración', [
        'La tesis no podrá durar menos de cuatro meses desde la aprobación del plan. Aunque no hay un límite preciso, se considera que debería desarrollarse en no más de un año.']),
    ('Presentación', [
        'La tesis se presenta por escrito (3 copias) con el estilo de una contribución científica, firmada por el alumno y el/los Director/es.',
        'Esquema orientativo: portada (Universidad, Facultad, título, autor, director/es, lugar de trabajo, mes y año, aclarando que es una Tesis de Licenciatura en Paleontología); resumen; introducción; materiales y métodos; resultados; discusión y/o conclusiones; referencias bibliográficas completas en orden alfabético.']),
    ('Jurados', [
        'La Comisión de Carrera designará tres jurados titulares y al menos dos suplentes, competentes en el área temática. Al menos uno de los tres jurados deberá ser Profesor de alguno de los Departamentos de la FCEN-UBA mencionados.',
        'Los jurados serán notificados por escrito y deberán aceptar la designación por escrito. Podrán ser reemplazados por los suplentes en caso de recusación, excusación, renuncia u otros impedimentos.',
        'El jurado evaluará la tesis en 30 días corridos y dictaminará si está en condiciones de ser defendida o si debe corregirse. En ese caso fijará un plazo, y luego tendrá 15 días corridos para evaluar la versión corregida. Si tras la segunda revisión no está en condiciones, la tesis será rechazada y deberá iniciarse una nueva en otra temática.',
        'Antes de la defensa se entregan dos ejemplares impresos de la versión definitiva y una copia digital para la Biblioteca Central de la FCEN-UBA y la Biblioteca Hildebranda Castellaro del Área de Paleontología.']),
    ('Exposición', [
        'La presentación será oral y pública, y la Comisión de Carrera le dará amplia difusión. El acta deberá estar firmada por al menos un jurado que sea profesor de la FCEN-UBA, con una calificación numérica de hasta 10 (diez).',
        'El día de la defensa deberá asistir al menos uno de los Directores, preferentemente el de la FCEN-UBA, quien presentará al estudiante.']),
]

def tesis(c):
    ico = c['ico']
    acc = ''
    for t, arts in REGLAMENTO:
        acc += f'<details><summary>{t}</summary><div class="accordion__body prose"><ul>' + ''.join(f'<li>{a}</li>' for a in arts) + '</ul></div></details>'
    return c['page_hero']('Tesis de <em>Licenciatura</em>', 'La tesis es una materia obligatoria de grado que tiene como meta principal iniciarte en la investigación científica.', 'tesis', 'Estudiantes') + c['page_index']([
        ('pasos', 'Paso a paso'), ('reglamento', 'Reglamento'), ('formularios', 'Formularios'), ('premio-camacho', 'Premio Camacho'), ('tesis-defendidas', 'Tesis defendidas')]) + f'''
<section class="section section--tight">
	<div class="container">
		<div class="prose reveal">
			<p>La tesis completa la formación mediante la adquisición de las bases conceptuales y metodológicas de la investigación: búsqueda bibliográfica, uso de distintas metodologías de trabajo, diseño experimental, análisis de datos, proposición de modelos explicativos y la correcta redacción, preparación y exposición del trabajo científico.</p>
			<p>El/la tesista es un/a estudiante de grado que se inicia en la investigación compartiendo alguna línea de trabajo del laboratorio que lo/la admite. <strong>No es, ni debe ser considerado/a, un/a técnico/a, docente ni auxiliar del laboratorio.</strong></p>
		</div>
	</div>
</section>

<section class="section section--sand" id="pasos">
	<div class="container">
		<h2 class="title-duo reveal"><span>Paso</span><strong>a paso</strong></h2>
		<ol class="steps reveal" style="max-width:820px">
			<li><h3>Aprobá los trabajos prácticos del ciclo obligatorio</h3><p>Es el requisito para empezar oficialmente la tesis. Al presentar el plan se adjunta la libreta universitaria o el certificado analítico.</p></li>
			<li><h3>Elegí director/a y lugar de trabajo</h3><p>Uno o dos directores. Al menos uno tiene que ser docente de la FCEN-UBA con título máximo.</p></li>
			<li><h3>Presentá el plan de tesis</h3><p>Con la solicitud de inscripción firmada por director/es y tutor/a. Usá el modelo de carta para presentar el plan de tesis.</p></li>
			<li><h3>La Comisión de Carrera evalúa el plan</h3><p>Puede consultar a especialistas o pedir revisiones.</p></li>
			<li><h3>Desarrollá la investigación</h3><p>Mínimo cuatro meses desde la aprobación del plan; idealmente, no más de un año.</p></li>
			<li><h3>Entregá la tesis escrita</h3><p>Tres copias, con el formato de una contribución científica. La Comisión designa al jurado.</p></li>
			<li><h3>Evaluación del jurado</h3><p>Hasta 30 días corridos para dictaminar si se puede defender o si requiere correcciones.</p></li>
			<li><h3>Defensa oral y pública</h3><p>Con la calificación final, de hasta 10 (diez).</p></li>
		</ol>
	</div>
</section>

<section class="section" id="reglamento">
	<div class="container">
		<div class="split split--top">
			<div class="reveal">
				<h2 class="title-duo"><span>Reglamento</span><strong>de tesis (2011)</strong></h2>
				<p>Resumen de los artículos del reglamento vigente. Ante cualquier duda, vale el texto completo.</p>
				<ul class="doc-list">
					<li><a href="archivos/reglamentos/reglamento-tesis.pdf">{ico('descarga')}<span>Reglamento de Tesis de Licenciatura en Paleontología<small>Texto completo, PDF</small></span></a></li>
				</ul>
			</div>
			<div class="accordion reveal">{acc}</div>
		</div>
	</div>
</section>

<section class="section section--sand" id="formularios">
	<div class="container">
		<h2 class="title-duo reveal"><span>Formularios</span><strong>y modelos</strong></h2>
		<ul class="doc-list reveal" style="max-width:820px">
			<li><a href="archivos/modelos/carta-plan-de-tesis-2026.doc">{ico('descarga')}<span>Modelo de carta para presentar el plan de tesis (2026)<small>Word</small></span></a></li>
			<li><a href="archivos/modelos/carta-presentar-tesis-2026.doc">{ico('descarga')}<span>Modelo de carta para presentar la tesis (2026)<small>Word</small></span></a></li>
			<li><a href="archivos/modelos/formulario-jurados-tesis.doc">{ico('descarga')}<span>Formulario de jurados de tesis<small>Formato Word</small></span></a></li>
			<li><a href="archivos/modelos/formulario-jurados-tesis.pdf">{ico('descarga')}<span>Formulario de jurados de tesis<small>Formato PDF</small></span></a></li>
			<li><a href="archivos/modelos/formulario-biblioteca-entrega-tesis.docx">{ico('descarga')}<span>Formulario de la Biblioteca FCEN para entregar las tesis<small>Versión 2023 · Word</small></span></a></li>
		</ul>
	</div>
</section>

<section class="section" id="premio-camacho">
	<div class="container">
		<div class="split">
			<div class="reveal">
				<h2 class="title-duo"><span>Premio</span><strong>Camacho</strong></h2>
				<p>El Premio Camacho distingue a la mejor Tesis de Licenciatura en Paleontología. Las condiciones y el procedimiento de selección están en su reglamento.</p>
				<p>Lleva el nombre de <strong>Horacio H. Camacho (1922–2015)</strong>, profesor de Paleontología en Exactas desde comienzos de la década de 1950 y Profesor Emérito de la UBA desde 1989. Su <em>Manual de invertebrados fósiles</em> (Eudeba, 1966) fue libro de referencia para más de cuarenta generaciones de estudiantes de habla hispana, e introdujo en la Universidad la enseñanza de la micropaleontología. Formó una amplia escuela de discípulos: dirigió 23 trabajos finales de licenciatura y 12 tesis doctorales.</p>
				<ul class="doc-list">
					<li><a href="archivos/reglamentos/reglamento-premio-camacho.pdf">{ico('descarga')}<span>Reglamento del Premio Camacho a la mejor Tesis de Licenciatura</span></a></li>
					<li><a href="https://www.scielo.org.ar/scielo.php?script=sci_arttext&amp;pid=S0004-48222016000200012">{ico('externo')}<span>Necrología de Horacio H. Camacho<small>Por Beatriz Aguirre-Urreta · Revista de la Asociación Geológica Argentina, 2016</small></span></a></li>
				</ul>
			</div>
			<div class="reveal offset-frame"><figure class="figure-portrait figure-portrait--illus"><img src="imgs/fotos/camacho-ilustracion.png" alt="Retrato ilustrado de Horacio H. Camacho" width="516" height="692"><figcaption><b>Horacio H. Camacho</b><small><a href="https://www.scielo.org.ar/scielo.php?script=sci_arttext&amp;pid=S0004-48222016000200012" title="Necrología de Horacio H. Camacho">1922–2015</a></small></figcaption></figure></div>
		</div>
	</div>
</section>

<section class="section section--sand" id="tesis-defendidas">
	<div class="container">
		<div class="prose reveal">
			<h2>Tesis defendidas</h2>
			<p>Hasta hoy se recibieron alrededor de 74 licenciados/as en Paleontología, con tesis sobre una gran diversidad de temas: paleontología de invertebrados y de vertebrados, micropaleontología y paleobotánica, y también reconstrucción paleoambiental y paleoclimática, icnología, tafonomía, paleohistología y paleoneurología.</p>
			<ul class="doc-list">
				<li><a href="archivos/tesis/listado-tesis-2008-2024.pdf">{ico('descarga')}<span>Listado de Tesis de Licenciatura defendidas, 2008–2024</span></a></li>
			</ul>
		</div>
	</div>
</section>
'''


# ---------------------------------------------------------------- COMISIÓN
def iniciales(n):
    ap, _, nom = n.partition(',')
    return (nom.strip()[:1] + ap.strip()[:1]).upper()

# Fotos de integrantes de la comisión (archivo en imgs/fotos/). Quien no tiene foto muestra sus iniciales.
FOTOS_PERSONAS = {
    'Lazo, Darío Gustavo': 'director-lazo',
    'Marsicano, Claudia Alicia': 'director-marsicano',
}

def persona(n, rol, titular=True, lead=False):
    cls = 'person' + (' person--titular' if titular else '') + (' person--lead' if lead else '')
    ap, _, nom = n.partition(',')
    if n in FOTOS_PERSONAS:
        avatar = f'<img class="person__avatar person__avatar--photo" src="imgs/fotos/{FOTOS_PERSONAS[n]}.jpg" alt="" width="240" height="240" loading="lazy">'
    else:
        avatar = f'<span class="person__avatar" aria-hidden="true">{iniciales(n)}</span>'
    return f'<li class="{cls}">{avatar}<span><b>{nom.strip()} {ap.strip()}</b><small>{rol}</small></span></li>'

CLAUSTROS = [
    ('Profesores', '', [
        ('Departamento de Ciencias Geológicas', [('Lazo, Darío Gustavo', 'Titular · Director de carrera', True, True), ('Marsicano, Claudia Alicia', 'Titular · Directora adjunta', True, True),
            ('Ottone, Eduardo Guillermo', 'Titular', True, False), ('Aguirre-Urreta, María Beatriz', 'Suplente', False, False), ('Concheyro, Graciela Andrea', 'Suplente', False, False), ('Pol, Diego', 'Suplente', False, False)]),
        ('Departamento de Biodiversidad y Biología Experimental', [('Maidana, Nora', 'Titular', True, False), ('López Greco, Laura Nora', 'Suplente', False, False)]),
        ('Departamento de Ecología, Genética y Evolución', [('Laprida, Cecilia', 'Titular', True, False)]),
    ]),
    ('Graduados', 'graduados.paleo@gmail.com', [
        ('Departamento de Ciencias Geológicas', [('Farina, Martín', 'Titular', True, False), ('Turazzini, Guillermo', 'Titular', True, False), ('Martin, Rodrigo', 'Suplente', False, False), ('Seoane, Federico', 'Suplente', False, False)]),
        ('Departamento de Ecología, Genética y Evolución', [('Tropea, Ana L.', 'Titular', True, False)]),
        ('Departamento de Biodiversidad y Biología Experimental', [('Picca, Pablo', 'Titular', True, False), ('Barrozo, Romina', 'Suplente', False, False)]),
    ]),
    ('Estudiantes · 2025-2026', 'ccalumnospaleo@gmail.com', [
        ('', [('Iglesias, Itziar', 'Titular', True, False), ('Liendro Bataglia, Nahuel', 'Titular', True, False), ('Fernández Kalen, Diego', 'Titular', True, False),
              ('Martini, Luca Nicolás', 'Suplente', False, False), ('Scaravilli Carballo, Bruno', 'Suplente', False, False), ('Krumpoeck, Ian Thomas', 'Suplente', False, False)]),
    ]),
]

def comision(c):
    ico = c['ico']
    claus = ''
    for nombre, mail, grupos in CLAUSTROS:
        claus += f'<div class="claustro reveal"><h3>Claustro de {nombre}</h3>'
        for dep, ps in grupos:
            if dep: claus += f'<h4>{dep}</h4>'
            claus += '<ul class="people">' + ''.join(persona(*p) for p in ps) + '</ul>'
        claus += '</div>'
    # Actas por año, de la más reciente a la más vieja
    por_anio = {}
    for (i, u, n, d, s, nota) in c['A'].rows:
        if not n.startswith('actas/'): continue
        f = n.split('/')[-1]
        anio = f[:4]
        if f[4:5] == '-' and f[5:7].isdigit():
            p = f.split('-')
            meses = ['', 'ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
            label = (f'{int(p[2])} {meses[int(p[1])]}' if len(p) == 3 and p[2].isdigit() else meses[int(p[1])].capitalize()) + f' {anio}'
        else:
            label = d.split(' (')[0].replace('Archivo sin título en la lista de actas 2015', 'Documento 2015')
        por_anio.setdefault(anio, []).append((n, label))
    acc = ''
    for k, anio in enumerate(sorted(por_anio, reverse=True)):
        items = sorted(por_anio[anio])
        li = ''.join(f'<li><a href="archivos/{n}.pdf">{ico("descarga")}{l}</a></li>' for n, l in items)
        acc += f'<details{" open" if k == 0 else ""}><summary>{anio} <small>{len(items)} documentos</small></summary><div class="accordion__body"><ul class="doc-grid">{li}</ul></div></details>'
    return c['page_hero']('Comisión de <em>Carrera</em>', 'La Comisión de Carrera de la Licenciatura en Paleontología está integrada por representantes de profesores, graduados y estudiantes. Período 2024-2026.', 'personas', 'Institucional') + c['page_index']([
        ('integrantes', 'Integrantes'), ('actas', 'Actas de reuniones'), ('contacto', 'Contacto')]) + f'''
<section class="section section--tight" id="integrantes">
	<div class="container">
		<div class="cards reveal directors" style="margin-bottom:50px">
			<div class="card director"><img class="director__photo" src="imgs/fotos/director-lazo.jpg" alt="Darío G. Lazo" width="240" height="240"><div><span class="eyebrow">Director de carrera</span><h3>Dr. Darío G. Lazo</h3><small class="director__credit">Foto: <a href="https://exactas.uba.ar/tres-de-tres/">Exactas UBA</a></small></div></div>
			<div class="card director"><img class="director__photo" src="imgs/fotos/director-marsicano.jpg" alt="Claudia A. Marsicano" width="240" height="240"><div><span class="eyebrow">Directora adjunta</span><h3>Dra. Claudia A. Marsicano</h3><small class="director__credit">Foto: <a href="https://commons.wikimedia.org/wiki/File:ClaudiaMarsicano01.jpg">CONICET Fotografía / Verónica Tello</a>, CC BY 4.0</small></div></div>
		</div>
		{claus}
	</div>
</section>

<section class="section section--sand" id="actas">
	<div class="container">
		<div class="split split--top">
			<div class="reveal">
				<h2 class="title-duo"><span>Actas de</span><strong>reuniones</strong></h2>
				<p>Actas de las reuniones de la Comisión de Carrera desde 2011.</p>
				<ul class="doc-list"><li><a href="archivos/reglamentos/reglamento-comision-carrera.pdf">{ico('descarga')}<span>Reglamento de la Comisión de Carrera</span></a></li></ul>
			</div>
			<div class="accordion reveal">{acc}</div>
		</div>
	</div>
</section>

<section class="section" id="contacto">
	<div class="container">
		<div class="prose reveal">
			<h2>Contacto</h2>
			<ul class="arrow-list">
				<li>Comisión de Carrera: <a href="mailto:{c['MAIL']}">{c['MAIL']}</a></li>
				<li>Claustro de graduados: <a href="mailto:graduados.paleo@gmail.com">graduados.paleo@gmail.com</a></li>
				<li>Claustro de estudiantes: <a href="mailto:ccalumnospaleo@gmail.com">ccalumnospaleo@gmail.com</a></li>
			</ul>
		</div>
	</div>
</section>
'''


# ---------------------------------------------------------------- DOCUMENTOS
def documentos(c):
    ico = c['ico']
    def lista(items):
        return '<ul class="doc-list">' + ''.join(f'<li><a href="{h}">{ico("externo" if h.startswith("http") else "descarga")}<span>{t}{"<small>" + s + "</small>" if s else ""}</span></a></li>' for h, t, s in items) + '</ul>'
    return c['page_hero']('Documentos', 'Resoluciones, reglamentos y modelos de notas para los trámites de la carrera.', 'carpeta', 'Institucional') + c['page_index']([
        ('resoluciones', 'Resoluciones'), ('reglamentos', 'Reglamentos'), ('modelos', 'Modelos de carta'), ('enlaces', 'Enlaces')]) + f'''
<section class="section section--tight" id="resoluciones">
	<div class="container narrow">
		<h2 class="title-duo reveal"><span>Resoluciones</span></h2>
		<div class="reveal">{lista([
            ('archivos/resoluciones/creacion-carrera-2001.pdf', 'Resolución de creación de la carrera', 'FCEN-UBA, 2001'),
            ('archivos/resoluciones/validez-nacional-titulo.pdf', 'Validez nacional del título otorgado por la UBA', 'Ministerio de Educación de la Nación'),
            ('archivos/resoluciones/res-cd-1911-2023.pdf', 'Res. CD 1911/2023', 'Física para Paleontólogos se reemplaza por Electromagnetismo y Óptica'),
            ('archivos/resoluciones/res-cd-2510-2017.pdf', 'Res. CD 2510/2017', 'Equivalencia de Química General e Inorgánica'),
            ('archivos/resoluciones/profesorado-biologia.pdf', 'Resolución del Profesorado de Enseñanza Media y Superior, especialidad Biología', '')])}</div>
	</div>
</section>

<section class="section section--sand" id="reglamentos">
	<div class="container narrow">
		<h2 class="title-duo reveal"><span>Reglamentos</span></h2>
		<div class="note reveal"><strong>Importante:</strong> es imprescindible leer el reglamento que corresponda según el trámite a realizar.</div>
		<div class="reveal">{lista([
            ('archivos/reglamentos/reglamento-comision-carrera.pdf', 'Reglamento de la Comisión de Carrera', ''),
            ('archivos/reglamentos/reglamento-tutores-y-planes-de-estudio.pdf', 'Reglamento de tutores y planes de estudio', ''),
            ('archivos/reglamentos/reglamento-tesis.pdf', 'Reglamento de Tesis de Licenciatura', 'Ver también el resumen en la página de Tesis'),
            ('archivos/reglamentos/reglamento-premio-camacho.pdf', 'Reglamento del Premio Camacho a la mejor Tesis de Licenciatura', '')])}</div>
	</div>
</section>

<section class="section" id="modelos">
	<div class="container narrow">
		<h2 class="title-duo reveal"><span>Modelos</span><strong>de carta</strong></h2>
		<p class="reveal">Al presentar el plan de tesis hay que adjuntar copia de la libreta universitaria o del certificado analítico, para que la Comisión compruebe que se completaron los trabajos prácticos de las materias obligatorias (Art. 4 del Reglamento de Tesis).</p>
		<div class="reveal">{lista([
            ('archivos/modelos/carta-plan-de-estudios-2026.docx', 'Modelo de carta para plan de estudios (2026)', 'Word'),
            ('archivos/modelos/carta-plan-de-tesis-2026.doc', 'Modelo de carta para presentar plan de tesis (2026)', 'Word'),
            ('archivos/modelos/carta-presentar-tesis-2026.doc', 'Modelo de carta para presentar tesis (2026)', 'Word'),
            ('archivos/tesis/listado-tesis-2008-2024.pdf', 'Listado de Tesis de Licenciatura defendidas, 2008–2024', '')])}</div>
	</div>
</section>

<section class="section section--sand" id="enlaces">
	<div class="container narrow">
		<h2 class="title-duo reveal"><span>Enlaces</span></h2>
		<h3 class="reveal" style="color:var(--slate)">Institucionales</h3>
		<div class="reveal">{lista([
            ('http://www.apaleontologica.org.ar/', 'Asociación Paleontológica Argentina', ''),
            ('http://www.gl.fcen.uba.ar/', 'Departamento de Ciencias Geológicas', 'FCEN-UBA'),
            ('https://exactas.uba.ar/', 'Facultad de Ciencias Exactas y Naturales', 'UBA'),
            ('http://www.bl.fcen.uba.ar/', 'Biblioteca Central Dr. Luis F. Leloir', 'FCEN-UBA'),
            ('http://www.idean.gl.fcen.uba.ar/', 'Instituto de Estudios Andinos (IDEAN)', 'UBA-CONICET'),
            ('http://igeba.gl.fcen.uba.ar/', 'Instituto de Geociencias Básicas, Ambientales y Aplicadas (IGEBA)', 'UBA-CONICET')])}</div>
		<h3 class="reveal" style="color:var(--slate);margin-top:2em">Otros recursos</h3>
		<div class="reveal">{lista([
            ('http://www.scotese.com/', 'Mapas paleogeográficos', 'PALEOMAP Project'),
            ('https://stratigraphy.org/', 'International Commission on Stratigraphy', '')])}</div>
	</div>
</section>
'''


# ---------------------------------------------------------------- DOCTORADO
def doctorado(c):
    ico = c['ico']
    return c['page_hero']('Doctorado en <em>Paleontología</em>', 'El Doctorado de la Universidad de Buenos Aires, Área Paleontología, se dicta en Exactas y cuenta con dictamen favorable de la CONEAU (Acta N.º 546/2021). Es el título de mayor jerarquía que otorga la UBA, en una especialidad prácticamente sin equivalentes en la región.', 'birrete', 'Posgrado') + c['page_index']([
        ('objetivos', 'El doctorado'), ('competencias', 'Competencias'), ('inscripcion', 'Cómo inscribirse'), ('historia', 'Historia'), ('documentos', 'Documentos')]) + f'''
<section class="section section--tight" id="objetivos">
	<div class="container">
		<div class="split split--top">
			<div class="prose reveal">
				<h2>El doctorado</h2>
				<p>La paleontología es una ciencia fundamental para entender la historia de la vida a través del tiempo geológico. El análisis del registro fósil comprende subdisciplinas como la Paleontología de Vertebrados y de Invertebrados, la Paleobotánica, la Palinología, la Micropaleontología, la Paleoecología, la Paleobiología y la Tafonomía, lo que abre un abanico de temas muy diverso para realizar un doctorado.</p>
				<p>Las investigaciones pueden ser de ciencia básica (por ejemplo, aspectos sistemáticos, ecológicos y evolutivos de especies extinguidas) o aplicadas: la resolución de problemas geológicos, la determinación de la edad relativa de las secuencias, la reconstrucción de los ambientes y del clima del pasado, con aplicaciones directas en la industria del petróleo o en el reconocimiento de los impactos de los cambios climáticos globales sobre las biotas.</p>
				<p>Por su naturaleza disciplinar, también pueden realizarse doctorados interdisciplinarios con otras grandes ramas de la ciencia, como la Arqueología, la Antropología biológica, la Geología, la Biología y las Ciencias de la Atmósfera y los Océanos. Además de quienes se gradúan en Paleontología, es una opción para graduados y graduadas en Biología o Geología que realizan tesis sobre temas paleontológicos.</p>
				<p>La tarea fundamental de un candidato o una candidata al doctorado es realizar un trabajo de investigación científica que signifique una contribución original al conocimiento del área científica o tecnológica elegida.</p>
			</div>
			<div class="reveal offset-frame">{foto('doctorado-laboratorio-campo')}</div>
		</div>
	</div>
</section>

<section class="section section--sand" id="competencias">
	<div class="container">
		<h2 class="title-duo reveal"><span>Competencias</span><strong>del egresado</strong></h2>
		<div class="note reveal" style="max-width:860px">El título de Doctor/a expedido por la UBA es de carácter netamente académico y <strong>no habilita para el ejercicio profesional</strong>.</div>
		<div class="cards cards--3">
			<div class="card reveal"><span class="card__num">1</span><p>Dominio de métodos y tecnologías de investigación relacionados con el campo seleccionado.</p></div>
			<div class="card reveal"><span class="card__num">2</span><p>Capacidad de realizar un análisis crítico y una evaluación del estado del arte en el campo seleccionado.</p></div>
			<div class="card reveal"><span class="card__num">3</span><p>Capacidad de comunicación científica y de divulgación sobre su ámbito de conocimiento.</p></div>
			<div class="card reveal"><span class="card__num">4</span><p>Incorporación en la labor cotidiana de los aspectos relevantes de higiene y seguridad en los ámbitos de investigación.</p></div>
			<div class="card reveal"><span class="card__num">5</span><p>Ética profesional y prácticas de trabajo responsables.</p></div>
			<div class="card reveal"><span class="card__num">6</span><p>Espíritu crítico y capacidad argumentativa.</p></div>
		</div>
	</div>
</section>

<section class="section" id="inscripcion">
	<div class="container">
		<div class="split split--top">
			<div class="prose reveal">
				<h2>Cómo inscribirse</h2>
				<p>El doctorado se rige por el Reglamento de Doctorado de Exactas. Los informes, la admisión y la inscripción se gestionan a través de la Secretaría de Posgrado de la Facultad.</p>
				<ul class="arrow-list">
					<li>Correo electrónico: <a href="mailto:postgrado@de.fcen.uba.ar">postgrado@de.fcen.uba.ar</a></li>
					<li>Pabellón 2, planta baja, Ciudad Universitaria</li>
					<li>Atención presencial: lunes a viernes de 10 a 13 y de 14 a 16</li>
				</ul>
			</div>
			<div class="reveal">
				<ul class="doc-list">
					<li><a href="https://doctorado.exactas.uba.ar/">{ico('externo')}<span>Doctorados de Exactas<small>Informes e inscripción</small></span></a></li>
					<li><a href="https://exactas.uba.ar/ensenanza/carreras-de-posgrado/">{ico('externo')}<span>Secretaría de Posgrado<small>exactas.uba.ar</small></span></a></li>
				</ul>
			</div>
		</div>
	</div>
</section>

<section class="section section--sand" id="historia">
	<div class="container">
		<h2 class="title-duo reveal"><span>Veinte años</span><strong>de historia</strong></h2>
		<ol class="steps reveal" style="max-width:860px">
			<li><h3>2001 · Creación de la licenciatura</h3><p>El antecedente más directo del doctorado: la FCEN solicita al Consejo Superior la creación de la Licenciatura en Paleontología (Res. CD 0317/2001), tras la revisión de los Departamentos de Ciencias Geológicas y Ciencias Biológicas y de una comisión ad hoc.</p></li>
			<li><h3>2005 · Primera postulación</h3><p>En octubre, la Comisión de Carrera, de común acuerdo entre los claustros, solicita a la Secretaría Académica incorporar el área Paleontología a la carrera de doctorado de la Facultad.</p></li>
			<li><h3>2007 · Primeros graduados</h3><p>Se reciben los primeros licenciados y licenciadas. Sin un doctorado específico, quienes quieren doctorarse deben hacerlo en Biología o en Geología.</p></li>
			<li><h3>2011 y 2015 · Nuevos pedidos</h3><p>Las sucesivas direcciones de la carrera reiteran el pedido. En 2015 se argumenta que entre 2000 y 2014 se defendieron 29 tesis doctorales en Geología y 14 en Biología sobre temas paleontológicos.</p></li>
			<li><h3>2014 · Validez nacional del título de grado</h3><p>El Ministerio de Educación de la Nación otorga reconocimiento oficial y validez nacional al título de Licenciado/a en Paleontología (Res. N.º 922/2014).</p></li>
			<li><h3>2018 · Resolución del Consejo Directivo</h3><p>El 26 de marzo, la Res. CD N.º 0628/2018 solicita al Consejo Superior incorporar el Área Paleontología al doctorado. Se destacan los 41 egresados de la licenciatura hasta entonces, el precedente de 52 tesis doctorales sobre temas paleontológicos (33 en Geología y 19 en Biología), cartas de apoyo de profesionales e instituciones del país y del exterior, y el aval de las subcomisiones de doctorado de Ciencias Geológicas; Ecología, Genética y Evolución; y Biodiversidad y Biología Experimental.</p></li>
			<li><h3>2019 · Resolución del Consejo Superior</h3><p>El 15 de mayo, el Consejo Superior de la UBA incorpora el área Paleontología al Reglamento de Doctorado de la FCEN (Exp-UBA 21.801-2019).</p></li>
			<li><h3>2021 · Dictamen de la CONEAU</h3><p>El 16 de junio, en su sesión N.º 546 (Acta N.º 546/2021), la Comisión Nacional de Evaluación y Acreditación Universitaria recomienda otorgar el reconocimiento oficial provisorio del título a la carrera nueva de Doctorado de la Universidad de Buenos Aires, Área Paleontología. Sus principales impulsores fueron los doctores Beatriz Aguirre-Urreta, Darío G. Lazo y Cecilia Laprida.</p></li>
		</ol>
	</div>
</section>

<section class="section" id="documentos">
	<div class="container narrow">
		<h2 class="title-duo reveal"><span>Documentos</span></h2>
		<ul class="doc-list reveal">
			<li><a href="archivos/doctorado/reglamento-doctorado-fcen-2021.pdf">{ico('descarga')}<span>Reglamento de Doctorado de la FCEN-UBA<small>Res. CS 577/2021</small></span></a></li>
			<li><a href="archivos/doctorado/resolucion-coneau-acreditacion.pdf">{ico('descarga')}<span>Dictamen de la CONEAU sobre el Doctorado de la UBA, Área Paleontología<small>Acta N.º 546, 16 de junio de 2021</small></span></a></li>
			<li><a href="https://exactas.uba.ar/paleontologia-tiene-su-doctorado/">{ico('externo')}<span>«Paleontología tiene su doctorado»<small>Nota de Exactas, septiembre de 2021</small></span></a></li>
		</ul>
	</div>
</section>
'''


PAGINAS = [
    dict(slug='index', title='Licenciatura en Paleontología | UBA Exactas', og='Licenciatura en Paleontología',
         desc='Estudiá Paleontología en Exactas UBA: una carrera que integra biología y geología para develar la historia de la vida en la Tierra.', body=inicio),
    dict(slug='ingresantes', title='Ingresantes | Licenciatura en Paleontología | UBA Exactas',
         desc='Qué es la paleontología, perfil del egresado, campo laboral, incumbencias del título y cómo ingresar a la Licenciatura en Paleontología de Exactas UBA.', body=ingresantes),
    dict(slug='carrera', title='Plan de estudios | Licenciatura en Paleontología | UBA Exactas',
         desc='Plan de estudios de la Licenciatura en Paleontología: materias obligatorias, correlatividades, optativas, electivas y carga horaria.', body=carrera, scripts=['js/plan.js?v=1']),
    dict(slug='estudiantes', title='Estudiantes | Licenciatura en Paleontología | UBA Exactas',
         desc='Plan de materias y tutor, programas de las materias, equivalencias y trámites para estudiantes de Paleontología.', body=estudiantes),
    dict(slug='tesis', title='Tesis de Licenciatura | Licenciatura en Paleontología | UBA Exactas',
         desc='Reglamento, pasos, formularios y Premio Camacho de la Tesis de Licenciatura en Paleontología.', body=tesis),
    dict(slug='comision', title='Comisión de Carrera | Licenciatura en Paleontología | UBA Exactas',
         desc='Integrantes y actas de la Comisión de Carrera de la Licenciatura en Paleontología.', body=comision),
    dict(slug='documentos', title='Documentos | Licenciatura en Paleontología | UBA Exactas',
         desc='Resoluciones, reglamentos, modelos de carta y enlaces de la Licenciatura en Paleontología.', body=documentos),
    dict(slug='doctorado', title='Doctorado en Paleontología | UBA Exactas',
         desc='Doctorado de la Universidad de Buenos Aires, área Paleontología: objetivos, perfil e historia.', body=doctorado),
]
