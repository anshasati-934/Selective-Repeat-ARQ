import tkinter as tk

def create_end_credits(canvas):
    text = [
        "Thank You",
        "",
        "",
        "A Project By:",
        "",
        "Ansh Asati"
        # Add more names or credits as needed
    ]

    y_position = 600
    text_objects = []

    for index, line in enumerate(text):
        font_size = 40 if index == 0 else 14  # Larger font size for "Thank You"
        text_object = canvas.create_text(
            400, y_position, text=line, font=("Helvetica", font_size), fill="white"
        )
        text_objects.append(text_object)
        y_position += 20

    animate_credits(canvas, text_objects)

def animate_credits(canvas, text_objects):
    for _ in range(150):
        for text_object in text_objects:
            canvas.move(text_object, 0, -3)
        canvas.update()
        canvas.after(15)

def main():
    root = tk.Tk()
    root.title("End Credits")

    canvas = tk.Canvas(root, width=800, height=600, bg="navy blue")
    canvas.pack()

    create_end_credits(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()
