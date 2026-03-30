import streamlit as st

st.set_page_config(
    page_title="智能传感监测平台",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 智能传感监测平台")
st.subheader("面向智能穿戴与智能床垫的多模式信号采集、分析与识别系统")

st.markdown("---")

left, right = st.columns([1.2, 1])

with left:
    st.markdown("## 项目简介")
    st.write(
        "本平台用于演示多种传感器数据的可视化、预处理与智能识别流程。"
        "系统当前包含两个核心应用场景：智能紧身衣深蹲姿势识别，以及智能床垫姿态与翻身监测。"
    )

    st.markdown("### 平台能力")
    st.write("✅ 多页面模式切换")
    st.write("✅ 多通道信号展示")
    st.write("✅ 压力分布热力图显示")
    st.write("✅ 预处理与特征提取流程预留")
    st.write("✅ 支持后续扩展真实传感器接入与机器学习预测")

with right:
    st.markdown("## 当前模块")
    st.info("模块 1：智能紧身衣——深蹲姿势识别")
    st.info("模块 2：智能床垫——姿态监测与翻身检测")

    st.markdown("## 当前状态")
    st.success("Project04 首页已完成")
    st.warning("当前演示版本使用模拟数据")
    st.caption("后续可扩展接入真实传感器与训练模型")

st.markdown("---")

c1, c2 = st.columns(2)

with c1:
    st.markdown("### 智能紧身衣模块")
    st.write(
        "展示多通道传感信号、预处理后波形、动作识别结果与姿态判断。"
        "适用于深蹲训练动作质量评估等场景。"
    )

with c2:
    st.markdown("### 智能床垫模块")
    st.write(
        "展示压力分布热力图、姿态识别结果、翻身检测信息与状态提示。"
        "适用于卧姿监测与人体状态分析等场景。"
    )

st.markdown("---")
st.caption("Project04 · Streamlit 演示版")