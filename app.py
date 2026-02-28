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
# QUESTIONS (Phiên bản Nâng cao & Đa dạng)
# =============================

questions = [
# ===== GRAMMAR (1-20) =====
("Hardly _____ the office when the phone started ringing.", ["I had left", "had I left", "I left", "was I leaving"], 1),
("If you _____ more carefully, you wouldn't have had that accident.", ["drive", "drove", "had driven", "have driven"], 2),
("The bridge _____ by the end of next year.", ["will finish", "will be finished", "finishes", "is finishing"], 1),
("I'd rather you _____ anyone what I told you.", ["don't tell", "didn't tell", "not tell", "not to tell"], 1),
("Not only _____ fluently, but she also writes beautifully.", ["she speaks", "does she speak", "is she speaking", "she did speak"], 1),
("It’s high time the government _____ something about pollution.", ["does", "did", "has done", "is doing"], 1),
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
("She is very _____ – she always thinks about others.", ["considerate", "considerable", "selfish", "rude"], 0),
("The situation is _____ and requires immediate action.", ["critical", "trivial", "minor", "unimportant"], 0),
("He was _____ for his bravery during the rescue.", ["commended", "criticized", "ignored", "punished"], 0),

# ===== READING: TRUE/FALSE/NOT GIVEN (36-50) =====
# Đoạn văn giả định về Năng lượng mặt trời (Solar Energy)
# 36. Solar energy is the most popular form of renewable energy today. (NOT GIVEN - Bài chỉ nói nó đang phát triển, không nói nó nhất)
("T/F/NG: Solar energy is currently the most popular renewable energy source globally.", 
 ["True", "False", "Not Given"], 2),

# 37. Solar panels work by converting sunlight into electricity. (TRUE)
("T/F/NG: Solar panels function by transforming light from the sun into electrical power.", 
 ["True", "False", "Not Given"], 0),

# 38. The cost of solar technology has increased in recent years. (FALSE - Thực tế là giảm)
("T/F/NG: In recent years, the price of solar technology has risen significantly.", 
 ["True", "False", "Not Given"], 1),

# 39. Germany produces more solar power than any other country. (NOT GIVEN)
("T/F/NG: Germany is the world's leading producer of solar energy.", 
 ["True", "False", "Not Given"], 2),

# 40. Solar energy can be collected even on cloudy days. (TRUE)
("T/F/NG: It is possible to generate solar energy even when the sky is overcast.", 
 ["True", "False", "Not Given"], 0),

# 41. Maintenance of solar panels is extremely expensive. (FALSE - Thường là thấp)
("T/F/NG: Keeping solar panels in good condition requires a huge financial investment.", 
 ["True", "False", "Not Given"], 1),

# 42. Solar energy helps reduce greenhouse gas emissions. (TRUE)
("T/F/NG: Utilizing solar power contributes to a decrease in greenhouse gases.", 
 ["True", "False", "Not Given"], 0),

# 43. Most solar panels are made of silicon. (NOT GIVEN - Bài không đề cập cấu tạo)
("T/F/NG: Silicon is the primary material used in the manufacturing of most solar panels.", 
 ["True", "False", "Not Given"], 2),

# 44. Solar energy is a finite resource. (FALSE - Nó là vô tận/renewable)
("T/F/NG: Solar energy will eventually run out and is considered a finite resource.", 
 ["True", "False", "Not Given"], 1),

# 45. Some homeowners can sell excess energy back to the grid. (TRUE)
("T/F/NG: Homeowners may have the option to sell surplus electricity back to the main power supply.", 
 ["True", "False", "Not Given"], 0),

# 46. Governments always provide subsidies for solar installation. (FALSE - Không phải "always")
("T/F/NG: Every government in the world provides financial support for installing solar panels.", 
 ["True", "False", "Not Given"], 1),

# 47. Solar farms can be built on water. (TRUE - Floating solar)
("T/F/NG: It is technically feasible to construct solar energy farms on bodies of water.", 
 ["True", "False", "Not Given"], 0),

# 48. Solar power is only used for heating water. (FALSE - Còn dùng cho điện, v.v.)
("T/F/NG: The sole application of solar energy is for the purpose of heating water.", 
 ["True", "False", "Not Given"], 1),

# 49. Space-based solar power is currently used to power Earth. (FALSE - Vẫn đang nghiên cứu)
("T/F/NG: Electricity generated in space is currently being transmitted to power cities on Earth.", 
 ["True", "False", "Not Given"], 1),

# 50. Batteries are used to store solar energy for nighttime use. (TRUE)
("T/F/NG: Solar energy can be stored in batteries to be utilized after the sun goes down.", 
 ["True", "False", "Not Given"], 0),
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
# SUBMIT & LOGIC
# =============================

if st.button("Submit & Get Result"):
    grammar_score = 0
    vocab_score = 0
    reading_score = 0

    for i, (question, options, correct) in enumerate(questions):
        answer = st.session_state.get(f"question_{i}")
        if answer == options[correct]:
            # Grammar: câu 0-19
            if i <= 19:
                grammar_score += 1
            # Vocabulary: câu 20-34
            elif i <= 34:
                vocab_score += 1
            # Reading: câu 35-49
            else:
                reading_score += 1

    total_score = grammar_score + vocab_score + reading_score

    st.success(f"🎯 Tổng điểm: {total_score}/50")
    st.markdown("## 📊 Phân tích theo từng kỹ năng")
    st.write(f"🔹 Grammar: {grammar_score}/20")
    st.write(f"🔹 Vocabulary: {vocab_score}/15")
    st.write(f"🔹 Reading: {reading_score}/15")

    # =============================
    # ĐÁNH GIÁ CHI TIẾT
    # =============================
    st.markdown("---")
    st.markdown("## 🔎 Đánh giá chuyên sâu")

    # ===== GRAMMAR =====
    if grammar_score < 10:
        st.warning("### 🧩 Grammar: Yếu")
        st.write("Bạn còn nhầm lẫn về thì, cấu trúc câu và mệnh đề. Cần ôn lại nền tảng 12 thì và cấu trúc câu cơ bản.")
    elif grammar_score < 16:
        st.info("### 🧩 Grammar: Trung bình")
        st.write("Bạn nắm cơ bản tốt nhưng còn sai ở câu phức, điều kiện và bị động. Nên luyện thêm cấu trúc nâng cao.")
    else:
        st.success("### 🧩 Grammar: Tốt")
        st.write("Bạn kiểm soát cấu trúc ngữ pháp khá chắc. Chỉ cần tinh chỉnh độ chính xác và tự nhiên khi viết.")

    # ===== VOCAB =====
    if vocab_score < 7:
        st.warning("### 📖 Vocabulary: Yếu")
        st.write("Vốn từ còn hạn chế, đặc biệt là collocations và giới từ. Nên học theo chủ đề và ghi nhớ theo cụm từ.")
    elif vocab_score < 12:
        st.info("### 📖 Vocabulary: Trung bình")
        st.write("Bạn có nền tảng từ vựng khá. Cần mở rộng từ học thuật và từ đồng nghĩa.")
    else:
        st.success("### 📖 Vocabulary: Tốt")
        st.write("Vốn từ phong phú và dùng khá chính xác. Có thể nâng lên mức học thuật cao hơn.")

    # ===== READING =====
    if reading_score < 7:
        st.warning("### 📚 Reading: Yếu")
        st.write("Bạn đọc còn chậm và phụ thuộc dịch từng từ. Cần luyện kỹ năng skim và scan.")
    elif reading_score < 12:
        st.info("### 📚 Reading: Trung bình")
        st.write("Bạn hiểu nội dung chính nhưng còn mất điểm chi tiết. Cần luyện kỹ năng suy luận.")
    else:
        st.success("### 📚 Reading: Tốt")
        st.write("Bạn đọc hiểu nhanh và nắm ý chính tốt. Có thể luyện bài đọc học thuật dài hơn.")

    # =============================
    # ĐÁNH GIÁ TỔNG THỂ & BAND
    # =============================
    st.markdown("---")
    st.markdown("## 🧠 Đánh giá tổng thể")

    if total_score < 20:
        overall = "Beginner"
        band = "4.0 – 4.5"
    elif total_score < 35:
        overall = "Intermediate"
        band = "5.0 – 5.5"
    elif total_score < 40:
        overall = "Advanced"
        band = "6.0 – 6.5"
    elif total_score < 45:
        overall = "Advanced High"
        band = "7.0"
    else:
        overall = "Expert"
        band = "7.5+"

    st.markdown(f"### 🌟 Trình độ tổng thể: {overall}")
    st.markdown(f"## 🏆 Band ước lượng tương đương: {band}")

    # =============================
    # PHÂN TÍCH CHUYÊN SÂU THEO ĐIỂM
    # =============================
    st.markdown("## 🔎 Phân tích chi tiết năng lực")
    if total_score < 20:
        st.warning("""
Bạn đang ở mức nền tảng.
Vấn đề chính:
• Ngữ pháp chưa chắc 12 thì
• Từ vựng còn hạn chế
• Đọc còn dịch từng từ
• Thiếu chiến lược làm bài
Bạn chưa có nền móng đủ để làm bài thi học thuật.
""")
    elif total_score < 35:
        st.info("""
Bạn đã có nền tảng tương đối.
Điểm mạnh:
• Nắm được cấu trúc cơ bản
• Hiểu ý chính bài đọc
Điểm yếu:
• Sai câu nâng cao
• Dễ mất điểm ở chi tiết nhỏ
• Thiếu vốn từ học thuật
""")
    else:
        st.success("""
Bạn có nền tảng khá tốt.
Bạn có khả năng đạt mức học thuật.
Cần tập trung tăng độ chính xác và tốc độ xử lý.
""")

    # =============================
    # LỘ TRÌNH HỌC 12 TUẦN
    # =============================
    st.markdown("## 📅 Lộ trình học 12 tuần (Thực tế & hiệu quả)")
    if total_score < 20:
        st.markdown("""
### Giai đoạn 1 (Tuần 1–4): Xây nền
Mỗi ngày 90 phút:
• 30 phút: Ôn 12 thì tiếng Anh  
• 30 phút: Học 20 từ vựng/ngày (theo chủ đề)  
• 30 phút: Đọc đoạn văn 300–400 từ  
Mục tiêu: Không còn dịch từng từ.
---
### Giai đoạn 2 (Tuần 5–8): Củng cố
• Làm 1 passage Reading/ngày  
• Luyện dạng True/False/Not Given  
• Ghi lại toàn bộ lỗi sai  
---
### Giai đoạn 3 (Tuần 9–12): Ứng dụng
• Làm full test 60 phút  
• Phân tích lỗi ít nhất 45 phút sau mỗi bài  
• Mục tiêu đạt 60%+
""")
    elif total_score < 35:
        st.markdown("""
### Giai đoạn 1 (Tuần 1–4): Nâng cấp kỹ năng
• Luyện paraphrase mỗi ngày  
• Học collocations & từ đồng nghĩa  
• Làm 2 passages/ngày  
---
### Giai đoạn 2 (Tuần 5–8): Tăng tốc
• Full test 3 lần/tuần  
• Quản lý thời gian 15-20-25 phút  
• Tăng tốc độ đọc lên 200 từ/phút  
---
### Giai đoạn 3 (Tuần 9–12): Tối ưu
• Giảm lỗi bất cẩn  
• Phân tích kỹ từng câu sai  
• Mục tiêu 75–80%
""")
    else:
        st.markdown("""
### Giai đoạn 1 (Tuần 1–4):
• Duy trì 1 full test/ngày  
• Tập trung vào độ chính xác  
---
### Giai đoạn 2 (Tuần 5–8):
• Luyện Cambridge 12–18  
• Mục tiêu 85%+  
---
### Giai đoạn 3 (Tuần 9–12):
• Mô phỏng thi thật mỗi tuần  
• Giữ phong độ ổn định  
""")

    st.markdown("## 🛠 Cách khắc phục hiệu quả")
    st.markdown("""
1️⃣ Không đọc toàn bài trước.  
2️⃣ Đọc câu hỏi → gạch keyword → scan tìm đoạn.  
3️⃣ Luôn tìm bằng chứng trong bài.  
4️⃣ Không trả lời theo suy nghĩ cá nhân.  
5️⃣ Sau mỗi bài test, dành ít nhất 30 phút phân tích lỗi.  
""")
