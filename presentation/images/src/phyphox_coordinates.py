from pyx import bitmap, canvas, color, deco, path, text, unit

axiscolor = color.rgb(0.7, 0, 0)
i = bitmap.jpegimage("phyphox_measurement.jpg")
unit.set(vscale=10, wscale=10, xscale=10)
c = canvas.canvas()
c.insert(bitmap.bitmap(0, 0, i, compressmode=None))
c.stroke(path.line(40, 26, 40, 45), [axiscolor, deco.earrow])
c.text(41, 45, '$z$', [text.valign.top, axiscolor])
c.stroke(path.line(40, 26, 46, 10), [axiscolor, deco.earrow])
c.text(46.8, 10.5, '$x$', [axiscolor])
c.stroke(path.line(40, 26, 66, 32), [axiscolor, deco.earrow])
c.text(66, 33.5, '$y$', [text.halign.right, axiscolor])
c.writePDFfile()
