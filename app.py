import streamlit as st

st.set_page_config(
    page_title="English Test 50 Questions",
    page_icon="📘",
    layout="wide"
)

st.title("📘 English Proficiency Test - 50 Questions")

if "submitted" not in st.session_state:
    st.session_state.submitted = False

# =============================
# QUESTIONS
# Format: (Question, [options], correct_index)
# =============================

questions = [

# ===== GRAMMAR (1-20) =====
("She _____ to school every day.", ["go", "goes", "going", "gone"], 1),
("They _____ watching TV now.", ["is", "are", "was", "be"], 1),
("I have lived here _____ 5 years.", ["since", "for", "from", "at"], 1),
("If I _____ rich, I would travel the world.", ["am", "was", "were", "be"], 2),
("He _____ already finished his homework.", ["has", "have", "had", "having"], 0),
("This is the _____ movie I’ve ever seen.", ["more interesting", "most interesting", "very interesting", "interesting"], 1),
("She speaks English very _____.", ["good", "well", "better", "best"], 1),
("There isn’t _____ milk left.", ["many", "much", "a few", "several"], 1),
("I prefer coffee _____ tea.", ["than", "from", "to", "over"], 2),
("The book _____ was on the table is mine.", ["who", "which", "where", "when"], 1),

("We were tired, _____ we continued working.", ["but", "and", "so", "because"], 0),
("She asked me where I _____.", ["live", "lived", "am living", "was live"], 1),
("He is not as _____ as his brother.", ["tall", "taller", "tallest", "more tall"], 0),
("She has _____ friends in this city.", ["a little", "a few", "much", "any"], 1),
("By next year, I _____ my degree.", ["finish", "will finish", "will have finished", "finished"], 2),
("The meeting was canceled _____ the storm.", ["because", "because of", "although", "despite"], 1),
("She made me _____ sorry.", ["feel", "to feel", "feeling", "felt"], 0),
("This house is _____ than that one.", ["expensive", "more expensive", "most expensive", "very expensive"], 1),
("He drives _____ than I do.", ["careful", "carefully", "more carefully", "most carefully"], 2),
("She didn’t go out _____ it was raining.", ["because", "although", "despite", "however"], 0),

# ===== VOCABULARY (21-35) =====
("Generous means _____.", ["kind", "mean", "selfish", "angry"], 0),
("Huge means _____.", ["small", "tiny", "very big", "short"], 2),
("The opposite of 'cheap' is _____.", ["low", "expensive", "small", "weak"], 1),
("She felt _____ after the exam.", ["relieved", "angry", "hungry", "cold"], 0),
("He has a strong _____ in science.", ["interest", "boring", "fear", "weakness"], 0),
("The movie was very _____.", ["excite", "exciting", "excited", "excitement"], 1),
("She is good _____ math.", ["at", "in", "on", "for"], 0),
("He apologized _____ being late.", ["for", "to", "at", "with"], 0),
("She depends _____ her parents.", ["in", "at", "on", "for"], 2),
("He is famous _____ his paintings.", ["for", "in", "at", "with"], 0),

("The weather is getting _____.", ["cold", "colder", "coldest", "more cold"], 1),
("She gave me some useful _____.", ["advices", "advice", "advise", "advises"], 1),
("He works very _____.", ["hard", "hardly", "harder", "hardest"], 0),
("She is afraid _____ spiders.", ["of", "from", "at", "in"], 0),
("He succeeded _____ passing the exam.", ["in", "at", "on", "with"], 0),

# ===== READING (36-50) =====
("Tom is a doctor. He works in a hospital. Where does Tom work?", 
 ["At school", "At a hospital", "At home", "At a bank"], 1),

("Anna loves animals. She has three cats. What does Anna love?", 
 ["Cars", "Animals", "Food", "Books"], 1),

("John studies every day. He wants to pass the exam. Why does John study?", 
 ["To fail", "To travel", "To pass the exam", "To sleep"], 2),

("It was raining, so we stayed inside. Why did we stay inside?", 
 ["Because it was sunny", "Because it was raining", "Because we were tired", "Because it was hot"], 1),

("Mary bought a new phone because her old one was broken. Why did Mary buy a phone?", 
 ["She was bored", "Her old phone was broken", "She was rich", "She lost money"], 1),

("The sun rises in the east. Where does the sun rise?", 
 ["North", "South", "East", "West"], 2),

("Peter is taller than Mike. Who is taller?", 
 ["Mike", "Peter", "Both", "None"], 1),

("Sarah went to the market to buy vegetables. Why did she go?", 
 ["To buy vegetables", "To sleep", "To study", "To run"], 0),

("The train was late because of heavy rain. Why was the train late?", 
 ["Because of snow", "Because of heavy rain", "Because of wind", "Because of sun"], 1),

("David practices football every day. What does he practice?", 
 ["Basketball", "Football", "Tennis", "Swimming"], 1),

("Lisa reads books before bed. When does she read?", 
 ["Morning", "Afternoon", "Before bed", "At noon"], 2),

("The baby is crying because he is hungry. Why is the baby crying?", 
 ["Sleepy", "Happy", "Hungry", "Angry"], 2),

("They went to the beach last Sunday. When did they go?", 
 ["Last Sunday", "Tomorrow", "Next week", "Today"], 0),

("Emma is studying medicine at university. What is Emma studying?", 
 ["Law", "Art", "Medicine", "Music"], 2),

("The car stopped because it ran out of fuel. Why did it stop?", 
 ["Flat tire", "No fuel", "Engine broke", "Driver tired"], 1),
]

# =============================
# DISPLAY QUESTIONS
# =============================

for i, (question, options, correct) in enumerate(questions):
    st.radio(
        f"Câu {i+1}: {question}",
        options,
        index=None,
        key=f"question_{i}"
    )

# =============================
# SUBMIT
# =============================

if st.button("Submit & Get Result"):

    score = 0

    for i, (question, options, correct) in enumerate(questions):
        answer = st.session_state.get(f"question_{i}")
        if answer == options[correct]:
            score += 1

    st.success(f"Your Score: {score}/50")

    if score < 20:
        level = "Beginner"
    elif score < 35:
        level = "Intermediate"
    else:
        level = "Advanced"

    st.markdown(f"## Your Level: {level}")

    if level == "Beginner":
        st.write("• Focus on basic grammar and vocabulary.")
        st.write("• Practice daily reading.")
    elif level == "Intermediate":
        st.write("• Improve writing and speaking skills.")
        st.write("• Expand academic vocabulary.")
    else:
        st.write("• Practice IELTS/TOEFL tests.")
        st.write("• Focus on advanced writing structures.")
