const fileUpload = document.getElementById("fileUpload");
const preview = document.getElementById("preview");

// Detect if we are running on Vercel or locally
const IS_PRODUCTION = window.location.hostname !== "localhost" && window.location.hostname !== "127.0.0.1";

// USE VERCEL PROXY IN PRODUCTION TO BYPASS CORS
const API_BASE_URL = IS_PRODUCTION ? "/api" : (import.meta.env.VITE_API_URL || "http://localhost:5000");
const PREDICT_URL = `${API_BASE_URL}/predict`;
const GENERATE_PDF_URL = `${API_BASE_URL}/generate_pdf`;

let uploadedFile = null;

// Fallback image map for key breeds if backend doesn't provide one
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
  if (!el) return;
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

  // Add premium animation styles
  if (!document.getElementById('pawprint-premium-animations')) {
    const style = document.createElement('style');
    style.id = 'pawprint-premium-animations';
    style.textContent = `
      @keyframes premium-scan {
        0% { transform: translateY(-10px); opacity: 0; }
        50% { opacity: 1; }
        100% { transform: translateY(180px); opacity: 0; }
      }
      @keyframes pulse-ring {
        0% { transform: scale(0.8); opacity: 0.5; }
        100% { transform: scale(1.2); opacity: 0; }
      }
      .glitch-text {
        text-shadow: 0.05em 0 0 rgba(226, 98, 21, 0.75), -0.025em -0.05em 0 rgba(241, 90, 36, 0.75);
        animation: glitch 500ms infinite;
      }
      @keyframes glitch {
        0% { text-shadow: 0.05em 0 0 rgba(226, 98, 21, 0.75), -0.025em -0.05em 0 rgba(241, 90, 36, 0.75); }
        50% { text-shadow: -0.05em -0.025em 0 rgba(226, 98, 21, 0.75), 0.025em 0.025em 0 rgba(241, 90, 36, 0.75); }
        100% { text-shadow: 0.025em 0.05em 0 rgba(226, 98, 21, 0.75), 0.05em 0 0 rgba(241, 90, 36, 0.75); }
      }
    `;
    document.head.appendChild(style);
  }

  // Show GOD MODE premium loading UI (Compact)
  preview.innerHTML = `
    <div class="w-full py-8 flex flex-col items-center justify-center" id="loadingBox">
      <div class="relative w-full max-w-md bg-white/90 backdrop-blur-xl border border-white/60 rounded-[2rem] p-8 shadow-xl overflow-hidden">
        <div class="text-center mb-6 relative z-10">
          <div class="inline-block px-3 py-1 rounded-full bg-[#e26215]/10 text-[#e26215] text-[9px] font-bold tracking-[0.2em] uppercase mb-2">Neural Engine Active</div>
          <h2 class="text-2xl font-black text-[#2d1810] font-poppins tracking-tight">AI BIOMETRIC SCAN</h2>
        </div>

        <div class="relative h-48 mb-6 rounded-2xl bg-[#1a0f08] border border-white/10 overflow-hidden flex items-center justify-center">
          <div class="absolute inset-0 bg-[linear-gradient(to_right,#e2621510_1px,transparent_1px),linear-gradient(to_bottom,#e2621510_1px,transparent_1px)] bg-[size:15px_15px]"></div>
          <div class="absolute inset-0">
            <div class="h-[2px] w-full bg-gradient-to-r from-transparent via-[#e26215] to-transparent shadow-[0_0_10px_#e26215]" style="animation: premium-scan 2s ease-in-out infinite;"></div>
          </div>
          <div class="relative z-10 flex flex-col items-center">
            <div class="w-16 h-16 rounded-full border border-[#e26215]/30 flex items-center justify-center relative">
              <div class="absolute inset-0 rounded-full border border-[#e26215]/50" style="animation: pulse-ring 2s infinite;"></div>
              <span class="material-symbols-outlined text-[#e26215] text-2xl animate-pulse">pets</span>
            </div>
          </div>
        </div>

        <div class="space-y-3 relative z-10">
          <div class="flex justify-between items-end">
            <span class="text-[10px] text-[#e26215] font-bold" id="statusMsg">Optimizing Weights...</span>
            <span class="text-2xl font-black text-[#2d1810] font-poppins" id="progressPercent">0%</span>
          </div>
          <div class="relative h-2 bg-[#1a0f08]/5 rounded-full overflow-hidden">
            <div id="progressBar" class="h-full bg-gradient-to-r from-[#e26215] to-[#f15a24] rounded-full transition-all duration-500" style="width: 0%;"></div>
          </div>
        </div>
      </div>
    </div>
  `;

  const statusMsgs = ["Initializing...", "Extracting Features...", "Cross-referencing...", "Analyzing...", "Finalizing..."];
  let progress = 0;
  let msgIdx = 0;
  const progressInterval = setInterval(() => {
    if (progress < 92) {
      progress += Math.random() * 15;
      if (progress > 92) progress = 92;
      msgIdx = Math.min(Math.floor((progress / 100) * statusMsgs.length), statusMsgs.length - 1);
      document.getElementById("statusMsg").textContent = statusMsgs[msgIdx];
    }
    document.getElementById("progressBar").style.width = progress + "%";
    document.getElementById("progressPercent").textContent = Math.round(progress) + "%";
  }, 250);

  const form = new FormData();
  form.append("image", file);

  try {
    const res = await fetch(PREDICT_URL, { method: "POST", body: form });
    clearInterval(progressInterval);

    if (!res.ok) {
      preview.innerHTML = `<p class="text-red-600 font-bold p-6 bg-white rounded-2xl">Server error: ${res.status}</p>`;
      return;
    }

    const data = await res.json();
    if (data.error || !data.predictions?.length) {
      preview.innerHTML = `<p class="text-red-600 font-bold p-6 bg-white rounded-2xl">Error: ${data.error || "No match"}</p>`;
      return;
    }

    document.getElementById("progressBar").style.width = "100%";
    document.getElementById("progressPercent").textContent = "100%";
    await new Promise(r => setTimeout(r, 400));

    const top = data.predictions[0];
    const confidence = Math.round(top.confidence * 100);
    const desc = top.description || {};
    const breedClean = top.breed.replace(/_/g, " ").toUpperCase();
    const breedKey = top.breed.toLowerCase();

    // IMAGE LOGIC: Backend > Map > Local
    const breedImageUrl = desc.image_url || BREED_IMAGES[breedKey] || `static/breed_examples/${top.breed}.jpg`;

    // Professional Layout (Compact & Clean)
    preview.innerHTML = `
      <div class="flex flex-col items-center gap-6 w-full max-w-4xl mx-auto py-6" id="resultBox" style="opacity: 0">
        
        <!-- Header: Confirmed Identity -->
        <div class="w-full bg-white/80 backdrop-blur-lg border border-white/60 rounded-[2rem] p-6 md:p-8 shadow-lg flex flex-col md:flex-row items-center gap-6">
          <div class="flex-1 text-center md:text-left">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#e26215]/10 text-[#e26215] text-[9px] font-black tracking-widest uppercase mb-3">Identity Confirmed</div>
            <h2 class="font-poppins font-black text-3xl md:text-4xl text-[#2d1810] leading-tight mb-3 glitch-text">${breedClean}</h2>
            <p class="text-[#8a4f2a]/80 text-sm md:text-base leading-relaxed line-clamp-3">${desc.short_desc || "No description available."}</p>
          </div>
          
          <div class="relative w-32 h-32 flex items-center justify-center shrink-0">
            <svg class="absolute w-full h-full -rotate-90" viewBox="0 0 100 100">
              <circle cx="50" cy="50" r="45" stroke="rgba(226,98,21,0.1)" stroke-width="8" fill="none"/>
              <circle id="progressCircle" cx="50" cy="50" r="45" stroke="#e26215" stroke-width="8" fill="none" stroke-linecap="round" stroke-dasharray="283" stroke-dashoffset="283" style="transition: stroke-dashoffset 1.5s ease-out"/>
            </svg>
            <div class="flex flex-col items-center">
              <span class="text-3xl font-black text-[#2d1810]">${confidence}%</span>
              <span class="text-[8px] uppercase font-bold text-[#e26215]">Precision</span>
            </div>
          </div>
        </div>

        <!-- Content Grid: Image & Details -->
        <div class="w-full grid grid-cols-1 md:grid-cols-2 gap-6">
          <div class="rounded-3xl overflow-hidden shadow-lg border-2 border-white h-64 md:h-80">
            <img src="${breedImageUrl}" alt="${breedClean}" class="w-full h-full object-cover" onerror="this.src='images/logo.png'">
          </div>

          <div class="flex flex-col gap-4">
            <div class="bg-white/60 backdrop-blur-md rounded-2xl p-5 border border-white/40 shadow-sm flex-1">
              <h3 class="text-[10px] font-black text-[#e26215] uppercase tracking-widest mb-4">Biometric Data</h3>
              <div class="grid grid-cols-2 gap-4">
                <div><span class="text-[9px] text-gray-400 uppercase block">Origin</span><p class="text-xs font-bold text-[#2d1810]">${desc.origin || "Unknown"}</p></div>
                <div><span class="text-[9px] text-gray-400 uppercase block">Size</span><p class="text-xs font-bold text-[#2d1810]">${desc.size || "Standard"}</p></div>
                <div class="col-span-2"><span class="text-[9px] text-gray-400 uppercase block">Temperament</span><p class="text-xs font-bold text-[#2d1810]">${desc.temperament || "Varies"}</p></div>
              </div>
            </div>
            
            <div class="bg-[#1a0f08] rounded-2xl p-5 text-white shadow-md">
              <h3 class="text-[10px] font-black text-[#e26215] uppercase tracking-widest mb-2">Health Protocol</h3>
              <p class="text-[11px] text-gray-300 leading-relaxed">${desc.health_notes || "Regular veterinary checkups recommended."}</p>
            </div>
          </div>
        </div>

        <!-- Traits & Action -->
        <div class="w-full flex flex-col md:flex-row items-center gap-4">
          <div class="bg-[#fef9f6] rounded-2xl p-5 border border-[#e26215]/10 flex-1 w-full">
            <h3 class="text-[10px] font-black text-[#2d1810] uppercase mb-3">Core Traits</h3>
            <div class="flex flex-wrap gap-2">
              ${(desc.traits || ["Loyal", "Intelligent"]).map(t => `<span class="px-3 py-1 bg-white border border-[#e26215]/20 rounded-lg text-[10px] font-bold text-[#2d1810]">${t}</span>`).join("")}
            </div>
          </div>
          
          <button id="generatePdfBtn" data-breed="${breedClean}" class="w-full md:w-auto bg-[#2d1810] text-white px-8 py-4 rounded-2xl font-black text-xs tracking-widest hover:bg-[#e26215] transition-all flex items-center justify-center gap-3">
            <span class="material-symbols-outlined text-lg" id="pdfSpinner">description</span>
            GENERATE ANALYTICAL REPORT
          </button>
        </div>
      </div>
    `;

    document.getElementById("generatePdfBtn").addEventListener("click", async function () {
      const breed = this.getAttribute("data-breed");
      const spinner = document.getElementById("pdfSpinner");
      spinner.classList.add("animate-spin");
      spinner.innerText = "sync";
      this.disabled = true;

      try {
        const pdfRes = await fetch(GENERATE_PDF_URL, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ breed })
        });
        const pdfData = await pdfRes.json();
        if (pdfData.pdf_url) window.open(pdfData.pdf_url, "_blank");
        else alert("Export failed.");
      } catch (e) {
        alert("Network error.");
      } finally {
        spinner.classList.remove("animate-spin");
        spinner.innerText = "description";
        this.disabled = false;
      }
    });

    setTimeout(() => {
      const circle = document.getElementById("progressCircle");
      if (circle) circle.style.strokeDashoffset = 283 - (confidence / 100) * 283;
    }, 100);

    animateElement(document.getElementById("resultBox"), { opacity: [0, 1], translateY: [30, 0] });
  } catch (err) {
    clearInterval(progressInterval);
    preview.innerHTML = `<p class="text-red-600 font-bold p-6 bg-white rounded-2xl text-center">Connection Lost</p>`;
  }
});
