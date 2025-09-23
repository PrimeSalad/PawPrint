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
fileUpload.addEventListener("change", function () {
  const file = this.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = function (e) {
      // Show uploaded image & results in two-column layout
      preview.innerHTML = `
        <div class="flex flex-col md:flex-row items-center justify-between gap-12 w-full max-w-[1000px] mt-12">
          
          <!-- LEFT SIDE: Progress + Info -->
          <div class="flex flex-col items-center md:items-start gap-6 text-center md:text-left max-w-[450px]">
            
            <!-- Progress Circle -->
            <div class="relative w-[170px] h-[170px] flex items-center justify-center">
              <svg class="absolute w-full h-full -rotate-90">
                <circle cx="50%" cy="50%" r="78" stroke="#ddd" stroke-width="15" fill="none"/>
                <circle id="progressCircle" cx="50%" cy="50%" r="78" 
                  stroke="#e26215" stroke-width="15" fill="none"
                  stroke-linecap="round" stroke-dasharray="490" stroke-dashoffset="490"/>
              </svg>
              <span id="progressText" class="text-4xl font-bold text-[#7a3f1a]">0%</span>
            </div>

            <!-- Breed Info -->
            <div>
              <h3 class="font-poppins font-extrabold text-[26px] text-[#e26215] mb-3">
                GOLDEN RETRIEVER
              </h3>
              <p class="italic text-[#555] text-[16px] leading-[1.7]">
                The Golden Retriever is a Scottish breed of retriever dog of medium size. 
                It is characterised by a gentle and affectionate nature and a striking golden coat. 
                It is a working dog, and registration is subject to successful completion of a working trial.
              </p>
            </div>
          </div>

          <!-- RIGHT SIDE: Uploaded Image -->
          <div class="flex flex-col items-center gap-5">
            <img src="${e.target.result}" alt="Uploaded Dog" 
              class="w-[350px] h-[220px] object-cover rounded-xl shadow-md border-2 border-[#e26215]" />
            
            <p class="text-[14px] italic text-[#555] max-w-[350px] text-center leading-relaxed">
              Breed predictions are generated through AI image recognition. 
              They may not always reflect your dog's exact genetic background. 
              For verified results, seek professional testing from a vet or certified provider.
            </p>

            <a href="#" 
              class="btn-ghost font-poppins font-bold text-[18px] px-8 py-3 rounded-full border-4 border-[#e26215] bg-transparent text-[#e26215] no-underline inline-block transition-all duration-150 hover:-translate-y-1 hover:bg-[#e26215] hover:text-white hover:border-[#cc500f]">
              DOWNLOAD REPORT
            </a>
          </div>

        </div>
      `;

      // Animate progress bar (example: 90%)
      let percent = 0;
      const target = 90;
      const circle = document.getElementById("progressCircle");
      const text = document.getElementById("progressText");
      const circumference = 490;

      const interval = setInterval(() => {
        if (percent >= target) {
          clearInterval(interval);
        } else {
          percent++;
          text.textContent = percent + "%";
          const offset = circumference - (percent / 100) * circumference;
          circle.style.strokeDashoffset = offset;
        }
      }, 20);
    };
    reader.readAsDataURL(file);
  }
});
