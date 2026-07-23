import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time

st.set_page_config(page_title="ICT4D Financial Inclusion Engine", layout="wide")

st.title("Serverless ICT4D Middleware Pipeline")
st.caption("Real-Time Mobile Money Aggregation & Digital Inclusion Analytics")

st.sidebar.header("Middleware Configuration")
selected_region = st.sidebar.selectbox("Target Underserved Region", ["Sub-Saharan Africa (Cross-Border)", "Southeast Asia (Rural Nodes)", "South Asia (Unbanked Sector)"])
telecom_friction = st.sidebar.slider("Simulate Telecom Network Friction", 1.0, 5.0, 2.5)
run_simulation = st.sidebar.button("Initialize Financial Middleware")

st.sidebar.markdown("---")
st.sidebar.caption("Architecture: Mobile Endpoints -> AWS Lambda Normalization -> Cloud Ledger")

if run_simulation:
    st.subheader(f"Active Financial Inclusion Monitoring: {selected_region}")
    
    col1, col2, col3, col4 = st.columns(4)
    metric_volume = col1.empty()
    metric_latency = col2.empty()
    metric_cost = col3.empty()
    metric_index = col4.empty()

    chart_placeholder = st.empty()
    log_placeholder = st.empty()

    np.random.seed(707)
    time_steps = pd.date_range(start=pd.Timestamp.now(), periods=100, freq="s")
    
    latency_levels = []
    inclusion_scores = []
    
    base_latency = 120.0 
    
    for i in range(100):
        if i < 30:
            current_latency = base_latency + (telecom_friction * 10.0) + np.random.uniform(-10.0, 10.0)
            current_inclusion = np.random.uniform(40.0, 50.0)
            tx_volume = int(np.random.uniform(100, 500))
        elif i >= 30 and i < 60:
            current_latency = base_latency - (i - 30) * 2.0 + np.random.uniform(-5.0, 5.0)
            current_inclusion = np.random.uniform(50.0, 75.0)
            tx_volume = int(np.random.uniform(1000, 3000))
        else:
            current_latency = 45.0 + np.random.uniform(-5.0, 5.0)
            current_inclusion = np.random.uniform(85.0, 95.0) 
            tx_volume = int(np.random.uniform(5000, 12000))
            
        latency_levels.append(current_latency)
        inclusion_scores.append(current_inclusion)
        
        simulated_cost = (current_latency / 1000.0) * 0.05 
        
        metric_volume.metric("Micro-Tx Volume", f"{tx_volume:,} Tx/s")
        metric_latency.metric("Processing Latency", f"{current_latency:.1f} ms", f"{(current_latency - base_latency):.1f} ms")
        metric_cost.metric("Marginal Cost per Tx", f"${simulated_cost:.5f}", "- Reduced Friction")
        
        if current_inclusion >= 80.0:
            metric_index.metric("Digital Inclusion Index", f"{current_inclusion:.1f} pts", "High Penetration")
        else:
            metric_index.metric("Digital Inclusion Index", f"{current_inclusion:.1f} pts", "Low Access")
            
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=time_steps[:i+1], y=latency_levels, mode='lines', name='Network Latency (ms)', line=dict(color='orange')))
        fig.add_trace(go.Scatter(x=time_steps[:i+1], y=inclusion_scores, mode='lines', name='Digital Inclusion Index', yaxis='y2', line=dict(color='green', dash='dot')))
        
        fig.update_layout(
            title="ICT4D Analytics: Serverless Optimization vs Digital Empowerment",
            xaxis=dict(title="High-Frequency Telemetry Timestamp"),
            yaxis=dict(title="Latency (ms)"),
            yaxis2=dict(title="Inclusion Index (0-100)", overlaying='y', side='right', range=[0, 100]),
            height=400,
            margin=dict(l=0, r=0, t=40, b=0)
        )
        
        chart_placeholder.plotly_chart(fig, use_container_width=True)
        
        if current_inclusion >= 80.0:
            log_placeholder.success(f"ICT4D LOG: AWS Lambda middleware successfully optimizing cross-border validation at {time_steps[i].strftime('%H:%M:%S')}. Transaction costs approaching zero. High capability expansion detected.")
        else:
            log_placeholder.warning(f"Log: Legacy telecom friction detected. Telemetry tick {i} ingested. Serverless middleware rerouting to mitigate latency.")
            
        time.sleep(0.15)
        
    st.info("Simulation Complete. The cloud-native middleware successfully reduced transaction friction, dramatically expanding digital financial inclusion.")
else:
    st.info("Click 'Initialize Financial Middleware' in the sidebar to simulate high-frequency ICT4D data ingestion.")