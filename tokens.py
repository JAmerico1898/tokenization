import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import hashlib
from datetime import datetime
import graphviz

# -----------------------------------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Tokenização e DLT - App Educacional",
    page_icon="🔗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados para "Cards" e visual
st.markdown("""
<style>
    .card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        margin-bottom: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    .metric-box {
        text-align: center;
        padding: 10px;
        background-color: #ffffff;
        border-radius: 5px;
    }
    .stButton>button {
        width: 100%;
    }
    h1, h2, h3 {
        color: #0E1117;
    }
    .highlight {
        color: #FF4B4B;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# FUNÇÕES AUXILIARES (BLOCKCHAIN SIMULATION)
# -----------------------------------------------------------------------------
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8') +
                   str(self.nonce).encode('utf-8'))
        return sha.hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

def create_genesis_block():
    return Block(0, datetime.now(), "Bloco Gênese", "0")

def next_block(last_block, data):
    this_index = last_block.index + 1
    this_timestamp = datetime.now()
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, data, this_hash)

# Estado da Sessão para Blockchain
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = [create_genesis_block()]

# -----------------------------------------------------------------------------
# NAVEGAÇÃO
# -----------------------------------------------------------------------------
st.sidebar.title("🎓 Tokenização & DLT")
st.sidebar.info("Jornada de Aprendizado para Finanças")

menu = st.sidebar.radio(
    "Navegue pelos Módulos:",
    [
        "Início: Jornada",
        "1 - Fundamentos",
        "2 - Mecânica da Tokenização",
        "3 - Sandbox Blockchain (DLT)",
        "4 - Ciclo de Vida do Ativo",
        "5 - Matriz de Riscos",
        "6 - Casos Reais",
        "7 - Smart Contracts",
        "8 - Quiz Final"
    ]
)

# -----------------------------------------------------------------------------
# PÁGINA: INÍCIO
# -----------------------------------------------------------------------------
if menu == "Início: Jornada":
    st.markdown(
    """
    <div style='text-align: center;'>
        <h1>Bem-vindo à Revolução dos Ativos Digitais</h1>
        <h2><b>A Jornada da Tokenização: Transformando um ativo real em um ativo digital</b></h2>
        <h4>Uma experiência interativa para entender o futuro da infraestrutura financeira</h4>
    </div>
    """,
    unsafe_allow_html=True
    )
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("https://img.icons8.com/fluency/240/blockchain-technology.png", width=200)
        st.caption("Tokenização, DLT e Smart Contracts")
        
    with col2:
        st.markdown("""
        Este aplicativo foi desenhado para estudantes de MBA e Finanças visualizarem conceitos complexos como:
        
        * **Desmaterialização:** Como ativos físicos viram código.
        * **Fracionalização:** Como dividir um prédio em mil pedaços negociáveis.
        * **Imutabilidade:** Como funciona a confiança matemática da Blockchain.
        """)

    st.markdown("---")
    st.subheader("🗺️ Seu Mapa de Aprendizado")
    
    # Visual Journey Map using Graphviz
    journey = graphviz.Digraph()
    journey.attr(rankdir='LR', size='10')
    journey.attr('node', shape='rectangle', style='filled', color='lightblue')
    
    journey.edge('Fundamentos', 'Mecânica\nTokenização')
    journey.edge('Mecânica\nTokenização', 'Sandbox\nBlockchain')
    journey.edge('Sandbox\nBlockchain', 'Ciclo de Vida')
    journey.edge('Ciclo de Vida', 'Matriz de Risco')
    journey.edge('Matriz de Risco', 'Casos Reais')
    journey.edge('Casos Reais', 'Smart Contracts')
    journey.edge('Smart Contracts', 'Quiz Final')
    
    st.graphviz_chart(journey)
    
    st.info("👈 Selecione o **Módulo 1** na barra lateral para começar.")

# -----------------------------------------------------------------------------
# PÁGINA 1: FUNDAMENTOS
# -----------------------------------------------------------------------------
elif menu == "1 - Fundamentos":
    st.title("1 - Fundamentos da Tokenização")
    st.markdown("Entenda os conceitos básicos antes de mergulhar na tecnologia.")
    
    tab1, tab2, tab3 = st.tabs(["🃏 Conceitos Chave", "🔄 O Fluxo", "🏷️ Classificação"])
    
    with tab1:
        st.subheader("Cartões de Conceito")
        col1, col2 = st.columns(2)
        with col1:
            with st.expander("O que é um Token?", expanded=True):
                st.write("Um token é a **representação digital** de um ativo ou utilidade em uma blockchain. Não é o arquivo PDF do contrato, mas o registro programável de propriedade.")
            with st.expander("Fungível vs. Não Fungível (NFT)"):
                st.write("**Fungível:** Dinheiro, ações (uma nota de R$10 vale o mesmo que outra).")
                st.write("**Não Fungível:** Obras de arte, Imóveis (cada unidade é única e insubstituível).")
        with col2:
            with st.expander("Ledger vs. Blockchain"):
                st.write("**Ledger:** Livro razão (registro contábil).")
                st.write("**Blockchain:** Um tipo de DLT (Distributed Ledger Technology) onde os registros são agrupados em blocos encadeados criptograficamente.")
            with st.expander("Custódia (On-chain vs. Off-chain)"):
                st.write("O grande desafio. Se tokenizo um prédio (Off-chain), quem garante que o dono do token é dono do prédio? É necessário um **Custodiante Jurídico** e oráculos.")

    with tab2:
        st.subheader("Fluxo de Tokenização")
        st.markdown("Como um ativo sai do mundo real e vai para a Blockchain.")
        
        flow = graphviz.Digraph()
        flow.attr(rankdir='LR')
        flow.node('A', 'Ativo Real\n(Imóvel, Recebível)', shape='box', style='filled', fillcolor='#ffcccc')
        flow.node('B', 'SPV / Veículo Legal\n(Auditoria & Custódia)', shape='box')
        flow.node('C', 'Emissão do Smart Contract\n(Minting)', shape='box', style='filled', fillcolor='#ccffcc')
        flow.node('D', 'Distribuição\n(Carteira do Investidor)', shape='ellipse')
        
        flow.edge('A', 'B', label='Formalização')
        flow.edge('B', 'C', label='Oraculização')
        flow.edge('C', 'D', label='Venda Primária')
        
        st.graphviz_chart(flow)

    with tab3:
        st.subheader("Explorador de Classificação de Tokens")
        ativo = st.selectbox("Escolha um ativo para analisar:", 
                             ["Títulos Públicos", "Cotas de FIDC", "Imóvel Real", "Obra de Arte", "Crédito de Carbono"])
        
        info = {
            "Títulos Públicos": {"Tipo": "Security Token (RWA)", "Regulação": "Alta (Tesouro/CVM)", "Fracionalização": "Alta", "Padrão": "ERC-20 / DREX"},
            "Cotas de FIDC": {"Tipo": "Security Token", "Regulação": "CVM 175", "Fracionalização": "Média", "Padrão": "ERC-20 com Whitelist"},
            "Imóvel Real": {"Tipo": "Security/Utility Híbrido", "Regulação": "Cartório + CVM", "Fracionalização": "Baixa (SPV necessário)", "Padrão": "ERC-1400 (Security)"},
            "Obra de Arte": {"Tipo": "NFT (Non-Fungible)", "Regulação": "Baixa/Média", "Fracionalização": "Possível (Sharding)", "Padrão": "ERC-721"},
            "Crédito de Carbono": {"Tipo": "Utility/Commodity", "Regulação": "Emergente", "Fracionalização": "Alta (Toneladas)", "Padrão": "Token Climático"}
        }
        
        data = info[ativo]
        c1, c2 = st.columns(2)
        c1.metric("Tipo de Token", data["Tipo"])
        c2.metric("Regulação", data["Regulação"])
        c3, c4 = st.columns(2)
        c3.metric("Fracionalização", data["Fracionalização"])
        c4.metric("Padrão Técnico", data["Padrão"])

# -----------------------------------------------------------------------------
# PÁGINA 2: MECÂNICA
# -----------------------------------------------------------------------------
elif menu == "2 - Mecânica da Tokenização":
    st.title("2 - Simulador de Mecânica e Fracionalização")
    st.markdown("Vamos tokenizar um ativo agora. Ajuste os parâmetros e veja o resultado.")
    
    col_input, col_output = st.columns([1, 1])
    
    with col_input:
        st.markdown("### 🎛️ Parâmetros do Ativo")
        asset_name = st.text_input("Nome do Ativo", "Edifício Faria Lima 2025")
        valuation = st.number_input("Valuation do Ativo (R$)", min_value=10000.0, value=10000000.0, step=50000.0)
        fraction_count = st.slider("Número de Tokens (Fracionalização)", min_value=100, max_value=1000000, value=1000, step=100)
        standard = st.selectbox("Padrão do Token", ["ERC-20 (Fungível)", "ERC-721 (Único)"])
        
        st.markdown("---")
        st.markdown("### ⚖️ Governança")
        custody_quality = st.select_slider("Qualidade da Custódia Off-chain", options=["Baixa/Inexistente", "Média (Auditoria Anual)", "Alta (Banco Top-tier)"])
    
    token_price = valuation / fraction_count
    
    with col_output:
        st.markdown("### 🏭 Resultado da Emissão (Minting)")
        
        c1, c2 = st.columns(2)
        c1.metric("Preço por Token", f"R$ {token_price:,.2f}")
        c2.metric("Market Cap Inicial", f"R$ {valuation:,.2f}")
        
        # Gráfico de Distribuição
        df_dist = pd.DataFrame({
            'Stakeholder': ['Investidores Varejo', 'Emissor (Retido)', 'Taxa Plataforma', 'Reserva de Liquidez'],
            'Quantidade': [fraction_count*0.6, fraction_count*0.2, fraction_count*0.05, fraction_count*0.15]
        })
        fig = px.pie(df_dist, values='Quantidade', names='Stakeholder', title=f'Distribuição de Tokens: {asset_name}', hole=0.4)
        st.plotly_chart(fig, use_container_width=True)
        
        # Flags de Risco
        st.markdown("### 🚩 Análise de Risco Automática")
        if token_price < 10:
            st.warning("⚠️ **Risco de Pulverização:** Preço muito baixo pode atrair especulação excessiva e dificultar governança.")
        if custody_quality == "Baixa/Inexistente":
            st.error("🚨 **Risco Crítico:** Sem custódia robusta, o token não tem lastro real. Potencial fraude.")
        elif custody_quality == "Média (Auditoria Anual)":
            st.info("ℹ️ **Atenção:** Auditoria anual pode não capturar fraudes em tempo real.")
        else:
            st.success("✅ **Estrutura Robusta:** Custódia de alta qualidade mitiga risco de contraparte.")

# -----------------------------------------------------------------------------
# PÁGINA 3: SANDBOX BLOCKCHAIN
# -----------------------------------------------------------------------------
elif menu == "3 - Sandbox Blockchain (DLT)":
    st.title("3 - Sandbox: Construa sua Blockchain")
    st.markdown("Entenda como a imutabilidade funciona na prática visualizando hashs e blocos.")

    col_sim, col_viz = st.columns([1, 2])

    with col_sim:
        st.subheader("Mineração")
        data_input = st.text_input("Dados da Transação (Ex: Alice paga Bob 10 Tokens)", "Transação Inicial")
        difficulty = st.slider("Dificuldade de Mineração (Zeros no Hash)", 1, 4, 2)
        
        if st.button("Minerar Bloco"):
            with st.spinner('Minerando (encontrando o Nonce)...'):
                last_block = st.session_state.blockchain[-1]
                new_block = next_block(last_block, data_input)
                new_block.mine_block(difficulty)
                st.session_state.blockchain.append(new_block)
            st.success("Bloco adicionado à cadeia!")
            
        if st.button("Reiniciar Blockchain"):
            st.session_state.blockchain = [create_genesis_block()]
            st.rerun()

    with col_viz:
        st.subheader("Explorador da Cadeia")
        chain_df = []
        for block in st.session_state.blockchain:
            chain_df.append({
                "Index": block.index,
                "Timestamp": block.timestamp.strftime("%H:%M:%S"),
                "Dados": block.data,
                "Hash Atual": block.hash,
                "Hash Anterior": block.previous_hash,
                "Nonce": block.nonce
            })
        
        df_chain = pd.DataFrame(chain_df)
        st.dataframe(df_chain, hide_index=True)
        
        # Visualização Gráfica da Cadeia
        st.markdown("#### Visualização da Ligação Criptográfica")
        chain_graph = graphviz.Digraph()
        chain_graph.attr(rankdir='LR')
        
        for i, block in enumerate(st.session_state.blockchain):
            label = f"Bloco #{block.index}\nNonce: {block.nonce}\nDados: {block.data[:15]}..."
            chain_graph.node(str(block.index), label, shape='box', style='filled', fillcolor='#e1f5fe' if i > 0 else '#fff9c4')
            if i > 0:
                chain_graph.edge(str(i-1), str(i), label=f"Hash Prev:\n{block.previous_hash[:6]}...")
        
        st.graphviz_chart(chain_graph)
        
    st.markdown("---")
    st.subheader("🧪 Laboratório de Ataques")
    st.info("**Experimento Mental:** Se você tentar alterar os dados do Bloco #0, o hash dele mudará. Como o Bloco #1 contém o 'Hash Anterior' do Bloco #0, o hash do Bloco #1 também mudará, invalidando toda a cadeia futura. É assim que a blockchain garante segurança.")

# -----------------------------------------------------------------------------
# PÁGINA 4: CICLO DE VIDA
# -----------------------------------------------------------------------------
elif menu == "4 - Ciclo de Vida do Ativo":
    st.title("4 - Simulador de Ciclo de Vida")
    st.markdown("Acompanhe a evolução de um ativo tokenizado ao longo do tempo.")

    asset_type = st.selectbox("Escolha o cenário:", ["Imóvel (Aluguel)", "Título de Dívida Corporativa (Debênture)"])
    years = st.slider("Período de Simulação (Anos)", 1, 10, 5)

    # Setup da simulação
    np.random.seed(42)
    months = np.arange(1, (years * 12) + 1)
    
    if asset_type == "Imóvel (Aluguel)":
        base_value = 100
        volatility = 0.02
        yield_rate = 0.005 # 0.5% ao mês
        
        prices = [base_value]
        dividends = []
        
        for m in months[1:]:
            change = np.random.normal(0, volatility)
            new_price = prices[-1] * (1 + change)
            prices.append(new_price)
            dividends.append(new_price * yield_rate)
            
        # Ajuste de arrays
        dividends.insert(0, 0)
        
        df_lifecycle = pd.DataFrame({
            'Mês': months,
            'Preço do Token (R$)': prices,
            'Dividendos Pagos (R$)': dividends
        })
        
        st.subheader("Fluxo de Caixa (Smart Contract Payout)")
        col1, col2 = st.columns([3, 1])
        with col1:
            fig = px.line(df_lifecycle, x='Mês', y=['Preço do Token (R$)', 'Dividendos Pagos (R$)'], 
                          title="Valor do Token vs. Pagamento de Aluguéis")
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            total_dividends = sum(dividends)
            capital_gain = prices[-1] - prices[0]
            roi = ((total_dividends + capital_gain) / prices[0]) * 100
            
            st.metric("Total Pago em Dividendos", f"R$ {total_dividends:.2f}")
            st.metric("Variação de Capital", f"R$ {capital_gain:.2f}")
            st.metric("ROI Total do Investidor", f"{roi:.1f}%")
            
            st.markdown("""
            **Evento Smart Contract:**
            Todo dia 05, o contrato inteligente verifica o pagamento do inquilino e distribui automaticamente para as carteiras dos detentores do token.
            """)

    elif asset_type == "Título de Dívida Corporativa (Debênture)":
        par_value = 1000
        coupon_rate = 0.10 # 10% aa
        default_prob = st.slider("Probabilidade de Calote (Default)", 0.0, 0.2, 0.02)
        
        # Simulação simples
        cash_flows = []
        status = "Adimplente"
        
        for y in range(1, years + 1):
            if np.random.random() < default_prob:
                status = "Default (Calote)"
                cash_flows.append(0)
                break
            else:
                cash_flows.append(par_value * coupon_rate)
        
        # Se sobreviveu até o final, paga principal
        if status == "Adimplente":
            cash_flows[-1] += par_value
            
        st.subheader(f"Status do Título: {status}")
        
        df_bond = pd.DataFrame({
            'Ano': range(1, len(cash_flows) + 1),
            'Fluxo de Caixa': cash_flows
        })
        
        fig = px.bar(df_bond, x='Ano', y='Fluxo de Caixa', title="Fluxos Recebidos pelo Investidor")
        st.plotly_chart(fig, use_container_width=True)
        
        if status == "Default (Calote)":
            st.error("⚠️ Ocorreu um evento de Default! O Smart Contract interrompeu pagamentos e iniciou execução de garantias.")

# -----------------------------------------------------------------------------
# PÁGINA 5: MATRIZ DE RISCO
# -----------------------------------------------------------------------------
elif menu == "5 - Matriz de Riscos":
    st.title("5 - Matriz de Risco Multidimensional")
    st.markdown("Tokenização não elimina riscos, ela adiciona novas camadas tecnológicas.")
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.markdown("### Teste de Estresse")
        market_shock = st.slider("Choque de Mercado (Queda Preço)", 0, 100, 20)
        tech_fail = st.checkbox("Falha no Smart Contract (Hack)")
        reg_change = st.checkbox("Mudança Regulatória Adversa")
        
    with col2:
        # Dados base de risco
        risks = ['Mercado', 'Operacional', 'Cibernético', 'Regulatório', 'Liquidez', 'Custódia']
        impact = [30, 20, 50, 40, 25, 35] # Base
        
        # Aplicar estresse
        if market_shock > 50:
            impact[0] += 40 # Mercado sobe muito
            impact[4] += 30 # Liquidez seca
        elif market_shock > 20:
            impact[0] += 20
            
        if tech_fail:
            impact[2] = 100 # Risco Ciber Maximo
            impact[1] += 50 # Operacional sobe
            
        if reg_change:
            impact[3] = 90 # Risco Regulatório sobe
            impact[4] += 40 # Liquidez
            
        # Heatmap data
        df_risk = pd.DataFrame([impact], columns=risks, index=['Nível de Risco'])
        
        fig = px.imshow(df_risk, 
                        labels=dict(x="Categoria de Risco", y="", color="Intensidade (0-100)"),
                        x=risks, y=['Impacto'],
                        color_continuous_scale='RdYlGn_r', range_color=[0, 100])
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        st.caption("Verde = Seguro | Vermelho = Crítico")

# -----------------------------------------------------------------------------
# PÁGINA 6: CASOS REAIS
# -----------------------------------------------------------------------------
elif menu == "6 - Casos Reais":
    st.title("6 - Estudos de Caso")
    st.markdown("Exemplos do Brasil e do Mundo.")
    
    case_tab1, case_tab2, case_tab3 = st.tabs(["🇧🇷 FIDC Tokenizado", "🇺🇸 Títulos do Tesouro (BUIDL)", "🌍 Créditos de Carbono"])
    
    with case_tab1:
        st.header("FIDC e Recebíveis no Brasil")
        st.markdown("""
        **O Cenário:** O Brasil é pioneiro na tokenização de recebíveis (FIDC). 
        
        * **Como funciona:** Uma empresa (ex: varejista) tem notas fiscais a receber em 90 dias.
        * **Tokenização:** Essas notas são empacotadas, validadas e transformadas em tokens.
        * **Investidor:** Compra o token com desconto (ex: paga 95 para receber 100).
        * **Regulação:** CVM Resolução 175 e Sandbox Regulatório.
        
        **Vantagem:** Redução de intermediários bancários e custo de captação menor para a empresa.
        """)
        st.info("Empresas envolvidas no ecossistema: Liqi, Vórtx, MB.")
        
    with case_tab2:
        st.header("BlackRock BUIDL & Franklin Templeton")
        st.markdown("""
        **O Cenário:** Grandes gestoras trazendo Títulos do Tesouro Americano (Treasuries) para a blockchain.
        
        * **Produto:** Fundo de liquidez tokenizado.
        * **Mecânica:** Cada token vale $1. O rendimento é pago diariamente via *rebasing* (aumenta a quantidade de tokens na carteira) ou dividendo mensal.
        * **Blockchain:** Ethereum (ERC-20).
        * **Sucesso:** O fundo BUIDL da BlackRock atingiu >$500 milhões em ativos em tempo recorde.
        """)
        st.metric("TVL (Total Value Locked) estimado no Setor RWA", "$ 12 Bilhões+")
        
    with case_tab3:
        st.header("Toucan Protocol & Klima DAO")
        st.markdown("""
        **O Cenário:** Tokenização de créditos de carbono 'zumbis' (antigos).
        
        * **O Problema:** Créditos antigos de baixa qualidade foram tokenizados e vendidos como offsets "premium".
        * **A Lição:** A Blockchain garante que o token é único, mas não garante a **qualidade do ativo subjacente**.
        * **Consequência:** A certificadora Verra suspendeu a tokenização direta para criar regras mais rígidas.
        """)
        st.warning("Lição aprendida: 'Garbage In, Garbage Out'. A tecnologia não conserta um ativo ruim.")

# -----------------------------------------------------------------------------
# PÁGINA 7: SMART CONTRACTS
# -----------------------------------------------------------------------------
elif menu == "7 - Smart Contracts":
    st.title("7 - Explorador de Smart Contracts")
    st.markdown("Veja como a lógica é programada (Pseudo-Solidity).")
    
    contract_type = st.selectbox("Modelo de Contrato", ["Token Simples (ERC-20)", "Restrição de Compliance (Whitelist)"])
    
    if contract_type == "Token Simples (ERC-20)":
        supply = st.number_input("Supply Total", value=1000000)
        name = st.text_input("Símbolo", "MTOKEN")
        
        code = f"""
// Contrato Simplificado ERC-20 - Criação de um ativo digital (MTOKEN) 
// que pode ser transferido entre endereços na blockchain, 
// representando frações tokenizadas de algum valor real.
contract {name} {{
    string public name = "Meu Token MBA";
    string public symbol = "{name}";
    uint8 public decimals = 18;
    uint256 public totalSupply = {supply} * (10 ** uint256(decimals));

    mapping(address => uint256) public balanceOf;

    event Transfer(address indexed from, address indexed to, uint256 value);

    constructor() {{
        // O criador do contrato recebe todos os tokens inicialmente
        balanceOf[msg.sender] = totalSupply;
    }}

    function transfer(address to, uint256 value) public returns (bool success) {{
        require(balanceOf[msg.sender] >= value, "Saldo insuficiente");
        
        balanceOf[msg.sender] -= value;
        balanceOf[to] += value;
        
        emit Transfer(msg.sender, to, value);
        return true;
    }}
}}
        """
        st.code(code, language='solidity')
        st.caption("Explicação: Este código define um mapa (tabela) de saldos. A função transfer apenas subtrai de um endereço e soma em outro. Simples e eficiente.")

    elif contract_type == "Restrição de Compliance (Whitelist)":
        st.code("""
contract ComplianceToken {
    mapping(address => bool) public whitelist;
    address public admin;

    constructor() {
        admin = msg.sender;
    }

    // Apenas investidores aprovados (KYC) podem receber tokens
    modifier onlyWhitelisted(address _addr) {
        require(whitelist[_addr] == true, "Investidor nao autorizado (KYC Pendente)");
        _;
    }

    function addToWhitelist(address _investor) public {
        require(msg.sender == admin, "Apenas admin");
        whitelist[_investor] = true;
    }

    function transfer(address to, uint256 value) public onlyWhitelisted(to) {
        // Lógica de transferência...
        // A transferência falhará se o destinatário não estiver na whitelist
    }
}
        """, language='solidity')
        st.caption("Explicação: Adicionamos um 'Modificador'. Antes de transferir, o código checa se o destino está numa lista aprovada (KYC/AML). Fundamental para Security Tokens.")

# -----------------------------------------------------------------------------
# PÁGINA 8: QUIZ
# -----------------------------------------------------------------------------
elif menu == "8 - Quiz Final":
    st.title("🎯 Avaliação de Conhecimento")
    st.markdown("Teste o que você aprendeu.")
    
    score = 0
    
    q1 = st.radio("1. Qual a principal diferença entre Tokenização e Securitização tradicional?", 
                  ["Não há diferença.", 
                   "A tokenização permite fracionalização granular e liquidação programável (D+0).", 
                   "A tokenização dispensa advogados."], index=0)
    if q1 == "A tokenização permite fracionalização granular e liquidação programável (D+0).":
        score += 1
        
    st.markdown("---")
    
    q2 = st.radio("2. Se um hacker altera um registro em um bloco antigo de uma blockchain, o que acontece?", 
                  ["Nada, o sistema aceita a mudança.", 
                   "O hash do bloco muda, invalidando toda a cadeia subsequente.", 
                   "O hacker ganha todos os tokens."], index=0)
    if q2 == "O hash do bloco muda, invalidando toda a cadeia subsequente.":
        score += 1
        
    st.markdown("---")
    
    q3 = st.radio("3. O que é um 'Security Token'?", 
                  ["Um token usado apenas para pagar taxas de rede.", 
                   "Um avatar digital em jogos.", 
                   "Uma representação digital de um valor mobiliário regulado (investimento)."], index=0)
    if q3 == "Uma representação digital de um valor mobiliário regulado (investimento).":
        score += 1
        
    st.markdown("---")
    
    if st.button("Verificar Resultado"):
        if score == 3:
            st.balloons()
            st.success(f"Parabéns! Você acertou {score}/3. Você é um Mestre da Tokenização! 🎓")
        elif score == 2:
            st.warning(f"Bom trabalho! Você acertou {score}/3.")
        else:
            st.error(f"Sua pontuação: {score}/3. Revise os Módulos 1 e 3.")

# -----------------------------------------------------------------------------
# RODAPÉ
# -----------------------------------------------------------------------------
# Footer
st.divider()

st.markdown(
    """
    <div style='text-align: center;'>
        <p style='font-size: 0.9em; color: gray;'>
            © 2025 Tokenization Journey Teaching Tool | Developed for educational purposes
        </p>
        <p style='font-size: 0.9em; color: gray;'>
            Prof. José Américo – Coppead
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
