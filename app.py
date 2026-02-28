import streamlit as st
import plotly.graph_objects as go

# Cấu hình trang
st.set_page_config(
    page_title="English Proficiency Diagnostic",
    page_icon="🧠",
    layout="wide"
)

# Giao diện tiêu đề
st.title("📘 English Proficiency Test - Chẩn đoán chuyên sâu")
st.markdown("""
Bài kiểm tra này được thiết kế để đánh giá 3 kỹ năng chính: **Ngữ pháp (Grammar)**, **Từ vựng (Vocabulary)**, và **Đọc hiểu (Reading)**.
""")

# =============================
# BỘ CÂU HỎI (50 CÂU - CLEAN)
# =============================
questions = [
    # ===== GRAMMAR (1-20) =====
    ("Hardly _____ the office when the phone started ringing.", ["I had left", "had I left", "I left", "was I leaving"], 1),
    ("If you _____ more carefully, you wouldn't have had that accident.", ["drive", "drove", "had driven", "have driven"], 2),
    ("The bridge _____ by the end of next year.", ["will finish", "will be finished", "finishes", "is finishing"], 1),
    ("I'd rather you _____ anyone what I told you.", ["don't tell", "didn't tell", "not tell", "not to tell"], 1),
    ("Not only _____ fluently, but she also writes beautifully.", ["she speaks", "does she speak", "is she speaking", "she did speak"], 1),
    ("It's high time the government _____ something about pollution.", ["does", "did", "has done", "is doing"], 1),
    ("By the time the police arrived, the thief _____.", ["escaped", "has escaped", "had escaped", "was escaping"], 2),
    ("She was seen _____ the building late last night.", ["enter", "entered", "entering", "to enter"], 2),
    ("The more you practice, _____ you will become.", ["the good", "the better", "best", "the best"], 1),
    ("_____ being very tired, he stayed up to finish the report.", ["Despite", "Although", "However", "In spite"], 0),
    ("I regret _____ you that your application was unsuccessful.", ["inform", "to inform", "informing", "informed"], 1),
    ("The man _____ daughter is in my class is a famous actor.", ["who", "whom", "whose", "which"], 2),
    ("I wish I _____ so much chocolate this morning. I feel sick.", ["didn't eat", "not ate", "hadn't eaten", "don't eat"], 2),
    ("Neither my parents nor my brother _____ going to the party.", ["is", "are", "am", "be"], 0),
    ("You _____ better see a doctor about that cough.", ["should", "would", "had", "ought"], 2),
    ("She suggested _____ a taxi to the airport.", ["taking", "to take", "take", "should take"], 0),
    ("I am looking forward _____ you at the conference.", ["meet", "to meet", "meeting", "to meeting"], 3),
    ("They _____ have been at home; the lights were all off.", ["must", "can't", "might", "should"], 1),
    ("Little _____ that the surprise party was for him.", ["did he know", "he knew", "does he know", "he knows"], 0),
    ("The children were _____ to bed early.", ["made go", "made to go", "make go", "making go"], 1),

    # ===== VOCABULARY (21-35) =====
    ("'Meticulous' means _____.", ["careless", "extremely careful", "very fast", "angry"], 1),
    ("'Alleviate' is closest in meaning to _____.", ["make worse", "increase", "ease/relieve", "ignore"], 2),
    ("The CEO decided to _____ from his position.", ["resign", "fire", "apply", "hire"], 0),
    ("The project was a huge success _____ to everyone's hard work.", ["thanks", "because", "due", "result"], 2),
    ("She has an _____ memory; she never forgets a name.", ["incredible", "ordinary", "weak", "awful"], 0),
    ("The government is trying to _____ unemployment.", ["combat", "encourage", "support", "ignore"], 0),
    ("He gave a _____ account of his travels.", ["vivid", "blank", "pale", "dark"], 0),
    ("The company's profits have _____ significantly this year.", ["soared", "fell", "dropped", "stable"], 0),
    ("He is very _____ and always wants to win.", ["competitive", "lazy", "shy", "clumsy"], 0),
    ("The medicine had a positive _____ on her health.", ["affect", "effect", "effective", "efficient"], 1),
    ("We need to _____ a solution to this problem.", ["come up with", "put up with", "go through with", "catch up with"], 0),
    ("The music was so _____ that I couldn't concentrate.", ["distracting", "soothing", "pleasant", "quiet"], 0),
    ("She is very _____ - she always thinks about others.", ["considerate", "considerable", "selfish", "rude"], 0),
    ("The situation is _____ and requires immediate action.", ["critical", "trivial", "minor", "unimportant"], 0),
    ("He was _____ for his bravery during the rescue.", ["commended", "criticized", "ignored", "punished"], 0),

    # ===== READING: T/F/NG (36-50) =====
    ("T/F/NG: Solar energy is currently the most popular renewable energy source globally.", ["True", "False", "Not Given"], 2),
    ("T/F/NG: Solar panels function by transforming light from the sun into electrical power.", ["True", "False", "Not Given"], 0),
    ("T/F/NG: In recent years, the price of solar technology has risen significantly.", ["True", "False", "Not Given"], 1),
    ("T/F/NG: Germany is the world's leading producer of solar energy.", ["True", "False", "Not Given"], 2),
    ("T/F/NG: It is possible to generate solar energy even when the sky is overcast.", ["True", "False", "Not Given"], 0),
    ("T/F/NG: Keeping solar panels in good condition requires a huge financial investment.", ["True", "False", "Not Given"], 1),
    ("T/F/NG: Utilizing solar power contributes to a decrease in greenhouse gases.", ["True", "False", "Not Given"], 0),
    ("T/F/NG: Silicon is the primary material used in the manufacturing of most solar panels.", ["True", "False", "Not Given"], 2),
    ("T/F/NG: Solar energy will eventually run out and is considered a finite resource.", ["True", "False", "Not Given"], 1),
    ("T/F/NG: Homeowners may have the option to sell surplus electricity back to the main power supply.", ["True", "False", "Not Given"], 0),
    ("T/F/NG: Every government in the world provides financial support for installing solar panels.", ["True", "False", "Not Given"], 1),
    ("T/F/NG: It is technically feasible to construct solar energy farms on bodies of water.", ["True", "False", "Not Given"], 0),
    ("T/F/NG: The sole application of solar energy is for the purpose of heating water.", ["True", "False", "Not Given"], 1),
    ("T/F/NG: Electricity generated in space is currently being transmitted to power cities on Earth.", ["True", "False", "Not Given"], 1),
    ("T/F/NG: Solar energy can be stored in batteries to be utilized after the sun goes down.", ["True", "False", "Not Given"], 0),
]

