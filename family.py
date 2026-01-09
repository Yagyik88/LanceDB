import lancedb
import pandas as pd
from pyvis.network import Network

 
db = lancedb.connect("family_db")
print("Connected to LanceDB")

 
people = pd.DataFrame([
 
    {"person_id": 1, "name": "Paternal_Grandfather", "age": 75},
    {"person_id": 2, "name": "Paternal_Grandmother", "age": 72},
 
    {"person_id": 3, "name": "Father", "age": 45},
    {"person_id": 4, "name": "Paternal_Uncle_2", "age": 43},
    {"person_id": 5, "name": "Paternal_Uncle_3", "age": 41},
    {"person_id": 6, "name": "Paternal_Aunt_1", "age": 39},
    {"person_id": 7, "name": "Paternal_Aunt_2", "age": 37},
    {"person_id": 8, "name": "Paternal_Aunt_3", "age": 35},

    
    {"person_id": 9,  "name": "You", "age": 22},
    {"person_id": 10, "name": "Sibling_1", "age": 20},

    {"person_id": 11, "name": "Cousin_P1", "age": 18},
    {"person_id": 12, "name": "Cousin_P2", "age": 16},

    {"person_id": 13, "name": "Cousin_P3", "age": 19},
    {"person_id": 14, "name": "Cousin_P4", "age": 17},

    {"person_id": 15, "name": "Cousin_P5", "age": 14},
    {"person_id": 16, "name": "Cousin_P6", "age": 12},

    {"person_id": 17, "name": "Cousin_P7", "age": 13},
    {"person_id": 18, "name": "Cousin_P8", "age": 11},

    {"person_id": 19, "name": "Cousin_P9", "age": 10},
    {"person_id": 20, "name": "Cousin_P10", "age": 8},

     
    {"person_id": 21, "name": "Maternal_Grandfather", "age": 73},
    {"person_id": 22, "name": "Maternal_Grandmother", "age": 70},

     
    {"person_id": 23, "name": "Maternal_Uncle_1", "age": 44},
    {"person_id": 24, "name": "Maternal_Uncle_2", "age": 42},
    {"person_id": 25, "name": "Mother", "age": 40},
    {"person_id": 26, "name": "Maternal_Aunt_2", "age": 38},

    
    {"person_id": 27, "name": "Cousin_M1", "age": 15},
    {"person_id": 28, "name": "Cousin_M2", "age": 13},
    {"person_id": 31, "name": "Cousin_M5", "age": 9},
    {"person_id": 32, "name": "Cousin_M6", "age": 7},
])


