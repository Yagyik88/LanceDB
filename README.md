# LanceDB Family Graph

A simple Python project that demonstrates building and visualizing a family graph database using Python.  
This project stores family relationships, and generates an interactive graph that you can view in a browser.

## 🧠 What This Project Does

- Models a **family database** with relationships and people.
- Stores the data under the `family_db/` folder.
- Generates a visual HTML graph (`family_graph.html`) that shows family connections.
- Uses Python scripts inside `lib/` to manage and interact with the database.

This makes it easier to explore and visualize family relationships in an intuitive way.

## 🚀 Features

- Simple CLI-style Python interface for adding and querying family members.
- Automatic graph generation using Python libraries.
- Interactive HTML output that can be opened in a browser.
- A reusable structure that you can extend for more complex relationships.


## 🛠️ How to Run It

1. **Clone the repository**
    ```sh
    git clone https://github.com/Yagyik88/LanceDB.git
    cd LanceDB
    ```

2. **Create and activate a Python virtual environment (optional but recommended)**
    ```sh
    python -m venv venv
    source venv/bin/activate      # Linux / macOS
    venv\Scripts\activate         # Windows
    ```

3. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```
    *(If you don’t have a `requirements.txt`, install needed libraries like networkx, pyvis, etc.)*

4. **Run the main script**
    ```sh
    python family.py
    ```

5. **Open the generated HTML graph**
    ```sh
    open family_graph.html
    ```
    *(Or open it in a browser manually)*

## 🧪 Example Output

After running the program, the `family_graph.html` file will show a visual graph of your family relationships — useful for exploration and demonstration.

## 📁 Extend the Project

- Add support for more relationship types (e.g., aunt, nephew).
- Include export options (PDF, JSON, CSV).
- Add a simple web UI using Flask or FastAPI.

## 🛡️ License

This project is open-source and free to use. Feel free to adapt it to your own needs.

## 🙌 Author

**Yagyik88**  
GitHub: https://github.com/Yagyik88  
