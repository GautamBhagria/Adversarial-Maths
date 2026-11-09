cat << 'EOF' > sidechannel_analyzer.py
import numpy as np
import scipy.linalg as la
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Spectral Graph Analyzer", layout="wide")
st.title("Project 2: Spectral Graph Laplacian Side-Channel Defect Analyzer")

st.markdown("""
### Graph Theory Formulation
Hardware side-channel bugs alter execution trace topologies. We model execution states as a directed, weighted graph $G = (V, E, W)$. We isolate structural code leaks by computing the **Unnormalized Graph Laplacian Matrix**: $$L = D - A$$
""")

st.sidebar.header("Graph Setup")
nodes = st.sidebar.slider("Execution Trace Nodes ($|V|$)", 10, 50, 20, 5)
leak_magnitude = st.sidebar.slider("Side-Channel Leakage Coefficient", 0.0, 5.0, 2.5, 0.5)

np.random.seed(42)
A = np.random.rand(nodes, nodes)
A = (A + A.T) / 2
np.fill_diagonal(A, 0)

if nodes > 8:
    A[0:4, 4:8] += leak_magnitude
    A[4:8, 0:4] += leak_magnitude

D = np.diag(np.sum(A, axis=1))
L = D - A

eigenvalues, eigenvectors = la.eigh(L)
idx = np.argsort(eigenvalues)
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

fiedler_val = eigenvalues[1]
fiedler_vector = eigenvectors[:, 1]

col1, col2 = st.columns(2)
with col1:
    st.subheader("Laplacian Matrix Spectrum Analysis")
    fig, ax = plt.subplots()
    ax.stem(range(len(eigenvalues)), eigenvalues, linefmt='b-', markerfmt='bo', basefmt='r-')
    ax.set_ylabel("Eigenvalues ($\lambda$)")
    st.pyplot(fig)

with col2:
    st.subheader("Structural Defect Boundary Isolation")
    fig2, ax2 = plt.subplots()
    ax2.bar(range(nodes), fiedler_vector, color=['red' if val < 0 else 'blue' for val in fiedler_vector])
    ax2.set_ylabel("Fiedler Vector Amplitude Component")
    st.pyplot(fig2)

if fiedler_val < 0.8:
    st.warning(f"Structural Defect Flagged: Low algebraic connectivity ($\lambda_2$ = {fiedler_val:.4f}) indicates an informational leak.")
else:
    st.success("Execution graph demonstrates robust spectral uniformity.")
EOF

