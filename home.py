import streamlit as st


st.set_page_config(
    page_title = "Home",
    page_icon= "src/imgs/logo ventures.png",
    layout='wide'
)

with open('style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

#alinhando a imagem
col1, col2, col3 = st.columns(3)
with col2: 
   st.image('ventures.png', width=300)


col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
with col2:
   st.markdown("""<h1>Controle de Perdas e Validade</h1>""", unsafe_allow_html=True)


st.header("Descrição do projeto")

st.markdown("""O principal problema do fabricante de medicamentos é a gestão do controle de estoque e movimentação de produtos, que apresenta falhas. As principais consequências disso são a falta de gestão sobre quantidade, distribuição para processo fabril de medicamentos, vencimento e necessidade de aquisição.
Foram passados <b>20 indicadores</b> diferentes entre os quais deveríamos escolher no mínimo três para trabalhar, e os indicadores escolhidos para o nosso projeto foram os seguintes:

- <b>Índices de perdas e/ou rendimento dos lotes;</b>
- <b>Custo (R$) das perdas;</b>
- <b>Controle da validade dos insumos;</b>
- <b>Sinalização dos insumos mais próximos do vencimento;</b>

Por preferência do fabricante de medicamentos, utilizamos dashboards para realizar este acompanhamento dos indicadores.""",unsafe_allow_html=True )
st.divider()


st.header("Páginas Principais")
col1, col2 = st.columns(2)
with col1:
   st.markdown("""<div class="divider"></div>""",unsafe_allow_html=True)
   st.page_link("pages/Controle de Insumo.py", label="Controle de Insumo", use_container_width=True)
   st.markdown("""<div class="divider"></div>""",unsafe_allow_html=True )
   st.markdown("""<p class="descricao"> Na página de controle de insumos, oferecemos uma <b>análise gráfica</b> que permite a <i>seleção</i> específica de elementos e o controle detalhado do estoque desses insumos. Além disso, é possível <i>visualizar</i> um balanceamento abrangente de todos os insumos utilizados, mostrando claramente as <i>sobras</i> ou <i>faltas</i> em um determinado mês, conforme desejado.</p>""",unsafe_allow_html=True)

with col2: 
   st.markdown("""<div class="divider"></div>""",unsafe_allow_html=True)
   indice = st.page_link("pages/Indices de Perdas.py", label="Indice de Perdas", use_container_width=True)
   st.markdown("""<div class="divider"></div>""",unsafe_allow_html=True)
   st.markdown("""<p>exemplo de texto</p>""",unsafe_allow_html=True)

st.divider()


with st.expander("Dados Fornecidos", expanded=True):
   st.markdown("""<h4>Tabelas antes da visualização dos dados em dashboards</h4>""", unsafe_allow_html=True)
   col1, col2, col3 = st.columns(3)

   with col1:
      st.write("Validade")
      st.image("src/imgs/tabela validade.png",)
   with col2:
      st.write("Preço Custo")
      st.image("src/imgs/tabela preco custo.png", )
   with col3:
      st.write("Consolidação estoque")
      st.image("src/imgs/tabela consolidacao.png",)
 



with st.expander("Instalação e Configuração", expanded=True):
   st.markdown("""<h4>Inicializando o projeto</h4>""", unsafe_allow_html=True)
   st.write(":heavy_check_mark: [Baixe o repositório](https://github.com/wildestmaii/LAFEPE-ProjetA) em sua máquina.")
   st.image('src/imgs/print1.png', width=500)

   st.write(":heavy_check_mark: Após extrair o arquivo, abra a pasta com o VS Code ou uma IDE de sua preferência:")
   st.image('src/imgs/print2.png', width=500)

   st.write(":heavy_check_mark: No cmd, inicie o seguinte comando para baixar as dependências necessárias:")
   code = '''pip install streamlit'''
   st.code(code, language='python')

   st.write(":heavy_check_mark: Em seguida, instale a biblioteca matplotlib:")
   code = '''pip install matplotlib'''
   st.code(code, language='python')

   st.write(":heavy_check_mark: E por fim, inicie o projeto:")
   code = '''streamlit run [diretório do arquivo "index.py" do projeto]'''
   st.code(code, language='python')

   st.write("Assim que o projeto for iniciado, o streamlit mostrará formas de acessar através de urls no terminal.")





with st.expander("Estrutura do código", expanded=True):
   st.markdown("""<h4>Estrutura do código</h4>""", unsafe_allow_html=True)
   st.write("Estrutura do código.")




#apresentação dos membros da equipe
with st.expander("Nossa equipe", expanded=True):

   col1, col2, col3, col4, col5, col6, col7 = st.columns(7, gap="medium")

   with col1:
      st.image("src/imgs/ayrton.png", width=100,  caption='Ayrton Maia')

   with col2:
      st.image("src/imgs/Karolayne.PNG", width=100, caption='Karolayne Silva')

   with col3:

      st.image("src/imgs/maiara.png", width=100, caption='Maiara Meneses') 

   with col4:

      st.image("src/imgs/higor.png", width=100, caption='Higor Cabral')

   with col5:

      st.image("src/imgs/quezia.png", width=100, caption='Quézia Cassiano')

   with col6:

      st.image("src/imgs/erika.png", width=100, caption='Erika Santos')

   with col7:

      st.image("src/imgs/everton.png", width=100, caption='Everton Gabriel')


col1, col2, col3, = st.columns(3)
with col2:
   st.write("Nosso repositório do github :coffee: ")
   st.link_button("Go to the repository", "https://github.com/wildestmaii/LAFEPE-ProjetAI")