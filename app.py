# SQLite fix for free cloud deployment engines
try:
    import sys
    import pysqlite3
    sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")
except ImportError:
    pass

import streamlit as st
from crewai import Agent, Task, Crew
from langchain_openai import AzureChatOpenAI

st.set_page_config(page_title="Green Fiber Solutions Control Center", layout="wide")

st.title("⚡ Green Fiber Solutions")
st.subheader("Unrestricted Azure-Powered C-Suite Platform")
st.write("---")

# Secure Sidebar Credentials for Azure AI Foundry
st.sidebar.header("🔑 Azure AI Credentials")
azure_key = st.sidebar.text_input("Azure API Key", type="password")
azure_endpoint = st.sidebar.text_input("Azure Endpoint URL", placeholder="https://your-resource.openai.azure.com/")
azure_deployment = st.sidebar.text_input("Deployment Name", placeholder="e.g., gpt-4o")

st.sidebar.write("---")
st.sidebar.markdown(f"""
### 📊 Enterprise Metadata
* **Entity Status:** Active (EIN Verified)
* **Regional Node:** Denver / Aurora CO
* **Compute Source:** Microsoft Azure Credits
* **Operational Mode:** Unrestricted
""")

if not (azure_key and azure_endpoint and azure_deployment):
    st.warning("⚠️ Access locked. Please enter your Azure OpenAI credentials in the sidebar to activate your crew.")
else:
    try:
        # Streamlined initialization to completely bypass Pydantic configuration errors
        llm = AzureChatOpenAI(
            azure_deployment=azure_deployment,
            api_key=azure_key,
            azure_endpoint=azure_endpoint,
            api_version="2024-05-01-preview",
            temperature=0.7,
            verbose=True
        )

        # Instantiate the Virtual C-Suite
        ceo = Agent(
            role="Chief Executive Officer",
            goal="Drive immediate $100K MVR revenue pipeline using zero-capital Colorado corporate frameworks.",
            backstory="Hyper-aggressive corporate strategist focused on immediate cash-flow realization, local contract arbitrage, and scaling B2B solutions.",
            llm=llm,
            allow_delegation=False
        )

        sales = Agent(
            role="VP of Sales",
            goal="Scrape, target, and close high-value B2B environmental and infrastructure accounts along the I-70 corridor.",
            backstory="Elite closer. Expert in bypassing corporate gatekeepers, pain-point pitching, and structured upfront retainer execution.",
            llm=llm,
            allow_delegation=False
        )

        operations = Agent(
            role="VP of Operations",
            goal="Fulfill corporate contracts flawlessly using white-label networks and open-source infrastructure.",
            backstory="Logistics expert. Specializes in scaling physical and digital delivery systems with zero upfront expenditure.",
            llm=llm,
            allow_delegation=False
        )

        # Interface UI Layout
        col1, col2 = st.columns([1, 2])

        with col1:
            st.markdown("### 🤖 Activate Agent Node")
            target_agent = st.selectbox("Select Agent to Command:", ["CEO", "VP Sales", "VP Operations"])
            
            agent_mapping = {"CEO": ceo, "VP Sales": sales, "VP Operations": operations}
            active_agent = agent_mapping[target_agent]

        with col2:
            st.markdown("### 📥 Input Operational Directive")
            user_order = st.text_area("Issue explicit directive:", placeholder="e.g., Draft the I-70 corridor cultivation hit-list.")
            launch_execution = st.button("🚀 Fire Execution Sequence", type="primary")

        if launch_execution and user_order:
            st.write("---")
            st.markdown("### 📟 Live Process Streaming")
            
            with st.spinner("Agent running live analytics execution..."):
                task = Task(
                    description=user_order,
                    expected_output="Direct, elite, production-grade operational payload with zero conversational filler.",
                    agent=active_agent
                )
                crew = Crew(agents=[active_agent], tasks=[task], verbose=True)
                output = crew.kickoff()
                
                st.success("Execution sequence complete.")
                st.markdown("### 📦 Output Payload Received")
                st.markdown(output)
                
    except Exception as e:
        st.error(f"Initialization Error: {str(e)}")
