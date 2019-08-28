from math import atan, degrees
from pyx import canvas, color, path, style, text, unit

unit.set(xscale=0.8)
c = canvas.canvas()
c.fill(path.circle(0, 0, 0.1), [color.grey(0.5)])
c.fill(path.circle(2, 1, 0.1), [color.grey(0.5)])
c.stroke(path.line(0, 0, -1., -0.2),
         [style.linewidth.Thick, style.linestyle.dotted])
c.stroke(path.line(2, 1, 2.7, 1.7),
         [style.linewidth.Thick, style.linestyle.dotted])
c.stroke(path.line(0, 0, 2, 1), [style.linewidth.thick])
c.stroke(path.path(path.moveto(0, 0),
                   path.lineto(2, 0),
                   path.lineto(2, 1)))
c.text(0.5, 0.1, r'$\varphi$')
c.stroke(path.path(path.arc(0, 0, 0.8, 0, degrees(atan(0.5)))))
c.text(1, 0.6, r'$\ell=1$', [text.halign.right])
c.text(1, -0.1, r'$\cos(\varphi)$', [text.halign.center, text.valign.top])
c.text(2.1, 0.5, r'$\sin(\varphi)$', [text.valign.middle])
c.writeGSfile(device='pnggray', resolution=200)
