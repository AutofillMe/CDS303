## Black Box Diagram
```mermaid
flowchart LR
    id1(Punctuation Frequency,\nCapital Symbols/Not Capital)
    id2(Frequency of Key Phrases,\n Frequency of most common Keywords)
    id3(Hyperlink Statistics)
    id5(Sentiment: Positive or Negative)
    subgraph sb [Black Box]
        direction LR
        id4{{\n\Logistic Regression\n\n\n}}        
    end
    id1 --> id4
    id2 --> id4
    id3 --> id4
    id5 --> id4
    id4 --> id8((Output:\n Phishing/Spam or Safe))
```
