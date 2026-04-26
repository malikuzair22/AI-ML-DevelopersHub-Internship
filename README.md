# 🤖 AI/ML Engineering Internship — DevelopersHub Corporation

![Python](https://img.shields.io/badge/Python-3.11-blue)
![ML](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![LangChain](https://img.shields.io/badge/LangChain-Groq-green)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)

This repository contains completed AI/ML tasks for the **DevelopersHub Corporation Internship**.
Each task demonstrates real-world AI/ML skills including data exploration, model training, evaluation, and chatbot development.

---

## 📁 Repository Structure
AI-ML-DevelopersHub-Internship/
├── Task1_Iris_EDA/
│   ├── IRIS_EDA.ipynb
│   └── IRIS.csv
├── Task2_Stock_Price_Prediction/
│   ├── stock_price.ipynb
│   └── (data fetched via yfinance)
├── Task3_Heart_Disease_Prediction/
│   ├── heart_disease.ipynb
│   └── heart.csv
├── Task4_Health_Query_Chatbot/
│   ├── health_chatbot.py
│   └── .env (not included - see setup)
├── Task6_House_Price_Prediction/
│   ├── house_price.ipynb
│   └── Housing.csv
└── README.md

---

## ✅ Completed Tasks

### Task 1 — Iris Dataset EDA
**Objective:** Explore and visualize the Iris dataset to understand data trends and distributions.

| Detail | Info |
|--------|------|
| Dataset | Iris Dataset (CSV) |
| Libraries | Pandas, Matplotlib, Seaborn |
| Techniques | EDA, Scatter plots, Histograms, Box plots, Pair plots |

**Key Findings:**
- Iris-setosa is clearly separable from other species based on petal features
- Petal length and petal width are the most distinguishing features
- No missing values found in the dataset

---

### Task 2 — Stock Price Prediction
**Objective:** Predict Apple (AAPL) next day closing price using historical stock data.

| Detail | Info |
|--------|------|
| Dataset | Yahoo Finance via yfinance (2021-2024) |
| Model | Random Forest Regressor |
| Features | Open, High, Low, Volume |
| Target | Close Price |

**Results:**
- MAE: ~7.47
- RMSE: ~9.96
- Feature Importance: High and Low prices are most influential

---

### Task 3 — Heart Disease Prediction
**Objective:** Predict whether a patient is at risk of heart disease using health data.

| Detail | Info |
|--------|------|
| Dataset | Heart Disease UCI Dataset |
| Models | Logistic Regression + Decision Tree |
| Evaluation | Accuracy, ROC-AUC, Confusion Matrix |

**Results:**
- Logistic Regression Accuracy: ~85%
- Decision Tree Accuracy: ~78%
- Top features: chest pain type, max heart rate, number of vessels

---

### Task 4 — General Health Query Chatbot
**Objective:** Build a chatbot that answers general health questions using an LLM.

| Detail | Info |
|--------|------|
| Model | Llama3-8b via Groq API |
| Framework | LangChain + Streamlit |
| Features | Prompt engineering, Safety filter, Chat history |

**Key Features:**
- Friendly and empathetic responses
- Safety filter for dangerous queries
- Suggests doctor for serious symptoms
- Clean Streamlit UI with chat history

---

### Task 6 — House Price Prediction
**Objective:** Predict house prices based on property features.

| Detail | Info |
|--------|------|
| Dataset | Housing Prices Dataset (Kaggle) |
| Models | Linear Regression + Gradient Boosting |
| Evaluation | MAE, RMSE |

**Results:**
- Gradient Boosting outperformed Linear Regression
- Area and number of bathrooms are top price predictors
- Feature scaling improved model performance

---

## 🛠️ Setup & Installation

### Prerequisites
- Python 3.11+
- Git

### Installation
```bash
# Clone the repo
git clone https://github.com/malikuzair22/AI-ML-DevelopersHub-Internship.git
cd AI-ML-DevelopersHub-Internship

# Install dependencies
pip install numpy pandas matplotlib seaborn scikit-learn yfinance groq langchain langchain-groq streamlit python-dotenv
```

### For Task 4 Chatbot
Create a `.env` file in `Task4_Health_Query_Chatbot/`:

GROQ_API_KEY=your_groq_api_key_here

Get your free API key at 👉 https://console.groq.com

Run the chatbot:
```bash
cd Task4_Health_Query_Chatbot
streamlit run health_chatbot.py
```

---

## 🧰 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.11 | Core language |
| Pandas & NumPy | Data manipulation |
| Matplotlib & Seaborn | Data visualization |
| Scikit-Learn | ML models |
| yfinance | Stock data fetching |
| LangChain | LLM framework |
| Groq API | LLM inference |
| Streamlit | Chatbot UI |

---

## 👨‍💻 Author

**Malik Uzair**
- GitHub: [@malikuzair22](https://github.com/malikuzair22)
- Internship: DevelopersHub Corporation — AI/ML Engineering

---

## 📄 License
This project is for educational and internship purposes.


