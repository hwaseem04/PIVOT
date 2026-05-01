from manim import *
from pydub import AudioSegment
import textwrap
from moviepy.editor import VideoFileClip
class Math_visual(Scene):
    def __init__(self, plan=None):
        super().__init__()
        self.plan = plan
    def construct(self):
        # Title for the formula
        if "scenario" in self.plan:
            title = Text(self.plan["scenario"], font_size=36).to_edge(UP)
            self.play(FadeIn(title))

        col_width   = config.frame_width / 3
        col_center  = RIGHT * (config.frame_width / 3)

        wrapped_lines = textwrap.fill(self.plan["audio_content"], width=20).splitlines()

        ruler = Text("A"*20, font_size=80)
        for font in range(80, 9, -2):
            ruler.font_size = font
            if ruler.width <= col_width - 0.4:
                break
        optimal_font = font

        paragraph = Paragraph(
            *wrapped_lines,           
            font_size=optimal_font,
            line_spacing=1.3,
            alignment="center"
        )

        paragraph.move_to(col_center)

        self.play(FadeIn(paragraph))
    
        self.animate()

    def animate(self):
        # Create axes for complexity visualization
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 100, 10],
            x_length=6,
            y_length=6,
            axis_config={"include_tip": True}
        ).to_edge(DOWN, buff=0.5)
    
        # Define complexity functions: O(N^2) and O(N)
        n_squared = axes.plot(lambda x: x**2, x_range=[0, 9.5], color=RED)
        n_linear = axes.plot(lambda x: 8*x, x_range=[0, 10], color=GREEN)
    
        # Labels for the curves positioned using coordinate-to-point mapping
        n_squared_label = MathTex("O(N^2)", color=RED).scale(0.6).move_to(axes.c2p(7, 85))
        n_linear_label = MathTex("O(N)", color=GREEN).scale(0.6).move_to(axes.c2p(9, 55))
    
        # Contextual labels for the graph using standard axis label methods
        title = Tex("Computational Complexity Analysis").to_edge(UP)
        x_label = axes.get_x_axis_label(MathTex("N"))
        y_label = axes.get_y_axis_label(MathTex("T(N)"))
    
        # Animation sequence
        self.play(Create(axes), Write(title))
        self.play(Write(x_label), Write(y_label))
        
        # Show growth of O(N^2) - Quadratic complexity
        self.play(Create(n_squared), Write(n_squared_label))
        
        # Show growth of O(N) - Linear complexity
        self.play(Create(n_linear), Write(n_linear_label))
    
        # Highlight the Efficiency Gap at N=9
        p_top = axes.c2p(9, 81)
        p_bottom = axes.c2p(9, 72)
        indicator_line = DashedLine(start=p_bottom, end=p_top, color=YELLOW)
        gap_text = Tex("Efficiency Gap", color=YELLOW).scale(0.5).next_to(indicator_line, RIGHT)
        
        self.play(Create(indicator_line), Write(gap_text))
        self.wait(5)



# Main rendering function that returns the video
def render_video(dir, plan):
    config.media_dir = dir  # Set media directory
    config.output_file = "scene.mp4"  # Set output file name
    scene = Math_visual(plan)  # Create scene
    scene.render()  # Render the video
    return config.output_file  # Return the generated video file path

    
