from cv2 import circle
from manim import *
class VortexScene(ThreeDScene):
    CONFIG={
        'n_circles':10,
    }
    def construct(self):
        axes=ThreeDAxes()
        axes.set_stroke(width=1)
        self.add(axes)
        self.move_camera(phi=60*DEGREES,theta=60*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)
        torus=self.get_torus(2,5,0.5)
        self.play(Create(torus))
        self.wait()
    def get_torus(self,out_r,in_r,in_r_var):
        result=VGroup()
        for u in sorted(np.random.random(self.CONFIG['n_circles'])):
            r=in_r+in_r_var*np.random.random()
            circle=ParametricFunction(
                lambda t: r*np.array([
                    np.cos(TAU*t),
                    np.sin(TAU*t),
                    0
                ])
            )
            circle.shift(out_r*RIGHT)
            circle.rotate(TAU*u-PI,about_point=ORIGIN,axis=DOWN)
            result.add(circle)
        return result