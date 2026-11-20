# id, carpeta/nombre destino (sin extension), descripcion, seccion
B="http://paleo.gl.fcen.uba.ar/index.php/download_file/view/%s/%s/"
MESES={'enero':1,'febrero':2,'marzo':3,'abril':4,'mayo':5,'junio':6,'julio':7,'agosto':8,'septiembre':9,'octubre':10,'noviembre':11,'diciembre':12}
actas = [  # id, fecha ISO, nota
(250,'2011-12-19',''),(251,'2011-11-22',''),(252,'2011-09-14',''),(253,'2011-08-02',''),(254,'2011-05-24',''),
(258,'2012-02-10',''),(259,'2012-02-24',''),(260,'2012-05-07',''),(279,'2012-08-03',''),(261,'2012-10-12',''),(262,'2012-12-17',''),
(264,'2013-02-06',''),(263,'2013-02-18',''),(276,'2013-06-03',''),(278,'2013-07-11',''),(290,'2013-11-27',''),(292,'2013-12-26',''),
(294,'2014-02-14',''),(295,'2014-02-24',''),(296,'2014-04-07',''),(297,'2014-05-12',''),(298,'2014-07-04',''),(299,'2014-09-02',''),(301,'2014-10-20',''),(302,'2014-12','El sitio viejo dice solo "Diciembre de 2014"'),
(303,'2015-02-26','En el sitio viejo figuraba sin título'),(304,'2015-04-01',''),(310,'2015-05-08',''),(311,'2015-06-05',''),(312,'2015-07-10',''),(313,'2015-08-06',''),(314,'2015-10-01',''),(315,'2015-10-26',''),(316,'2015-11-26',''),
(318,'2016-02-11',''),(317,'2016-04-14',''),(319,'2016-05-24',''),(324,'2016-08-08',''),(322,'2016-08-22',''),(323,'2016-09-26',''),
(328,'2017-02-21',''),(329,'2017-03-20',''),(330,'2017-04-24',''),(331,'2017-06-26',''),(332,'2017-08-22',''),(334,'2017-10-30',''),(333,'2017-12-05',''),
(335,'2018-02-02',''),(336,'2018-03-06',''),(337,'2018-04-13',''),(338,'2018-05-11',''),(344,'2018-06-14',''),(345,'2018-08-10',''),(346,'2018-10-12',''),(347,'2018-11-09',''),(348,'2018-12-04',''),(349,'2018-12-28',''),
(350,'2019-02-04',''),(351,'2019-02-25',''),(352,'2019-03-29',''),(353,'2019-04-29',''),(355,'2019-05-31',''),(356,'2019-06-28',''),(359,'2019-08-23',''),(360,'2019-09-30',''),(361,'2019-10-31',''),(362,'2019-11-27',''),(370,'2019-12-18',''),
(396,'2020-02-14',''),(389,'2020-05-22',''),(390,'2020-06-19',''),(391,'2020-07-17',''),(392,'2020-08-21',''),(393,'2020-09-24',''),(394,'2020-10-29',''),(395,'2020-12-15',''),
(399,'2021-02-17',''),(400,'2021-03-29',''),(401,'2021-04-30',''),(402,'2021-05-31',''),(403,'2021-08-23',''),(404,'2021-10-04',''),(405,'2021-11-15',''),(406,'2021-12-20',''),
(408,'2022-02-21',''),(409,'2022-06-06',''),(416,'2022-08-12',''),(415,'2022-10-24',''),(413,'2022-12-05',''),
(417,'2023-02-15',''),(418,'2023-04-18',''),(420,'2023-06-22',''),(421,'2023-09-13',''),(422,'2023-11-23',''),(423,'2023-12-21','VERIFICAR: el sitio viejo lo titula "21 de diciembre 2024" pero está en la lista de 2023'),
(424,'2024-02-15','VERIFICAR: el sitio viejo lo titula "15 de febrero 2022" pero está en la lista de 2024'),(436,'2024-04-29',''),(437,'2024-07-30',''),(438,'2024-10-03',''),(439,'2024-11-04',''),
(463,'2025-03-06',''),(445,'2025-05-27',''),(446,'2025-10-01',''),(460,'2025-11-18',''),
(461,'2026-03-06',''),(462,'2026-05-04',''),
]
otros_comision=[(277,'actas/2013-elecciones-estudiantes','Acta de elecciones de estudiantes 2013',''),
(300,'actas/2014-carta-4th-international-palaeontological-congress','Carta 4th International Palaeontological Congress (2014)','')]
programas=[(426,'biodiversidad-de-animales','Biodiversidad de Animales'),(427,'biodiversidad-de-vegetales','Biodiversidad de Vegetales'),
(428,'fisica-para-paleontologos','Física para Paleontólogos'),(447,'electromagnetismo-y-optica','Electromagnetismo y Óptica (reemplaza a Física para Paleontólogos)'),
(429,'introduccion-biologia-molecular','Int. a la Biología Molecular para Paleontólogos'),(430,'quimica-organica','Química Orgánica para Paleontólogos'),
(431,'quimica-general-e-inorganica','Química General e Inorgánica para Paleontólogos'),(432,'paleontologia','Paleontología'),
(433,'genetica-general','Genética General para Paleontólogos'),(434,'biometria','Biometría'),(435,'vertebrados','Vertebrados'),
(441,'evolucion','Evolución para Paleontólogos'),(442,'introduccion-ciencias-atmosfera-oceanos','Int. a las Cs. de la Atmósfera y los Océanos'),
(443,'paleobotanica','Paleobotánica'),(444,'paleontologia-de-invertebrados','Paleontología de Invertebrados'),(459,'paleontologia-de-vertebrados','Paleontología de Vertebrados')]
docs=[
(371,1,'folleto-paleontologia','Folleto informativo de la Licenciatura','Inicio',''),
(372,148,'resoluciones/creacion-carrera-2001','Resolución de creación de la carrera (2001)','Documentos',''),
(358,148,'resoluciones/validez-nacional-titulo','Validez nacional del título (Res. ME 922/2014)','Documentos',''),
(457,148,'resoluciones/profesorado-biologia','Resolución del Profesorado de Enseñanza Media y Superior, especialidad Biología','Documentos',''),
(448,131,'resoluciones/res-cd-1911-2023','Res. CD 1911/2023 (Física → Electromagnetismo y Óptica)','La licenciatura',''),
(449,131,'resoluciones/res-cd-2510-2017','Res. CD 2510/2017 (equivalencia de Química General e Inorgánica)','La licenciatura',''),
(283,148,'reglamentos/reglamento-comision-carrera','Reglamento de la Comisión de Carrera','Documentos',''),
(282,148,'reglamentos/reglamento-tutores-y-planes-de-estudio','Reglamento de tutores y planes de estudio','Documentos',''),
(281,148,'reglamentos/reglamento-tesis','Reglamento de Tesis de Licenciatura','Documentos','Probablemente igual al n.º 266; bajar los dos y comparar'),
(266,147,'reglamentos/reglamento-tesis-2011','Reglamento de Tesis de Licenciatura (versión de la página Tesis)','Tesis de Licenciatura','Probablemente igual al n.º 281'),
(397,148,'reglamentos/reglamento-premio-camacho','Reglamento del Premio Camacho a la mejor Tesis de Licenciatura','Documentos',''),
(450,148,'modelos/carta-plan-de-estudios-2026','Modelo de carta para plan de estudios (2026)','Documentos','Puede ser Word en vez de PDF'),
(458,148,'modelos/carta-plan-de-tesis-2026','Modelo de carta para presentar plan de tesis (2026)','Documentos','Puede ser Word en vez de PDF'),
(452,148,'modelos/carta-presentar-tesis-2026','Modelo de carta para presentar tesis (2026)','Documentos','Puede ser Word en vez de PDF'),
(326,147,'modelos/formulario-jurados-tesis','Formulario de jurados de tesis (Word)','Tesis de Licenciatura','Es Word: guardarlo con la extensión que traiga (.doc o .docx)'),
(327,147,'modelos/formulario-jurados-tesis','Formulario de jurados de tesis (PDF)','Tesis de Licenciatura',''),
(414,147,'modelos/formulario-biblioteca-entrega-tesis','Formulario de la Biblioteca FCEN para entregar las tesis (2023)','Tesis de Licenciatura',''),
(383,154,'doctorado/reglamento-doctorado-fcen-2021','Reglamento de Doctorado de la FCEN-UBA (2021)','Doctorado',''),
(384,154,'doctorado/resolucion-coneau-acreditacion','Resolución CONEAU de acreditación del Doctorado, Área Paleontología','Doctorado',''),
(425,148,'tesis/listado-tesis-2008-2024','Listado de Tesis de Licenciatura defendidas 2008-2024','Documentos',''),
]
def fecha_txt(f):
    p=f.split('-'); m=[k for k,v in MESES.items() if v==int(p[1])][0]
    return (f"{int(p[2])} de {m} de {p[0]}" if len(p)==3 else f"{m} de {p[0]}")
rows=[]
for i,c,n,d,s,nota in docs: rows.append((i,B%(i,c),n,d,s,nota))
for i,n,d in programas: rows.append((i,B%(i,149),'programas/'+n,'Programa: '+d,'Materias',''))
for i,f,nota in sorted(actas,key=lambda a:a[1]): rows.append((i,B%(i,129),'actas/'+f,'Acta de la Comisión de Carrera, '+fecha_txt(f),'Comisión de Carrera',nota))
for i,n,d,nota in otros_comision: rows.append((i,B%(i,129),n,d,'Comisión de Carrera',nota))
