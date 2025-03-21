$ README for wall drawing 123

  corrected error on line 51:

x + np.cumsum(np.random.uniform(-noise_factor, noise_factor, plot_height_mm))  # Add noise

  previous runtime error message shows:

knm@920:~/code/SolLeWitt/123$ python3 123_openai_002.py 
Traceback (most recent call last):
  File "/home/knm/code/SolLeWitt/123/123_openai_002.py", line 53, in <module>
    draw_wall_drawing_123(
  File "/home/knm/code/SolLeWitt/123/123_openai_002.py", line 34, in draw_wall_drawing_123
    x += np.cumsum(np.random.uniform(-noise_factor, noise_factor, plot_height_mm))  # Add noise
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
numpy.core._exceptions._UFuncOutputCastingError: Cannot cast ufunc 'add' output from dtype('float64') to dtype('int64') with casting rule 'same_kind'

  This appears to be fixed by changing the 'x += np...' to 'x + np...' not sure what it doing?


  Resonable 'canvas settings' appear to be around:

    num_lines=75, # 30 is to little and looks sparce this appears to be aroudn the max value given output.
    plot_height_mm=430, # Epson 5070 default output, fixed width of paper roll.
    plot_width_mm=430, # Make it square, I am printing it width as roll length 
    noise_factor=0.5, 
    dpi=600, 
    bg_color="white", # this doesn't work when set to black bg white fg
    line_color="black", 
    save_folder="drawings"

