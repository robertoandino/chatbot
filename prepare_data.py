import pandas as pd

# Process the movie lines fine and prepare a dataset
def prepare_data(file_path):
    
    dialogs = []
    
    with open(file_path, 'r', encoding='iso-8859-1') as file:
        
        for line in file: 
            
            parts = line.strip().split("+++$+++")
            
            if len(parts) == 5:
                dialogs.append(parts[4].strip())

    # Pair consecutive lines 
    questions = dialogs[:-1]
    responses = dialogs[1:]
    # Return dataframe with pairs of Qs and As
    return pd.DataFrame({'Question': questions, 'Answer': responses})

# Load and preprocess the dataset
data = prepare_data("movie_lines.txt")
# Save to csv file
data.to_csv("chatbot_data.csv", index=False)