# Pizzabot

**Pizzabot** is an application which delivers pizza
to all the houses in a neighbourhood. It receives a size of 
the neighbourhood (**grid**) and **points** representing houses 
in need of pizza delivery and shows a set of instructions 
how to deliver the pizza. The bot accepts the following instructions:
- `E`: Move east
- `W`: Move west
- `N`: Move north
- `S`: Move south
- `D`: Drop pizza

Pizzabot always starts at the origin point (0, 0). 
As with a Cartesian plane, this point lies at the most 
south-westerly point of the grid. After reaching each point 
the bot "drops" the pizza.

For the following description please see the [PDF](ICO-TechTest-20201101-Branding-CodeChallenge-final.pdf).
## Requirements:
Python 3


## How to run:
1. Clone the repo 
2. Open the terminal in the project folder
3. Run the following command:

- For macOS and Linux: `python3 pizzabot.py "args"`
- For Windows: `python pizzabot.py "args"`

Quotation marks are required

### Input
Example of **args**: `"5x5 (1, 3) (4, 4)"`
### Output
`ENNNDEEEND`