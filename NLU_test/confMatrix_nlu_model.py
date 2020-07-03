from sklearn.metrics import confusion_matrix
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

y_true = ["affirm", "affirm", "affirm", "affirm", "affirm", "affirm", "affirm", "affirm", "ask_for_story",
          "ask_for_story",  "ask_for_story", "ask_for_story", "ask_for_story", "ask_for_story", "ask_for_story",
          "ask_for_story", "greet", "greet", "greet", "greet", "greet", "greet", "greet", "greet", "thanks", "thanks",
          "thanks", "thanks", "thanks", "thanks", "thanks", "thanks", "comment", "comment", "comment", "comment",
          "comment", "comment", "comment", "comment", "exclaim_pos", "exclaim_pos", "exclaim_pos", "exclaim_pos",
          "exclaim_pos", "exclaim_pos", "exclaim_pos", "exclaim_pos", "exclaim_neg", "exclaim_neg", "exclaim_neg",
          "exclaim_neg", "exclaim_neg", "exclaim_neg", "exclaim_neg", "exclaim_neg", "request_increment",
          "request_increment", "request_increment", "request_increment", "request_increment", "request_increment",
          "request_increment", "request_increment", "ynq", "ynq", "ynq", "ynq", "ynq", "ynq", "ynq", "ynq", "whq",
          "whq", "whq", "whq", "whq", "whq", "whq", "whq", "goodbye", "goodbye", "goodbye", "goodbye", "goodbye",
          "goodbye", "goodbye", "goodbye"]
y_pred = ["affirm", "comment", "affirm", "affirm", "affirm", "affirm", "affirm", "affirm",  "ask_for_story",
          "ask_for_story", "ask_for_story", "ask_for_story", "ask_for_story", "ask_for_story", "ask_for_story",
          "ask_for_story", "greet", "greet", "greet", "greet", "greet", "greet", "whq", "greet", "thanks", "thanks",
          "thanks", "thanks", "thanks", "thanks", "thanks", "thanks", "comment", "comment", "comment", "ynq", "comment",
          "comment", "comment", "request_increment", "exclaim_pos", "exclaim_pos", "exclaim_pos", "exclaim_pos",
          "affirm", "exclaim_pos", "exclaim_pos", "exclaim_pos", "exclaim_neg", "exclaim_neg", "comment", "exclaim_neg",
          "exclaim_neg", "exclaim_neg", "exclaim_neg", "exclaim_neg", "request_increment", "request_increment",
          "request_increment", "request_increment", "request_increment", "request_increment", "request_increment",
          "request_increment", "ynq", "goodbye", "ynq", "whq", "ynq", "ynq", "exclaim_neg", "whq", "whq", "whq", "whq",
          "whq", "whq", "whq", "whq", "whq", "goodbye", "goodbye", "goodbye", "goodbye", "goodbye", "goodbye",
          "goodbye", "goodbye"]
array = confusion_matrix(y_true, y_pred, normalize='true')
df_cm = pd.DataFrame(array, index=[i for i in ["affirm", "ask_for_story", "greet", "thanks", "comment", "exclaim_pos", "exclaim_neg", "request_increment", "ynq", "whq", "goodbye"]],
                     columns=[i for i in ["affirm", "ask_for_story", "greet", "thanks", "comment", "exclaim_pos", "exclaim_neg", "request_increment", "ynq", "whq", "goodbye"]])
plt.figure(figsize=(10, 7))
sn.heatmap(df_cm, annot=True)
plt.show()

