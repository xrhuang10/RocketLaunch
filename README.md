# Rocket Launch Project
As an avid fan of space exploration, I have always been curious about how rockets work, so I built a water bottle rocket and launched it with a pressure pump and some physics. This project was divided into two parts, a theoretical simulation, and an experimental launch.
<h2>Theoretical Simulation</h2>
<h3>Preface</h3>
<p>
  After building the rocket, I took down lots of data. With that data and knowledge from high school physics courses, I calculated the rocket's flight path, such as max height and flight duration. Then, to compare, I transformed the calculations into code. Instead of using calculus integration, I set dt to be a very small increment of time and ran those increments in Python, so the results would be similar.
</p>
<h3>Process</h3>
<p>
  The water bottle was simplified to a cylinder with a cone attached to the bottom. From the rocket equation, I derived the thrust and accelerations, and the rest was down to kinematics.
  The whole process was very confusing, because one factor would be dependent on many others. For example, the thrust depended on the exhaust speed, which depended on the cross-sectional water area and the bottle pressure, which in turn depended on the water height in the bottle...
  The measures that I took down were:
  <ul>
    <li>Radius of water bottle body - 0.054m</li>
    <li>Radius of water bottle cap - 0.011 m</li>
    <li>Mass of water poured into bottle - 0.8 kg</li>
    <li>Drag Coefficient - 0.77</li>
    <li>Angle of water bottle - 65.8 deg</li>
    <li>Height of conic section - 0.12 m</li>
    <li>Pressure pumped into bottle - 413685 Pa</li>
  </ul>
  Also, since this simulation was carried out through a real-life experiment later on, I set some general constants that reflected our physical world, such as g = 9.8 m/s^2, atmospheric pressure = 101300 Pa, water density = 1000 kg/m^3, and air density = 1.3 kg/m^3.
</p>
<h3>Results</h3>
<p>
  After running the Python program, I found that the rocket would theoretically land after 4.89 seconds, and reach its peak height of 28 meters at around the 2-second mark. I also noticed that at 0.087 seconds, the water would run out, causing the thrust, exhaust speed, and flow rate to all hit 0. The pressure would also stabilize at 101300 Pa, since the water would no longer be blocking the atmospheric pressure.
</p>

<h2>Experimental Launch</h2>
<h3>Preface</h3>
<p>
  After having carried out the Python program and the calculations, I went and launched the rocket with 413685 Pa of pressure. I tried my best to film the launch with a stable camera, so I could then process the video into a software called Tracker and analyze the flight trajectory.
</p>
<h3>Process</h3>
<p>
  Although the rocket did not go in a perfectly straight line upward, I was able to capture its entire path on camera. I uploaded the video on Tracker, and from that, set coordinate points at every 0.01 second. From that, I extracted times and y-positions (I ignored x-positions because it was probably due to wind or some other source of error).
  Between each time increment, using y/t, I found the velocities. From that, I could plot positions and velocities over time with Python.
  An issue that I had to correct with Python was that I did not start the video exactly at the launch time. The video had rolled for around 14 seconds before the rocket took off, so I offset the data by 14 seconds by setting the data points as arrays and iterating through them in Python.
</p>
<h3>Results</h3>
<p>
  From the results, the experimental launch was not smooth compared to the theoretical flight. The theoretical flight went much higher, by over 12m. I believe this can be attributed to a few sources of error:
  <ul>
    <li>The rocket did not stay head first throughout its path. By rotating onto its side (or flipping in the air), the drag coefficient increases drastically, which increases the air resistance, thus diminishing the overall acceleration on its upward trajectory.</li>
    <li>The water did not exit perfectly straight, since the air pumped into the bottle cannot be perfectly uniform. This caused the rocket to shake, which resulted in lots of energy being wasted; the x-motion took away from the y-motion</li>
    <li>External factors such as wind, heat, or atmospheric pressure may have caused disruptions.</li>
  </ul>
</p>


