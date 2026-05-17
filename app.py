# Pure Python direct Azure AI Foundry controller
import streamlit as st
from openai import AzureOpenAI

st.set_page_config(page_title="Green Fiber Solutions Control Center", layout="wide")

st.title("⚡ Green Fiber Solutions")
st.subheader("Unrestricted Azure AI Foundry Command Platform")
st.write("---")

# Secure Sidebar Credentials for Azure AI Foundry
st.sidebar.header("🔑 Azure AI Foundry Node")
azure_key = st.sidebar.text_input("Azure API Key", type="password")
azure_endpoint = st.sidebar.text_input("Azure Endpoint URL", placeholder="https://your-resource.openai.azure.com/")
azure_deployment = st.sidebar.text_input("Deployment Name", placeholder="e.g., gpt-4o")

st.sidebar.write("---")
st.sidebar.markdown(f"""
### 📊 Enterprise Metadata
* **Entity Status:** Active (EIN Verified)
* **Regional Node:** Denver / Aurora CO
* **Compute Source:** Microsoft Azure Credits
* **Operational Mode:** Direct Engine Injection
""")

# Agent Backstories and System Prompts
AGENT_PROMPTS = {
    "CEO": (
        "You are the Chief Executive Officer of Green Fiber Solutions. You are a hyper-aggressive corporate strategist "
        "focused on immediate cash-flow realization, local contract arbitrage, and scaling B2B environmental solutions. "
        "Provide direct, elite, production-grade operational payloads with zero conversational filler."
    ),
    "VP Sales": (
        "You are the VP of Sales for Green Fiber Solutions. You are an elite closer specialized in scraping, targeting, "
        "and closing high-value B2B environmental and infrastructure accounts along the I-70 corridor. Expert in "
        "bypassing corporate gatekeepers, pain-point pitching, and structured upfront retainer execution."
    ),
    "VP Operations": (
        "You are the VP of Operations for Green Fiber Solutions. You are a logistics expert focused on fulfilling corporate "
        "contracts flawlessly using white-label networks, open-source infrastructure, and scaling delivery systems with zero upfront expenditure."
    )
}

if not (azure_key and azure_endpoint and azure_deployment):
    st.warning("⚠️ Access locked. Please enter your Azure AI Foundry credentials in the sidebar to activate your C-Suite engine.")
else:
    try:
        # Direct, lightweight connection to Azure AI Foundry gateway
        client = AzureOpenAI(
            azure_endpoint=azure_endpoint,
            api_key=azure_key,
            api_version="2024-05-01-preview"
        )

        # Interface UI Layout
        col1, col2 = st.columns([1, 2])

        with col1:
            st.markdown("### 🤖 Activate Agent Node")
            target_agent = st.selectbox("Select Agent to Command:", ["CEO", "VP Sales", "VP Operations"])
            system_prompt = AGENT_PROMPTS[target_agent]

        with col2:
            st.markdown("### 📥 Input Operational Directive")
            user_order = st.text_area("Issue explicit directive:", placeholder="e.g., Draft the I-70 corridor cultivation hit-list.")
            launch_execution = st.button("🚀 Fire Execution Sequence", type="primary")

        if launch_execution and user_order:
            st.write("---")
            st.markdown("### 📟 Live Process Streaming")
            
            with st.spinner(f"{target_agent} compiling raw data and executing directive..."):
                # Direct model execution call using your Azure credits
                response = client.chat.completions.create(
                    model=azure_deployment,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_order}
                    ],
                    temperature=0.7
                )
                
                output = response.choices[0].message.content
                
                st.success("Execution sequence complete.")
                st.markdown("### 📦 Output Payload Received")
                st.markdown(output)
                
    except Exception as e:
        st.error(f"Engine Connection Error: {str(e)}")