# =============================
# GIAO DIỆN BÀI THI
# =============================
with st.container():
    for i, (question, options, _) in enumerate(questions):
        st.radio(f"Câu {i+1}: {question}", options, index=None, key=f"q_{i}")
        st.write("")

# =============================
# XỬ LÝ KẾT QUẢ
# =============================
if st.button("Submit & Phân tích chuyên sâu", type="primary"):
    grammar_sc, vocab_sc, reading_sc = 0, 0, 0
    results_detail = []

    for i, (question, options, correct) in enumerate(questions):
        user_choice = st.session_state.get(f"q_{i}")
        is_correct = (user_choice == options[correct])
        
        if is_correct:
            if i <= 19: grammar_sc += 1
            elif i <= 34: vocab_sc += 1
            else: reading_sc += 1
        
        results_detail.append({
            "is_correct": is_correct,
            "question": question,
            "user_choice": user_choice,
            "correct_ans": options[correct]
        })

    total_sc = grammar_sc + vocab_sc + reading_sc

    # --- Hiển thị Metrics ---
    st.markdown("---")
    st.header("📊 Kết quả chẩn đoán")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Tổng điểm", f"{total_sc}/50")
    col2.metric("Ngữ pháp", f"{grammar_sc}/20")
    col3.metric("Từ vựng", f"{vocab_sc}/15")
    col4.metric("Đọc hiểu", f"{reading_sc}/15")

    # --- Biểu đồ Radar ---
    st.markdown("### 🕸️ Biểu đồ mạng nhện năng lực")
    
    categories = ['Ngữ pháp', 'Từ vựng', 'Đọc hiểu']
    scores = [(grammar_sc/20)*100, (vocab_sc/15)*100, (reading_sc/15)*100]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
          r=scores + [scores[0]],
          theta=categories + [categories[0]],
          fill='toself',
          line_color='teal',
          name='Năng lực'
    ))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=False)
    st.plotly_chart(fig)

    # --- Phân tích Band ---
    if total_sc < 20: band = "4.0 - 4.5"; status = "Beginner"
    elif total_sc < 30: band = "5.0 - 5.5"; status = "Pre-Intermediate"
    elif total_sc < 40: band = "6.0 - 6.5"; status = "Intermediate"
    elif total_sc < 46: band = "7.0 - 7.5"; status = "Advanced"
    else: band = "8.0+"; status = "Expert"

    st.success(f"🌟 **Trình độ ước tính: {status}** (Band: {band})")

    # --- Chi tiết câu sai ---
    with st.expander("📂 Chi tiết các câu trả lời sai (Error Analysis)"):
        for idx, res in enumerate(results_detail):
            if not res["is_correct"]:
                st.error(f"**Câu {idx+1}**: {res['question']}")
                st.write(f"❌ Bạn chọn: {res['user_choice']} | ✅ Đáp án: {res['correct_ans']}")
                st.markdown("---")

    # --- Lộ trình học ---
    st.markdown("## 📅 Lộ trình hành động")
    tab1, tab2 = st.columns(2)
    with tab1:
        st.info("### 🧩 Điểm cần cải thiện")
        if grammar_sc < 15: st.write("- Ôn tập đảo ngữ (Inversion) và câu điều kiện hỗn hợp.")
        if vocab_sc < 10: st.write("- Bổ sung Collocations mức độ C1.")
        if reading_sc < 10: st.write("- Luyện kỹ năng phân biệt False và Not Given.")
    with tab2:
        st.success("### 📚 Tài liệu khuyên dùng")
        if total_sc < 35:
            st.write("- **Destination B2** (Vocabulary & Grammar)")
            st.write("- **Mindset for IELTS Level 2**")
        else:
            st.write("- **Cambridge IELTS Academic 15-18**")
            st.write("- **Destination C1 & C2**")

    st.balloons()
