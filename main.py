from flask import *
from healthcare import healthcare1
from  e_comerce import e_comerce1
from  finance import finance1
from  technology import technology1
from  domain import domain1

carriers={ "doctor":{"name":"doctor","image":"https://img.freepik.com/free-photo/attractive-young-male-nutriologist-lab-coat-smiling-against-white-background_662251-2960.jpg","para":["A doctor is a licensed medical professional who is trained to diagnose and treat illnesses, injuries, and medical conditions in patients. Doctors can specialize in a particular area of medicine, such as cardiology, pediatrics, or oncology, among others.","To become a doctor, one must first complete a bachelor's degree, followed by medical school, which typically takes four years to complete. After medical school, doctors must complete a residency program, which can take anywhere from three to  seven years, depending on their area of specialization. During this time, they work under the supervision of experienced doctors and gain hands-on experience in treating patients.","Doctors play a vital role in the healthcare system, and their work involves examining patients, ordering diagnostic tests, prescribing medications,and performing medical procedures when necessary. They also provide guidance on reventive care, such as vaccinations and lifestyle changes, to help patients maintain their health and prevent illnesses from occurring in the first place.","Overall, being a doctor is a highly demanding and challenging profession, but it can also be incredibly rewarding, as doctors have the opportunity to make a significant impact on the lives of their patients."],"types":["General Practitioners/Family Physicians","Pediatricians","Obstetricians/Gynecologists","Cardiologists","Neurologists","Psychiatrists","Dermatologists","Oncologists","Endocrinologists","Gastroenterologists","Pulmonologists","Rheumatologists","Orthopedists","Ophthalmologists","ENT (Ear, Nose, and Throat) Specialists"]},
            
            "engineer":{"name":"Engineer","image":"https://www.capgemini.com/wp-content/uploads/2022/02/Capgemini-Engineering_HERO-BANNER-ERD-Career-Page-e1643889563615.jpg","para":["An engineer is a professional who applies scientific and mathematical principles to design, develop, and maintain various types of products, systems, and processes. Engineers are responsible for developing solutions to problems, improving existing technologies, and creating new innovations.","Engineers need to have strong problem-solving skills, critical thinking abilities, and good communication skills. They also need to have a deep understanding of mathematics, physics, and other sciences.In order to become an engineer, one typically needs to earn a bachelor's degree in engineering from an accredited university or college. Some engineers also go on to earn advanced degrees, such as a master's degree or a Ph.D. in engineering.","Overall, engineers play a critical role in society by creating and implementing solutions that improve the quality of life for people. They work in a variety of industries, including manufacturing, construction, transportation, healthcare, energy, and many others."],"types":["Mechanical Engineers","Electrical Engineers","Civil Engineers","Chemical Engineers","Aerospace Engineers","Computer Engineers","Environmental Engineers","Biomedical Engineers","Industrial Engineers","Materials Engineers","Nuclear Engineers","Petroleum Engineers","Software Engineers"]},

            "teacher":{"name":"Teachers","image":"https://wallpaperaccess.com/full/697849.jpg","para":["A teacher is a professional who educates and instructs students in a variety of subjects, ranging from academic to vocational areas. Teachers may work in public or private schools, universities, community colleges, or other educational institutions. They play a critical role in helping students develop knowledge, skills, and attitudes that will prepare them for future success.","Teachers need to have strong communication skills, patience, and creativity. They must also be able to adapt their teaching style to meet the diverse learning needs of their students. In addition, they must stay up-to-date with changes in curriculum, teaching methods, and educational technologies.To become a teacher, one typically needs to earn a bachelor's degree in education or a specific subject area, such as math or English. Many states also require teachers to earn a teaching credential or license, which involves completing a teacher education program and passing state certification exams.","Overall, teachers play a critical role in society by educating and inspiring the next generation of leaders, innovators, and problem-solvers. They have a profound impact on the lives of their students and help shape the future of society."],"types":["High school teacher","College professor","Special education teacher","ESL teacher","Vocational education teacher","Music teacher","Art teacher","Physical education teacher"]},         

            "artist":{"name":"Artist","image":"https://wallpaperaccess.com/full/1209478.jpg","para":["An artist is a person who creates art, which is a form of expression that uses various mediums, such as painting, drawing, sculpture, music, dance, and many others. Artists often use their creativity and imagination to convey ideas, emotions, and messages through their work.","To become an artist, one typically needs to have a natural talent or a passion for art, as well as the technical skills and knowledge of various mediums and techniques. Some artists may earn a formal education in art or a related field, such as art history or design.The role of an artist can vary depending on their specific field. For example, a painter may create original works of art using paint, brushes, and canvas, while a graphic designer may create designs using digital software. A sculptor may create three-dimensional works of art using various materials, such as clay, metal, or wood.","Overall, artists play a critical role in society by creating works of art that inspire, challenge, and move people. They have the power to transform the way we see the world, and their work often reflects the cultural, social, and political issues of their time."],"types":["Painter","Sculptor","PhotographerAnimator","Filmmaker","Musician","Singer,""Dancer","Actor","Writer","Poet"]},
         
            "architect":{"name":"Architect","image":"https://www.pixelstalk.net/wp-content/uploads/2016/10/Architectural-HD-Wallpapers.jpg","para":["Architecture is the art and science of designing and planning buildings and other physical structures. It involves the creation of functional and aesthetically pleasing spaces that meet the needs of the people who will use them. Architects are professionals who specialize in the design, planning, and construction of buildings and other physical structures.","Overall, the role of an architect is to use their knowledge and skills to create functional, sustainable, and aesthetically pleasing buildings and other physical structures that meet the needs of the people who will use them."],"types":["Residential Architects","Commercial Architects","Landscape Architects","Interior Architects","Urban Design Architects","Sustainable Design Architects","Restoration Architects"]},

            "accountant":{"name":"Accountant","image":"https://wallpapercave.com/wp/wp2164078.jpg","para":["An accountant is a professional who specializes in financial management and record-keeping. They play a crucial role in helping individuals, businesses, and organizations maintain accurate financial records and make informed decisions regarding their finances. ","A bachelor's degree in accounting, finance, or a related field is typically required to become an accountant.Professional certifications such as Certified Public Accountant (CPA), Certified Management Accountant (CMA), or Chartered Accountant (CA) may be required or preferred depending on the job and location.Strong analytical, communication, and organizational skills are essential for success in this field.","Overall, an accountant is a highly skilled and valuable professional who plays a crucial role in managing financial records and ensuring the financial health of individuals and organizations."],"types":["Public Accountant","Management Accountant","Government Accountant","Internal Auditor","Forensic Accountant","Tax Accountant","Cost Accountant"]}
         }
