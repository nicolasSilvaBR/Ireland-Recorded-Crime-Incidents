import pandas as pd
import streamlit as st
import plotly.express as px
from functions.line_chart import line_chart
from functions.bar_chart import bar_chart

# Configuração da página
st.set_page_config(layout='wide')

# Ler os dados e processar o DataFrame
columns = ['Quarter', 'Garda Division', 'Type of Offence', 'VALUE']
df = pd.read_csv('data/cso_data.csv', usecols=columns)

# Processar colunas
df['Q'] = df['Quarter'].str[-2:]
df['Year'] = df['Quarter'].str[0:4]
df.rename(columns={'Quarter': 'Year_Quarter'}, inplace=True)
df['Garda Division'] = df['Garda Division'].str.replace('Garda Division', '', regex=False).str.strip()
df = df[['Year_Quarter', 'Year', 'Q', 'Garda Division', 'Type of Offence', 'VALUE']]

# Sidebar com opções de seleção
with st.sidebar:
    # Adicionar "All" às opções e ordená-las
    years_options = ['All'] + df['Year'].drop_duplicates().sort_values().tolist()
    quarter_options = ['All'] + df['Q'].drop_duplicates().sort_values().tolist()
    offence_option = ['All'] + df['Type of Offence'].drop_duplicates().sort_values().tolist()
    garda_division_options = ['All'] + df['Garda Division'].drop_duplicates().sort_values().tolist()
    
    # Criar caixas de seleção
    selected_year = st.multiselect(label='Year', options=years_options, default='All')
    selected_quarter = st.multiselect(label='Quarter', options=quarter_options, default='All')
    selected_division = st.multiselect(label='Garda Division', options=garda_division_options, default='All')
    selected_offence = st.multiselect(label='Type of Offence', options=offence_option, default='All')

# Aplicar os filtros (ignorar quando "All" está selecionado)
filtered_df = df[
    ((df['Year'].isin(selected_year)) | ('All' in selected_year)) &
    ((df['Q'].isin(selected_quarter)) | ('All' in selected_quarter)) &
    ((df['Garda Division'].isin(selected_division)) | ('All' in selected_division)) &
    ((df['Type of Offence'].isin(selected_offence)) | ('All' in selected_offence))
]

# Agrupar por 'Year_Quarter' e somar os valores
year_quarter_sum = filtered_df.groupby('Year_Quarter')['VALUE'].sum().reset_index()
year = filtered_df.groupby('Year')['VALUE'].sum().reset_index()

st.subheader(selected_offence)
# Plotar o gráfico de linha com Plotly
#dataset, x_axis, y_axis, title, x_axis_title, y_axis_title
line_chart(
        year_quarter_sum,                       # Data source
        'Year_Quarter',                         # Categorical Column (datetime)
        'VALUE',                                # Numerical Column (number)
        'Crime by Year/Quarter', # Chart Title
        'Year_Quarter',                          # X Axis Title
        ''
    )

bar_chart(
        year,
        'Year',
        'VALUE',
        'Crimes by Year',
        '',
        ''
)

# Mostrar o DataFrame filtrado
st.dataframe(filtered_df, use_container_width=True, hide_index=True)
