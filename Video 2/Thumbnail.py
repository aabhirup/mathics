from manim import *
class YoutubeThumbnail(Scene):
    def construct(self):
        self.camera.background_color = ManimColor("#0B0C10")
        top_text = Text(
            "Solving One of the",
            color=ManimColor("#F3D213")
        ).scale(0.5).to_edge(UP, buff=1.2)
        main_hook = Text(
            "The Toughest Question",
            color=ManimColor("#FF2C2C")
        ).scale(1.3).next_to(top_text, DOWN*0.7, buff=0.4)
        exam_text = Text(
            "of JEE Advanced 2022",
            color=ManimColor("#FF2C2C")
        ).scale(1.1).next_to(main_hook, DOWN*0.7, buff=0.3)
        self.add(top_text, main_hook, exam_text)
