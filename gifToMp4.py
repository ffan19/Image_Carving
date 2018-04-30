import ffmpy

ff = ffmpy.FFmpeg(inputs={'carving_test1.gif': None}, outputs={'output.avi': None})
ff.run()