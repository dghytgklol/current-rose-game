import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="海流玫瑰圖小遊戲 🌸🐬", page_icon="🌊")

st.markdown("""
# 🌸 海流玫瑰圖小遊戲  
輸入 **3 組 U、V** 以及 **流向（角度，0°=北）**，按下按鈕即可生成玫瑰圖！  
""")

st.markdown("---")

# 使用者輸入區塊
st.write("請輸入 3 組數值：")
cols = st.columns(3)
u_values = []
v_values = []
dir_values = []

for i in range(3):
    with cols[i]:
        u = st.number_input(f"U{i+1}", value=0.0)
        v = st.number_input(f"V{i+1}", value=0.0)
        d = st.number_input(f"方向{i+1}°", value=0.0, min_value=0.0, max_value=360.0)
        u_values.append(u)
        v_values.append(v)
        dir_values.append(d)
        
if st.button("🌸 生成玫瑰圖！"):
    # 計算流速
    speeds = np.sqrt(np.array(u_values)**2 + np.array(v_values)**2)
    angles = np.radians(dir_values)

    # 繪製玫瑰圖
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, polar=True)
    ax.bar(angles, speeds, width=np.radians(20), edgecolor='black', color='skyblue')
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_title("海流玫瑰圖 (帶輸入流向)")  # 不加 emoji

    st.pyplot(fig)

    st.markdown("🌊 海流玫瑰圖 (帶輸入流向)")  # Emoji 交給 Streamlit
    st.success("✅ 圖已成功生成！")


st.markdown("---")
st.markdown("由海洋物理講師江函霖製作 🐳💙")
