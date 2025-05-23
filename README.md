## 📄 PDF/CSV/XML File Reader & JSON Converter Bot (CrewAI)

This Python project uses [CrewAI](https://github.com/joaomdmoura/crewAI) to automate the process of reading structured/unstructured data from files (PDF, CSV, XML, or plain text) and converting that information into a standardized `.json` format. It's a practical tool for extracting and transforming file content using autonomous agents with LLM support.

### 🧠 What It Does

* **Step 1: User Input**

  * You provide a file path (PDF, CSV, XML, or plain text) as input.

* **Step 2: Data Extraction Agent**

  * A `retrieval_agent` reads the input file using the appropriate CrewAI tools (`PDFSearchTool`, `CSVSearchTool`, `XMLSearchTool`, or `FileReadTool`).

* **Step 3: Conversion Agent**

  * A `converter_agent` receives the extracted content as context and transforms it into a `.json` file using a predefined format (based on a sample file).

* **Step 4: Output**

  * The final JSON data is printed or saved to the working directory.

---

### 🛠️ Components

#### `main.py`

* Initializes the environment using `dotenv`.
* Accepts the input file path from the user.
* Creates agents and tasks using `FileAgents` and `ReadingTasks`.
* Runs the Crew using `crew.kickoff()`.

#### `tasks.py`

Defines two main tasks using CrewAI's `Task` class:

* `reading_task`: Reads all content from the input file.
* `data_conversion_task`: Converts the content to JSON format based on a sample structure.

#### `agents.py` *(Assumed file, not shown above)*

Defines agent behavior for:

* **Data Retrieval Agent**: Handles file reading using the appropriate tools.
* **Data Converter Agent**: Converts extracted text into structured JSON.

#### `tools.py`

Defines tools for handling different file types:

* `PDFSearchTool`
* `CSVSearchTool`
* `XMLSearchTool`
* `FileReadTool`

Each tool uses:

* **LLM** (`llama3` via `ollama`) to process and understand content.
* **Embeddings** (`google` model) for semantic document understanding.

---

### ✅ How to Use

```bash
pip install -r requirements.txt
python main.py
```

Then input the full path to your file when prompted.

---

### 📁 Sample JSON Format

A sample JSON file path is hardcoded in `tasks.py` (`sample1.json`) and used to guide the formatting of the output.

---

### 📌 Requirements

* Python 3.8+
* `.env` file with required API keys (if using OpenAI or Google)
* `crewAI`, `langchain`, `ollama`, etc.


