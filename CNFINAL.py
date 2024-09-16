import tkinter as tk
from tkinter import Canvas, messagebox
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from end_credits import create_end_credits

class SelectiveRepeatSimulation:
    def __init__(self, window, total_packets):
        self.window = window
        self.total_packets = total_packets
        self.window.title("Selective Repeat Simulation") 
        self.canvas = Canvas(window, width=500, height=600, bg="purple")
        self.canvas.pack()

        self.sender_base_y = 50
        self.receiver_base_y = 500
        self.packet_spacing = 50

        self.sender_packets = []
        self.receiver_packets = []
        self.animations = []
        self.packet_states = ["red"] * self.total_packets  
        self.window_size = 5
        self.sender_pointer = 0
        faulty_packet = 7

        self.init_packets()
        self.init_animation()


    def init_packets(self):
        for i in range(self.total_packets):
            sender_packet = self.canvas.create_rectangle(
                50, self.sender_base_y + i * self.packet_spacing,
                100, self.sender_base_y + (i + 1) * self.packet_spacing,
                fill=self.packet_states[i]
            )
            receiver_packet = self.canvas.create_rectangle(
                150, self.receiver_base_y - (i + 1) * self.packet_spacing,
                200, self.receiver_base_y - i * self.packet_spacing,
                fill="red", outline="black"
            )
            self.sender_packets.append(sender_packet)
            self.receiver_packets.append(receiver_packet)

            self.canvas.create_text(
                75, self.sender_base_y + i * self.packet_spacing + 25,
                text=f"S{i+1}", fill="black"
            )
            self.canvas.create_text(
                175, self.receiver_base_y - i * self.packet_spacing - 25,
                text=f"S{i+1}", fill="black"
            )

    def init_animation(self):
        for i in range(self.total_packets):
            animation_obj = self.canvas.create_line(
                100, self.sender_base_y + i * self.packet_spacing + 25,
                150, self.receiver_base_y - i * self.packet_spacing - 25,
                arrow=tk.LAST, fill="black"
            )
            self.animations.append(animation_obj)


    def animate(self, step):
        faulty_packet = 8
        if step >= 5:
            for i in range(5):
                self.canvas.itemconfig(self.sender_packets[i], outline="black", width=6)
            for i in range(5, 10):
                self.canvas.itemconfig(self.sender_packets[i],outline="white", width=6)
        if step < self.total_packets:
            self.packet_states[step] = "lightgreen"
            self.canvas.itemconfig(self.sender_packets[step], fill="lightgreen", outline="white", width=6)
            self.canvas.itemconfig(self.animations[step], arrow=tk.LAST, fill="lightgreen")
            if step != faulty_packet:
                self.canvas.itemconfig(self.receiver_packets[step], fill="lightgreen")
                msg = " Acknowledgement: " + str(step + 1) + " packet received"
                messagebox.showinfo("Receiver", msg)
        elif step == self.total_packets:
            self.packet_states[3] = "red"
            self.canvas.itemconfig(self.sender_packets[faulty_packet], fill="red")
            self.canvas.itemconfig(self.animations[faulty_packet], arrow=tk.LAST, fill="red")
            self.canvas.itemconfig(self.receiver_packets[faulty_packet], fill="red")
        if step >= self.total_packets + 1:
            temp = "Resending " + str(faulty_packet + 1) + " th..."
            messagebox.showinfo("Sender ", temp)
            self.packet_states[3] = "lightgreen"
            self.canvas.itemconfig(self.sender_packets[faulty_packet], fill="lightgreen")
            self.canvas.itemconfig(self.animations[faulty_packet], arrow=tk.LAST, fill="lightgreen")
            self.canvas.itemconfig(self.receiver_packets[faulty_packet], fill="lightgreen")
            messagebox.showinfo("Receiver", "All packets received.")

            self.window.destroy()

def animate_simulation(simulation, total_steps):
    def update(frame):
        simulation.animate(frame)

    ani = animation.FuncAnimation(
        plt.figure(),
        update,
        frames=total_steps,
        repeat=False,
        interval=1000,
        blit=False
    )

    plt.show()

def main():
    root = tk.Tk()
    total_packets = 10
    simulation = SelectiveRepeatSimulation(root, total_packets)
    total_steps =  total_packets + 2

    def network_guru_intro():
        message = (
            "🌟🌈 Welcome to the World of Selective Repeat! 🌈🌟\n\n"
            "Hello! I am the Network Guru, here to guide you through the wonders of Selective Repeat.\n\n"
            "Selective Repeat is a brilliant technique used in computer networks. It lets us transmit only the lost or corrupted packets, avoiding resending Entire Frame, "
            "making our communication efficient and magical.\n\n"
            "🚀 Click 'OK' to start the simulation and witness the magic unfold! 🚀"
        )
        messagebox.showinfo("Network Guru", message)

    network_guru_intro()

    def start_simulation():
        animate_simulation(simulation, total_steps)

    start_button = tk.Button(root, text="Start Simulation", command=start_simulation, bg="green", fg="white", font=("Helvetica", 14, "bold"))
    start_button.pack(pady=20)

    root.mainloop()
    end()
def end():
    root = tk.Tk()
    root.title("Main Window")
    canvas = tk.Canvas(root, width=800, height=600, bg="blue")
    canvas.pack()
    create_end_credits(canvas)
    root.mainloop()
if __name__ == "__main__":
    main()
