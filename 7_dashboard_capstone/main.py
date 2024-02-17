import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

URL = "https://raw.githubusercontent.com/marcopeix/MachineLearningModelDeploymentwithStreamlit/master/12_dashboard_capstone/data/quarterly_canada_population.csv"

@st.cache_data
def read_data():
    df = pd.read_csv(URL, dtype={'Quarter': str, 
                            'Canada': np.int32,
                            'Newfoundland and Labrador': np.int32,
                            'Prince Edward Island': np.int32,
                            'Nova Scotia': np.int32,
                            'New Brunswick': np.int32,
                            'Quebec': np.int32,
                            'Ontario': np.int32,
                            'Manitoba': np.int32,
                            'Saskatchewan': np.int32,
                            'Alberta': np.int32,
                            'British Columbia': np.int32,
                            'Yukon': np.int32,
                            'Northwest Territories': np.int32,
                            'Nunavut': np.int32})
    return df 

df = read_data()
st.title("Population of Canada")
st.markdown("Source table can be found [here](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000901)")

with st.expander('Click to see the full table'):
    st.write(df)

with st.form('population-form'):
    col1, col2, col3 = st.columns(3)
    quarter_list = df['Quarter'].apply(lambda x: x.split()[0]).unique()
    year = df['Quarter'].apply(lambda x: int(x.split()[1])).unique()
    min_year = np.min(year)
    max_year = np.max(year)

    with col1:
        st.write("Choose a starting date")
        start_quater = st.selectbox("Quater", options=quarter_list, index=0, key='start_q')
        start_year = st.slider("Year", min_value=min_year, max_value=max_year, value=min_year, step=1, key='start_y')

    with col2:
        st.write("Choose an end date")
        end_quater = st.selectbox("Quater", options=quarter_list, index=len(quarter_list)-1, key='end_q')
        end_year = st.slider("Year", min_value=min_year, max_value=max_year, value=min_year, step=1, key='end_y')

    with col3:
        st.write("Choose a location")
        target = st.selectbox("Choose a location", options=df.columns[1:], index=0)

    submit_btn = st.form_submit_button("Analyze", type="primary")

start_date = f"{start_quater} {start_year}"
end_date = f"{end_quater} {end_year}"

@st.cache_data
def format_date_for_comparison(date):
    if date[1] == 2:
        return float(date[2:]) + 0.25
    elif date[1] == 3:
        return float(date[2:]) + 0.50
    elif date[1] == 4:
        return float(date[2:]) + 0.50
    else:
        return float(date[2:])

@st.cache_data    
def end_before_start(start_date, end_date):
    num_start_date = format_date_for_comparison(start_date)
    num_end_date = format_date_for_comparison(end_date)

    if num_start_date > num_end_date:
        return True
    else:
        return False

@st.cache_data
def percentage_diff(start_date, end_date, target):
    initial = df.loc[df['Quarter'] == start_date, target].item()
    final = df.loc[df['Quarter'] == end_date, target].item()
    percentage_diff = round((final - initial) / initial * 100, 2)
    return percentage_diff
    
# Cannot cache this function, because we are returning some widget elements when you have UI elements return in some function sometimes we cache it, sometimes
# we cannot cache it In this case we cannot cache it
def display_dashboard(start_date, end_date, target):
    tab1, tab2, tab3 = st.tabs(["Population change", "Compare", "bar comparison"])
    
    with tab1:
        st.subheader(f"Population change of {target} from {start_date} to {end_date}")

        col1, col2 = st.columns(2)
        
        with col1:
            initial = df.loc[df['Quarter'] == start_date, target].item()
            final = df.loc[df['Quarter'] == end_date, target].item()
            percentage_change = percentage_diff(start_date, end_date, target)
            delta = f"{percentage_change}%"
            st.metric(start_date, value=initial)
            st.metric(end_date, value=final, delta=delta)
            
        with col2:
            start_idx = df.loc[df['Quarter'] == start_date].index.item()
            end_idx = df.loc[df['Quarter'] == end_date].index.item()
            filtered_df = df.iloc[start_idx: end_idx+1]
            fig = px.line(filtered_df, x='Quarter', y=target, title="Line Chart")
            fig.update_xaxes(title="Time", tickvals=[filtered_df['Quarter'].iloc[0], filtered_df['Quarter'].iloc[-1]])
            fig.update_yaxes(title="Population")
            st.plotly_chart(fig)
            
        with tab2:
            st.subheader('Compare with other locations')
            all_targets = st.multiselect("Choose other locations", options=filtered_df.columns[1:], default=[target], key='tab2')
            if len(all_targets) == 0:
                st.error("Please select at least one location for comparison.")
            else:
                fig = px.line(filtered_df, x='Quarter', y=all_targets, title="Comparison of Population Change")
                fig.update_xaxes(title="Time", tickvals=[filtered_df['Quarter'].iloc[0], filtered_df['Quarter'].iloc[-1]])
                fig.update_yaxes(title="Population")
                st.plotly_chart(fig)

        with tab3:
            st.subheader('Bar comparison')
            comparison_data = []
            selected_targets = st.multiselect("Choose other locations", options=filtered_df.columns[1:], default=[target], key='tab3')
            if len(selected_targets) == 0:
                st.error("Please select at least one location for comparison.")
            else:
                for location in selected_targets:
                    percentage_change = percentage_diff(start_date, end_date, location)
                    comparison_data.append({'Location': location, 'Percentage Difference': percentage_change})
                comparison_df = pd.DataFrame(comparison_data)
                fig = px.bar(comparison_df, x='Location', y='Percentage Difference', title=f"Percentage Difference in Population from {start_date} to {end_date}")
                st.plotly_chart(fig)


if start_date not in df['Quarter'].tolist() or end_date not in df['Quarter'].tolist():
    st.error("No data available. Check your quarter and year selection")
elif end_before_start(start_date, end_date):
    st.error("Dates don't work. Start date must come before end date.")
else:
    display_dashboard(start_date, end_date, target)
