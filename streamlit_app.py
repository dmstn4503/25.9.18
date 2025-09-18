
import streamlit as st

st.title("Streamlit 요소 데모")
st.header("Header 예시")
st.subheader("Subheader 예시")
st.text("텍스트 예시: 간단한 설명을 추가할 수 있습니다.")

st.markdown("**Markdown** _예시_ : Streamlit은 마크다운을 지원합니다.")

st.write("write 함수는 다양한 타입의 데이터를 출력할 수 있습니다.")

st.success("성공 메시지 예시")
st.info("정보 메시지 예시")
st.warning("경고 메시지 예시")
st.error("에러 메시지 예시")

st.checkbox("체크박스 예시")
st.radio("라디오 버튼 예시", ["옵션 1", "옵션 2", "옵션 3"])
st.selectbox("셀렉트박스 예시", ["A", "B", "C"])
st.multiselect("멀티셀렉트 예시", ["X", "Y", "Z"])

st.slider("슬라이더 예시", 0, 100, 50)
st.number_input("숫자 입력 예시", min_value=0, max_value=10, value=5)
st.text_input("텍스트 입력 예시", "기본값")
st.text_area("텍스트 영역 예시", "여기에 입력하세요")

st.file_uploader("파일 업로더 예시")

st.button("버튼 예시")

st.image(
    "https://static.streamlit.io/examples/dog.jpg",
    caption="이미지 예시: 강아지",
    use_column_width=True
)

import pandas as pd
import numpy as np
df = pd.DataFrame(
    np.random.randn(10, 3),
    columns=["a", "b", "c"]
)
st.dataframe(df, use_container_width=True)
st.table(df.head())

st.line_chart(df)
st.bar_chart(df)
