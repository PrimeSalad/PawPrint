const fileUpload = document.getElementById("fileUpload");
const preview = document.getElementById("preview");

const IS_PRODUCTION = window.location.hostname !== "localhost" && window.location.hostname !== "127.0.0.1";
const API_BASE_URL = IS_PRODUCTION ? "/api" : (import.meta.env.VITE_API_URL || "http://localhost:5000");
const PREDICT_URL = `${API_BASE_URL}/predict`;
const GENERATE_PDF_URL = `${API_BASE_URL}/generate_pdf`;

// High-fidelity fallback images for popular breeds
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

function animateElement(el, props = {}) {
  if (!el) return;
  el.animate(
    [
      { opacity: props.opacity?.[0] ?? 0, transform: `translateY(${props.translateY?.[0] ?? 20}px)` },
      { opacity: props.opacity?.[1] ?? 1, transform: `translateY(${props.translateY?.[1] ?? 0}px)` }
    ],
    { duration: 600, fill: "forwards", easing: "ease-out" }
  );
}

fileUpload.addEventListener("change", async function () {
  const file = this.files[0];
  if (!file) return;

  // Add styles for scanning effect
  if (!document.getElementById('pp-scanner-css')) {
    const style = document.createElement('style');
    style.id = 'pp-scanner-css';
    style.textContent = `
      @keyframes scan-line { 0% { top: 0%; opacity: 0; } 50% { opacity: 1; } 100% { top: 100%; opacity: 0; } }
      .scanner-active::after { content: ''; position: absolute; left: 0; width: 100%; height: 4px; background: #e26215; box-shadow: 0 0 20px #e26215; animation: scan-line 2.5s linear infinite; z-index: 20; }
    `;
    document.head.appendChild(style);
  }

  // Initial HUD loading state
  preview.innerHTML = `
    <div class="w-full max-w-xl mx-auto py-12 px-4" id="loadingHUD">
      <div class="bg-[#1a0f08] border border-[#e26215]/30 rounded-3xl p-8 relative overflow-hidden shadow-2xl">
        <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,#e2621510,transparent)]"></div>
        <div class="relative z-10 text-center">
          <div class="inline-block px-4 py-1 rounded-full border border-[#e26215]/40 text-[#e26215] text-[11px] font-bold tracking-[0.3em] uppercase mb-6">Neural Link Established</div>
          <div class="w-20 h-20 mx-auto mb-6 rounded-full border-2 border-dashed border-[#e26215]/50 flex items-center justify-center animate-spin" style="animation-duration: 10s">
            <span class="material-symbols-outlined text-[#e26215] text-4xl animate-pulse" style="animation: none">biotech</span>
          </div>
          <h2 class="text-white font-black text-3xl tracking-tighter mb-2">SCANNING BIOMETRICS</h2>
          <div class="flex items-center justify-between text-[#e26215] font-mono text-sm mb-2 px-2">
            <span id="statusMsg">Initializing core...</span>
            <span id="progressPercent">0%</span>
          </div>
          <div class="h-2 w-full bg-white/10 rounded-full overflow-hidden">
            <div id="progressBar" class="h-full bg-[#e26215] shadow-[0_0_15px_#e26215] transition-all duration-500" style="width: 0%"></div>
          </div>
        </div>
      </div>
    </div>
  `;

  const statusMsgs = ["Fetching Pixels...", "Analyzing Patterns...", "DNA Sequencing...", "Finalizing Profile..."];
  let progress = 0;
  const progressInterval = setInterval(() => {
    if (progress < 95) {
      progress += Math.random() * 12;
      if (progress > 95) progress = 95;
      document.getElementById("progressBar").style.width = progress + "%";
      document.getElementById("progressPercent").textContent = Math.round(progress) + "%";
      document.getElementById("statusMsg").textContent = statusMsgs[Math.floor((progress/100)*statusMsgs.length)];
    }
  }, 200);

  const form = new FormData();
  form.append("image", file);

  try {
    const res = await fetch(PREDICT_URL, { method: "POST", body: form });
    clearInterval(progressInterval);
    if (!res.ok) throw new Error("Connection failed");

    const data = await res.json();
    if (data.error || !data.predictions?.length) throw new Error(data.error || "No match found");

    document.getElementById("progressBar").style.width = "100%";
    document.getElementById("progressPercent").textContent = "100%";
    await new Promise(r => setTimeout(r, 400));

    const top = data.predictions[0];
    const confidence = Math.round(top.confidence * 100);
    const desc = top.description || {};
    const breedDisplayName = top.breed.replace(/_/g, " ").toUpperCase();
    const breedKey = top.breed.toLowerCase();

    // IMAGE LOGIC: 
    // 1. Backend direct image_url
    // 2. High-res manual map (using lowercase key)
    // 3. Local path (using original model case string)
    // 4. Fallback logo
    const imgUrl = desc.image_url || BREED_IMAGES[breedKey] || `static/breed_examples/${top.breed}.jpg`;

    preview.innerHTML = `
      <div class="w-full max-w-5xl mx-auto py-8 px-4" id="resultContainer" style="opacity:0">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch">
          
          <!-- LEFT: Image Card (5/12) -->
          <div class="lg:col-span-5 h-full flex flex-col">
            <div class="relative flex-1 rounded-[2.5rem] overflow-hidden border-[6px] border-white shadow-2xl scanner-active bg-gray-50 min-h-[450px]">
              <img src="${imgUrl}" alt="${breedDisplayName}" 
                class="w-full h-full object-cover" 
                onerror="this.src='images/logo.png'">
              <div class="absolute bottom-8 left-8 right-8">
                <div class="backdrop-blur-xl bg-black/40 border border-white/20 rounded-2xl p-5 shadow-2xl">
                   <div class="flex justify-between items-center mb-2">
                      <span class="text-white/70 text-[11px] font-black tracking-widest uppercase">Match Analysis</span>
                      <span class="text-[#e26215] font-black text-2xl font-poppins">${confidence}%</span>
                   </div>
                   <div class="h-2 w-full bg-white/20 rounded-full overflow-hidden">
                      <div class="h-full bg-gradient-to-r from-[#e26215] to-[#f15a24]" style="width: ${confidence}%"></div>
                   </div>
                </div>
              </div>
            </div>
          </div>

          <!-- RIGHT: Data Card (7/12) -->
          <div class="lg:col-span-7 flex flex-col gap-6">
            <div class="bg-white rounded-[2.5rem] p-10 md:p-12 shadow-2xl flex-1 flex flex-col border border-gray-100">
              <div class="mb-8">
                <div class="inline-block px-4 py-1.5 bg-[#e26215]/10 text-[#e26215] rounded-xl text-[11px] font-black tracking-[0.2em] uppercase mb-6">Confirmed Genetic Profile</div>
                <h2 class="text-[#2d1810] font-black text-4xl md:text-5xl lg:text-6xl tracking-tighter leading-[0.9] mb-8">${breedDisplayName}</h2>
                <p class="text-gray-600 text-base md:text-lg leading-relaxed font-medium line-clamp-4 italic">"${desc.short_desc || "Breed markers successfully decoded. Synthesis complete."}"</p>
              </div>

              <!-- Biometric Grid -->
              <div class="grid grid-cols-2 gap-6 mb-10">
                <div class="bg-[#fef9f6] p-6 rounded-3xl border border-[#e26215]/10 shadow-sm">
                  <span class="text-[11px] font-black text-[#e26215] uppercase tracking-widest block mb-2">Origin</span>
                  <span class="text-[#2d1810] font-black text-sm md:text-base leading-tight block">${desc.origin || "Ancient lineage"}</span>
                </div>
                <div class="bg-[#fef9f6] p-6 rounded-3xl border border-[#e26215]/10 shadow-sm">
                  <span class="text-[11px] font-black text-[#e26215] uppercase tracking-widest block mb-2">Size Metric</span>
                  <span class="text-[#2d1810] font-black text-sm md:text-base leading-tight block">${desc.size || "Standard Canine"}</span>
                </div>
                <div class="col-span-2 bg-[#1a0f08] p-6 rounded-3xl shadow-xl relative overflow-hidden group">
                  <div class="absolute inset-0 bg-gradient-to-r from-[#e26215]/5 to-transparent"></div>
                  <span class="text-[11px] font-black text-[#e26215] uppercase tracking-widest block mb-3 relative z-10">Temperament Core</span>
                  <span class="text-white text-base md:text-lg font-bold leading-relaxed relative z-10">${desc.temperament || "Alert, loyal, and balanced profile."}</span>
                </div>
              </div>

              <!-- Action & Traits Row -->
              <div class="mt-auto flex flex-col sm:flex-row items-center gap-6">
                <div class="flex-1 flex flex-wrap gap-3">
                   ${(desc.traits || ["Loyal", "Active", "Smart"]).slice(0, 3).map(t => `<span class="px-5 py-2 bg-gray-50 border border-gray-100 rounded-xl text-xs font-black text-[#2d1810] uppercase tracking-tight shadow-sm hover:scale-105 transition-transform">${t}</span>`).join("")}
                </div>
                <button id="pdfBtn" data-breed="${breedDisplayName}" class="w-full sm:w-auto bg-[#2d1810] hover:bg-[#e26215] hover:scale-105 active:scale-95 text-white px-10 py-5 rounded-2xl font-black text-xs tracking-[0.2em] transition-all flex items-center justify-center gap-3 shadow-2xl">
                  <span class="material-symbols-outlined text-xl" id="pdfIco">article</span>
                  GENERATE REPORT
                </button>
              </div>
            </div>

            <!-- Health Protocol Overlay (Large & Bold) -->
            <div class="bg-gradient-to-br from-[#f15a24] to-[#e26215] text-white p-8 rounded-[2.5rem] shadow-2xl flex items-center gap-8 border-4 border-white/20">
              <div class="w-16 h-16 bg-white/20 rounded-2xl flex items-center justify-center shrink-0 shadow-inner">
                <span class="material-symbols-outlined text-4xl">medical_services</span>
              </div>
              <div>
                <h4 class="text-[11px] font-black uppercase tracking-[0.3em] mb-2 text-white/90">Clinical Health Protocol</h4>
                <p class="text-sm md:text-base font-black leading-tight">${desc.health_notes || "Consult a certified veterinarian for specialized diagnostic maintenance."}</p>
              </div>
            </div>
          </div>

        </div>
      </div>
    `;

    // PDF Handler
    document.getElementById("pdfBtn").addEventListener("click", async function () {
      const b = this.getAttribute("data-breed");
      const i = document.getElementById("pdfIco");
      i.classList.add("animate-spin");
      i.innerText = "sync";
      try {
        const res = await fetch(GENERATE_PDF_URL, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ breed: b })
        });
        const d = await res.json();
        if (d.pdf_url) window.open(d.pdf_url, "_blank");
      } catch (e) { alert("Report Sync Failed"); }
      finally { i.classList.remove("animate-spin"); i.innerText = "article"; }
    });

    animateElement(document.getElementById("resultContainer"), { opacity: [0, 1], translateY: [50, 0] });

  } catch (err) {
    preview.innerHTML = `<div class="p-16 text-center bg-white rounded-3xl shadow-2xl max-w-md mx-auto border-b-8 border-red-500"><h3 class="text-red-500 font-black text-2xl mb-4">SYSTEM CRITICAL ERROR</h3><p class="text-gray-500 font-bold">${err.message}</p></div>`;
  }
});
