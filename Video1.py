"""
video1.py
=========
Manim animation: Finding the value of 'a' where the tangent to C2 at point A
meets C1 at point B, given the curves C1: y = x² - 3 and C2: y = kx².

Usage
-----
    manim -pql video1.py video1        # low quality preview
    manim -pqh video1.py video1        # high quality render

Dependencies
------------
    pip install manim
"""

from manim import *


class video1(Scene):
    """
    Full worked solution for the following problem:

    The curves C1: y = x² - 3 and C2: y = kx² (k < 1) intersect at two points.
    The tangent to C2 at point A = (a, y₁), with a > 0, meets C1 at B(1, y₂)
    where y₁ ≠ y₂. Find the value of a.

    Answer: a = 3
    """

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _build_axes(self) -> Axes:
        return (
            Axes(
                x_range=[-5, 5, 1],
                y_range=[-7, 9, 1],
                x_length=6,
                y_length=5,
            )
            .shift(UP * 0.5)
            .scale(1.2)
        )

    def _build_solution_steps(self) -> tuple:
        """Return individual solution-step Tex objects and the assembled VGroup."""
        sol0 = Tex(r"$C_1: y = x^2 - 3, \quad C_2: y = kx^2$").scale(0.65)
        sol2 = Tex(r"Slope at $C_2: y = kx^2 \Rightarrow \frac{dy}{dx} = 2kx$").scale(0.65)
        sol3 = Tex(r"Slope at $A(a,\, ka^2) = 2ka$").scale(0.65)
        sol4 = Tex(r"$\frac{y - y_1}{x - a} = \frac{y - ka^2}{x - a} = 2ka$").scale(0.65)
        sol5 = Tex(r"$\Rightarrow y = 2kax - ka^2$").scale(0.65)

        sol6_label = Tex(r"$A$ satisfies $C_1$ \& $C_2$:").scale(0.65)
        c1_eq = Tex(r"$\overset{C_1}{a^2 - 3}$", color=YELLOW).scale(0.65)
        c2_eq = Tex(r"$= \overset{C_2}{ka^2}$", color=BLUE).scale(0.65)
        sol6_eq = VGroup(c1_eq, c2_eq).arrange(RIGHT, buff=0.1)
        sol6_full = VGroup(sol6_label, sol6_eq).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        sol7 = Tex(r"$\Rightarrow k = \frac{a^2 - 3}{a^2}$").scale(0.65)
        sol8 = Tex(r"Sub into tangent eq: $a^3 - 2a^2 - 5a + 6 = 0$").scale(0.65)
        sol9 = Tex(r"$(a - 1)(a - 3)(a + 2) = 0$").scale(0.65)

        steps = [sol0, sol2, sol3, sol4, sol5, sol6_full, sol7, sol8, sol9]

        solution = VGroup(*steps)
        solution.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        solution.to_edge(LEFT).shift(RIGHT * 0.4)

        return steps, solution

    def _build_root_checks(self) -> tuple:
        """Return per-root VGroups and the assembled full-check VGroup."""
        roots_title = Tex(r"\underline{Checking all roots:}", color=YELLOW).scale(0.8)

        # a = 1 (rejected: y₁ = y₂)
        r1_head  = Tex(r"$a = 1$", color=RED).scale(0.75)
        r1_line1 = Tex(r"Tangent at $A$: $y = 2kax - ka^2$").scale(0.6)
        r1_line2 = Tex(r"At $A(1, y_1) \Rightarrow y_1 = 2k(1) - k(1)^2 = k$").scale(0.6)
        r1_line3 = Tex(r"At $B(1, y_2) \Rightarrow y_2 = 2k(1) - k(1)^2 = k$").scale(0.6)
        r1_line4 = Tex(r"So $y_1 = y_2 = k$").scale(0.6)
        r1_line5 = Tex(r"BUT question states $y_1 \neq y_2$").scale(0.6).set_color(YELLOW)
        r1_cross = Tex(r"$\therefore a \neq 1$", color=RED).scale(0.7)
        r1_lines = [r1_line1, r1_line2, r1_line3, r1_line4, r1_line5]
        r1 = VGroup(r1_head, *r1_lines, r1_cross).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        # a = -2 (rejected: a > 0)
        r2_head  = Tex(r"$a = -2$", color=RED).scale(0.75)
        r2_line1 = Tex(r"$a > 0$ is given").scale(0.6)
        r2_line2 = Tex(r"$a = -2 < 0$").scale(0.6)
        r2_cross = Tex(r"$\therefore a = -2$ rejected $\times$", color=RED).scale(0.7)
        r2_lines = [r2_line1, r2_line2]
        r2 = VGroup(r2_head, *r2_lines, r2_cross).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        # a = 3 (accepted)
        r3_head  = Tex(r"$a = 3$", color=GREEN).scale(0.75)
        r3_line1 = Tex(r"$a = 3 > 0$ \checkmark").scale(0.6)
        r3_line2 = Tex(r"$A = (3,\ 2.7)$").scale(0.6)
        r3_line3 = Tex(r"$B = (1,\ -2)$").scale(0.6)
        r3_line4 = Tex(r"$y_1 = 2.7 \neq y_2 = -2$ \checkmark").scale(0.6)
        r3_tick  = Tex(r"$\therefore \boxed{a = 3}$", color=GREEN).scale(0.75)
        r3_lines = [r3_line1, r3_line2, r3_line3, r3_line4]
        r3 = VGroup(r3_head, *r3_lines, r3_tick).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        all_roots  = VGroup(r1, r2, r3).arrange(RIGHT, aligned_edge=UP, buff=0.6)
        full_check = VGroup(roots_title, all_roots).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        full_check.center()

        return (
            roots_title,
            r1_head, r1_lines, r1_cross,
            r2_head, r2_lines, r2_cross,
            r3_head, r3_lines, r3_tick,
            full_check,
        )

    def _build_credits(self) -> tuple:
        made_with   = Tex(r"made with", color=GRAY).scale(0.5)
        manim_title = Tex(r"Manim Community Edition", color=WHITE).scale(1.2)
        divider     = Line(LEFT * 3, RIGHT * 3, color=GRAY, stroke_width=0.8)
        open_source = Tex(
            r"an open source project by the manim community", color=GRAY
        ).scale(0.48)
        thank_you = Tex(
            r"thank you to every contributor who made mathematical animation"
            r" accessible to everyone",
            color=GRAY,
        ).scale(0.48)
        github_line = Tex(
            r"link to the source code of this video is on my github", color=GRAY
        ).scale(0.48)

        credits_group = VGroup(
            made_with, manim_title, divider, open_source, thank_you, github_line
        ).arrange(DOWN, buff=0.3)
        credits_group.center()

        return made_with, manim_title, divider, open_source, thank_you, github_line, credits_group

    # ------------------------------------------------------------------
    # Main construct
    # ------------------------------------------------------------------

    def construct(self):
        # ── Build all objects ─────────────────────────────────────────────────
        axes = self._build_axes()

        c1 = axes.plot(lambda x: x**2 - 3, color=YELLOW, x_range=[-3, 3])
        c2 = axes.plot(lambda x: 0.3 * x**2, color=BLUE)

        dot  = Dot(axes.coords_to_point(-2.07, 1.28571), color=RED)
        dot1 = Dot(axes.coords_to_point( 2.07, 1.28571), color=RED)
        dot2 = Dot(axes.coords_to_point( 1,   -2),       color=RED)

        label    = Tex(r"A $(a,\,y_1)$").next_to(dot,  RIGHT, buff=-0.3).scale(0.5)
        label2   = Tex(r"B $(1,\,y_2)$").next_to(dot2, DOWN).scale(0.5)
        c1_label = Tex(r"$C_1$").next_to(c1, UL, buff=0.2)
        c2_label = Tex(r"$C_2$").next_to(c2, UL, buff=0.2)

        math = Tex(
            r"The curves $C_1: y = x^2 - 3$ and $C_2: y = kx^2$, $k < 1$, intersect each other\\"
            r"at two points. The tangent to\\"
            r"$C_2$ at point $A = (a,\,y_1)$, $a > 0$, meets $C_1$ at $B(1,\,y_2)$, $y_1 \neq y_2$.\\"
            r"Find $a = ?$"
        ).to_edge(UP).shift(DOWN * 0.5).scale(0.9)

        try_text = (
            Tex(r"Try solving it on your own")
            .scale(0.7)
            .set_color(YELLOW)
            .next_to(math, DOWN, buff=0.3)
        )

        steps, solution = self._build_solution_steps()
        (
            roots_title,
            r1_head, r1_lines, r1_cross,
            r2_head, r2_lines, r2_cross,
            r3_head, r3_lines, r3_tick,
            full_check,
        ) = self._build_root_checks()

        (
            made_with, manim_title, divider,
            open_source, thank_you, github_line, credits_group,
        ) = self._build_credits()

        # ── Scene 1: Question ─────────────────────────────────────────────────
        self.play(Write(math))
        self.play(Write(try_text))
        self.wait(10)
        self.play(Unwrite(math), Unwrite(try_text))

        # ── Scene 2: Graphs and intersection dots ─────────────────────────────
        self.play(Create(axes))
        self.play(Create(c1), Create(c2))
        self.play(FadeIn(dot), Write(label))
        self.play(FadeIn(dot1))
        self.play(Write(c1_label))
        self.play(Write(c2_label))

        # ── Scene 3: Rolling tangent along C2 ────────────────────────────────
        t = ValueTracker(0)

        def get_tangent():
            x0    = t.get_value()
            y0    = 0.3 * x0**2
            slope = 0.6 * x0
            return axes.plot(
                lambda x: slope * (x - x0) + y0,
                color=RED,
                x_range=[-5, 3.5],
            )

        rolling_tangent = always_redraw(get_tangent)
        self.add(rolling_tangent)
        self.play(t.animate.set_value(-1.7837), run_time=3)
        self.play(FadeIn(dot2), Write(label2))
        self.wait(3)

        # ── Scene 4: Freeze tangent; shift graph to the right ─────────────────
        frozen_tangent = axes.plot(
            lambda x: -1.0702 * x - 0.9298,
            color=RED,
            x_range=[-5, 3.5],
        )
        self.remove(rolling_tangent)
        self.add(frozen_tangent)

        graph_group = VGroup(
            axes, c1, c2, dot, dot1, dot2,
            label, label2, c1_label, c2_label, frozen_tangent,
        )
        self.play(graph_group.animate.scale(0.75).shift(RIGHT * 3), run_time=2)
        self.wait(1)

        # ── Scene 5: Solution steps ───────────────────────────────────────────
        for step in steps:
            self.play(Write(step), run_time=1)
            self.wait(0.5)
        self.wait(1)

        # ── Scene 6: Root-checking ────────────────────────────────────────────
        self.play(FadeOut(graph_group), FadeOut(solution), run_time=0.8)
        self.play(Write(roots_title))
        self.wait(0.3)

        self.play(Write(r1_head))
        for line in r1_lines:
            self.play(Write(line), run_time=0.8)
        self.play(Write(r1_cross))
        self.wait(0.5)

        self.play(Write(r2_head))
        for line in r2_lines:
            self.play(Write(line), run_time=0.8)
        self.play(Write(r2_cross))
        self.wait(0.5)

        self.play(Write(r3_head))
        for line in r3_lines:
            self.play(Write(line), run_time=0.8)
        self.play(Write(r3_tick))
        self.wait(4)

        self.play(FadeOut(full_check), run_time=0.8)

        # ── Scene 7: Credits ──────────────────────────────────────────────────
        self.play(FadeIn(made_with), run_time=1.5)
        self.play(Write(manim_title), run_time=2, rate_func=linear)
        self.play(GrowFromCenter(divider), run_time=1.2)
        self.play(FadeIn(open_source), run_time=1)
        self.play(FadeIn(thank_you,    shift=UP * 0.2), run_time=1.2)
        self.play(FadeIn(github_line,  shift=UP * 0.2), run_time=1.2)
        self.wait(4)
        self.play(FadeOut(credits_group, shift=DOWN * 0.3), run_time=2)