const fileUpload = document.getElementById("fileUpload");
const preview = document.getElementById("preview");

// Detect if we are running on Vercel or locally
const IS_PRODUCTION = window.location.hostname !== "localhost" && window.location.hostname !== "127.0.0.1";

// USE VERCEL PROXY IN PRODUCTION TO BYPASS CORS
const API_BASE_URL = IS_PRODUCTION ? "/api" : (import.meta.env.VITE_API_URL || "http://localhost:5000");
const PREDICT_URL = `${API_BASE_URL}/predict`;
const GENERATE_PDF_URL = `${API_BASE_URL}/generate_pdf`;

console.log("Environment:", IS_PRODUCTION ? "Production (Vercel Proxy)" : "Development");

let uploadedFile = null;

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

function animateElement(el, { opacity = [0, 1], translateY = [20, 0], duration = 600, delay = 0 } = {}) {
  el.animate(
    [
      { opacity: opacity[0], transform: `translateY(${translateY[0]}px)` },
      { opacity: opacity[1], transform: `translateY(${translateY[1]}px)` },
    ],
    { duration, delay, fill: "forwards", easing: "ease-out" }
  );
}

fileUpload.addEventListener("change", async function () {
  const file = this.files[0];
  if (!file) return;
  uploadedFile = file;

  if (!document.getElementById('pawprint-premium-animations')) {
    const style = document.createElement('style');
    style.id = 'pawprint-premium-animations';
    style.textContent = `
      @keyframes premium-scan {
        0% { transform: translateY(-20px); opacity: 0; }
        50% { opacity: 1; }
        100% { transform: translateY(280px); opacity: 0; }
      }
      @keyframes pulse-ring {
        0% { transform: scale(0.8); opacity: 0.5; }
        100% { transform: scale(1.2); opacity: 0; }
      }
      .glitch-text {
        text-shadow: 0.05em 0 0 rgba(226, 98, 21, 0.75), -0.025em -0.05em 0 rgba(241, 90, 36, 0.75), 0.025em 0.05em 0 rgba(122, 63, 26, 0.75);
        animation: glitch 500ms infinite;
      }
      @keyframes glitch {
        0% { text-shadow: 0.05em 0 0 rgba(226, 98, 21, 0.75), -0.025em -0.05em 0 rgba(241, 90, 36, 0.75), 0.025em 0.05em 0 rgba(122, 63, 26, 0.75); }
        15% { text-shadow: -0.05em -0.025em 0 rgba(226, 98, 21, 0.75), 0.025em 0.025em 0 rgba(241, 90, 36, 0.75), -0.05em -0.05em 0 rgba(122, 63, 26, 0.75); }
        50% { text-shadow: 0.025em 0.05em 0 rgba(226, 98, 21, 0.75), 0.05em 0 0 rgba(241, 90, 36, 0.75), 0 -0.05em 0 rgba(122, 63, 26, 0.75); }
        100% { text-shadow: -0.025em 0 0 rgba(226, 98, 21, 0.75), -0.025em -0.025em 0 rgba(241, 90, 36, 0.75), -0.025em -0.05em 0 rgba(122, 63, 26, 0.75); }
      }
    `;
    document.head.appendChild(style);
  }

  preview.innerHTML = `
    <div class="w-full py-8 md:py-12 flex flex-col items-center justify-center relative" id="loadingBox">
      <div class="relative w-full max-w-xl px-4">
        <div class="relative bg-white/90 backdrop-blur-2xl border border-white/60 rounded-[2rem] md:rounded-[3rem] p-6 md:p-10 shadow-[0_30px_100px_-20px_rgba(226,98,21,0.2)] overflow-hidden">
          <div class="text-center mb-8 relative z-10">
            <div class="inline-block px-4 py-1.5 rounded-full bg-[#e26215]/10 text-[#e26215] text-[10px] font-bold tracking-[0.2em] uppercase mb-4">Neural Engine Active</div>
            <h2 class="text-2xl md:text-4xl font-black text-[#2d1810] font-poppins mb-3 tracking-tight">AI BIOMETRIC SCAN</h2>
            <p class="text-[#7a3f1a]/60 text-sm md:text-base font-medium">Decoding canine DNA markers...</p>
          </div>
          <div class="relative h-60 md:h-80 mb-8 rounded-[1.5rem] md:rounded-[2.5rem] bg-[#1a0f08] border border-white/10 overflow-hidden flex items-center justify-center shadow-inner">
            <div class="absolute inset-0 bg-[linear-gradient(to_right,#e2621510_1px,transparent_1px),linear-gradient(to_bottom,#e2621510_1px,transparent_1px)] bg-[size:20px_20px]"></div>
            <div class="absolute inset-0 flex flex-col justify-around">
              <div class="h-[2px] w-full bg-gradient-to-r from-transparent via-[#e26215] to-transparent shadow-[0_0_20px_#e26215]" style="animation: premium-scan 2s ease-in-out infinite;"></div>
            </div>
            <div class="relative z-10 flex flex-col items-center">
              <div class="w-24 h-24 md:w-32 md:h-32 rounded-full border-2 border-[#e26215]/30 flex items-center justify-center relative">
                <div class="absolute inset-0 rounded-full border border-[#e26215]/50" style="animation: pulse-ring 2s infinite;"></div>
                <span class="material-symbols-outlined absolute text-[#e26215] text-3xl md:text-4xl animate-pulse">pets</span>
              </div>
              <div class="mt-6 font-mono text-[9px] md:text-[11px] text-[#e26215]/80 tracking-[0.4em] uppercase font-bold">DNA Sequencing</div>
            </div>
          </div>
          <div class="space-y-4 relative z-10">
            <div class="flex justify-between items-end px-2">
              <div class="flex flex-col">
                <span class="text-[9px] md:text-[10px] uppercase tracking-[0.2em] font-black text-[#2d1810]">Confidence</span>
                <span class="text-[11px] md:text-[12px] text-[#e26215] font-bold" id="statusMsg">Optimizing...</span>
              </div>
              <span class="text-3xl md:text-4xl font-black text-[#2d1810] font-poppins" id="progressPercent">0%</span>
            </div>
            <div class="relative h-3 md:h-4 bg-[#1a0f08]/5 rounded-full overflow-hidden p-1">
              <div id="progressBar" class="h-full bg-gradient-to-r from-[#e26215] to-[#f15a24] rounded-full transition-all duration-500" style="width: 0%"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  `;

  const statusMsgs = ["Initializing...", "Extracting Vectors...", "Cross-referencing...", "Analyzing Morph...", "Calculating...", "Synthesizing..."];
  let progress = 0;
  let msgIdx = 0;
  const progressInterval = setInterval(() => {
    if (progress < 92) {
      progress += Math.random() * 15;
      if (progress > 92) progress = 92;
      if (progress > (msgIdx + 1) * 15 && msgIdx < statusMsgs.length - 1) {
        msgIdx++;
        document.getElementById("statusMsg").textContent = statusMsgs[msgIdx];
      }
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
      preview.innerHTML = `<p class="text-red-600 font-bold p-8 bg-white rounded-3xl shadow-xl">Connection issue.</p>`;
      return;
    }
    const data = await res.json();
    if (data.error || !data.predictions || !data.predictions.length) {
      preview.innerHTML = `<p class="text-red-600 font-bold p-8 bg-white rounded-3xl shadow-xl">No markers detected.</p>`;
      return;
    }

    document.getElementById("progressBar").style.width = "100%";
    document.getElementById("progressPercent").textContent = "100%";
    await new Promise(r => setTimeout(r, 600));

    const top = data.predictions[0];
    const confidence = Math.round(top.confidence * 100);
    const desc = top.description || { short_desc: "Synthesizing data...", traits: ["Unique"], fun_fact: "Unique signature." };
    const breedClean = top.breed.replace(/_/g, " ").toUpperCase();
    
    const localImageUrl = `breed_examples/${top.breed}.jpg`;
    const backendImageUrl = desc.image_url;
    const breedKey = top.breed.toLowerCase().replace(/-/g, "_");
    const mapImageUrl = BREED_IMAGES[breedKey];

    preview.innerHTML = `
      <div class="flex flex-col items-center w-full max-w-6xl mx-auto py-4 md:py-8 px-4" id="resultBox">
        <div class="relative w-full rounded-[2rem] md:rounded-[3.5rem] bg-white/70 backdrop-blur-2xl border border-white shadow-[0_20px_60px_-20px_rgba(226,98,21,0.2)] overflow-hidden">
          
          <!-- Header -->
          <div class="p-6 md:p-12 lg:p-16 border-b border-white grid grid-cols-1 md:grid-cols-[1fr_auto] items-center gap-8 md:gap-16 relative overflow-hidden bg-gradient-to-br from-white to-transparent">
            <div class="text-center md:text-left z-10 order-2 md:order-1">
              <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#e26215]/10 text-[#e26215] text-[8px] md:text-[11px] font-black tracking-[0.2em] uppercase mb-4 shadow-sm border border-[#e26215]/20">Match Found</div>
              <h2 class="font-poppins font-black text-3xl md:text-6xl lg:text-8xl mb-4 text-[#2d1810] tracking-tighter uppercase glitch-text leading-[1.1] drop-shadow-sm">${breedClean}</h2>
              <p class="text-[#8a4f2a] text-sm md:text-xl lg:text-2xl leading-relaxed font-medium opacity-90 max-w-3xl">${desc.short_desc}</p>
            </div>
            <div class="flex justify-center md:justify-end z-10 order-1 md:order-2">
              <div class="relative w-32 h-32 md:w-52 md:h-52 lg:w-60 lg:h-60 flex items-center justify-center">
                <div class="absolute inset-0 bg-gradient-to-br from-[#e26215]/20 to-[#f15a24]/20 rounded-full blur-xl animate-pulse"></div>
                <svg class="absolute w-full h-full -rotate-90" viewBox="0 0 200 200">
                  <circle cx="100" cy="100" r="85" stroke="rgba(226,98,21,0.1)" stroke-width="12" fill="none"/>
                  <circle id="progressCircle" cx="100" cy="100" r="85" stroke="url(#grad1)" stroke-width="12" fill="none" stroke-linecap="round" stroke-dasharray="534" stroke-dashoffset="534" style="transition: stroke-dashoffset 2s cubic-bezier(0.4, 0, 0.2, 1)"/>
                  <defs><linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" style="stop-color:#e26215"/><stop offset="100%" style="stop-color:#f15a24"/></linearGradient></defs>
                </svg>
                <div class="flex flex-col items-center relative z-10">
                  <span class="text-3xl md:text-6xl lg:text-7xl font-black text-[#2d1810] font-poppins">${confidence}%</span>
                  <span class="text-[8px] md:text-[12px] uppercase tracking-[0.2em] font-bold text-[#e26215]">Precision</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Content -->
          <div class="p-6 md:p-12 grid grid-cols-1 lg:grid-cols-12 gap-8 md:gap-12 items-stretch bg-white/30">
            <div class="lg:col-span-8 relative rounded-[1.5rem] md:rounded-[3rem] overflow-hidden shadow-xl border-2 md:border-4 border-white aspect-[4/3] md:aspect-[16/9] lg:aspect-auto min-h-[300px] md:min-h-[550px] bg-gray-50">
              <div id="imageSpinner" class="absolute inset-0 flex flex-col items-center justify-center gap-3 z-0 bg-gray-50/50">
                 <span class="material-symbols-outlined animate-spin text-4xl text-[#e26215]/30">sync</span>
              </div>
              <img id="breedImage" src="${localImageUrl}" alt="${breedClean}" onload="document.getElementById('imageSpinner').style.display='none'" onerror="this.onerror=null; this.src='${backendImageUrl || mapImageUrl || 'images/logo.png'}'; if(this.src.includes('logo.png')) document.getElementById('imageSpinner').style.display='none';" class="absolute inset-0 w-full h-full object-cover z-10" />
              <div class="absolute inset-0 bg-gradient-to-t from-[#2d1810]/80 via-transparent to-transparent z-20"></div>
              <div class="absolute bottom-4 left-4 right-4 md:bottom-8 md:left-8 md:right-8 z-30">
                 <div class="px-4 py-3 md:px-8 md:py-5 rounded-[1.2rem] md:rounded-[2rem] bg-[#1a0f08]/60 backdrop-blur-xl border border-white/20 text-white flex items-center justify-between">
                   <span class="text-[9px] md:text-[12px] font-black uppercase tracking-[0.2em]">Visual Match</span>
                   <span class="text-xs md:text-lg font-mono font-bold text-[#ff9a56]">#${Math.floor(Math.random()*9000)+1000}</span>
                 </div>
              </div>
            </div>

            <div class="lg:col-span-4 flex flex-col gap-4 md:gap-6">
              <div class="grid grid-cols-1 gap-4">
                <div class="bg-white rounded-2xl md:rounded-3xl p-5 md:p-8 border border-white/60 shadow-sm">
                  <span class="text-[8px] md:text-[10px] uppercase tracking-[0.2em] font-black text-[#e26215] block mb-1">Origin</span>
                  <span class="text-base md:text-xl font-bold text-[#2d1810]">${desc.origin || "Global"}</span>
                </div>
                <div class="bg-white rounded-2xl md:rounded-3xl p-5 md:p-8 border border-white/60 shadow-sm">
                  <span class="text-[8px] md:text-[10px] uppercase tracking-[0.2em] font-black text-[#e26215] block mb-1">Biometrics</span>
                  <span class="text-base md:text-xl font-bold text-[#2d1810]">${desc.size || "Standard"}</span>
                </div>
              </div>
              <div class="bg-white rounded-2xl md:rounded-3xl p-5 md:p-8 border border-white/60 shadow-sm flex-1">
                <span class="text-[8px] md:text-[10px] uppercase tracking-[0.2em] font-black text-[#e26215] block mb-1">Temperament</span>
                <span class="text-base font-bold text-[#2d1810] leading-relaxed">${desc.temperament || "Alert"}</span>
              </div>
              <div class="bg-gradient-to-br from-[#fef9f6] to-white rounded-2xl md:rounded-3xl p-5 md:p-8 border border-[#e26215]/10">
                <div class="flex flex-wrap gap-2">
                  ${(desc.traits || []).map(trait => `<span class="px-3 py-1 bg-[#e26215]/10 text-[#e26215] rounded-lg text-[9px] font-black tracking-widest uppercase border border-[#e26215]/20">${trait}</span>`).join("")}
                </div>
              </div>
              <div class="bg-gradient-to-br from-[#1a0f08] to-[#2d1810] rounded-2xl md:rounded-3xl p-5 md:p-8 text-white shadow-xl relative overflow-hidden">
                <h4 class="font-poppins font-black text-[9px] md:text-[11px] mb-2 uppercase text-[#e26215]">Health Protocol</h4>
                <p class="text-white/80 text-xs md:text-sm font-medium relative z-10">${desc.health_notes || "Regular veterinary diagnostics recommended."}</p>
              </div>
            </div>
          </div>
        </div>

        <div class="w-full flex flex-col items-center gap-4 mt-6 px-4">
          <button id="generatePdfBtn" data-breed="${breedClean}" class="w-full md:w-auto group relative font-poppins font-black text-xs md:text-sm px-8 md:px-12 py-4 md:py-5 rounded-full bg-[#2d1810] text-white shadow-2xl overflow-hidden uppercase tracking-widest">
            <div class="absolute inset-0 bg-gradient-to-r from-[#e26215] to-[#f15a24] opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
            <div class="relative z-10 flex items-center justify-center gap-3">
              <span class="material-symbols-outlined text-lg md:text-xl" id="pdfSpinner">description</span>
              <span id="pdfBtnText">Generate Report</span>
            </div>
          </button>
          <p class="text-[7px] md:text-[9px] text-[#8a4f2a]/50 uppercase tracking-[0.3em] font-bold text-center">Encrypted Data Stream • ISO-2026 Compliant</p>
        </div>
      </div>
    `;

    document.getElementById("generatePdfBtn").addEventListener("click", async function () {
      const breed = this.getAttribute("data-breed");
      const btnText = document.getElementById("pdfBtnText");
      const spinner = document.getElementById("pdfSpinner");
      btnText.innerText = "SYNTHESIZING...";
      spinner.classList.add("animate-spin");
      this.disabled = true;
      try {
        const pdfRes = await fetch(GENERATE_PDF_URL, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ breed }) });
        const pdfData = await pdfRes.json();
        if (pdfData.pdf_url) window.open(pdfData.pdf_url, "_blank");
        else alert("Export Failed.");
      } catch (e) { alert("Network Error."); } finally {
        btnText.innerText = "Generate Report";
        spinner.classList.remove("animate-spin");
        this.disabled = false;
      }
    });

    setTimeout(() => {
      const circle = document.getElementById("progressCircle");
      if (circle) {
        const circumference = 534;
        const offset = circumference - (confidence / 100) * circumference;
        circle.style.strokeDashoffset = offset;
      }
    }, 100);

    animateElement(document.getElementById("resultBox"), { opacity: [0, 1], translateY: [50, 0] });
  } catch (err) {
    clearInterval(progressInterval);
    preview.innerHTML = `<div class="p-10 bg-white rounded-3xl shadow-xl text-center"><p class="text-red-600 font-bold">AI Link Failure</p></div>`;
  }
});