db.create_table("persons", people, mode="overwrite")
print("Persons (nodes) created")

 
relationships = pd.DataFrame([

    
    {"from_id": 1, "to_id": 3, "relation": "PARENT_OF"},
    {"from_id": 1, "to_id": 4, "relation": "PARENT_OF"},
    {"from_id": 1, "to_id": 5, "relation": "PARENT_OF"},
    {"from_id": 1, "to_id": 6, "relation": "PARENT_OF"},
    {"from_id": 1, "to_id": 7, "relation": "PARENT_OF"},
    {"from_id": 1, "to_id": 8, "relation": "PARENT_OF"},

    {"from_id": 2, "to_id": 3, "relation": "PARENT_OF"},
    {"from_id": 2, "to_id": 4, "relation": "PARENT_OF"},
    {"from_id": 2, "to_id": 5, "relation": "PARENT_OF"},
    {"from_id": 2, "to_id": 6, "relation": "PARENT_OF"},
    {"from_id": 2, "to_id": 7, "relation": "PARENT_OF"},
    {"from_id": 2, "to_id": 8, "relation": "PARENT_OF"},

 
    {"from_id": 3, "to_id": 9, "relation": "PARENT_OF"},
    {"from_id": 3, "to_id": 10, "relation": "PARENT_OF"},

    
    {"from_id": 4, "to_id": 11, "relation": "PARENT_OF"},
    {"from_id": 4, "to_id": 12, "relation": "PARENT_OF"},
    {"from_id": 5, "to_id": 13, "relation": "PARENT_OF"},
    {"from_id": 5, "to_id": 14, "relation": "PARENT_OF"},
    {"from_id": 6, "to_id": 15, "relation": "PARENT_OF"},
    {"from_id": 6, "to_id": 16, "relation": "PARENT_OF"},
    {"from_id": 7, "to_id": 17, "relation": "PARENT_OF"},
    {"from_id": 7, "to_id": 18, "relation": "PARENT_OF"},
    {"from_id": 8, "to_id": 19, "relation": "PARENT_OF"},
    {"from_id": 8, "to_id": 20, "relation": "PARENT_OF"},

      
    {"from_id": 21, "to_id": 23, "relation": "PARENT_OF"},
    {"from_id": 21, "to_id": 24, "relation": "PARENT_OF"},
    {"from_id": 21, "to_id": 25, "relation": "PARENT_OF"},
    {"from_id": 21, "to_id": 26, "relation": "PARENT_OF"},

    {"from_id": 22, "to_id": 23, "relation": "PARENT_OF"},
    {"from_id": 22, "to_id": 24, "relation": "PARENT_OF"},
    {"from_id": 22, "to_id": 25, "relation": "PARENT_OF"},
    {"from_id": 22, "to_id": 26, "relation": "PARENT_OF"},

    
    {"from_id": 23, "to_id": 27, "relation": "PARENT_OF"},
    {"from_id": 24, "to_id": 28, "relation": "PARENT_OF"},
   
     {"from_id": 25, "to_id": 9,  "relation": "PARENT_OF"},  
     {"from_id": 25, "to_id": 10, "relation": "PARENT_OF"},  

    {"from_id": 26, "to_id": 31, "relation": "PARENT_OF"},
    {"from_id": 26, "to_id": 32, "relation": "PARENT_OF"},
    {"from_id": 3, "to_id": 25, "relation": "SPOUSE_OF"},
    {"from_id": 21, "to_id": 22, "relation": "SPOUSE_OF"},
    {"from_id": 1, "to_id": 2, "relation": "SPOUSE_OF"},
    
     
])


db.create_table("relationships", relationships, mode="overwrite")
print("Relationships (edges) created")

 
persons_df = db.open_table("persons").to_pandas()
relations_df = db.open_table("relationships").to_pandas()

 
print("\nChildren of Father:")
children = relations_df[
    (relations_df["from_id"] == 1) &
    (relations_df["relation"] == "PARENT_OF")
]
print(children)

print("\nParents of Daughter:")
parents = relations_df[
    (relations_df["to_id"] == 4) &
    (relations_df["relation"] == "PARENT_OF")
]
print(parents)

print("\nSpouse relationship:")
spouse = relations_df[
    (relations_df["relation"] == "SPOUSE_OF")
]
print(spouse)

#  graph visualization
net = Network(
    height="800px",
    width="100%",
    directed=True,
    bgcolor="#ffffff",
    font_color="black"
)

# Spread graph cleanly
net.repulsion(
    node_distance=300,
    central_gravity=0.15,
    spring_length=300,
    spring_strength=0.03,
    damping=0.09
)

GEN1_COLOR = "#DA68A0"    
GEN2_COLOR = "#4CAF50"  
GEN3_COLOR = "#F4CE14"  
generation_1 = {1, 2, 21, 22}
generation_2 = {3,4,5,6,7,8,23,24,25,26}
generation_3 = set(persons_df["person_id"]) - generation_1 - generation_2

 
for _, row in persons_df.iterrows():
    pid = row["person_id"]

    if pid in generation_1:
        color = GEN1_COLOR
        group = "Grandparents"
    elif pid in generation_2:
        color = GEN2_COLOR
        group = "Parents / Uncles / Aunts"
    else:
        color = GEN3_COLOR
        group = "Children"

    net.add_node(
        pid,
        label=row["name"],
        title=f"{row['name']} | Age: {row['age']} | {group}",
        color=color,
        shape="dot",
        size=25
    )

 
for _, row in relations_df.iterrows():
    edge_color = "gray"
    edge_width = 1

    if row["relation"] == "SPOUSE_OF":
        edge_color = "red"
        edge_width = 3

    net.add_edge(
        row["from_id"],
        row["to_id"],
        label=row["relation"],
        color=edge_color,
        width=edge_width
    )

 
net.write_html("family_graph.html", open_browser=True)


