# Specify the path to the CSV file
import pandas as pd
import panel as pn

file_name = "./data.csv"

# Read the CSV file into a DataFrame and drop the 'id' column
data = pd.read_csv(file_name).drop(columns=["id"])

# Create a Plotly pane for interactive plotting
plot_pane = pn.pane.Plotly(sizing_mode="stretch_width")

# Initialize a FileInput widget for uploading files
file_input = pn.widgets.FileInput()

# Initialize a TextInput widget for user questions
text_input = pn.widgets.TextInput(
    name="Question",
    placeholder="Ask a question from the CSV",
    sizing_mode="scale_width",
)

# Initialize a Button widget labeled 'Ask' for submitting questions
ask_button = pn.widgets.Button(name="Ask", button_type="primary", height=60)

# Initialize a Button widget labeled 'Load' for loading data
load_button = pn.widgets.Button(name="Load", button_type="primary")

# Initialize a Button widget labeled 'Plot' for generating plots
plot_button = pn.widgets.Button(name="Plot", button_type="primary")

# Initialize a ChatBox widget to display messages
chat_box = pn.widgets.ChatInterface(
    value=[],  # Initialize with an empty message list
    message_hue=220,  # Set the hue for message background color
    ascending=True,  # Display messages in ascending order
    allow_input=False,  # Disable user input in the chat box
)

# Display the FileInput widget to allow users to upload a file
file_input
