#!/usr/bin/env python


from manim import *
from manim.mobject.geometry.line import AnchoredArrow


class Demo(Scene):
    def construct(self):
        tl, tr = Text("NULL").scale(0.8), Text("NULL").scale(0.8)
        dl, dr = Dot().next_to(tl, RIGHT, buff=0), Dot().next_to(tr, LEFT, buff=0)

        tlg = VGroup(tl, dl).to_edge(LEFT)
        trg = VGroup(tr, dr).to_edge(RIGHT)

        s1m = (
            Rectangle(color="#f54272", height=1, width=2)
            .shift(2 * DOWN)
            .shift(2 * RIGHT)
        )
        s1l = Rectangle(color="#f54272", height=1, width=2).next_to(s1m, LEFT, buff=0)
        s1r = Rectangle(color="#f54272", height=1, width=2).next_to(s1m, UP, buff=4)
        s1t = Text("data").scale(0.8).move_to(s1m.get_center())

        s2m = (
            Rectangle(color="#8442f5", height=1, width=2)
            .shift(2 * DOWN)
            .shift(2 * RIGHT)
        )
        s2l = Rectangle(color="#8442f5", height=1, width=2).next_to(s2m, LEFT, buff=0)
        s2r = Rectangle(color="#8442f5", height=1, width=2).next_to(s2m, UP, buff=4)
        s2t = Text("data").scale(0.8).move_to(s2m.get_center())

        s3m = Rectangle(color="#42f587", height=1, width=2)
        s3l = Rectangle(color="#42f587", height=1, width=2).next_to(s3m, LEFT, buff=0)
        s3r = Rectangle(color="#42f587", height=1, width=2).next_to(s3m, RIGHT, buff=0)
        s3t = Text("data").scale(0.8).move_to(s3m.get_center())

        s1g = VGroup(s1m, s1r).shift(6 * LEFT)
        s2g = VGroup(s2m, s2r).shift(2 * RIGHT)
        s3g = VGroup(s3m, s3r, s3t).shift(8 * RIGHT)

        l = VGroup(s1g, s2g, s3g)

        a1 = AnchoredArrow(start=s1m, end=s2m)
        ta = AnchoredArrow(start=s1r, end=s2r)
        td1 = Dot(color="#ffffff").move_to(s1m.get_center())
        td2 = Dot(color="#ffffff").move_to(s1r.get_center())
        td3 = Dot(color="#ffffff").move_to(s2m.get_center())
        td4 = Dot(color="#ffffff").move_to(s2r.get_center())

        self.play(Create(s1m), Create(s1r), Create(s2m), Create(s2r))
        self.play(Create(ta), Create(a1), run_time=0.5)
        a1.add_updater(lambda mob: mob.update_endpoints(s1m, s2m))
        ta.add_updater(lambda mob: mob.update_endpoints(s1r, s2r))
        self.wait(0.5)
        self.play(
            s1m.animate.scale(2),
            s1r.animate.scale(2),
            s2m.animate.scale(2),
            s2r.animate.scale(2),
        )
        self.wait(0.25)
        self.play(
            s1m.animate.scale(0.5),
            s1r.animate.scale(0.5),
            s2m.animate.scale(0.5),
            s2r.animate.scale(0.5),
        )
        a1.clear_updaters()
        ta.clear_updaters()
        self.play(
            Create(td1),
            Create(td2),
            a1.animate.update_endpoints(td1, s2m),
            ta.animate.update_endpoints(td2, s2r),
            run_time=0.5,
        )
        self.play(
            a1.animate.update_endpoints(td1, s2r),
            ta.animate.update_endpoints(td2, s2m),
            run_time=0.5,
        )
        self.play(
            a1.animate.update_endpoints(td1, s2m),
            ta.animate.update_endpoints(td2, s2r),
            run_time=0.5,
        )
        a1.scaling(lock=True)
        ta.scaling(lock=True)
        self.play(
            Create(td3),
            Create(td4),
            a1.animate.update_endpoints(td1, td3),
            ta.animate.update_endpoints(td2, td4),
            run_time=0.5,
        )
        self.play(
            a1.animate.update_endpoints(td1, s2m),
            ta.animate.update_endpoints(td2, s2r),
            Uncreate(td3),
            Uncreate(td4),
            run_time=0.5,
        )
        a1.scaling(target=True)
        self.play(
            a1.animate.update_endpoints(s1m, s2m),
            ta.animate.update_endpoints(s1r, s2r),
            Uncreate(td1),
            Uncreate(td2),
            run_time=0.5,
        )
        self.wait(0.25)
        self.play(
            a1.animate.update_endpoints(s1m, s2r),
            ta.animate.update_endpoints(s1r, s2m),
            run_time=0.5,
        )
        self.play(ta.animate.update_endpoints(s1m, s2m), run_time=0.5)
        self.play(ta.animate.update_endpoints(s2m, s1m), run_time=0.5)
        self.play(a1.animate.update_endpoints(s1r, s2m), run_time=0.5)

        a1.add_updater(lambda mob: mob.update_endpoints(s1r, s2m))
        self.play(Uncreate(ta), run_time=0.5)
        self.play(
            s1r.animate.next_to(s1m, RIGHT, buff=0),
            s2r.animate.next_to(s2m, RIGHT, buff=0),
        )
        self.play(
            s1g.animate.shift(2 * UP).shift(2 * LEFT),
            s2g.animate.shift(2 * UP).shift(2 * LEFT),
        )
        s1g.add(s1t.move_to(s1m.get_center()))
        s2g.add(s2t.move_to(s2m.get_center()))
        self.play(Create(s1t), Create(s2t), run_time=0.5)
        self.play(
            s1g.animate.shift(4 * LEFT), s2g.animate.center(), Create(s3m), Create(s3r)
        )

        a2 = AnchoredArrow(start=s2r, end=s3m)
        a2.add_updater(lambda mob: mob.update_endpoints(s2r, s3m))
        self.play(Create(s3t), Create(a2), run_time=0.5)

        self.play(s2g.animate.move_to(3 * UP), run_time=0.5)
        self.play(s2g.animate.shift(4 * LEFT), run_time=0.5)
        self.play(s2g.animate.shift(8 * RIGHT), run_time=0.5)
        self.play(s2g.animate.move_to(4 * DOWN), run_time=0.5)
        self.play(s2g.animate.center())

        s1g.add(s1l.next_to(s1m, LEFT, buff=0))
        s2g.add(s2l.next_to(s2m, LEFT, buff=0))
        s3g.add(s3l.next_to(s3m, LEFT, buff=0))

        a3 = AnchoredArrow(start=s2l, end=s1r)
        a4 = AnchoredArrow(start=s3l, end=s2r)
        a5 = AnchoredArrow(start=s1l, end=dl).scaling(match=a1)
        a6 = AnchoredArrow(start=s3r, end=dr).scaling(match=a1)

        a4.add_updater(
            lambda mob: mob.update_endpoints(
                s3l, s2r, start_x=-1, start_y=-0.4, end_x=1, end_y=-0.4
            )
        )
        a3.add_updater(
            lambda mob: mob.update_endpoints(
                s2l, s1r, start_x=-1, start_y=-0.4, end_x=1, end_y=-0.4
            )
        )
        a5.add_updater(lambda mob: mob.update_endpoints(s1l, dl))
        a6.add_updater(lambda mob: mob.update_endpoints(s3r, dr))

        self.play(
            Create(s1l),
            Create(s2l),
            Create(s3l),
            a1.clear_updaters().animate.update_endpoints(s1r, s2l),
            a2.clear_updaters().animate.update_endpoints(s2r, s3l),
            run_time=0.75,
        )
        a1.add_updater(lambda mob: mob.update_endpoints(s1r, s2l))
        a2.add_updater(lambda mob: mob.update_endpoints(s2r, s3l))
        self.play(l.animate.center().arrange(buff=3))
        self.play(
            a1.clear_updaters().animate.update_endpoints(
                s1r, s2l, start_x=1, start_y=0.4, end_x=-1, end_y=0.4
            ),
            a2.clear_updaters().animate.update_endpoints(
                s2r, s3l, start_x=1, start_y=0.4, end_x=-1, end_y=0.4
            ),
        )
        a1.add_updater(
            lambda mob: mob.update_endpoints(
                s1r, s2l, start_x=1, start_y=0.4, end_x=-1, end_y=0.4
            )
        )
        a2.add_updater(
            lambda mob: mob.update_endpoints(
                s2r, s3l, start_x=1, start_y=0.4, end_x=-1, end_y=0.4
            )
        )
        self.play(Create(a3), Create(a4), run_time=0.5)
        self.play(Create(tl), Create(tr), Create(a5), Create(a6))

        self.play(s2g.animate.shift(3 * UP), run_time=0.5)
        self.play(s2g.animate.shift(6 * DOWN), run_time=0.5)
        self.play(s2g.animate.center())

        self.play(
            Uncreate(tl),
            Uncreate(tr),
            Uncreate(a3.clear_updaters()),
            Uncreate(a2.clear_updaters()),
            Uncreate(a5.clear_updaters()),
            Uncreate(a6.clear_updaters()),
            a1.clear_updaters().animate.update_endpoints(s1r, s2l),
            a4.clear_updaters().animate.update_endpoints(s2r, s3l),
        )
        a1.add_updater(lambda mob: mob.update_endpoints(s1r, s2l))
        a4.add_updater(lambda mob: mob.update_endpoints(s2r, s3l))

        c = Circle(color="#f54272", radius=1.5).move_to(s1g.get_center())
        st = Star(n=5, color="#8442f5").scale(2)
        t = Triangle(color="#42f587").scale(2).move_to(s3g.get_center())

        shapes = VGroup(c, st, t)

        self.play(
            ReplacementTransform(s2g, st),
            ReplacementTransform(s1g, c),
            ReplacementTransform(s3g, t),
        )
        a1.add_updater(lambda mob: mob.update_endpoints(c, st))
        a4.add_updater(lambda mob: mob.update_endpoints(st, t))
        self.play(shapes.animate.arrange(buff=3))
        # self.play(l.animate.arrange(buff=2).center())
        self.wait(1)

        self.play(
            Rotate(st, angle=-2 * PI, rate_func=linear),
            Rotate(c, angle=2 * PI, about_point=st.get_center(), rate_func=linear),
            Rotate(t, angle=2 * PI, about_point=st.get_center(), rate_func=linear),
            run_time=6,
        )

        self.play(
            Uncreate(shapes),
            Uncreate(a1.clear_updaters()),
            Uncreate(a4.clear_updaters()),
        )

        self.wait(2)


