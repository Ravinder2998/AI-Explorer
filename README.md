# AI Travel Planner (Gemini Version) ✈

## Overview
AI Travel Planner is a smart trip-planning application that generates personalized itineraries based on your destination, travel style, budget, and interests. It uses AI (simulated Gemini API) and web search (DuckDuckGo) to provide relevant travel suggestions.

## Features 🚀
- 🔍 **Live Web Search:** Fetches real-time travel details from DuckDuckGo.
- 🏝 **Personalized Itineraries:** Plans trips based on user preferences.
- 🎭 **Multiple Travel Styles:** Adventure, Relaxation, Cultural, Food & Wine, Business.
- 💰 **Budget Flexibility:** Economy, Standard, Luxury.
- 🎯 **Interest-Based Planning:** Museums, Outdoor Activities, Historical Sites, Shopping, Nightlife, Local Cuisine.

## Installation 🛠
### Prerequisites
Ensure you have Python installed. You also need the following libraries:
```bash
pip install streamlit dotenv duckduckgo-search
```

### Clone the Repository
```bash
git clone https://github.com/your-username/AI-Travel-Planner.git
cd AI-Travel-Planner
```

### Setup Environment Variables
Create a `.env` file in the project root and add:
```env
GEMINI_API_KEY=your_api_key_here
```

## Usage 🏃‍♂️
Run the Streamlit app:
```bash
streamlit run app.py
```
Enter a destination, select your preferences, and generate your travel plan!

## Project Structure 📁
```
├── app.py              # Main Streamlit application
├── requirements.txt    # Dependencies
├── README.md           # Project documentation
├── .env                # Environment variables
```

## Future Enhancements 🔮
- 🌍 **Integrate real Gemini AI API** for more dynamic recommendations.
- 📅 **Add a calendar view** for itinerary visualization.
- 📍 **Include Google Maps integration** for route planning.

## Contributing 🤝
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push and create a pull request.

## License 📜
This project is licensed under the MIT License. See `LICENSE` for details.

## Contact 📬
For any issues, feel free to reach out via [GitHub Issues](https://github.com/your-username/AI-Travel-Planner/issues).

