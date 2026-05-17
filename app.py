import streamlit as st
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI

# Platform UI Configuration
st.set_page_config(page_title="Green Fiber Solutions - AI Command Center", layout="wide")

st.title("🚀 Green Fiber Solutions")
st.subheader("Autonomous C-Suite Command Platform")
st.write("---")

# Sidebar for Secure Authentication
st.sidebar.header("🔑 Authentication")
api_key = st.sidebar.text_input("OpenAI API Key", type="password", help="Your key is only used to power this session.")

st.sidebar.write("---")
st.sidebar.markdown("""
### 📊 System Status
* **Core Network:** Connected
* **Agent Sync:** 100% Operational
* **Capital Burn Rate:** $0.00/mo
""")

# Main Workspace Layout
if not api_key:
    st.warning("⚠️ Please enter your OpenAI API Key in the sidebar to activate your AI crew.")
else:
    # Initialize LLM with user's key
    llm = ChatOpenAI(model="gpt-4", api_key=api_key, temperature=0.8)

    # Define the Agent Pool
    agents = {
        "CEO Agent": Agent(
            role="CEO",
            goal="Generate $100K revenue in 30 days with $0 capital",
            backstory="Aggressive, hyper-focused on revenue, rapid execution, and non-dilutive funding.",
            llm=llm,
            verbose=True
        ),
        "VP Sales": Agent(
            role="VP of Sales",
            goal="Close $100K in B2B environmental and fiber services contracts within 30 days",
            backstory="Expert closer. Specializes in pain-point selling, high-volume cold outreach, and rapid closing cycles.",
            llm=llm,
            verbose=True
        ),
        "VP Operations": Agent(
            role="VP of Operations",
            goal="Deliver services flawlessly with zero upfront infrastructure costs",
            backstory="Master of white-labeling, contractor networks, and open-source software integration.",
            llm=llm,
            verbose=True
        ),
        "VP Finance": Agent(
            role="VP of Finance",
            goal="Optimize cash flow, structure upfront retainers, and maintain positive runway",
            backstory="Strict cash-flow manager. Expert in revenue-based financing and minimizing operational burn.",
            llm=llm,
            verbose=True
        )
    }

    # Task Execution Interface
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("### 🤖 Select Active Agent")
        selected_agent_name = st.selectbox("Choose who to command:", list(agents.keys()))
        active_agent = agents[selected_agent_name]
        
        st.info(f"**Current Objective:** {active_agent.goal}")

    with col2:
        st.markdown("### 📝 Issue Execution Order")
        user_directive = st.text_area(
            f"What should the {selected_agent_name} execute right now?",
            placeholder="e.g., Draft a high-velocity cold email sequence targeting Denver data centers or structure a 48-hour cash flow bridge plan."
        )
        
        execute_button = st.button("🚀 Execute Command", type="primary")

    # Live Terminal Output
    if execute_button and user_directive:
        st.write("---")
        st.markdown("### 📟 Live Terminal Readout")
        
        with st.spinner(f"The {selected_agent_name} is processing your directive..."):
            # Programmatically construct the task based on user input
            execution_task = Task(
                description=user_directive,
                expected_output="Direct, high-fidelity, PhD-level professional execution artifact without conversational filler.",
                agent=active_agent
            )
            
            # Assemble the single-agent crew for instant execution
            crew = Crew(
                agents=[active_agent],
                tasks=[execution_task],
                verbose=True
            )
            
            # Run and return response
            result = crew.kickoff()
            
            st.success("Execution Complete.")
            st.markdown(f"### 📥 {selected_agent_name} Response Payload")
            st.markdown(result)  
