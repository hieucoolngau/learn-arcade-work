import arcade

#open window
arcade.open_window(width=800,
                   height=600,
                   window_title="draw with func",
                   resizable=True)
arcade.set_background_color(arcade.csscolor.AQUAMARINE)
#gui
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(0,800,200,0,arcade.csscolor.AZURE)







#finish render
arcade.finish_render()
#run
arcade.run()
