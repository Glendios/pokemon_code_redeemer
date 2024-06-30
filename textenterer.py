import tkinter as tk 
import pyautogui
#import threading
import time 
from tkinter import font

class textboxFollowingCursor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.attributes("-alpha", 0.8)

        self.entry = tk.Entry(self.root, width = 20, fg='white', bg='#ffb6d3', highlightbackground='white', highlightcolor='white', highlightthickness=2)
        self.entry.pack()

        #weight="bold"
        self.font = font.Font(family="Century Gothic", size=20, weight="bold")
        #self.font = font.Font(font=self.entry['font'])
        self.entry.config(font = self.font)

        self.follow_cursor()
        #self.follow_cursor_thread = threading.Thread(target = self.thread_start)
        #self.follow_cursor_thread.daemon = True 
        #self.follow_cursor_thread.start()

    def follow_cursor(self):
        x, y = pyautogui.position()
        self.root.geometry(f"+{x+30}+{y+40}")
        self.root.after(10, self.follow_cursor)
    
    def text_entry(self, text):
        self.entry.delete(0, tk.END)
        self.entry.insert(0,text)
        text_width = self.font.measure(text)

        self.entry.config(width=text_width // self.font.measure('0')+1)
        #self.entry.pack
    
    def kill_self(self):
        self.root.quit()
        self.root.destroy()


class Crosshair:
    def __init__(self, root):

        self.root = root
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-alpha", 0.3)
        self.root.configure(bg='pink')
        self.root.bind("<Button-1>", self.on_click)
        
        self.canvas = tk.Canvas(root, bg='pink', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.update_crosshair()

    def update_crosshair(self):
        self.canvas.delete("all")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x, y = pyautogui.position()

        self.canvas.create_line(0,y,screen_width, y, fill='red', width=2)
        self.canvas.create_line(x,0,x,screen_height, fill='red', width=2)
        self.root.after(1, self.update_crosshair)

    def on_click(self, event):
        global x, y 
        x, y = event.x_root, event.y_root
        if self.root.winfo_exists():
            #self.canvas.delete("all")
            self.root.quit()
            #self.root.destroy()
    
    def get_coordinates(self):
        self.root.mainloop()
        return x, y
    
    def kill_self(self):
        self.root.quit()
        self.root.destroy()

print(f"Click inside the text box for code input.\nThen click the Submit button under it:")

app = textboxFollowingCursor()
app.text_entry("Click inside the Enter code text box for code input.")
temp_root = tk.Tk()
crosshair = Crosshair(temp_root)
enter_coords = crosshair.get_coordinates()
app.text_entry("Now click the red submit code button under it.")
submit_button_coords = crosshair.get_coordinates()
#collect_all_coords = get_coordinates()
app.root.withdraw()
temp_root.withdraw()

print(f"Textbox coords: {enter_coords}")
print(f"Submit button coords: {submit_button_coords}")

def click_paste_10(lines, batch_size=10, start_index=0):
    try:
        pyautogui.click(enter_coords)
        pyautogui.click(enter_coords)
        #for line in lines:
        time.sleep(2)
        for i, line in enumerate(lines[start_index:], start=start_index):
            if i>start_index and (i-start_index)% batch_size == 0:
                input(f"Entered {i} codes. Press Enter to continue.")
            pyautogui.click(enter_coords)
            pyautogui.typewrite(line)
            pyautogui.click(submit_button_coords)
            time.sleep(3)
        print(f"Entered {i+1} codes. Complete.")
            
    except KeyboardInterrupt:
        print("Interrupted by user")

#linecock = ['cockball', 'ballcock']
#click_paste_10(linecock)