import tkinter as tk
from graphviz import Digraph
import graphviz as gv

sampleData = [{'id': 1, 'parentId': None},
        {'id': 2, 'parentId': 1},
        {'id': 3, 'parentId': 1},
        {'id': 4, 'parentId': 2},
        {'id': 5, 'parentId': 2},
        {'id': 6, 'parentId': 3},
        {'id': 7, 'parentId': 3},
        ]

def check_parent_id_list(data_list, value):
    flag = False
    if value == '':
        return False
    for d in data_list:
        if d.get('id') == int(value):
            flag = True
    return flag
            

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("ADDIING NODE")
        master.geometry("800x600")

        # Create the input label and field
        self.input_label = tk.Label(master, text="Enter ParentNodeId:")
        self.input_label.pack()

        self.input_field = tk.Entry(master)
        self.input_field.pack()

        # Create the plot button
        plot_button = tk.Button(master, text="Plot Graph", command=self.add_node)
        plot_button.pack()

        # Create the Digraph frame 
        self.image_Label = tk.Label(master)
        self.image_Label.pack()
        self.plot_graph()

    def add_node(self):
        pid = self.input_field.get()
        print(check_parent_id_list(sampleData, pid))
        if(check_parent_id_list(sampleData, pid)):
            sampleData.append({'id':len(sampleData)+1, 'parentId':pid})
            self.input_label.config(text="Success")
            self.plot_graph()
        else:
            self.input_label.config(text="Wrong Input")

    def plot_graph(self):
        self.image_Label.config(image=None)
        # create Digraph object
        dot = Digraph()
        # add nodes to Digraph object
        for node in sampleData:
            node_id = str(node['id'])
            dot.node(node_id)
        # add edges to Digraph object
        for node in sampleData:
            node_id = str(node['id'])
            parent_id = str(node['parentId'])
            if parent_id != 'None':
                dot.edge(parent_id, node_id)
        # render Digraph object
        img = gv.Source(dot.source).pipe(format='png')
        image = tk.PhotoImage(data=img)
        self.image_Label.config(image=image)
        self.image_Label.image = image


if __name__ == '__main__':
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