app = Flask(__name__,template_folder="templates",static_url_path='/static')





["Technology", "Finance", "E-commerce", "Healthcare"]
@app.route("/")
def index():
    return render_template('home.html') 

@app.route("/interest")
def intrest():
    return render_template('intrest.html') 

@app.route("/carrier/<name>")
def carrier(name):
    return render_template('carrier.html',data=carriers[name]) 


@app.route('/survey')
def quiz():
    return render_template('form.html')

@app.route('/form', methods=['POST'])
def form():
    answers = []
    answers.append(request.form['q1'])
    answers.append(request.form['q2'])
    answers.append(request.form['q3'])
    answers.append(request.form['q4'])
    answers.append(request.form['q5'])
    answers.append(request.form['q6'])
    answers.append(request.form['q7'])
    answers.append(request.form['q8'])
    answers.append(request.form['q9'])
    answers.append(request.form['q10'])
    answers.append(request.form['q11'])
    answers.append(request.form['q12'])
    answers.append(request.form['q13'])
    answers.append(request.form['q14'])
    answers.append(request.form['q15'])  
    a=domain1(answers)
    print(a)
    if a=="Technology":
        return render_template('technology.html')
    if a=="Finance":
        return render_template('finance.html')
    if a=="E-commerce":
        return render_template('e_commerce.html')
    if a=="Healthcare":
        return render_template('healthcare.html')    

@app.route('/technology', methods=['POST'])
def technology():
    answers = []
    answers.append(request.form['q1'])
    answers.append(request.form['q2'])
    answers.append(request.form['q3'])
    answers.append(request.form['q4'])
    answers.append(request.form['q5'])
    answers.append(request.form['q6'])
    answers.append(request.form['q7'])
    answers.append(request.form['q8'])
    answers.append(request.form['q9'])
    answers.append(request.form['q10']) 
    a=technology1(answers)
    print(answers) 
    print(a)  
    return render_template('arts.html')

@app.route('/finance', methods=['POST'])
def finance():
    answers = []
    answers.append(request.form['q1'])
    answers.append(request.form['q2'])
    answers.append(request.form['q3'])
    answers.append(request.form['q4'])
    answers.append(request.form['q5'])
    answers.append(request.form['q6'])
    answers.append(request.form['q7'])
    answers.append(request.form['q8'])
    answers.append(request.form['q9'])
    answers.append(request.form['q10']) 
    a=finance1(answers)
    print(answers) 
    print(a)  
    return render_template('arts.html')

@app.route('/e_commerce', methods=['POST'])
def e_commerce():
    answers = []
    answers.append(request.form['q1'])
    answers.append(request.form['q2'])
    answers.append(request.form['q3'])
    answers.append(request.form['q4'])
    answers.append(request.form['q5'])
    answers.append(request.form['q6'])
    answers.append(request.form['q7'])
    answers.append(request.form['q8'])
    answers.append(request.form['q9'])
    answers.append(request.form['q10']) 
    a=e_comerce1(answers)
    print(answers) 
    print(a)  
    return render_template('arts.html')

@app.route('/healthcare', methods=['POST'])
def healthcare():
    answers = []
    answers.append(request.form['q1'])
    answers.append(request.form['q2'])
    answers.append(request.form['q3'])
    answers.append(request.form['q4'])
    answers.append(request.form['q5'])
    answers.append(request.form['q6'])
    answers.append(request.form['q7'])
    answers.append(request.form['q8'])
    answers.append(request.form['q9'])
    answers.append(request.form['q10']) 
    a=healthcare1(answers)
    print(answers) 
    print(a)  
    return render_template('arts.html')


if __name__ == '__main__':
    app.run(debug=True)


