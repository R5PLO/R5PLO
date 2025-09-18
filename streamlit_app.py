import streamlit as st

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

st.title("소수 판별 계산기")

num = st.number_input("숫자를 입력하세요", min_value=0, step=1)

if st.button("소수 판별하기"):
    if is_prime(int(num)):
        st.success(f"{int(num)}은(는) 소수입니다!")
    else:
        st.error(f"{int(num)}은(는) 소수가 아닙니다.")

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
