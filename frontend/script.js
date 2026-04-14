const fileUpload = document.getElementById("fileUpload");
const preview = document.getElementById("preview");

// Detect if we are running on Vercel or locally
const IS_PRODUCTION = window.location.hostname !== "localhost" && window.location.hostname !== "127.0.0.1";

// USE VERCEL PROXY IN PRODUCTION TO BYPASS CORS
// Browser -> Vercel (/api/predict) -> Render (https://.../predict)
const API_BASE_URL = IS_PRODUCTION ? "/api" : (import.meta.env.VITE_API_URL || "http://localhost:5000");
const PREDICT_URL = `${API_BASE_URL}/predict`;
const GENERATE_PDF_URL = `${API_BASE_URL}/generate_pdf`;

console.log("Environment:", IS_PRODUCTION ? "Production (Vercel Proxy)" : "Development");
console.log("API_BASE_URL:", API_BASE_URL);

let uploadedFile = null;

// Breed image URLs (reliable internet sources)
const BREED_IMAGES = {
  "dachshund": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Dachshund_Longhaired_001.jpg/1024px-Dachshund_Longhaired_001.jpg",
  "chihuahua": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Chihuahua1.jpg/1024px-Chihuahua1.jpg",
  "siberian_husky": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Siberian_Husky_blue_eyes_Flickr.jpg/1024px-Siberian_Husky_blue_eyes_Flickr.jpg",
  "golden_retriever": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Golden_Retriever.jpg/1024px-Golden_Retriever.jpg",
  "labrador_retriever": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Labrador_on_Quantock.jpg/1024px-Labrador_on_Quantock.jpg",
  "german_shepherd": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/German_Shepherd_-_DSC_4797.JPG/1024px-German_Shepherd_-_DSC_4797.JPG",
  "bulldog": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/English_Bulldog_ad1.jpg/1024px-English_Bulldog_ad1.jpg",
  "poodle": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Apricot_Standard_Poodle.jpg/1024px-Apricot_Standard_Poodle.jpg",
  "french_bulldog": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Frenchie_Isabella.JPG/1024px-Frenchie_Isabella.JPG",
  "beagle": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Beagle_4.jpg/1024px-Beagle_4.jpg",
  "rottweiler": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Rottweiler_standing.jpg/1024px-Rottweiler_standing.jpg",
  "yorkshire_terrier": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Yorkshireterrier_Groom.jpg/1024px-Yorkshireterrier_Groom.jpg"
};

function animateElement(
  el,
  { opacity = [0, 1], translateY = [20, 0], duration = 600, delay = 0 } = {}
) {
  el.animate(
    [
      { opacity: opacity[0], transform: `translateY(${translateY[0]}px)` },
      { opacity: opacity[1], transform: `translateY(${translateY[1]}px)` },
    ],
    {
      duration,
      delay,
      fill: "forwards",
      easing: "ease-out",
    }
  );
}


