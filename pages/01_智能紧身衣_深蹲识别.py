import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="智能紧身衣：深蹲姿势识别", layout="wide")

st.title("🏋️ 智能紧身衣：深蹲姿势识别系统")
st.caption("多通道传感信号展示、预处理预留、动作识别与训练评估演示页面")

st.markdown("---")

top1, top2, top3, top4 = st.columns(4)
top1.metric("系统模式", "深蹲识别")
top2.metric("数据状态", "模拟数据")
top3.metric("模型状态", "演示版")
top4.metric("运行状态", "正常")

st.markdown("---")

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("## 参数控制区")

    data_source = st.selectbox(
        "数据来源",
        ["模拟数据", "上传CSV数据", "实时传感器接口（后续接入）"]
    )

    subject_id = st.text_input("受试者编号", value="S001")

    sample_rate = st.number_input("采样频率（Hz）", min_value=10, max_value=5000, value=100)

    channel = st.selectbox(
        "选择主显示通道",
        ["通道1", "通道2", "通道3", "通道4"]
    )

    filter_type = st.selectbox(
        "滤波方式",
        ["Butterworth低通", "Butterworth高通", "带通滤波", "暂不滤波"]
    )

    noise_mode = st.selectbox(
        "降噪方式",
        ["均值平滑", "中值滤波", "暂不降噪"]
    )

    model_name = st.selectbox(
        "分类模型",
        ["RandomForest", "SVM", "LogisticRegression（后续）", "LSTM（后续）"]
    )

    st.markdown("### 操作区")
    st.button("开始采集 / 分析", use_container_width=True)
    st.button("停止", use_container_width=True)

with col2:
    st.markdown("## 系统说明")

    st.info(
        "该页面用于演示智能紧身衣多通道传感数据的展示与分析流程。"
        "当前版本使用模拟数据完成波形显示，后续可扩展真实采集、滤波降噪、"
        "特征提取、模型分类与动作评分。"
    )

    result_col1, result_col2, result_col3 = st.columns(3)
    result_col1.metric("预测类别", "等待数据")
    result_col2.metric("动作评分", "--")
    result_col3.metric("姿势判断", "未开始")

st.markdown("---")
st.markdown("## 多通道模拟信号")

x = np.linspace(0, 10, 500)
signal_1 = np.sin(2 * np.pi * 0.8 * x) + 0.08 * np.random.randn(500)
signal_2 = 0.8 * np.sin(2 * np.pi * 1.2 * x + 0.5) + 0.08 * np.random.randn(500)
signal_3 = 0.6 * np.sin(2 * np.pi * 1.6 * x + 1.0) + 0.08 * np.random.randn(500)
signal_4 = 0.9 * np.sin(2 * np.pi * 0.5 * x + 0.2) + 0.08 * np.random.randn(500)

channel_map = {
    "通道1": signal_1,
    "通道2": signal_2,
    "通道3": signal_3,
    "通道4": signal_4,
}

selected_signal = channel_map[channel]

raw_df = pd.DataFrame({
    "Time": x,
    "Raw Signal": selected_signal
})

processed_signal = pd.Series(selected_signal).rolling(window=5, min_periods=1).mean()

processed_df = pd.DataFrame({
    "Time": x,
    "Processed Signal": processed_signal
})

c1, c2 = st.columns(2)

with c1:
    st.markdown("### 原始信号波形")
    st.line_chart(raw_df.set_index("Time"), use_container_width=True)

with c2:
    st.markdown("### 预处理后波形（演示版）")
    st.line_chart(processed_df.set_index("Time"), use_container_width=True)

st.markdown("---")
st.markdown("## 特征提取结果（占位）")

feature_df = pd.DataFrame({
    "特征名称": ["均值", "标准差", "RMS", "峰峰值", "能量", "主频", "零交叉率"],
    "当前值": ["待计算", "待计算", "待计算", "待计算", "待计算", "待计算", "待计算"]
})
st.dataframe(feature_df, use_container_width=True)

st.caption("当前页面为展示版，后续可接入真实动作识别模型。")