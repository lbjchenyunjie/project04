import streamlit as st
import numpy as np
from streamlit_echarts import st_echarts

st.set_page_config(page_title="智能床垫：姿态监测", layout="wide")

st.title("🛏️ 智能床垫：姿态监测与翻身检测系统")
st.caption("压力分布热力图展示、姿态监测、翻身检测与状态分析演示页面")

st.markdown("---")

top1, top2, top3, top4 = st.columns(4)
top1.metric("系统模式", "床垫监测")
top2.metric("数据状态", "模拟数据")
top3.metric("识别状态", "演示版")
top4.metric("运行状态", "正常")

st.markdown("---")

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("## 参数控制区")

    data_source = st.selectbox(
        "数据来源",
        ["模拟数据", "上传CSV数据", "实时压力阵列接口（后续接入）"]
    )

    mattress_rows = st.number_input("压力阵列行数", min_value=4, max_value=32, value=8)
    mattress_cols = st.number_input("压力阵列列数", min_value=4, max_value=32, value=8)

    detect_mode = st.selectbox(
        "监测模式",
        ["姿态识别", "翻身检测", "综合监测"]
    )

    threshold = st.slider("压力阈值", min_value=0.0, max_value=1.0, value=0.3, step=0.05)

    model_name = st.selectbox(
        "识别模型",
        ["RandomForest", "SVM", "LogisticRegression（后续）", "CNN（后续）"]
    )

    st.markdown("### 操作区")
    st.button("开始监测", use_container_width=True)
    st.button("停止监测", use_container_width=True)

with col2:
    st.markdown("## 系统说明")

    st.info(
        "该页面用于演示智能床垫压力分布数据的可视化与状态识别流程。"
        "当前版本使用模拟压力矩阵完成热力图显示，后续可扩展真实床垫阵列数据输入、"
        "姿态分类、翻身检测、压力中心分析与风险提示。"
    )

    r1, r2, r3 = st.columns(3)
    r1.metric("当前姿态", "等待数据")
    r2.metric("翻身次数", "0")
    r3.metric("异常提示", "无")

st.markdown("---")
st.markdown("## 实时压力热力图（模拟）")

pressure_map = np.random.rand(mattress_rows, mattress_cols)

heatmap_data = []
for i in range(mattress_rows):
    for j in range(mattress_cols):
        heatmap_data.append([j, i, float(pressure_map[i, j])])

option = {
    "tooltip": {"position": "top"},
    "grid": {"height": "70%", "top": "10%"},
    "xAxis": {
        "type": "category",
        "data": [str(i) for i in range(mattress_cols)],
        "splitArea": {"show": True},
    },
    "yAxis": {
        "type": "category",
        "data": [str(i) for i in range(mattress_rows)],
        "splitArea": {"show": True},
    },
    "visualMap": {
        "min": 0,
        "max": 1,
        "calculable": True,
        "orient": "horizontal",
        "left": "center",
        "bottom": "0%"
    },
    "series": [
        {
            "name": "压力值",
            "type": "heatmap",
            "data": heatmap_data,
            "label": {"show": False},
            "emphasis": {
                "itemStyle": {
                    "shadowBlur": 10,
                    "shadowColor": "rgba(0, 0, 0, 0.5)"
                }
            },
        }
    ],
}

st_echarts(option, height="500px")

st.markdown("---")
st.caption("当前页面为展示版，后续可接入真实压力阵列和姿态识别模型。")