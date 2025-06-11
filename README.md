# AnatomyMentor 

An AI-powered anatomy tutoring application designed to help medical students learn complex anatomical concepts with ease.

##  Overview

AnatomyMentor is a Streamlit-based web application that uses Google's Gemini AI to provide:
- Interactive anatomy topic explanations
- MCQ question generation for practice
- Image analysis of anatomical structures
- Personalized learning support

##  Features

### 🧠 Topic Analysis
- Enter any anatomy topic (nerves, muscles, organs, etc.)
- Get detailed AI-generated explanations
- Real-time streaming text display

### 📝 Question Generation
- Generate custom multiple-choice questions
- Specify the number of questions (default: 10)
- Practice questions tailored to your topic

### 🖼️ Image Analysis
- Upload anatomical structure images
- AI analyzes and explains the structures
- Visual learning support

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini Pro
- **Image Processing**: PIL (Python Imaging Library)
- **Environment Management**: python-dotenv

## 📦 Installation

### Prerequisites
- Python 3.7+
- Google API key for Gemini AI

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/NajmiHassan/anatomy_mentor.git
   cd anatomy-mentor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. ## 🔑 API Setup

### Getting Google Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key to your `.env` file


4. **Set up environment variables**
   - Create a `.env` file in the project root
   - Add your Google API key:
     ```
     api_key=your_google_api_key_here
     ```

5. **Run the application**
   ```bash
   streamlit run file.py
   ```

## 🔧 Configuration

The app includes custom Streamlit theming in `.streamlit/config.toml`:
- Primary Color: `#f1ef99` (Light yellow)
- Background: `#eceaad` (Cream)
- Secondary Background: `#b0c5a4` (Light green)
- Text Color: `#925050` (Brown)

## 📁 Project Structure

```
anatomy-mentor/
├── file.py                 # Main application file
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables (create this)
├── .gitignore            # Git ignore rules
├── .streamlit/
│   └── config.toml       # Streamlit configuration
└── images/
    └── image.png         # App logo/header image
```

## 🚀 Usage

1. **Start the application**
   ```bash
   streamlit run file.py
   ```

2. **Access the web interface**
   - Open your browser and go to `http://localhost:8501`

3. **Use the features**
   - **Topic Analysis**: Enter an anatomy topic in the sidebar
   - **Question Generation**: Specify number of MCQs and click "Generate analysis and questions"
   - **Image Analysis**: Upload an anatomical image for AI analysis

## 🎯 Core Functions

### `analyze_anatomy_topic(topic)`
- Analyzes user-entered anatomy topics
- Returns formatted explanations using Gemini AI

### `analyze_anatomy_questions(topic, questions)`
- Generates MCQ questions for specified topics
- Customizable question count

### `anatomy_picture_request(image)`
- Processes uploaded anatomical images
- Provides detailed structure analysis

### `stream_data(data)`
- Creates streaming text effect
- Enhances user experience with word-by-word display

## 🎨 User Interface

The app features a clean, medical-themed interface with:
- **Sidebar Controls**: Input fields and upload area
- **Two-Column Layout**: 
  - Left: Topic analysis
  - Right: Question generation and image analysis
- **Streaming Text**: Engaging real-time content display

## 🔒 Security Notes

- API keys are stored in environment variables
- `.env` file is included in `.gitignore`
- No sensitive data is hardcoded

## 🐛 Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure `.env` file exists with correct API key
   - Verify API key is valid and has proper permissions

2. **Import Errors**
   - Install all requirements: `pip install -r requirements.txt`
   - Check Python version compatibility

3. **Image Upload Issues**
   - Ensure uploaded images are in supported formats (PNG, JPG, JPEG)
   - Check image file size

## 📈 Future Enhancements

- Add more anatomy topics and specializations
- Implement user progress tracking
- Include interactive 3D anatomy models
- Add quiz scoring and performance analytics
- Support for multiple languages
