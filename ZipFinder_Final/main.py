import tkinter as tk
from tkinter import filedialog
import subprocess
import time
class ZipcodeApp:
    def __init__(self, master):
        self.master = master
        self.requests_count = 0

        master.title("Zipcode Processing App")

        # Create and set up widgets
        self.input_label = tk.Label(master, text="Choose Input Path:")
        self.input_label.grid(row=0, column=0, padx=10, pady=10)

        self.input_path_entry = tk.Entry(master, width=40)
        self.input_path_entry.grid(row=0, column=1, padx=10, pady=10)

        self.input_browse_button = tk.Button(master, text="Browse", command=self.browse_input_path)
        self.input_browse_button.grid(row=0, column=2, padx=10, pady=10)

        self.output_label = tk.Label(master, text="Choose Output Path:")
        self.output_label.grid(row=1, column=0, padx=10, pady=10)

        self.output_path_entry = tk.Entry(master, width=40)
        self.output_path_entry.grid(row=1, column=1, padx=10, pady=10)

        self.output_browse_button = tk.Button(master, text="Browse", command=self.browse_output_path)
        self.output_browse_button.grid(row=1, column=2, padx=10, pady=10)

        self.submit_button = tk.Button(master, text="Submit", command=self.run_script)
        self.submit_button.grid(row=2, column=1, pady=20)

    def browse_input_path(self):
        path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")])
        self.input_path_entry.delete(0, tk.END)
        self.input_path_entry.insert(0, path)

    def browse_output_path(self):
        path = filedialog.askdirectory()
        self.output_path_entry.delete(0, tk.END)
        self.output_path_entry.insert(0, path)

    def run_script(self):
        input_path = self.input_path_entry.get()
        output_path = self.output_path_entry.get()

        if input_path and output_path:
            script_command = f"py zipradius_v2.py --input_path {input_path} --output_path {output_path}"

            # Check if the number of requests has reached 200
            if self.requests_count >= 200:
                tk.messagebox.showinfo("Info", "Waiting for an hour. Requests limit reached.")
                time.sleep(3600)  # Sleep for one hour (3600 seconds)
                self.requests_count = 0  # Reset the requests count after sleeping

            # Execute the script
            subprocess.run(script_command, shell=True)
            tk.messagebox.showinfo("Success", "Script executed successfully!")

            # Increment the requests count
            self.requests_count += 1

            # Clear input entries after execution
            self.input_path_entry.delete(0, tk.END)
            self.output_path_entry.delete(0, tk.END)
        else:
            tk.messagebox.showwarning("Warning", "Please choose both input and output paths.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ZipcodeApp(root)
    root.mainloop()
