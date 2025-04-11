import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSlider, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor


class FontAdjusterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Week 6")
        self.setGeometry(100, 100, 600, 400)

        # Set background pink
        self.setStyleSheet("background-color: #ffe6f0;")  

        # --- Label untuk menampilkan NIM ---
        self.label = QLabel("F1D022110", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 30))
        self.label.setStyleSheet("background-color: white; color: black;") 

        # --- Penanda Tugas ---
        self.signature = QLabel("Nama: Ameylia Intan Zurtika Ayu | NIM: F1D022110")
        self.signature.setAlignment(Qt.AlignCenter)
        self.signature.setStyleSheet("font-size: 16px;")

        # --- Sliders ---
        self.font_slider = QSlider(Qt.Horizontal)
        self.font_slider.setMinimum(20)
        self.font_slider.setMaximum(60)
        self.font_slider.setValue(30)
        self.font_slider.setTickPosition(QSlider.TicksBelow)
        self.font_slider.setTickInterval(5)
        self.font_slider.valueChanged.connect(self.update_font_size)

        self.font_color_slider = QSlider(Qt.Horizontal)
        self.font_color_slider.setMinimum(0)
        self.font_color_slider.setMaximum(255)
        self.font_color_slider.setValue(0)
        self.font_color_slider.valueChanged.connect(self.update_colors)

        self.bg_color_slider = QSlider(Qt.Horizontal)
        self.bg_color_slider.setMinimum(0)
        self.bg_color_slider.setMaximum(255)
        self.bg_color_slider.setValue(255)
        self.bg_color_slider.valueChanged.connect(self.update_colors)

        # --- Layout ---
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        layout.addWidget(QLabel("Font Size"))
        layout.addWidget(self.font_slider)

        layout.addWidget(QLabel("Font Color"))
        layout.addWidget(self.font_color_slider)

        layout.addWidget(QLabel("Background Color"))
        layout.addWidget(self.bg_color_slider)

        layout.addWidget(self.signature)

        self.setLayout(layout)
        self.update_colors()

    def update_font_size(self):
        size = self.font_slider.value()
        current_font = self.label.font()
        current_font.setPointSize(size)
        self.label.setFont(current_font)

    def update_colors(self):
        font_val = self.font_color_slider.value()
        bg_val = self.bg_color_slider.value()

        font_color = f"rgb({font_val}, {font_val}, {font_val})"
        bg_color = f"rgb({bg_val}, {bg_val}, {bg_val})"

        self.label.setStyleSheet(
            f"color: {font_color}; background-color: {bg_color}; border-radius: 8px; padding: 8px;"
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FontAdjusterApp()
    window.show()
    sys.exit(app.exec_())
