
<!DOCTYPE html>
<html>
<head>
  <title>Gravitational Waves Traveling Through Earth</title>
  <style>
    body {
      margin: 0;
      overflow: hidden;
      background-color: black;
    }
    #canvas {
      display: block;
    }
  </style>
</head>
<body>
  <canvas id="canvas"></canvas>
  <script>
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    const width = window.innerWidth;
    const height = window.innerHeight;
    const centerX = width / 2;
    const centerY = height / 2;

    canvas.width = width;
    canvas.height = height;

    const radius = 100;
    let deformationFactorX = 1.0;
    let deformationFactorY = 1.0;
    let waveColorOffset = 0;

    function animate() {
      context.clearRect(0, 0, width, height);

      // Gravitational Waves
      
      const waveAmplitude = 50;
      const waveFrequency = 0.03;
      const waveSpeed = 2;
      for (let x = 0; x < width; x++) {
        const y = centerY + Math.sin(x * waveFrequency + Date.now() * 0.002 * waveSpeed) * waveAmplitude;

        const waveColor = `hsl(${waveColorOffset}, 100%, 50%)`;
        context.fillStyle = waveColor;
        context.fillRect(x, y, 1, 1);
      }

      // Earth
      
      const deformationAmplitude = 0.1;
      deformationFactorX = 1 + Math.sin(Date.now() * 0.001) * deformationAmplitude;
      deformationFactorY = 1 - Math.cos(Date.now() * 0.001) * deformationAmplitude;

      context.beginPath();
      context.ellipse(centerX, centerY, radius * deformationFactorX, radius * deformationFactorY, 0, 0, 2 * Math.PI);
      context.fillStyle = 'blue';
      context.fill();
      context.strokeStyle = 'blue';
      context.lineWidth = 2;
      context.stroke();

      waveColorOffset += 1; // Increment the wave color offset

      requestAnimationFrame(animate);
    }

    animate();
  </script>
</body>
</html>
