# Genera las páginas HTML del sitio (encabezado, menú y pie compartidos).
#
# Uso, desde la raíz del repositorio:
#     python3 _fuente/build.py
#
# - build.py     encabezado, menú, pie y armado de cada página
# - paginas.py   el contenido de cada página (textos, fotos y créditos)
# - archivos.py  la lista de documentos migrados del sitio viejo (actas, programas, etc.)
#
# El plan de estudios (materias, horas, correlatividades) NO está acá: está en js/plan.js.
import sys, os, html
sys.path.insert(0, os.path.dirname(__file__))
import archivos as A
from paginas import PAGINAS

# Las páginas se escriben en la carpeta raíz del repositorio (una arriba de _fuente/)
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..') + os.sep
MAIL = 'direccion_paleontologia@gl.fcen.uba.ar'

def ico(name, cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<svg aria-hidden="true"{c}><use href="imgs/fosiles.svg#{name}"/></svg>'

HEAD = '''<!DOCTYPE html>
<html lang="es" class="no-js">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>{title}</title>
	<meta name="description" content="{desc}">
	<meta property="og:title" content="{ogtitle}">
	<meta property="og:description" content="{desc}">
	<meta property="og:type" content="website">
	<meta name="twitter:card" content="summary_large_image">
	<meta name="theme-color" content="#b4532a">
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..700;1,9..144,400..700&family=Roboto:ital,wght@0,300..700;1,300..700&display=swap" rel="stylesheet">
	<link rel="stylesheet" href="css/style.css?v=1">
	<link rel="icon" href="imgs/favicon.svg" type="image/svg+xml">
</head>
<body class="{bodycls}">
<a class="skip-link" href="#contenido">Saltar al contenido</a>
'''

WORDMARK = '<a href="index.html" class="wordmark" aria-label="Licenciatura en Paleontología, inicio"><small>Licenciatura en</small><b>Paleontología</b></a>'

HEADER = '''<header class="site-header">
	<div class="container">
		<div class="site-header__inner">
			<div class="logos">
				''' + WORDMARK + '''
				<span class="logos__divider" aria-hidden="true"></span>
				<a href="https://exactas.uba.ar/" class="logo-exactas-link"><img src="imgs/exactas.svg" alt="UBA Exactas" class="logo-exactas" width="210" height="22"></a>
			</div>
			<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="menu">
				<span>MENÚ</span>
				<span class="menu-toggle__lines" aria-hidden="true"><i></i><i></i><i></i></span>
			</button>
		</div>
	</div>
</header>
'''

def menu():
    side = [('ingresantes.html#que-es', '¿Qué es la paleontología?'), ('ingresantes.html#por-que', '¿Por qué estudiar paleontología?'),
            ('ingresantes.html#campo-laboral', 'Campo laboral e incumbencias'), ('ingresantes.html#como-ingresar', 'Cómo ingresar'),
            ('archivos/folleto-paleontologia.pdf', 'Folleto informativo')]
    cols = [
        ('carrera.html', 'Plan de estudios', [('carrera.html#recorrido', 'Recorrido de la carrera'), ('carrera.html#correlatividades', 'Correlatividades'),
            ('carrera.html#obligatorias', 'Materias obligatorias'), ('carrera.html#orientacion', 'Optativas y electivas'), ('carrera.html#totales', 'Carga horaria')]),
        ('estudiantes.html', 'Estudiantes', [('estudiantes.html#tutor', 'Plan de materias y tutor'), ('estudiantes.html#programas', 'Programas de materias'),
            ('estudiantes.html#equivalencias', 'Equivalencias'), ('tesis.html', 'Tesis de Licenciatura'), ('tesis.html#premio-camacho', 'Premio Camacho')]),
        ('comision.html', 'Institucional', [('comision.html', 'Comisión de Carrera'), ('comision.html#actas', 'Actas de reuniones'),
            ('documentos.html', 'Documentos y reglamentos'), ('doctorado.html', 'Doctorado en Paleontología'), ('documentos.html#enlaces', 'Enlaces')]),
    ]
    li = lambda items: '\n'.join(f'\t\t\t\t\t<li><a href="{h}">{t}</a></li>' for h, t in items)
    s = f'''<div class="mega-menu" id="menu" role="dialog" aria-modal="true" aria-label="Menú principal" aria-hidden="true">
	<div class="mega-menu__side">
		{WORDMARK}
		<h4><a href="ingresantes.html">Ingresantes</a></h4>
		<ul>
{li(side)}
		</ul>
	</div>
	<div class="mega-menu__main">
		<button class="mega-menu__close" type="button" aria-label="Cerrar menú"></button>
		<svg class="mega-menu__fossil" aria-hidden="true"><use href="imgs/fosiles.svg#amonite"/></svg>
		<div class="mega-menu__cols">
'''
    for href, t, items in cols:
        s += f'''			<div class="mega-menu__col">
				<h4><a href="{href}">{t}</a></h4>
				<ul>
{li(items)}
				</ul>
			</div>
'''
    s += '''		</div>
	</div>
</div>
'''
    return s

FOOTER = f'''<footer class="site-footer">
	<div class="container">
		<div class="footer-grid">
			<div>
				{WORDMARK}
				<p style="margin-top:16px">Facultad de Ciencias Exactas y Naturales<br>Universidad de Buenos Aires</p>
				<a class="footer-contact" href="mailto:{MAIL}">{ico('mail')}{MAIL}</a>
			</div>
			<div>
				<h4>La carrera</h4>
				<ul>
					<li><a href="ingresantes.html">Ingresantes</a></li>
					<li><a href="carrera.html">Plan de estudios</a></li>
					<li><a href="carrera.html#correlatividades">Correlatividades</a></li>
					<li><a href="doctorado.html">Doctorado</a></li>
				</ul>
			</div>
			<div>
				<h4>Estudiantes</h4>
				<ul>
					<li><a href="estudiantes.html">Trámites y tutorías</a></li>
					<li><a href="tesis.html">Tesis de Licenciatura</a></li>
					<li><a href="documentos.html">Documentos</a></li>
					<li><a href="comision.html">Comisión de Carrera</a></li>
				</ul>
			</div>
			<div>
				<h4>Enlaces</h4>
				<ul>
					<li><a href="https://exactas.uba.ar/">Exactas UBA</a></li>
					<li><a href="http://www.gl.fcen.uba.ar/">Departamento de Ciencias Geológicas</a></li>
					<li><a href="https://www.cbc.uba.ar/">Ciclo Básico Común</a></li>
					<li><a href="https://exactas.uba.ar/extension/ov/">Orientación vocacional</a></li>
				</ul>
			</div>
		</div>
		<div class="footer-bottom">
			<span>© <span data-year>2026</span> Licenciatura en Paleontología · FCEN · UBA</span>
			<a href="https://exactas.uba.ar/"><img src="imgs/exactas.svg" alt="UBA Exactas" width="210" height="22"></a>
		</div>
	</div>
</footer>
'''

def page_hero(title_html, lead, fossil='amonite', eyebrow=''):
    eb = f'<span class="eyebrow">{eyebrow}</span>' if eyebrow else ''
    return f'''<section class="page-hero">
	<svg class="page-hero__fossil" aria-hidden="true"><use href="imgs/fosiles.svg#{fossil}"/></svg>
	<div class="container">
		{eb}
		<h1>{title_html}</h1>
		<p class="lead">{lead}</p>
	</div>
</section>
'''

def page_index(items):
    li = ''.join(f'<li><a href="#{i}">{t}</a></li>' for i, t in items)
    return f'<nav class="page-index" aria-label="En esta página"><div class="container"><ul>{li}</ul></div></nav>\n'

def build():
    ctx = dict(ico=ico, page_hero=page_hero, page_index=page_index, A=A, MAIL=MAIL, esc=html.escape)
    for p in PAGINAS:
        body = p['body'](ctx)
        out = HEAD.format(title=p['title'], desc=p['desc'], ogtitle=p.get('og', p['title']), bodycls=p['slug']) + HEADER + menu()
        out += f'<main id="contenido">\n{body}\n</main>\n' + FOOTER
        out += '<script src="js/main.js?v=1"></script>\n'
        for s in p.get('scripts', []):
            out += f'<script src="{s}"></script>\n'
        out += '</body>\n</html>\n'
        open(R + p['slug'] + '.html', 'w').write(out)
        print('ok', p['slug'])

if __name__ == '__main__':
    build()