class Scaling_Demo(Scene):
    def construct(self):
        scaling_text = (
            Text("Scaling options:").scale(0.75).center().to_edge(UP).shift(0.25 * UP)
        )  # .shift(0.01*DOWN)

        sDefault = Dot(color="#07b3f7")
        eDefault = Dot(color="#07b3f7").shift(4 * RIGHT)
        default = VGroup(sDefault, eDefault)
        sTarget = Dot(color="#07b3f7")
        eTarget = Dot(color="#07b3f7").shift(4 * RIGHT)
        target = VGroup(sTarget, eTarget)
        sTarLEN = Dot(color="#07b3f7")
        eTarLEN = Dot(color="#07b3f7").shift(4 * RIGHT)
        TarLEN = VGroup(sTarLEN, eTarLEN)
        sMatch = Dot(color="#07b3f7")
        eMatch = Dot(color="#07b3f7").shift(4 * RIGHT)
        match = VGroup(sMatch, eMatch)
        sLock = Dot(color="#07b3f7")
        eLock = Dot(color="#07b3f7").shift(4 * RIGHT)
        lock = VGroup(sLock, eLock)
        sCap = Dot(color="#07b3f7")
        eCap = Dot(color="#07b3f7").shift(4 * RIGHT)
        Cap = VGroup(sCap, eCap)
        sLim = Dot(color="#07b3f7")
        eLim = Dot(color="#07b3f7").shift(4 * RIGHT)
        Lim = VGroup(sLim, eLim)

        dots = VGroup(default, target, TarLEN, match, lock, Cap, Lim)
        dots.arrange(direction=np.array([0.0, -1.0, 0.0]), buff=0.8).center().shift(
            0.5 * DOWN
        )
        self.play(Create(scaling_text), run_time=0.5)
        self.wait(0.5)

        default_Text = Text("Scale with length").scale(0.4).next_to(default, UP)
        aDefault = AnchoredArrow(start=sDefault, end=eDefault, target_scaling=False)

        self.play(Create(default), Create(default_Text))
        self.wait(0.5)
        self.play(Create(aDefault))
        aDefault.add_updater(lambda mob: mob.update_endpoints(sDefault, eDefault))
        self.play(eDefault.animate.shift(3.5 * LEFT))
        self.wait(0.25)
        self.play(eDefault.animate.shift(3.5 * RIGHT))
        self.wait(0.5)
        self.play(eDefault.animate.scale(4).shift(0.24 * RIGHT))
        self.play(eDefault.animate.scale(0.25).shift(0.24 * LEFT))

        # --------------
        target_Text = Text("Scale with target size").scale(0.4).next_to(target, UP)
        aTarget = AnchoredArrow(start=sTarget, end=eTarget, length_scaling=False)

        self.play(Create(target), Create(target_Text))
        self.wait(0.5)
        self.play(Create(aTarget))
        aTarget.add_updater(lambda mob: mob.update_endpoints(sTarget, eTarget))
        self.play(eTarget.animate.shift(3.5 * LEFT))
        self.wait(0.25)
        self.play(eTarget.animate.shift(3.5 * RIGHT))
        self.wait(0.5)
        self.play(eTarget.animate.scale(4).shift(0.24 * RIGHT))
        self.play(eTarget.animate.scale(0.25).shift(0.24 * LEFT))

        # --------------
        TarLEN_Text = (
            Text("Scale with target size and length").scale(0.4).next_to(TarLEN, UP)
        )
        defaultT = Text("(Default)").scale(0.4).next_to(TarLEN_Text, RIGHT)
        aTarLEN = AnchoredArrow(start=sTarLEN, end=eTarLEN)

        self.play(Create(TarLEN), Create(TarLEN_Text), Create(defaultT))
        self.wait(0.5)
        self.play(Create(aTarLEN))
        aTarLEN.add_updater(lambda mob: mob.update_endpoints(sTarLEN, eTarLEN))
        self.play(eTarLEN.animate.shift(3.5 * LEFT))
        self.wait(0.25)
        self.play(eTarLEN.animate.shift(3.5 * RIGHT))
        self.wait(0.5)
        self.play(eTarLEN.animate.scale(4).shift(0.24 * RIGHT))
        self.play(eTarLEN.animate.scale(0.25).shift(0.24 * LEFT))

        # --------------
        match_Text = Text("Match scaling of another").scale(0.4).next_to(match, UP)
        aMatch = AnchoredArrow(
            start=sMatch, end=eMatch, match_scaling=True, scale_with=aTarLEN
        )

        self.play(Create(match), Create(match_Text))
        self.wait(0.5)
        self.play(Create(aMatch))
        aMatch.add_updater(lambda mob: mob.update_endpoints(sMatch, eMatch))
        self.play(eMatch.animate.shift(3.5 * LEFT))
        self.wait(0.25)
        self.play(eMatch.animate.shift(3.5 * RIGHT))
        self.wait(0.5)
        self.play(eMatch.animate.scale(4).shift(0.24 * RIGHT))
        self.play(eMatch.animate.scale(0.25).shift(0.24 * LEFT))
        self.wait(0.5)
        self.play(eTarLEN.animate.scale(4).shift(0.24 * RIGHT))
        self.play(eTarLEN.animate.scale(0.25).shift(0.24 * LEFT))

        # --------------
        Lock_Text = Text("Lock scaling to current values").scale(0.4).next_to(lock, UP)
        aLock = AnchoredArrow(start=sLock, end=eLock)

        self.play(Create(lock), Create(Lock_Text))
        self.wait(0.5)
        self.play(Create(aLock))
        aLock.add_updater(lambda mob: mob.update_endpoints(sLock, eLock))
        aLock.scaling(lock=True)
        self.play(eLock.animate.shift(3.5 * LEFT))
        self.wait(0.25)
        self.play(eLock.animate.shift(3.5 * RIGHT))
        self.wait(0.5)
        self.play(eLock.animate.scale(4).shift(0.24 * RIGHT))
        self.play(eLock.animate.scale(0.25).shift(0.24 * LEFT))

        # --------------
        Cap_Text = Text("Uncap scaling").scale(0.4).next_to(Cap, UP)
        aCap = AnchoredArrow(start=sCap, end=eCap, cap_scaling=False)

        self.play(Create(Cap), Create(Cap_Text))
        self.wait(0.5)
        self.play(Create(aCap))
        aCap.add_updater(lambda mob: mob.update_endpoints(sCap, eCap))
        self.play(eCap.animate.scale(4).shift(0.24 * RIGHT))
        self.play(eCap.animate.scale(0.05).shift(0.25 * LEFT))
        self.play(eCap.animate.scale(5).shift(0.01 * RIGHT))

        # --------------
        Lim_Text = Text("Set custom scaling bounds").scale(0.4).next_to(Lim, UP)
        aLim = AnchoredArrow(start=sLim, end=eLim, cap_scaling=False)

        self.play(Create(Lim), Create(Lim_Text))
        self.wait(0.5)
        self.play(Create(aLim))
        aLim.add_updater(lambda mob: mob.update_endpoints(sLim, eLim))
        self.play(eLim.animate.scale(4).shift(0.24 * RIGHT))
        self.play(eLim.animate.scale(0.25).shift(0.24 * LEFT))
        self.wait(0.25)
        aLim.scaling(target=True, stroke_cap=5, tip_cap=0.4375)
        self.play(eLim.animate.scale(4).shift(0.24 * RIGHT))
        self.play(eLim.animate.scale(0.25).shift(0.24 * LEFT))
        self.wait(0.5)
        self.play(eLim.animate.scale(0.2).shift(0.01 * LEFT))
        self.play(eLim.animate.scale(5).shift(0.01 * RIGHT))
        self.wait(0.25)
        aLim.scaling(target=True, floor=True, stroke_floor=1.5, tip_floor=0.0875)
        self.play(eLim.animate.scale(0.2).shift(0.01 * LEFT))
        self.play(eLim.animate.scale(5).shift(0.01 * RIGHT))

        self.wait(2)
