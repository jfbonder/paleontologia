# Archivos a migrar desde el sitio viejo

> **Migración completa (noviembre 2026).** Todos los archivos ya están en `archivos/`. Esta tabla queda como referencia del origen de cada documento. Notas: los dos reglamentos de tesis (n.º 266 y 281) eran idénticos y se dejó uno; el n.º 447 («Electromagnetismo y Óptica») era en realidad la Res. CD 1911/2023; el archivo sin título de 2015 (n.º 303) es el acta del 26/02/2015; las fechas marcadas con ⚠️ se verificaron con el contenido de cada acta.

Son **142 archivos** que hoy están en `paleo.gl.fcen.uba.ar` (sitio solo `http`, que no se puede leer desde el entorno de desarrollo).

## Opción rápida: script automático

Desde una computadora que pueda abrir el sitio viejo (Mac o Linux), en una carpeta vacía:

```bash
bash descargar_archivos.sh
```

Crea la carpeta `archivos/` con todo ya ordenado y con los nombres correctos. Después comprimí esa carpeta y subila.

## Opción manual

Bajar cada link y guardarlo **con el nombre de la columna "Guardar como"**, dentro de la carpeta `archivos/`, respetando las subcarpetas (`actas/`, `programas/`, etc.). La extensión (.pdf, .doc, .docx) es la que traiga el archivo.

Las filas marcadas con ⚠️ tienen algo para verificar (ver columna "Nota").

