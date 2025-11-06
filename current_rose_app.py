import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="可愛海流玫瑰圖小遊戲 🌸🐬", page_icon="🌊")

st.markdown("""
# 🌸 海流玫瑰圖小遊戲  
輸入 **3 組 U、V 分量**，按下下面的按鈕即可產生玫瑰圖！  
""")

# 可愛分隔線
st.markdown("---")

# 使用者輸入區塊
col1, col2 = st.columns(2)
with col1:
    u_values = [st.number_input(f"U{idx+1}", value=0.0) for idx in range(3)]
with col2:
    v_values = [st.number_input(f"V{idx+1}", value=0.0) for idx in range(3)]

if st.button("🌸 生成玫瑰圖！"):
    speeds = np.sqrt(np.array(u_values)**2 + np.array(v_values)**2)
    directions = np.degrees(np.arctan2(u_values, v_values)) % 360

    # 分成三個方向區塊
    angles = np.radians(directions)

    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, polar=True)
    ax.bar(angles, speeds, width=np.radians(20), edgecolor='black')
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    plt.title("🌊 海流玫瑰圖")
    st.pyplot(fig)

    st.success("✅ 圖已成功生成！")

st.markdown("---")
st.markdown("由你最可愛的海洋物理講師製作 🐳💙")
