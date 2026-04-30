# BiblioAI : Book Recommendation System with Flask UI

An intelligent **Book Recommendation System** built using **Collaborative Filtering (KNN)** and deployed with a **Flask-based web interface** to deliver real-time book suggestions.

---

## 📌 Overview

This project recommends books based on user preferences using **item-based collaborative filtering**. It is powered by a machine learning model and served through a **Flask web application**, enabling users to interact with the system via a clean UI.

---

## ✨ Features

- 📚 Get top 6 similar book recommendations  
- 🌐 Interactive **Flask web interface**  
- 🔍 Search-based recommendation system  
- 🧠 Machine Learning powered (KNN)  
- ⚡ Optimized using sparse matrices  
- 💾 Pre-trained model loaded using pickle  

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS (Flask Templates)  
- **Backend:** Flask (Python)  
- **ML Libraries:** Pandas, NumPy, Scikit-learn, SciPy  
- **Model Storage:** Pickle  

---

## 📂 Dataset

**Book-Crossing Dataset**

- BX-Books.csv  
- BX-Users.csv  
- BX-Book-Ratings.csv  

---

## ⚙️ How It Works

### 1. Data Preprocessing
- Cleaned and merged datasets  
- Removed null values  
- Standardized columns  

### 2. Filtering Strategy
- Users with > 200 ratings  
- Books with ≥ 50 ratings  

### 3. Model Creation
- Pivot table (Books × Users)  
- Sparse matrix conversion  
- KNN model training  

### 4. Recommendation Logic
- Input: Book name  
- Output: Top similar books using cosine similarity  

### 5. Web Integration (Flask)
- User inputs book name via UI  
- Flask fetches recommendations  
- Results displayed dynamically  

---

## 🧠 Model Details

- Algorithm: K-Nearest Neighbors  
- Similarity: Cosine Similarity  
- Type: Item-Based Collaborative Filtering  

---

## 📊 Evaluation Metrics

- **Precision@K** → Relevance of recommended books  
- **Recall@K** → Coverage of relevant books  
- **Cosine Similarity Score** → Measures similarity  
- **Coverage** → Diversity of recommendations  
- **Sparsity Optimization** → CSR matrix for efficiency  

---

## 💻 UI Preview

<img width="1866" height="921" alt="image" src="https://github.com/user-attachments/assets/17296982-8da3-4473-b441-17eb04da6d9f" />


<img width="1869" height="878" alt="image" src="https://github.com/user-attachments/assets/307dbbe6-9f6a-4741-aa5f-99df36b13a71" />

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/your-username/biblioai.git
cd biblioai

# Create and activate environment (Anaconda)
conda create -n books python=3.9
conda activate books

# Install dependencies
pip install pandas numpy scikit-learn scipy flask

# Run the app
python app.py

Open in browser: http://127.0.0.1:5000/
