function startProgress() {
  let progress = 0;
  const progressText = document.getElementById("progressText");
  const progressCircle = document.getElementById("progressCircle");
  const progressLabel = document.getElementById("progressLabel");

  progressLabel.textContent = "TESTING...";

  const interval = setInterval(() => {
    progress++;
    progressText.textContent = progress + "%";
    progressCircle.style.background = `conic-gradient(#e26215 ${
      progress * 3.6
    }deg, #ddd ${progress * 3.6}deg)`;

    if (progress >= 100) {
      clearInterval(interval);
      progressLabel.textContent = "DONE!";
    }
  }, 50);
}
