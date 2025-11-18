import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="海流玫瑰圖小遊戲", page_icon="🌊")

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
        u = st.number_input(f"U{i+1}", value=0.0, step=0.1, format="%.1f")
        v = st.number_input(f"V{i+1}", value=0.0, step=0.1, format="%.1f")
        d = st.number_input(f"方向{i+1}°", value=0, min_value=0, max_value=360, step=1, format="%d")
        u_values.append(u)
        v_values.append(v)
        dir_values.append(d)

if st.button("🌸 生成玫瑰圖！"):
    # 計算流速
    speeds = np.sqrt(np.array(u_values)**2 + np.array(v_values)**2)
    angles = np.radians(dir_values)

    # 最大流速用來設定玫瑰圖刻度
    max_speed = max(speeds) if max(speeds) > 0 else 1
    radial_ticks = np.linspace(0, max_speed, 5)[1:]  # 20-40-60-80-100% 分界

    # 繪製玫瑰圖
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, polar=True)
    ax.bar(angles, speeds, width=np.radians(25), edgecolor='black', color='skyblue')

    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)

    # 設定同心圓刻度
    ax.set_rgrids(radial_ticks, labels=[f"{int(r/max_speed*100)}%" for r in radial_ticks])

    # 標題（不使用 emoji）
    ax.set_title("海流玫瑰圖（依輸入流向與流速）", fontsize=14)

    st.pyplot(fig)

    # Streamlit 再補 emoji 顯示
    st.markdown("🌊 **海流玫瑰圖已生成！**")
    st.success("✅ 圖已成功生成！")

st.markdown("---")
st.markdown("由海洋物理講師江函霖製作 🐳💙")
