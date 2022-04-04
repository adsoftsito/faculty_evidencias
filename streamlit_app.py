import streamlit as st
from google.cloud import firestore

db = firestore.Client.from_service_account_json("names-firebase.json")
# st.image("/content/tecnologia.jpeg")

st.title("Registro de Evidencias de Capacitación de Profesores")

# Streamlit widgets to let a user create a new post
nombre = st.text_input("Nombre del Profesor")
nomina = st.text_input("Nomina del Profesor")

tipoContrato = st.radio(
     "Tipo de Contrato",
     ('Profesor de Planta', 'Profesor de Planta, status Investigador', 'Profesor de Cátedra', 'Especialista', 'Laboratorista', 'Otro'))


clasificacionPlanta = st.radio(
     "Tipo de Contrato",
     ('Profesor de Planta Sin clasificar', 'Profesor de Planta Asistente', 'Profesor de Planta  Asociado', 'Profesor de Planta Titular', 'Profesor de Cátedra Docente (imparte el equivalente a aprox. 3 clases)', 'Profesor de Cátedra Activo (profesor con puesto en una empresa y que imparte el equivalente  a aprox. 1 clase)', 'Profesor de Cátedra con Experiencia (profesor jubilado que imparte aprox. 1 clase)',  'Otro'))



region = st.radio(
     "Tipo de Contrato",
     ('Región Norte', 'Región Centro-Sur', 'Región Ciudad de México', 'Región Occidente', 'Otro'))


st.write('Por favor, lista los nombres de los Certificados que vas a subir y al lado escribe entre paréntisis el número de horas que acredita cada Certificado.')

uploaded_files = st.file_uploader("Choose a PDF file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
     bytes_data = uploaded_file.read()
     st.write("filename:", uploaded_file.name)
     #st.write(bytes_data)

st.write('¿Con mi conocimiento y con los cursos que tomé me siento capacitado para?:')
option_s = st.checkbox('Impartir cursos en Python básico')
option_u = st.checkbox('Impartir cursos en Python avanzado')
option_v = st.checkbox('Estadística con Visualización')
option_a = st.checkbox('Diseño de Dashboards')
option_t = st.checkbox('Modelación de Datos numéricos utilizando Máquinas Inteligentes')
option_x = st.checkbox('Modelación de Datos de Texto utilizando Máquinas Inteligentes')
option_y = st.checkbox('Curso de Big Data')
option_z = st.checkbox('Curso de IoT')
option_o = st.checkbox('Otro')

region = st.radio(
     "Si no eres investigador... ¿Te gustaría realizar investigación con un profesor investigador con miras a publicar un artículo de investigación?",
     ('Si me interesa y con algo de esfuerzo estoy seguro que puedo apoyar.', 'Si me interesa, pero siento que me falta algo de experiencia, pero si me guían seguro puedo aportar.', 'Otra opcion' ))


#st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>', unsafe_allow_html=True)
#st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>', unsafe_allow_html=True)

region = st.radio(
     "¿Te parece bien que los cursos CADI sean en en formato MOOC (i.e. Coursera)?",
     ('1', '2', '3', '4',  '5' ))

nombre = st.text_area("Comentarios")

submit = st.button("Submit new post")

# Once the user has submitted, upload it to the database
if nombre and nomina and submit:
	doc_ref = db.collection("posts").document(nombre)
	doc_ref.set({
		"nombre": nombre,
		"nomina": nomina
	})

# And then render each post, using some light Markdown
# posts_ref = db.collection("posts")
# for doc in posts_ref.stream():
#	post = doc.to_dict()
#	nombre = post["nombre"]
#	nomina = post["nomina"]

#	st.subheader(f"Items: {nombre} {nomina}")
	#st.write(f":link: [{url}]({url})")
