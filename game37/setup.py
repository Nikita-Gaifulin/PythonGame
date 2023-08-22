import cx_Freeze

executables = [cx_Freeze.Executable("game37.py")]

cx_Freeze.setup(
    name = "Andrew simulator",
    options = {"build_exe": {"packages": ["pygame"],
                                           "include_files":["right_1.png",
                                                             "right_2.png",
                                                             "right_3.png",
                                                             "left_1.png",
                                                             "left_2.png",
                                                             "left_3.png",
                                                             "swim_right_1.png",
                                                             "swim_right_2.png",
                                                             "swim_right_3.png",
                                                             "swim_left_1.png",
                                                             "swim_left_2.png",
                                                             "swim_left_3.png",
                                                             "idle.png",
                                                             "idleRight.png",
                                                             "idle_swim_left.png",
                                                             "idle_swim_right.png",
                                                             "bulletWord.png",
                                                             "bulletWordLeft.png",
                                                             "background.jpg",
                                                             "background2.jpg",
                                                             "background3.jpg",
                                                             "background4.jpg",
                                                             "sale.png",
                                                             "badAndrew.png",
                                                             "boom.png",
                                                             "test.mp3"]}},
    executables = executables
)