| # | Guardar como | Qué es | Link | Nota |
|---|---|---|---|---|
| 1 | `archivos/folleto-paleontologia` | Folleto informativo de la Licenciatura | [371](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/371/1/) |  |
| 2 | `archivos/resoluciones/creacion-carrera-2001` | Resolución de creación de la carrera (2001) | [372](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/372/148/) |  |
| 3 | `archivos/resoluciones/validez-nacional-titulo` | Validez nacional del título (Res. ME 922/2014) | [358](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/358/148/) |  |
| 4 | `archivos/resoluciones/profesorado-biologia` | Resolución del Profesorado de Enseñanza Media y Superior, especialidad Biología | [457](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/457/148/) |  |
| 5 | `archivos/resoluciones/res-cd-1911-2023` | Res. CD 1911/2023 (Física → Electromagnetismo y Óptica) | [448](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/448/131/) |  |
| 6 | `archivos/resoluciones/res-cd-2510-2017` | Res. CD 2510/2017 (equivalencia de Química General e Inorgánica) | [449](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/449/131/) |  |
| 7 | `archivos/reglamentos/reglamento-comision-carrera` | Reglamento de la Comisión de Carrera | [283](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/283/148/) |  |
| 8 | `archivos/reglamentos/reglamento-tutores-y-planes-de-estudio` | Reglamento de tutores y planes de estudio | [282](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/282/148/) |  |
| 9 | `archivos/reglamentos/reglamento-tesis` | Reglamento de Tesis de Licenciatura | [281](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/281/148/) | ⚠️ Probablemente igual al n.º 266; bajar los dos y comparar |
| 10 | `archivos/reglamentos/reglamento-tesis-2011` | Reglamento de Tesis de Licenciatura (versión de la página Tesis) | [266](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/266/147/) | ⚠️ Probablemente igual al n.º 281 |
| 11 | `archivos/reglamentos/reglamento-premio-camacho` | Reglamento del Premio Camacho a la mejor Tesis de Licenciatura | [397](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/397/148/) |  |
| 12 | `archivos/modelos/carta-plan-de-estudios-2026` | Modelo de carta para plan de estudios (2026) | [450](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/450/148/) | ⚠️ Puede ser Word en vez de PDF |
| 13 | `archivos/modelos/carta-plan-de-tesis-2026` | Modelo de carta para presentar plan de tesis (2026) | [458](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/458/148/) | ⚠️ Puede ser Word en vez de PDF |
| 14 | `archivos/modelos/carta-presentar-tesis-2026` | Modelo de carta para presentar tesis (2026) | [452](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/452/148/) | ⚠️ Puede ser Word en vez de PDF |
| 15 | `archivos/modelos/formulario-jurados-tesis` | Formulario de jurados de tesis (Word) | [326](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/326/147/) | ⚠️ Es Word: guardarlo con la extensión que traiga (.doc o .docx) |
| 16 | `archivos/modelos/formulario-jurados-tesis` | Formulario de jurados de tesis (PDF) | [327](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/327/147/) |  |
| 17 | `archivos/modelos/formulario-biblioteca-entrega-tesis` | Formulario de la Biblioteca FCEN para entregar las tesis (2023) | [414](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/414/147/) |  |
| 18 | `archivos/tesis/listado-tesis-2008-2024` | Listado de Tesis de Licenciatura defendidas 2008-2024 | [425](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/425/148/) |  |
| 19 | `archivos/programas/biodiversidad-de-animales` | Programa: Biodiversidad de Animales | [426](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/426/149/) |  |
| 20 | `archivos/programas/biodiversidad-de-vegetales` | Programa: Biodiversidad de Vegetales | [427](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/427/149/) |  |
| 21 | `archivos/programas/fisica-para-paleontologos` | Programa: Física para Paleontólogos | [428](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/428/149/) |  |
| 22 | `archivos/programas/electromagnetismo-y-optica` | Programa: Electromagnetismo y Óptica (reemplaza a Física para Paleontólogos) | [447](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/447/149/) |  |
| 23 | `archivos/programas/introduccion-biologia-molecular` | Programa: Int. a la Biología Molecular para Paleontólogos | [429](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/429/149/) |  |
| 24 | `archivos/programas/quimica-organica` | Programa: Química Orgánica para Paleontólogos | [430](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/430/149/) |  |
| 25 | `archivos/programas/quimica-general-e-inorganica` | Programa: Química General e Inorgánica para Paleontólogos | [431](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/431/149/) |  |
| 26 | `archivos/programas/paleontologia` | Programa: Paleontología | [432](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/432/149/) |  |
| 27 | `archivos/programas/genetica-general` | Programa: Genética General para Paleontólogos | [433](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/433/149/) |  |
| 28 | `archivos/programas/biometria` | Programa: Biometría | [434](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/434/149/) |  |
| 29 | `archivos/programas/vertebrados` | Programa: Vertebrados | [435](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/435/149/) |  |
| 30 | `archivos/programas/evolucion` | Programa: Evolución para Paleontólogos | [441](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/441/149/) |  |
| 31 | `archivos/programas/introduccion-ciencias-atmosfera-oceanos` | Programa: Int. a las Cs. de la Atmósfera y los Océanos | [442](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/442/149/) |  |
| 32 | `archivos/programas/paleobotanica` | Programa: Paleobotánica | [443](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/443/149/) |  |
| 33 | `archivos/programas/paleontologia-de-invertebrados` | Programa: Paleontología de Invertebrados | [444](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/444/149/) |  |
| 34 | `archivos/programas/paleontologia-de-vertebrados` | Programa: Paleontología de Vertebrados | [459](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/459/149/) |  |
| 35 | `archivos/actas/2011-05-24` | Acta de la Comisión de Carrera, 24 de mayo de 2011 | [254](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/254/129/) |  |
| 36 | `archivos/actas/2011-08-02` | Acta de la Comisión de Carrera, 2 de agosto de 2011 | [253](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/253/129/) |  |
| 37 | `archivos/actas/2011-09-14` | Acta de la Comisión de Carrera, 14 de septiembre de 2011 | [252](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/252/129/) |  |
| 38 | `archivos/actas/2011-11-22` | Acta de la Comisión de Carrera, 22 de noviembre de 2011 | [251](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/251/129/) |  |
| 39 | `archivos/actas/2011-12-19` | Acta de la Comisión de Carrera, 19 de diciembre de 2011 | [250](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/250/129/) |  |
| 40 | `archivos/actas/2012-02-10` | Acta de la Comisión de Carrera, 10 de febrero de 2012 | [258](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/258/129/) |  |
| 41 | `archivos/actas/2012-02-24` | Acta de la Comisión de Carrera, 24 de febrero de 2012 | [259](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/259/129/) |  |
| 42 | `archivos/actas/2012-05-07` | Acta de la Comisión de Carrera, 7 de mayo de 2012 | [260](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/260/129/) |  |
| 43 | `archivos/actas/2012-08-03` | Acta de la Comisión de Carrera, 3 de agosto de 2012 | [279](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/279/129/) |  |
| 44 | `archivos/actas/2012-10-12` | Acta de la Comisión de Carrera, 12 de octubre de 2012 | [261](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/261/129/) |  |
| 45 | `archivos/actas/2012-12-17` | Acta de la Comisión de Carrera, 17 de diciembre de 2012 | [262](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/262/129/) |  |
| 46 | `archivos/actas/2013-02-06` | Acta de la Comisión de Carrera, 6 de febrero de 2013 | [264](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/264/129/) |  |
| 47 | `archivos/actas/2013-02-18` | Acta de la Comisión de Carrera, 18 de febrero de 2013 | [263](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/263/129/) |  |
| 48 | `archivos/actas/2013-06-03` | Acta de la Comisión de Carrera, 3 de junio de 2013 | [276](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/276/129/) |  |
| 49 | `archivos/actas/2013-07-11` | Acta de la Comisión de Carrera, 11 de julio de 2013 | [278](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/278/129/) |  |
| 50 | `archivos/actas/2013-11-27` | Acta de la Comisión de Carrera, 27 de noviembre de 2013 | [290](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/290/129/) |  |
| 51 | `archivos/actas/2013-12-26` | Acta de la Comisión de Carrera, 26 de diciembre de 2013 | [292](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/292/129/) |  |
| 52 | `archivos/actas/2014-02-14` | Acta de la Comisión de Carrera, 14 de febrero de 2014 | [294](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/294/129/) |  |
| 53 | `archivos/actas/2014-02-24` | Acta de la Comisión de Carrera, 24 de febrero de 2014 | [295](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/295/129/) |  |
| 54 | `archivos/actas/2014-04-07` | Acta de la Comisión de Carrera, 7 de abril de 2014 | [296](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/296/129/) |  |
| 55 | `archivos/actas/2014-05-12` | Acta de la Comisión de Carrera, 12 de mayo de 2014 | [297](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/297/129/) |  |
| 56 | `archivos/actas/2014-07-04` | Acta de la Comisión de Carrera, 4 de julio de 2014 | [298](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/298/129/) |  |
| 57 | `archivos/actas/2014-09-02` | Acta de la Comisión de Carrera, 2 de septiembre de 2014 | [299](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/299/129/) |  |
| 58 | `archivos/actas/2014-10-20` | Acta de la Comisión de Carrera, 20 de octubre de 2014 | [301](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/301/129/) |  |
| 59 | `archivos/actas/2014-12` | Acta de la Comisión de Carrera, diciembre de 2014 | [302](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/302/129/) | ⚠️ El sitio viejo dice solo "Diciembre de 2014" |
| 60 | `archivos/actas/2015-04-01` | Acta de la Comisión de Carrera, 1 de abril de 2015 | [304](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/304/129/) |  |
| 61 | `archivos/actas/2015-05-08` | Acta de la Comisión de Carrera, 8 de mayo de 2015 | [310](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/310/129/) |  |
| 62 | `archivos/actas/2015-06-05` | Acta de la Comisión de Carrera, 5 de junio de 2015 | [311](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/311/129/) |  |
| 63 | `archivos/actas/2015-07-10` | Acta de la Comisión de Carrera, 10 de julio de 2015 | [312](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/312/129/) |  |
| 64 | `archivos/actas/2015-08-06` | Acta de la Comisión de Carrera, 6 de agosto de 2015 | [313](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/313/129/) |  |
| 65 | `archivos/actas/2015-10-01` | Acta de la Comisión de Carrera, 1 de octubre de 2015 | [314](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/314/129/) |  |
| 66 | `archivos/actas/2015-10-26` | Acta de la Comisión de Carrera, 26 de octubre de 2015 | [315](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/315/129/) |  |
| 67 | `archivos/actas/2015-11-26` | Acta de la Comisión de Carrera, 26 de noviembre de 2015 | [316](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/316/129/) |  |
| 68 | `archivos/actas/2016-02-11` | Acta de la Comisión de Carrera, 11 de febrero de 2016 | [318](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/318/129/) |  |
| 69 | `archivos/actas/2016-04-14` | Acta de la Comisión de Carrera, 14 de abril de 2016 | [317](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/317/129/) |  |
| 70 | `archivos/actas/2016-05-24` | Acta de la Comisión de Carrera, 24 de mayo de 2016 | [319](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/319/129/) |  |
| 71 | `archivos/actas/2016-08-08` | Acta de la Comisión de Carrera, 8 de agosto de 2016 | [324](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/324/129/) |  |
| 72 | `archivos/actas/2016-08-22` | Acta de la Comisión de Carrera, 22 de agosto de 2016 | [322](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/322/129/) |  |
| 73 | `archivos/actas/2016-09-26` | Acta de la Comisión de Carrera, 26 de septiembre de 2016 | [323](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/323/129/) |  |
| 74 | `archivos/actas/2017-02-21` | Acta de la Comisión de Carrera, 21 de febrero de 2017 | [328](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/328/129/) |  |
| 75 | `archivos/actas/2017-03-20` | Acta de la Comisión de Carrera, 20 de marzo de 2017 | [329](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/329/129/) |  |
| 76 | `archivos/actas/2017-04-24` | Acta de la Comisión de Carrera, 24 de abril de 2017 | [330](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/330/129/) |  |
| 77 | `archivos/actas/2017-06-26` | Acta de la Comisión de Carrera, 26 de junio de 2017 | [331](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/331/129/) |  |
| 78 | `archivos/actas/2017-08-22` | Acta de la Comisión de Carrera, 22 de agosto de 2017 | [332](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/332/129/) |  |
| 79 | `archivos/actas/2017-10-30` | Acta de la Comisión de Carrera, 30 de octubre de 2017 | [334](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/334/129/) |  |
| 80 | `archivos/actas/2017-12-05` | Acta de la Comisión de Carrera, 5 de diciembre de 2017 | [333](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/333/129/) |  |
| 81 | `archivos/actas/2018-02-02` | Acta de la Comisión de Carrera, 2 de febrero de 2018 | [335](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/335/129/) |  |
| 82 | `archivos/actas/2018-03-06` | Acta de la Comisión de Carrera, 6 de marzo de 2018 | [336](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/336/129/) |  |
| 83 | `archivos/actas/2018-04-13` | Acta de la Comisión de Carrera, 13 de abril de 2018 | [337](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/337/129/) |  |
| 84 | `archivos/actas/2018-05-11` | Acta de la Comisión de Carrera, 11 de mayo de 2018 | [338](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/338/129/) |  |
| 85 | `archivos/actas/2018-06-14` | Acta de la Comisión de Carrera, 14 de junio de 2018 | [344](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/344/129/) |  |
| 86 | `archivos/actas/2018-08-10` | Acta de la Comisión de Carrera, 10 de agosto de 2018 | [345](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/345/129/) |  |
| 87 | `archivos/actas/2018-10-12` | Acta de la Comisión de Carrera, 12 de octubre de 2018 | [346](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/346/129/) |  |
| 88 | `archivos/actas/2018-11-09` | Acta de la Comisión de Carrera, 9 de noviembre de 2018 | [347](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/347/129/) |  |
| 89 | `archivos/actas/2018-12-04` | Acta de la Comisión de Carrera, 4 de diciembre de 2018 | [348](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/348/129/) |  |
| 90 | `archivos/actas/2018-12-28` | Acta de la Comisión de Carrera, 28 de diciembre de 2018 | [349](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/349/129/) |  |
| 91 | `archivos/actas/2019-02-04` | Acta de la Comisión de Carrera, 4 de febrero de 2019 | [350](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/350/129/) |  |
| 92 | `archivos/actas/2019-02-25` | Acta de la Comisión de Carrera, 25 de febrero de 2019 | [351](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/351/129/) |  |
| 93 | `archivos/actas/2019-03-29` | Acta de la Comisión de Carrera, 29 de marzo de 2019 | [352](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/352/129/) |  |
| 94 | `archivos/actas/2019-04-29` | Acta de la Comisión de Carrera, 29 de abril de 2019 | [353](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/353/129/) |  |
| 95 | `archivos/actas/2019-05-31` | Acta de la Comisión de Carrera, 31 de mayo de 2019 | [355](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/355/129/) |  |
| 96 | `archivos/actas/2019-06-28` | Acta de la Comisión de Carrera, 28 de junio de 2019 | [356](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/356/129/) |  |
| 97 | `archivos/actas/2019-08-23` | Acta de la Comisión de Carrera, 23 de agosto de 2019 | [359](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/359/129/) |  |
| 98 | `archivos/actas/2019-09-30` | Acta de la Comisión de Carrera, 30 de septiembre de 2019 | [360](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/360/129/) |  |
| 99 | `archivos/actas/2019-10-31` | Acta de la Comisión de Carrera, 31 de octubre de 2019 | [361](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/361/129/) |  |
| 100 | `archivos/actas/2019-11-27` | Acta de la Comisión de Carrera, 27 de noviembre de 2019 | [362](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/362/129/) |  |
| 101 | `archivos/actas/2019-12-18` | Acta de la Comisión de Carrera, 18 de diciembre de 2019 | [370](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/370/129/) |  |
| 102 | `archivos/actas/2020-02-14` | Acta de la Comisión de Carrera, 14 de febrero de 2020 | [396](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/396/129/) |  |
| 103 | `archivos/actas/2020-05-22` | Acta de la Comisión de Carrera, 22 de mayo de 2020 | [389](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/389/129/) |  |
| 104 | `archivos/actas/2020-06-19` | Acta de la Comisión de Carrera, 19 de junio de 2020 | [390](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/390/129/) |  |
| 105 | `archivos/actas/2020-07-17` | Acta de la Comisión de Carrera, 17 de julio de 2020 | [391](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/391/129/) |  |
| 106 | `archivos/actas/2020-08-21` | Acta de la Comisión de Carrera, 21 de agosto de 2020 | [392](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/392/129/) |  |
| 107 | `archivos/actas/2020-09-24` | Acta de la Comisión de Carrera, 24 de septiembre de 2020 | [393](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/393/129/) |  |
| 108 | `archivos/actas/2020-10-29` | Acta de la Comisión de Carrera, 29 de octubre de 2020 | [394](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/394/129/) |  |
| 109 | `archivos/actas/2020-12-15` | Acta de la Comisión de Carrera, 15 de diciembre de 2020 | [395](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/395/129/) |  |
| 110 | `archivos/actas/2021-02-17` | Acta de la Comisión de Carrera, 17 de febrero de 2021 | [399](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/399/129/) |  |
| 111 | `archivos/actas/2021-03-29` | Acta de la Comisión de Carrera, 29 de marzo de 2021 | [400](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/400/129/) |  |
| 112 | `archivos/actas/2021-04-30` | Acta de la Comisión de Carrera, 30 de abril de 2021 | [401](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/401/129/) |  |
| 113 | `archivos/actas/2021-05-31` | Acta de la Comisión de Carrera, 31 de mayo de 2021 | [402](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/402/129/) |  |
| 114 | `archivos/actas/2021-08-23` | Acta de la Comisión de Carrera, 23 de agosto de 2021 | [403](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/403/129/) |  |
| 115 | `archivos/actas/2021-10-04` | Acta de la Comisión de Carrera, 4 de octubre de 2021 | [404](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/404/129/) |  |
| 116 | `archivos/actas/2021-11-15` | Acta de la Comisión de Carrera, 15 de noviembre de 2021 | [405](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/405/129/) |  |
| 117 | `archivos/actas/2021-12-20` | Acta de la Comisión de Carrera, 20 de diciembre de 2021 | [406](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/406/129/) |  |
| 118 | `archivos/actas/2022-02-21` | Acta de la Comisión de Carrera, 21 de febrero de 2022 | [408](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/408/129/) |  |
| 119 | `archivos/actas/2022-06-06` | Acta de la Comisión de Carrera, 6 de junio de 2022 | [409](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/409/129/) |  |
| 120 | `archivos/actas/2022-08-12` | Acta de la Comisión de Carrera, 12 de agosto de 2022 | [416](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/416/129/) |  |
| 121 | `archivos/actas/2022-10-24` | Acta de la Comisión de Carrera, 24 de octubre de 2022 | [415](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/415/129/) |  |
| 122 | `archivos/actas/2022-12-05` | Acta de la Comisión de Carrera, 5 de diciembre de 2022 | [413](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/413/129/) |  |
| 123 | `archivos/actas/2023-02-15` | Acta de la Comisión de Carrera, 15 de febrero de 2023 | [417](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/417/129/) |  |
| 124 | `archivos/actas/2023-04-18` | Acta de la Comisión de Carrera, 18 de abril de 2023 | [418](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/418/129/) |  |
| 125 | `archivos/actas/2023-06-22` | Acta de la Comisión de Carrera, 22 de junio de 2023 | [420](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/420/129/) |  |
| 126 | `archivos/actas/2023-09-13` | Acta de la Comisión de Carrera, 13 de septiembre de 2023 | [421](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/421/129/) |  |
| 127 | `archivos/actas/2023-11-23` | Acta de la Comisión de Carrera, 23 de noviembre de 2023 | [422](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/422/129/) |  |
| 128 | `archivos/actas/2023-12-21` | Acta de la Comisión de Carrera, 21 de diciembre de 2023 | [423](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/423/129/) | ⚠️ VERIFICAR: el sitio viejo lo titula "21 de diciembre 2024" pero está en la lista de 2023 |
| 129 | `archivos/actas/2024-02-15` | Acta de la Comisión de Carrera, 15 de febrero de 2024 | [424](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/424/129/) | ⚠️ VERIFICAR: el sitio viejo lo titula "15 de febrero 2022" pero está en la lista de 2024 |
| 130 | `archivos/actas/2024-04-29` | Acta de la Comisión de Carrera, 29 de abril de 2024 | [436](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/436/129/) |  |
| 131 | `archivos/actas/2024-07-30` | Acta de la Comisión de Carrera, 30 de julio de 2024 | [437](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/437/129/) |  |
| 132 | `archivos/actas/2024-10-03` | Acta de la Comisión de Carrera, 3 de octubre de 2024 | [438](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/438/129/) |  |
| 133 | `archivos/actas/2024-11-04` | Acta de la Comisión de Carrera, 4 de noviembre de 2024 | [439](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/439/129/) |  |
| 134 | `archivos/actas/2025-03-06` | Acta de la Comisión de Carrera, 6 de marzo de 2025 | [463](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/463/129/) |  |
| 135 | `archivos/actas/2025-05-27` | Acta de la Comisión de Carrera, 27 de mayo de 2025 | [445](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/445/129/) |  |
| 136 | `archivos/actas/2025-10-01` | Acta de la Comisión de Carrera, 1 de octubre de 2025 | [446](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/446/129/) |  |
| 137 | `archivos/actas/2025-11-18` | Acta de la Comisión de Carrera, 18 de noviembre de 2025 | [460](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/460/129/) |  |
| 138 | `archivos/actas/2026-03-06` | Acta de la Comisión de Carrera, 6 de marzo de 2026 | [461](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/461/129/) |  |
| 139 | `archivos/actas/2026-05-04` | Acta de la Comisión de Carrera, 4 de mayo de 2026 | [462](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/462/129/) |  |
| 140 | `archivos/actas/2013-elecciones-estudiantes` | Acta de elecciones de estudiantes 2013 | [277](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/277/129/) |  |
| 141 | `archivos/actas/2014-carta-4th-international-palaeontological-congress` | Carta 4th International Palaeontological Congress (2014) | [300](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/300/129/) |  |
| 142 | `archivos/actas/2015-sin-titulo` | Archivo sin título en la lista de actas 2015 | [303](http://paleo.gl.fcen.uba.ar/index.php/download_file/view/303/129/) | ⚠️ VERIFICAR: el link no tiene texto; abrirlo para ver qué es |
