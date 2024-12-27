# Customer Support LangChain

This project provides a simple customer support interface using LangFlow. The interface is built with Streamlit and allows users to interact with a pre-defined LangFlow chart for customer support automation.

## Features

- User-friendly Streamlit interface for chatting with the LangFlow-powered bot.
- Backend integration with Datastax Astra LangFlow API.
- Customizable flow with endpoint management.

## Prerequisites

- Python 3.7+
- A Datastax Astra LangFlow instance with an active flow.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/muhuuh/Customer_support_langchain.git
   cd Customer_support_langchain
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root directory and add your LangFlow Application Token:

   ```env
   APP_TOKEN=<YOUR_APPLICATION_TOKEN>
   ```

## Usage

1. Start the Streamlit application:

   ```bash
   streamlit run main.py
   ```

2. Open your browser and navigate to the Streamlit app URL (usually `http://localhost:8501`).

3. Enter your message in the text area and click the "Runflow" button to interact with the bot.

## Configuration

- The API details are configured in `main.py`. Update the following constants as needed:
  - `BASE_API_URL`
  - `LANGFLOW_ID`
  - `FLOW_ID`
  - `ENDPOINT`

## LangFlow Chart

The LangFlow chart used for this project can be accessed [here](https://astra.datastax.com/langflow/cd78d290-e791-45cd-b74d-b212fe9eb71c/flow/982d4184-8457-46c2-b2e1-ab85051a7446).

## File Structure

- `main.py`: The main application code.
- `requirements.txt`: Python dependencies.
- `.env`: Contains the application token (not included in the repository).

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Built using [Streamlit](https://streamlit.io/).
- Powered by [Datastax Astra LangFlow](https://www.datastax.com/products/datastax-astra).
