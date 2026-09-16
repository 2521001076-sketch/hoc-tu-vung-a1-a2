import streamlit as st
import random

# Tự tạo danh sách từ vựng trực tiếp trong file để không bị lỗi kết nối file khác
VOCAB_LIST = [
    (1, "assignment", "n", "/əˈsaɪn.mənt/", "bài tập tiểu luận"),
    (2, "attentive", "adj", "/əˈten.tɪv/", "chăm chú, chú ý"),
    (3, "admission", "n", "/ədˈmɪʃ.ən/", "sự nhận vào, cho vào"),
    (4, "curriculum", "n", "/kəˈrɪk.jə.ləm/", "chương trình học"),
    (5, "discipline", "n", "/ˈdɪs.ə.plɪn/", "kỷ luật"),
]

st.title("🎯 Ứng Dụng Học Từ Vựng Tiếng Anh")

# 1. Khởi tạo bài học
if "selected_words" not in st.session_state:
    # Lấy ngẫu nhiên các từ từ danh sách để đố
    st.session_state.selected_words = random.sample(VOCAB_LIST, len(VOCAB_LIST))
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.answered = False

# 2. Kiểm tra xem còn câu hỏi không
if st.session_state.current_index < len(st.session_state.selected_words):
    idx = st.session_state.current_index
    word_info = st.session_state.selected_words[idx]
    stt, english_word, word_type, phonetic, vietnamese_meaning = word_info

    # Hiển thị câu hỏi giống giao diện Terminal cũ của bạn
    st.subheader(f"📝 Câu {idx + 1}/{len(st.session_state.selected_words)}")
    st.info(f"👉 **Loại từ:** {word_type} | **Phiên âm:** {phonetic}")
    st.markdown(f"### Từ tiếng Việt: **>> {vietnamese_meaning} <<**")

    # Ô nhập đáp án
    user_input = st.text_input("Nhập từ tiếng Anh của bạn:", key=f"input_{idx}")

    # Nút kiểm tra
    if st.button("Kiểm tra đáp án", key=f"btn_{idx}"):
        st.session_state.answered = True
        if user_input.strip().lower() == english_word.strip().lower():
            st.success(f"🎉 CHÍNH XÁC! Từ đúng là: **{english_word}**")
            st.session_state.score += 1
        else:
            st.error(f"❌ SAI RỒI! Đáp án đúng phải là: **{english_word}**")

    # Nút chuyển câu
    if st.session_state.answered:
        if st.button("Câu tiếp theo ➡️"):
            st.session_state.current_index += 1
            st.session_state.answered = False
            st.rerun()
else:
    st.balloons() # Hiệu ứng bóng bay chúc mừng khi thắng cuộc
    st.success(f"🏆 Hoàn thành! Điểm số: {st.session_state.score}/{len(st.session_state.selected_words)}")
    if st.button("Làm lại bài mới 🔄"):
        del st.session_state.selected_words
        st.rerun()