fileUpload.addEventListener("change", async function () {
  const file = this.files[0];
  if (!file) return;

  uploadedFile = file;

  // Show GOD MODE premium loading UI
  preview.innerHTML = `
    <div class="w-full h-96 flex flex-col items-center justify-center relative" id="loadingBox">
      <!-- Premium scanning container -->
      <div class="relative w-full max-w-md">
        <!-- Glow effect background -->
        <div class="absolute inset-0 bg-gradient-to-r from-[#e26215]/20 to-[#ff9a56]/20 blur-3xl rounded-3xl"></div>
        
        <!-- Main card -->
        <div class="relative bg-white/80 backdrop-blur-xl border border-white/60 rounded-3xl p-8 shadow-2xl">
          <!-- Header -->
          <div class="text-center mb-8">
            <h2 class="text-2xl font-bold text-[#2d1810] font-poppins mb-2">Analyzing Breed</h2>
            <p class="text-sm text-[#7a3f1a]/70">Advanced AI Recognition</p>
          </div>

          <!-- Animated scanner visualization -->
          <div class="relative h-32 mb-8 rounded-2xl bg-gradient-to-b from-[#e26215]/10 to-transparent border border-[#e26215]/20 overflow-hidden flex items-center justify-center">
            <!-- Scanning lines -->
            <div class="absolute inset-0 flex flex-col justify-around opacity-30">
              <div class="h-px bg-gradient-to-r from-transparent via-[#e26215] to-transparent animate-pulse"></div>
              <div class="h-px bg-gradient-to-r from-transparent via-[#e26215] to-transparent" style="animation: scan 2.5s ease-in-out infinite; animation-delay: 0.3s;"></div>
              <div class="h-px bg-gradient-to-r from-transparent via-[#e26215] to-transparent" style="animation: scan 2.5s ease-in-out infinite; animation-delay: 0.6s;"></div>
              <div class="h-px bg-gradient-to-r from-transparent via-[#e26215] to-transparent" style="animation: scan 2.5s ease-in-out infinite; animation-delay: 0.9s;"></div>
            </div>

            <!-- Center pulsing dot -->
            <div class="relative w-12 h-12 rounded-full bg-gradient-to-br from-[#e26215] to-[#ff9a56] shadow-lg" style="animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;">
              <div class="absolute inset-2 rounded-full bg-white/40 backdrop-blur-sm"></div>
              <div class="absolute inset-4 rounded-full bg-gradient-to-br from-[#e26215]/80 to-[#ff9a56]/80"></div>
            </div>

            <!-- Outer ring -->
            <div class="absolute inset-0 border-2 border-transparent bg-gradient-to-r from-[#e26215]/40 to-[#ff9a56]/40 rounded-2xl" style="animation: spin 3s linear infinite;"></div>
          </div>

          <!-- Progress bar - premium style -->
          <div class="space-y-3">
            <div class="flex justify-between items-end">
              <span class="text-xs uppercase tracking-widest font-bold text-[#2d1810] font-poppins">Processing</span>
              <span class="text-sm font-bold text-transparent bg-clip-text bg-gradient-to-r from-[#e26215] to-[#ff9a56]" id="progressPercent">0%</span>
            </div>
            <div class="relative h-2 bg-white/40 rounded-full overflow-hidden border border-white/60">
              <div id="progressBar" class="h-full bg-gradient-to-r from-[#e26215] via-[#ff9a56] to-[#e26215] rounded-full transition-all duration-300 shadow-lg shadow-[#e26215]/50" style="width: 0%; background-size: 200% 100%; animation: shimmer 2s infinite;" ></div>
            </div>
          </div>

          <!-- Status text -->
          <div class="text-center mt-6">
            <p class="text-sm text-[#7a3f1a]/60 font-medium">Scanning image...</p>
          </div>
        </div>
      </div>
    </div>
  `;

  // Add shimmer animation
  const style = document.createElement('style');
  style.textContent = \`
    @keyframes shimmer {
      0% { background-position: 200% 0; }
      50% { background-position: -200% 0; }
      100% { background-position: 200% 0; }
    }
    @keyframes scan {
      0% { transform: translateY(-100%); opacity: 0; }
      10% { opacity: 1; }
      90% { opacity: 1; }
      100% { transform: translateY(400%); opacity: 0; }
    }
  \`;
  document.head.appendChild(style);

  // Simulate progress
  let progress = 0;
  const progressInterval = setInterval(() => {
    if (progress < 90) {
      progress += Math.random() * 30;
      if (progress > 90) progress = 90;
    }
    document.getElementById("progressBar").style.width = progress + "%";
    document.getElementById("progressPercent").textContent = Math.round(progress) + "%";
  }, 200);

  const form = new FormData();
  form.append("image", file);

  try {
    const res = await fetch(PREDICT_URL, {
      method: "POST",
      body: form,
    });

    clearInterval(progressInterval);

    if (!res.ok) {
      const text = await res.text();
      preview.innerHTML = `<p class="text-red-600">Server error: ${text}</p>`;
      return;
    }

    const data = await res.json();

    if (data.error) {
      preview.innerHTML = `<p class="text-red-600">Error: ${data.error}</p>`;
      return;
    }

    if (!data.predictions || !data.predictions.length) {
      preview.innerHTML = `<p class="text-red-600">No predictions returned.</p>`;
      return;
    }

    // Complete progress
    document.getElementById("progressBar").style.width = "100%";
    document.getElementById("progressPercent").textContent = "100%";

    const top = data.predictions[0];
    const confidence = Math.round(top.confidence * 100);
    const desc = top.description || {
      short_desc: "No description available.",
      traits: [],
      fun_fact: "No fun fact available.",
    };
    const breedClean = top.breed.replace(/_/g, " ").toUpperCase();
    const breedKey = top.breed.toLowerCase();

    // Use internet image URL or fallback
    const breedImageUrl = BREED_IMAGES[breedKey] || `static/breed_examples/${top.breed}.jpg`;

    preview.innerHTML = `
      <div class="flex flex-col items-center gap-10 w-full max-w-[1000px] mt-12 mx-auto" id="resultBox">
        
        <div class="flex flex-col md:flex-row items-center justify-center gap-10 w-full">
            <div class="relative w-[180px] h-[180px] flex items-center justify-center flex-shrink-0">
                <svg class="absolute w-full h-full -rotate-90">
                    <circle cx="50%" cy="50%" r="80" stroke="#eee" stroke-width="12" fill="none"/>
                    <circle id="progressCircle" cx="50%" cy="50%" r="80"
                        stroke="#e26215" stroke-width="12" fill="none"
                        stroke-linecap="round" stroke-dasharray="502.4" stroke-dashoffset="502.4"
                        style="transition: stroke-dashoffset 1.5s ease-out"/>
                </svg>
                <div class="flex flex-col items-center">
                    <span class="text-4xl font-bold text-[#e26215]">${confidence}%</span>
                    <span class="text-sm font-semibold uppercase text-[#7a3f1a]">Match</span>
                </div>
            </div>

            <div class="flex flex-col items-center md:items-start text-center md:text-left gap-4">
                <h3 class="font-poppins font-extrabold text-[32px] md:text-[42px] text-[#e26215] leading-tight">
                    ${breedClean}
                </h3>
                <p class="text-[18px] text-[#555] max-w-[500px] leading-relaxed">
                    ${desc.short_desc}
                </p>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 w-full">
            <div class="bg-white p-8 rounded-2xl shadow-lg border border-[#eee]">
                <h4 class="font-bold text-[#e26215] text-xl mb-4 flex items-center gap-2">
                    <span class="material-symbols-outlined">pets</span> Key Traits
                </h4>
                <ul class="space-y-3">
                    ${(desc.traits || [])
                      .map(
                        (trait) => `
                        <li class="flex items-center gap-3 text-[#555]">
                            <span class="w-2 h-2 bg-[#e26215] rounded-full"></span>
                            ${trait}
                        </li>
                    `
                      )
                      .join("")}
                </ul>
            </div>

            <div class="bg-[#fef9f6] p-8 rounded-2xl shadow-lg border border-[#fbd6bc]">
                <h4 class="font-bold text-[#e26215] text-xl mb-4 flex items-center gap-2">
                    <span class="material-symbols-outlined">lightbulb</span> Fun Fact
                </h4>
                <p class="text-[#7a3f1a] italic leading-relaxed">
                    "${desc.fun_fact}"
                </p>
            </div>
        </div>

        <div class="flex flex-col items-center gap-6 mt-4">
             <img id="breedImage" src="${breedImageUrl}" alt="${breedClean}"
                onerror="this.src='images/logo.png'"
                class="w-[400px] h-[260px] object-cover rounded-2xl shadow-xl border-4 border-[#e26215]" />
            
            <button id="generatePdfBtn" data-breed="${breedClean}"
                class="btn-ghost font-poppins font-bold text-[18px] px-10 py-4 rounded-full border-4 border-[#e26215] bg-transparent text-[#e26215] transition-all hover:bg-[#e26215] hover:text-white flex items-center justify-center gap-3">
                <span class="material-symbols-outlined hidden" id="pdfSpinner">autorenew</span>
                <span id="pdfBtnText">📄 GENERATE PDF REPORT</span>
            </button>
        </div>

      </div>
    `;

    document
      .getElementById("generatePdfBtn")
      .addEventListener("click", async function () {
        const breed = this.getAttribute("data-breed");
        const btnText = document.getElementById("pdfBtnText");
        const spinner = document.getElementById("pdfSpinner");

        btnText.innerText = "GENERATING...";
        spinner.classList.add("animate-spin");
        spinner.classList.remove("hidden");
        this.disabled = true;
        this.classList.add("opacity-50", "cursor-not-allowed");

        try {
          const pdfRes = await fetch(GENERATE_PDF_URL, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ breed }),
          });

          const pdfData = await pdfRes.json();

          if (pdfData.pdf_url) {
            window.open(pdfData.pdf_url, "_blank");
          } else {
            alert("Failed to generate PDF: " + (pdfData.error || "Unknown error"));
          }
        } catch (e) {
          console.error(e);
          alert("Error connecting to PDF generator.");
        } finally {
          btnText.innerText = "📄 GENERATE PDF REPORT";
          spinner.classList.remove("animate-spin");
          spinner.classList.add("hidden");
          this.disabled = false;
          this.classList.remove("opacity-50", "cursor-not-allowed");
        }
      });

    setTimeout(() => {
      const circle = document.getElementById("progressCircle");
      const circumference = 502.4;
      const offset = circumference - (confidence / 100) * circumference;
      circle.style.strokeDashoffset = offset;
    }, 100);

    animateElement(document.getElementById("resultBox"), {
      opacity: [0, 1],
      translateY: [30, 0],
    });
  } catch (err) {
    console.error(err);
    preview.innerHTML = `<p class="text-red-600">Failed to connect to backend.</p>`;
  }
});