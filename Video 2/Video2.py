
from manim import *
import numpy as np

class ManimCELogo(Scene):
    def construct(self):
        watermark = Text("MathClicks", font="Arial", weight=BOLD)
        watermark.scale(0.35)
        watermark.set_opacity(0.45)
        watermark.to_corner(DR, buff=0.4)
        self.add_foreground_mobjects(watermark)
        # ── constants ──────────────────────────────────────────────────────────
        a_val, b_val = 10, 8
        c_val  = np.sqrt(a_val**2 + b_val**2)     # 2√41 ≈ 12.806
        theta0 = 0.6                               # chosen for visual clarity
        Px = a_val / np.cos(theta0)                # ≈ 12.12
        Py = b_val * np.tan(theta0)                # ≈  5.47
        m  = (b_val**2 * Px) / (a_val**2 * Py)    # tangent slope ≈ 1.417
        slope_S1P = Py / (Px + c_val)              # slope of S₁P  ≈ 0.220
        P1x = c_val * (m + slope_S1P) / (m - slope_S1P)  # ≈ 17.5
        P1y = m * (P1x - c_val)                    # ≈  6.65
        # foot of perpendicular from P onto line SP₁
        num_foot   = m * Px - Py - m * c_val
        denom_foot = m**2 + 1
        xf = Px - m * num_foot / denom_foot
        yf = Py +     num_foot / denom_foot
        # ── axes ──────────────────────────────────────────────────────────────
        axes = Axes(
            x_range=[-20, 22, 5],
            y_range=[-12, 12, 4],
            x_length=7,
            y_length=5,
        ).scale(0.8)
        # ── hyperbola (both branches, parametric) ─────────────────────────────
        hyp_right = ParametricFunction(
            lambda t: axes.coords_to_point(a_val / np.cos(t), b_val * np.tan(t)),
            t_range=[-1.2, 1.2],
            color=YELLOW,
        )
        hyp_left = ParametricFunction(
            lambda t: axes.coords_to_point(-a_val / np.cos(t), b_val * np.tan(t)),
            t_range=[-1.2, 1.2],
            color=YELLOW,
        )
        hyp_label = (
            Tex(r"$\frac{x^2}{100}-\frac{y^2}{64}=1$", color=YELLOW)
            .scale(0.5)
            .next_to(axes.coords_to_point(15, 9), UR, buff=1.7)
        )
        # ── foci ──────────────────────────────────────────────────────────────
        S_dot  = Dot(axes.coords_to_point( c_val, 0), color=RED)
        S1_dot = Dot(axes.coords_to_point(-c_val, 0), color=RED)
        S_label  = Tex(r"$S$" ).scale(0.6).next_to(S_dot,  DOWN, buff=0.15)
        S1_label = Tex(r"$S_1$").scale(0.6).next_to(S1_dot, DOWN, buff=0.15)
        # ── point P ───────────────────────────────────────────────────────────
        P_dot   = Dot(axes.coords_to_point(Px, Py), color=GREEN)
        P_label = (
            Tex(r"$P$", color=GREEN)
            .scale(0.6)
            .next_to(P_dot, UR, buff=0.2)
        )
        # ── frozen tangent at P ────────────────────────────────────────────────
        frozen_tan = axes.plot(
            lambda x: m * (x - Px) + Py,
            x_range=[1, 16.5], color=RED, stroke_width=2,
        )
        tan_label = (
            Tex(r"tangent at $P$", color=RED)
            .scale(0.45)
            .next_to(P_dot, UL, buff=0.15)
        )
        # ── line through S with same slope as tangent ─────────────────────────
        S_line = axes.plot(
            lambda x: m * (x - c_val),
            x_range=[5.5, 18], color=PURPLE, stroke_width=2,
        )
        S_line_label = (
            Tex(r"through $S$, slope $=$ tangent slope", color=PURPLE)
            .scale(0.38)
            .next_to(axes.coords_to_point(9, m*(9 - c_val)), DOWN, buff=1.3)
        )
        # ── line S₁P ──────────────────────────────────────────────────────────
        S1P_line = axes.plot(
            lambda x: slope_S1P * (x + c_val),
            x_range=[-c_val, P1x + 0.4], color=BLUE, stroke_width=2,
        )
        beta_label = (
            Tex(r"$\beta = S_1P$", color=BLUE)
            .scale(0.45)
            .next_to(axes.coords_to_point(0, 2.7), UL, buff=0.2)
        )
        # ── P₁ ────────────────────────────────────────────────────────────────
        P1_dot   = Dot(axes.coords_to_point(P1x, P1y), color=PURPLE)
        P1_label = Tex(r"$P_1$").scale(0.55).next_to(P1_dot, UR, buff=0.08)
        # ── perpendicular from P to SP₁  (length = δ) ─────────────────────────
        perp = Line(
            axes.coords_to_point(Px, Py),
            axes.coords_to_point(xf, yf),
            color=ORANGE, stroke_width=2.5,
        )
        delta_label = (
            Tex(r"$\delta$", color=ORANGE)
            .scale(0.55)
            .next_to(axes.coords_to_point((Px + xf) / 2, (Py + yf) / 2), DL, buff=1)
        )
        # ── angle α label at P ─────────────────────────────────────────────────
        alpha_label = Tex(r"$\alpha$").scale(0.5).next_to(P_dot, DL, buff=0.18)
        # ── question text ──────────────────────────────────────────────────────
        math = Tex(
            r"Consider the hyperbola $\dfrac{x^2}{100}-\dfrac{y^2}{64}=1$\\",
            r"with foci at $S$ and $S_1$, where $S$ lies on the positive $x$-axis.\\",
            r"Let $P$ be a point on the hyperbola in the first quadrant, $\angle SPS_1=\alpha<\dfrac{\pi}{2}$.\\",
            r"The straight line through $S$ having the same slope as the tangent at $P$\\",
            r"intersects the straight line $S_1P$ at $P_1$.\\",
            r"Let $\delta$ be the distance of $P$ from the straight line $SP_1$, and $\beta=S_1P$.\\",
            r"The greatest integer less than or equal to $\dfrac{\beta\delta}{9}\sin\dfrac{\alpha}{2}$ is \underline{\hspace{1cm}}.",
        ).to_edge(UP).scale(0.58)
        try_text = (
            Tex(r"Try Solving it on your own")
            .scale(0.7).set_color(YELLOW)
            .next_to(math, DOWN, buff=0.3)
        )
        # ── solution steps ─────────────────────────────────────────────────────
        sol0 = Tex(
            r"Parametrize: $P=(10\sec\theta,\;8\tan\theta)$, $\theta\in\!\left(0,\tfrac\pi2\right)$"
        ).scale(0.60)
        sol1 = Tex(
            r"Tangent slope: $\dfrac{dy}{dx}=\dfrac{b^2 x}{a^2 y}"
            r"=\dfrac{64\cdot10\sec\theta}{100\cdot8\tan\theta}=\dfrac{4}{5\sin\theta}$"
        ).scale(0.60)
        sol2 = Tex(
            r"Focal radius: $\beta=S_1P=ex_P+a"
            r"=\dfrac{\sqrt{41}}{5}\cdot10\sec\theta+10=2\sqrt{41}\sec\theta+10$ (where $e$ is eccentricity)"
        ).scale(0.4)
        sol3 = Tex(
            r"Point-to-line dist: $\delta=\dfrac{|m(P_x-c)-P_y|}{\sqrt{m^2+1}}"
            r"=\dfrac{8(\sqrt{41}-5\cos\theta)}{\sqrt{16+25\sin^2\!\theta}}$"
        ).scale(0.60)
        sol4 = Tex(
            r"Cosine rule in $\triangle SPS_1$: "
            r"$\cos\alpha=\dfrac{r_1^2+r_2^2-4c^2}{2r_1r_2}$"
        ).scale(0.60)
        sol5 = Tex(
            r"Half-angle formula: "
            r"$\sin\dfrac{\alpha}{2}=\dfrac{4\cos\theta}{\sqrt{16+25\sin^2\!\theta}}$"
        ).scale(0.60)
        solution = VGroup(sol0, sol1, sol2, sol3, sol4, sol5)
        solution.arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        solution.to_edge(LEFT).shift(RIGHT * 0.4)
        # ── verification / key steps ───────────────────────────────────────────
        ver_title = Tex(
            r"\underline{Computing $\beta\,\delta\,\sin(\alpha/2)$:}", color=YELLOW
        ).scale(0.78)
        ver1 = Tex(
            r"$\beta\cdot\delta"
            r"=\dfrac{2(\sqrt{41}+5\cos\theta)}{\cos\theta}"
            r"\cdot\dfrac{8(\sqrt{41}-5\cos\theta)}{\sqrt{16+25\sin^2\!\theta}}$"
        ).scale(0.63)
        ver2 = Tex(
            r"$=\dfrac{16\,(41-25\cos^2\!\theta)}{\cos\theta\;\sqrt{16+25\sin^2\!\theta}}$"
        ).scale(0.63)
        key_lhs = Tex(r"Key identity: $41-25\cos^2\!\theta$", color=YELLOW).scale(0.63)
        key_rhs = Tex(r"$=\;16+25\sin^2\!\theta$", color=BLUE).scale(0.63)
        ver3    = VGroup(key_lhs, key_rhs).arrange(RIGHT, buff=0.1)
        ver4 = Tex(
            r"$\therefore\;\beta\delta"
            r"=\dfrac{16\,\sqrt{16+25\sin^2\!\theta}}{\cos\theta}$"
        ).scale(0.63)
        ver5 = Tex(
            r"$\beta\delta\cdot\sin\dfrac{\alpha}{2}"
            r"=\dfrac{16\,\sqrt{16+25\sin^2\!\theta}}{\cos\theta}"
            r"\cdot\dfrac{4\cos\theta}{\sqrt{16+25\sin^2\!\theta}}=64$"
        ).scale(0.63)
        ver6 = Tex(
            r"$\left\lfloor\dfrac{\beta\delta}{9}\sin\dfrac{\alpha}{2}\right\rfloor"
            r"=\left\lfloor\dfrac{64}{9}\right\rfloor"
            r"=\lfloor\,7.11\ldots\,\rfloor$",
            color=GREEN,
        ).scale(0.65)
        ver7 = Tex(r"$\boxed{=\;7}$", color=GREEN).scale(0.88)
        verification = VGroup(ver_title, ver1, ver2, ver3, ver4, ver5, ver6, ver7)
        verification.arrange(DOWN, aligned_edge=LEFT, buff=0.26)
        verification.center()
        # ── credits ────────────────────────────────────────────────────────────
        made_with   = Tex(r"made with", color=GRAY).scale(0.5)
        manim_title = Tex(r"Manim Community Edition", color=WHITE).scale(1.2)
        divider     = Line(LEFT * 3, RIGHT * 3, color=GRAY, stroke_width=0.8)
        open_source = Tex(r"an open source project by the manim community",
                          color=GRAY).scale(0.48)
        thank_you   = Tex(
            r"thank you to every contributor who made mathematical animation accessible to everyone",
            color=GRAY,
        ).scale(0.48)
        github_line = Tex(r"link to the source code of this video is on my github",
                          color=GRAY).scale(0.48)
        credits_group = VGroup(made_with, manim_title, divider,
                               open_source, thank_you, github_line)
        credits_group.arrange(DOWN, buff=0.3)
        credits_group.center()
        # ══════════════════════════════════════════════════════════════════════
        # Scene 1 — question
        # ══════════════════════════════════════════════════════════════════════
        self.play(Write(math))
        self.play(Write(try_text))
        self.wait(10)
        self.play(Unwrite(math), Unwrite(try_text))
        # ══════════════════════════════════════════════════════════════════════
        # Scene 2 — hyperbola + foci
        # ══════════════════════════════════════════════════════════════════════
        self.play(Create(axes))
        self.play(Create(hyp_right), Create(hyp_left))
        self.play(Write(hyp_label))
        self.play(
            FadeIn(S_dot),  Write(S_label),
            FadeIn(S1_dot), Write(S1_label),
        )
        self.wait(0.5)
        # ══════════════════════════════════════════════════════════════════════
        # Scene 3 — rolling tangent on right branch → freeze at θ₀
        # ══════════════════════════════════════════════════════════════════════
        t_tracker = ValueTracker(0.15)
        def get_tan_line():
            th  = t_tracker.get_value()
            x0  = a_val / np.cos(th)
            y0  = b_val * np.tan(th)
            mth = (b_val**2 * x0) / (a_val**2 * y0)
            return axes.plot(
                lambda x: mth * (x - x0) + y0,
                x_range=[1, 16.5],
                color=RED, stroke_width=2,
            )
        def get_moving_P():
            th = t_tracker.get_value()
            x0 = a_val / np.cos(th)
            y0 = b_val * np.tan(th)
            return Dot(axes.coords_to_point(x0, y0), color=GREEN, radius=0.07)
        rolling_tan = always_redraw(get_tan_line)
        moving_P    = always_redraw(get_moving_P)
        self.add(rolling_tan, moving_P)
        self.play(t_tracker.animate.set_value(theta0), run_time=3)
        self.wait(0.5)
        # freeze tangent and P dot
        self.remove(rolling_tan, moving_P)
        self.add(frozen_tan, P_dot)
        self.play(Write(P_label), Write(tan_label))
        self.wait(0.5)
        # draw lines and geometric labels
        self.play(Create(S1P_line), Write(beta_label))
        self.play(FadeIn(P1_dot), Write(P1_label))
        self.play(Create(S_line), Write(S_line_label))
        self.play(Create(perp), Write(delta_label))
        self.play(Write(alpha_label))
        self.wait(2)
        # ══════════════════════════════════════════════════════════════════════
        # Scene 4 — shift diagram right, write solution on left
        # ══════════════════════════════════════════════════════════════════════
        diagram = VGroup(
            axes, hyp_right, hyp_left, hyp_label,
            S_dot, S1_dot, S_label, S1_label,
            P_dot, P_label, frozen_tan, tan_label,
            S1P_line, beta_label,
            S_line, S_line_label, P1_dot, P1_label,
            perp, delta_label, alpha_label,
        )
        self.play(diagram.animate.scale(0.65).shift(RIGHT * 3.5), run_time=2)
        self.wait(0.5)
        for step in [sol0, sol1, sol2, sol3, sol4, sol5]:
            self.play(Write(step), run_time=1.0)
            self.wait(0.4)
        self.wait(1)
        # ══════════════════════════════════════════════════════════════════════
        # Scene 5 — clear and show the key computation
        # ══════════════════════════════════════════════════════════════════════
        self.play(FadeOut(diagram), FadeOut(solution), run_time=0.8)
        self.play(Write(ver_title))
        self.wait(0.3)
        for step in [ver1, ver2, ver3, ver4, ver5]:
            self.play(Write(step), run_time=1.0)
            self.wait(0.4)
        self.play(Write(ver6), run_time=1.0)
        self.wait(0.5)
        self.play(Write(ver7), run_time=1.2)
        self.wait(4)
        self.play(FadeOut(verification), run_time=0.8)
        # ══════════════════════════════════════════════════════════════════════
        # Scene 6 — credits
        # ══════════════════════════════════════════════════════════════════════
        self.play(FadeIn(made_with), run_time=1.5)
        self.play(Write(manim_title), run_time=2, rate_func=linear)
        self.play(GrowFromCenter(divider), run_time=1.2)
        self.play(FadeIn(open_source), run_time=1)
        self.play(FadeIn(thank_you,   shift=UP * 0.2), run_time=1.2)
        self.play(FadeIn(github_line, shift=UP * 0.2), run_time=1.2)
        self.wait(4)
        self.play(FadeOut(credits_group, shift=DOWN * 0.3), run_time=2)
