"""
WebP Converter GUI
github @foiegreis
2024
"""

import customtkinter
from customtkinter import filedialog
import cv2


class App:
    def __init__(self):
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("dark-blue")

        self.root = customtkinter.CTk()
        self.root.geometry("650x350")

        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        label_title = customtkinter.CTkLabel(master=self.frame, text="WEBP CONVERTER",
                                             font=("Roboto",20))
        label_title.grid(column=0, row=0, pady=5, padx=5, sticky='e')

    def file_uploader(self, row, text, command):
        """File uploader"""
        label = customtkinter.CTkLabel(master=self.frame, text=f"{text}: ", font=("Roboto", 13))
        label.grid(column=0, row=row, pady=2, padx=10, sticky='w')
        label_entry = customtkinter.CTkLabel(master=self.frame, text="File", font=("Roboto", 13),
                                             bg_color='white', fg_color='white',
                                             corner_radius=50, width=200,
                                             height=20)
        label_entry.grid(column=1, row=row, pady=2, padx=2)
        button = customtkinter.CTkButton(master=self.frame, text="Upload", command=command)
        button.grid(column=3, row=row, pady=2, padx=2)


class webpConverter(App):
    def __init__(self):
        super().__init__()
        self.file_path = None

        self.build_gui()
        self.root.mainloop()

    def build_gui(self):
        """Build gui"""
        self.file_uploader(1, "Select Image to Convert", lambda idx=1: self.upload_file(idx))
        convert_button = customtkinter.CTkButton(master=self.frame, text="Convert", command=self.convert)
        convert_button.grid(column=1, row=4, pady=10, padx=2)

    def upload_file(self, idx):
        """Upload file function"""
        # Open a file dialog for file selection
        self.file_path = filedialog.askopenfilename()
        print(self.file_path)

        # Update the corresponding label with the selected file path

        file_entry = customtkinter.CTkLabel(master=self.frame, text=f"{self.file_path.split('/')[-1]}",
                                       font=("Roboto", 13),
                                       bg_color='white', fg_color='white',
                                       corner_radius=50, width=200,
                                       height=20)
        file_entry.grid(column=1, row=idx, pady=2, padx=2)

    def reset(self):
        # delete textbox
        self.feedback_textbox.destroy()

        # delete new upload/retry button
        self.retry_button.destroy()

        # clear upload field
        file_entry = customtkinter.CTkLabel(master=self.frame, text="",
                                            font=("Roboto", 13),
                                            bg_color='white', fg_color='white',
                                            corner_radius=50, width=200,
                                            height=20)
        file_entry.grid(column=1, row=1, pady=2, padx=2)

        # clear filepath
        self.file_path = None

    def convert(self):
        """Converts to webp """

        if not self.file_path:
            self.feedback_textbox = customtkinter.CTkTextbox(master=self.frame, width=200, height=100, corner_radius=0,
                                               activate_scrollbars=True)
            self.feedback_textbox.grid(row=5, column=1, pady=10)
            self.feedback_textbox.insert("1.0", text="No image loaded. Please load an image first.")
            self.retry_button = customtkinter.CTkButton(master=self.frame, text="Retry", command=self.reset)
            self.retry_button.grid(row=7, column=1, pady=10, padx=2)

        else:
            if self.file_path:
                # Read the image using OpenCV
                img = cv2.imread(self.file_path)
                if img is not None:
                    # Convert and save the image in WebP format
                    webp_path = self.file_path.rsplit('.', 1)[0] + '.webp'
                    quality = 1 # TODO add quality seleector
                    cv2.imwrite(webp_path, img, [cv2.IMWRITE_WEBP_QUALITY, quality])

                    cv2.imwrite(webp_path, img)
                    self.feedback_textbox = customtkinter.CTkTextbox(master=self.frame, width=200, height=100, corner_radius=0,
                                                       activate_scrollbars=True)
                    self.feedback_textbox.grid(row=5, column=1, pady=10)
                    self.feedback_textbox.insert("1.0", text=f"Conversion successful. File saved as: {webp_path}")

                    self.retry_button = customtkinter.CTkButton(master=self.frame, text="Convert another image", command=self.reset)
                    self.retry_button.grid(row=7, column=1, pady=10, padx=2)
                else:
                    self.feedback_textbox = customtkinter.CTkTextbox(master=self.frame, width=200, height=100, corner_radius=0,
                                                       activate_scrollbars=True)
                    self.feedback_textbox.grid(row=5, column=1, pady=10)
                    self.feedback_textbox.insert("1.0", text=f"Failed to load Image. Make sure the path is correct.")

                    self.retry_button = customtkinter.CTkButton(master=self.frame, text="Retry", command=self.reset)
                    self.retry_button.grid(row=7, column=1, pady=10, padx=2)


if __name__ == '__main__':
    myapp = webpConverter()
