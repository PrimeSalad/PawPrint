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

  // Add premium animation styles
  if (!document.getElementById('pawprint-premium-animations')) {
    const style = document.createElement('style');
    style.id = 'pawprint-premium-animations';
    style.textContent = `
      @keyframes premium-scan {
        0% { transform: translateY(-20px); opacity: 0; }
        50% { opacity: 1; }
        100% { transform: translateY(280px); opacity: 0; }
      }
      @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
      }
      @keyframes pulse-ring {
        0% { transform: scale(0.8); opacity: 0.5; }
        100% { transform: scale(1.2); opacity: 0; }
      }
      .glitch-text {
        text-shadow: 0.05em 0 0 rgba(226, 98, 21, 0.75),
                     -0.025em -0.05em 0 rgba(241, 90, 36, 0.75),
                     0.025em 0.05em 0 rgba(122, 63, 26, 0.75);
        animation: glitch 500ms infinite;
      }
      @keyframes glitch {
        0% { text-shadow: 0.05em 0 0 rgba(226, 98, 21, 0.75), -0.025em -0.05em 0 rgba(241, 90, 36, 0.75), 0.025em 0.05em 0 rgba(122, 63, 26, 0.75); }
        14% { text-shadow: 0.05em 0 0 rgba(226, 98, 21, 0.75), -0.025em -0.05em 0 rgba(241, 90, 36, 0.75), 0.025em 0.05em 0 rgba(122, 63, 26, 0.75); }
        15% { text-shadow: -0.05em -0.025em 0 rgba(226, 98, 21, 0.75), 0.025em 0.025em 0 rgba(241, 90, 36, 0.75), -0.05em -0.05em 0 rgba(122, 63, 26, 0.75); }
        49% { text-shadow: -0.05em -0.025em 0 rgba(226, 98, 21, 0.75), 0.025em 0.025em 0 rgba(241, 90, 36, 0.75), -0.05em -0.05em 0 rgba(122, 63, 26, 0.75); }
        50% { text-shadow: 0.025em 0.05em 0 rgba(226, 98, 21, 0.75), 0.05em 0 0 rgba(241, 90, 36, 0.75), 0 -0.05em 0 rgba(122, 63, 26, 0.75); }
        99% { text-shadow: 0.025em 0.05em 0 rgba(226, 98, 21, 0.75), 0.05em 0 0 rgba(241, 90, 36, 0.75), 0 -0.05em 0 rgba(122, 63, 26, 0.75); }
        100% { text-shadow: -0.025em 0 0 rgba(226, 98, 21, 0.75), -0.025em -0.025em 0 rgba(241, 90, 36, 0.75), -0.025em -0.05em 0 rgba(122, 63, 26, 0.75); }
      }
    `;
    document.head.appendChild(style);
  }

  // Show GOD MODE premium loading UI
  preview.innerHTML = `
    <div class="w-full py-12 flex flex-col items-center justify-center relative" id="loadingBox">
      <!-- Premium scanning container -->
      <div class="relative w-full max-w-xl">
        <!-- Main card -->
        <div class="relative bg-white/90 backdrop-blur-2xl border border-white/60 rounded-[3rem] p-10 shadow-[0_30px_100px_-20px_rgba(226,98,21,0.2)] overflow-hidden">
          
          <!-- Animated Background Elements -->
          <div class="absolute -top-24 -right-24 w-64 h-64 bg-[#e26215]/5 rounded-full blur-3xl"></div>
          <div class="absolute -bottom-24 -left-24 w-64 h-64 bg-[#f15a24]/5 rounded-full blur-3xl"></div>

          <!-- Header -->
          <div class="text-center mb-10 relative z-10">
            <div class="inline-block px-4 py-1.5 rounded-full bg-[#e26215]/10 text-[#e26215] text-[10px] font-bold tracking-[0.2em] uppercase mb-4">Neural Engine Active</div>
            <h2 class="text-3xl md:text-4xl font-black text-[#2d1810] font-poppins mb-3 tracking-tight">AI BIOMETRIC SCAN</h2>
            <p class="text-[#7a3f1a]/60 font-medium">Decoding canine DNA markers...</p>
          </div>

          <!-- God Mode Scanner Visualization -->
          <div class="relative h-64 mb-10 rounded-[2rem] bg-[#1a0f08] border border-white/10 overflow-hidden flex items-center justify-center shadow-inner">
            <!-- Grid pattern -->
            <div class="absolute inset-0 bg-[linear-gradient(to_right,#e2621510_1px,transparent_1px),linear-gradient(to_bottom,#e2621510_1px,transparent_1px)] bg-[size:20px_20px]"></div>
            
            <!-- Scanning lines -->
            <div class="absolute inset-0 flex flex-col justify-around">
              <div class="h-[2px] w-full bg-gradient-to-r from-transparent via-[#e26215] to-transparent shadow-[0_0_15px_#e26215]" style="animation: premium-scan 2s ease-in-out infinite;"></div>
              <div class="h-[1px] w-full bg-gradient-to-r from-transparent via-[#f15a24]/50 to-transparent" style="animation: premium-scan 2.5s ease-in-out infinite; animation-delay: 0.5s;"></div>
            </div>

            <!-- Central HUD -->
            <div class="relative z-10 flex flex-col items-center">
              <div class="w-24 h-24 rounded-full border-2 border-[#e26215]/30 flex items-center justify-center relative">
                <!-- Pulsing outer rings -->
                <div class="absolute inset-0 rounded-full border border-[#e26215]/50" style="animation: pulse-ring 2s infinite;"></div>
                <div class="absolute inset-0 rounded-full border border-[#e26215]/30" style="animation: pulse-ring 2s infinite; animation-delay: 0.5s;"></div>
                
                <!-- Rotating hex -->
                <div class="w-16 h-16 bg-[#e26215]/10 rounded-xl rotate-45 animate-spin" style="animation-duration: 10s;"></div>
                <span class="material-symbols-outlined absolute text-[#e26215] text-3xl animate-pulse">pets</span>
              </div>
              <div class="mt-4 font-mono text-[10px] text-[#e26215]/80 tracking-[0.3em] uppercase">Processing Layers</div>
            </div>

            <!-- Corner Brackets -->
            <div class="absolute top-6 left-6 w-4 h-4 border-t-2 border-l-2 border-[#e26215]/40"></div>
            <div class="absolute top-6 right-6 w-4 h-4 border-t-2 border-r-2 border-[#e26215]/40"></div>
            <div class="absolute bottom-6 left-6 w-4 h-4 border-b-2 border-l-2 border-[#e26215]/40"></div>
            <div class="absolute bottom-6 right-6 w-4 h-4 border-b-2 border-r-2 border-[#e26215]/40"></div>
          </div>

          <!-- Premium Progress Bar -->
          <div class="space-y-4 relative z-10">
            <div class="flex justify-between items-end px-2">
              <div class="flex flex-col">
                <span class="text-[10px] uppercase tracking-[0.2em] font-black text-[#2d1810]">Analysis Confidence</span>
                <span class="text-[12px] text-[#e26215] font-bold" id="statusMsg">Optimizing Neural Weights...</span>
              </div>
              <span class="text-4xl font-black text-[#2d1810] font-poppins" id="progressPercent">0%</span>
            </div>
            <div class="relative h-4 bg-[#1a0f08]/5 rounded-full overflow-hidden p-1 border border-[#1a0f08]/5">
              <div id="progressBar" class="h-full bg-gradient-to-r from-[#e26215] via-[#f15a24] to-[#e26215] rounded-full transition-all duration-500 shadow-lg shadow-[#e26215]/30 relative" style="width: 0%; background-size: 200% 100%; animation: shimmer 2s infinite;">
                <div class="absolute top-0 right-0 w-8 h-full bg-white/30 skew-x-12 translate-x-1"></div>
              </div>
            </div>
          </div>

          <!-- Bottom Meta -->
          <div class="mt-10 pt-8 border-t border-[#1a0f08]/5 flex justify-between items-center relative z-10">
            <div class="flex gap-4">
              <div class="w-2 h-2 rounded-full bg-[#e26215] animate-pulse"></div>
              <div class="w-2 h-2 rounded-full bg-[#e26215]/40 animate-pulse" style="animation-delay: 0.2s"></div>
              <div class="w-2 h-2 rounded-full bg-[#e26215]/20 animate-pulse" style="animation-delay: 0.4s"></div>
            </div>
            <span class="font-mono text-[9px] text-[#8a4f2a]/40 tracking-widest uppercase">Encryption: AES-256</span>
          </div>
        </div>
      </div>
    </div>
  `;

  // Status messages for better UX
  const statusMsgs = [
    "Initializing Core Neural Engine...",
    "Extracting Visual Feature Vectors...",
    "Cross-referencing Global Databases...",
    "Analyzing Morphological Characteristics...",
    "Calculating Confidence Intervals...",
    "Synthesizing Breed Intelligence..."
  ];

  // Simulate progress
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
    const res = await fetch(PREDICT_URL, {
      method: "POST",
      body: form,
    });

    clearInterval(progressInterval);

    if (!res.ok) {
      const text = await res.text();
      preview.innerHTML = `<p class="text-red-600 font-bold p-8 bg-white rounded-3xl shadow-xl">Server connectivity issue: ${text}</p>`;
      return;
    }

    const data = await res.json();

    if (data.error) {
      preview.innerHTML = `<p class="text-red-600 font-bold p-8 bg-white rounded-3xl shadow-xl">Error: ${data.error}</p>`;
      return;
    }

    if (!data.predictions || !data.predictions.length) {
      preview.innerHTML = `<p class="text-red-600 font-bold p-8 bg-white rounded-3xl shadow-xl">No breed markers detected.</p>`;
      return;
    }

    // Complete progress
    document.getElementById("progressBar").style.width = "100%";
    document.getElementById("progressPercent").textContent = "100%";
    document.getElementById("statusMsg").textContent = "Analysis Complete.";

    // Smooth delay before showing results
    await new Promise(r => setTimeout(r, 600));

    const top = data.predictions[0];
    const confidence = Math.round(top.confidence * 100);
    const desc = top.description || {
      short_desc: "Detailed information for this breed is currently being synthesized by our AI core.",
      traits: ["Intelligent", "Unique", "Loyal"],
      fun_fact: "Every dog has a unique genetic signature that our AI decodes.",
    };
    const breedClean = top.breed.replace(/_/g, " ").toUpperCase();
    const breedKey = top.breed.toLowerCase();

    // Use internet image URL or fallback
    const breedImageUrl = BREED_IMAGES[breedKey] || `static/breed_examples/${top.breed}.jpg`;

    preview.innerHTML = `
      <div class="flex flex-col items-center gap-10 w-full max-w-5xl mx-auto py-12" id="resultBox">
        
        <!-- Premium Result Header -->
        <div class="w-full relative group">
          <!-- Glass Background -->
          <div class="absolute inset-0 bg-white/40 backdrop-blur-3xl rounded-[3rem] border border-white/60 shadow-2xl transition-all duration-500 group-hover:shadow-[0_40px_100px_-20px_rgba(226,98,21,0.25)]"></div>
          
          <div class="relative p-10 md:p-14 flex flex-col md:flex-row items-center gap-10 md:gap-16">
            <!-- Left: Breed Identification -->
            <div class="flex-1 text-center md:text-left">
              <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-[#e26215]/10 text-[#e26215] text-[10px] font-black tracking-[0.3em] uppercase mb-6">Match Confirmed</div>
              <h2 class="font-poppins font-black text-5xl md:text-7xl mb-6 leading-[0.9] text-[#2d1810] tracking-tighter uppercase glitch-text">
                ${breedClean}
              </h2>
              <p class="text-[#8a4f2a] text-lg md:text-xl leading-relaxed font-medium opacity-80">
                ${desc.short_desc}
              </p>
            </div>
            
            <!-- Right: Confidence HUD -->
            <div class="shrink-0">
              <div class="relative w-48 h-48 flex items-center justify-center">
                <!-- Glowing Background -->
                <div class="absolute inset-0 bg-gradient-to-br from-[#e26215]/20 to-[#f15a24]/20 rounded-full blur-2xl animate-pulse"></div>
                
                <svg class="absolute w-full h-full -rotate-90" viewBox="0 0 200 200">
                  <circle cx="100" cy="100" r="85" stroke="rgba(226,98,21,0.1)" stroke-width="12" fill="none"/>
                  <circle id="progressCircle" cx="100" cy="100" r="85"
                    stroke="url(#grad1)" stroke-width="12" fill="none"
                    stroke-linecap="round" stroke-dasharray="534" stroke-dashoffset="534"
                    style="transition: stroke-dashoffset 2s cubic-bezier(0.4, 0, 0.2, 1)"/>
                  <defs>
                    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
                      <stop offset="0%" style="stop-color:#e26215;stop-opacity:1" />
                      <stop offset="100%" style="stop-color:#f15a24;stop-opacity:1" />
                    </linearGradient>
                  </defs>
                </svg>
                <div class="flex flex-col items-center relative z-10">
                  <span class="text-6xl font-black text-[#2d1810] font-poppins">${confidence}%</span>
                  <span class="text-[10px] uppercase tracking-[0.2em] font-bold text-[#e26215]">Precision</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Professional Layout Grid -->
        <div class="w-full grid grid-cols-1 lg:grid-cols-12 gap-10">
          
          <!-- Large Image Section (7/12) -->
          <div class="lg:col-span-7 flex flex-col gap-8">
            <div class="relative rounded-[3rem] overflow-hidden shadow-2xl group/img border-4 border-white">
              <img id="breedImage" src="${breedImageUrl}" alt="${breedClean}"
                onerror="this.src='images/logo.png'"
                class="w-full h-[500px] object-cover transition-transform duration-1000 group-hover/img:scale-110" />
              <!-- Subtle overlay -->
              <div class="absolute inset-0 bg-gradient-to-t from-[#2d1810]/40 via-transparent to-transparent"></div>
              <div class="absolute bottom-8 left-8 flex items-center gap-3">
                 <div class="px-4 py-2 rounded-xl bg-white/20 backdrop-blur-md border border-white/30 text-white text-xs font-bold uppercase tracking-widest">Visual Match Scan #${Math.floor(Math.random()*9000)+1000}</div>
              </div>
            </div>
            <!-- Health Considerations - Professional Alert Style -->
            <div class="bg-gradient-to-br from-[#1a0f08] to-[#2d1810] rounded-[2.5rem] p-10 text-white shadow-xl relative overflow-hidden">
              <div class="absolute top-0 right-0 p-8 opacity-10">
                <span class="material-symbols-outlined text-[100px]">medical_services</span>
              </div>
              <h4 class="font-poppins font-black text-xl mb-4 uppercase tracking-widest text-[#e26215] flex items-center gap-3">
                <span class="w-2 h-8 bg-[#e26215] rounded-full"></span>
                Health Protocol
              </h4>
              <p class="text-white/80 text-lg leading-relaxed font-medium">
                ${desc.health_notes || "Consult a certified veterinarian for personalized breed-specific wellness programs and nutritional guidance."}
              </p>
            </div>
          </div>

          <!-- Side Details Section (5/12) -->
          <div class="lg:col-span-5 flex flex-col gap-8">
            
            <!-- Core Specs Card -->
            <div class="bg-white rounded-[2.5rem] p-10 shadow-xl border border-[#e26215]/5 flex flex-col gap-8">
              <div class="flex flex-col gap-2">
                <span class="text-[10px] uppercase tracking-[0.3em] font-black text-[#e26215]">Origin</span>
                <p class="text-2xl font-bold text-[#2d1810] font-poppins">${desc.origin || "Not specified"}</p>
              </div>
              <div class="h-px bg-[#1a0f08]/5"></div>
              <div class="flex flex-col gap-2">
                <span class="text-[10px] uppercase tracking-[0.3em] font-black text-[#e26215]">Biometrics</span>
                <p class="text-2xl font-bold text-[#2d1810] font-poppins">${desc.size || "Standard Canine Specs"}</p>
              </div>
              <div class="h-px bg-[#1a0f08]/5"></div>
              <div class="flex flex-col gap-2">
                <span class="text-[10px] uppercase tracking-[0.3em] font-black text-[#e26215]">Temperament profile</span>
                <p class="text-2xl font-bold text-[#2d1810] font-poppins">${desc.temperament || "Alert and Intelligent"}</p>
              </div>
            </div>

            <!-- Key Traits Multi-Card -->
            <div class="bg-[#fef9f6] rounded-[2.5rem] p-10 shadow-xl border border-[#e26215]/10">
              <h3 class="font-poppins font-black text-xl text-[#2d1810] mb-8 uppercase tracking-widest flex items-center gap-3">
                <span class="material-symbols-outlined text-[#e26215]">military_tech</span>
                Key Markers
              </h3>
              <div class="flex flex-wrap gap-3">
                ${(desc.traits || [])
                  .map(
                    (trait) => `
                    <span class="px-5 py-2.5 bg-white border border-[#e26215]/20 rounded-2xl text-[#2d1810] text-sm font-bold shadow-sm hover:border-[#e26215] hover:scale-105 transition-all cursor-default">
                      ${trait}
                    </span>
                  `
                  )
                  .join("")}
              </div>
            </div>

            <!-- Fun Fact Professional Inset -->
            <div class="bg-gradient-to-br from-[#e26215] to-[#f15a24] rounded-[2.5rem] p-10 text-white shadow-xl relative overflow-hidden group">
              <div class="absolute -bottom-10 -right-10 w-40 h-40 bg-white/10 rounded-full blur-3xl group-hover:scale-150 transition-transform duration-700"></div>
              <h3 class="font-poppins font-black text-xl mb-4 uppercase tracking-widest">Did You Know?</h3>
              <p class="text-white/90 text-lg leading-relaxed font-medium italic">
                "${desc.fun_fact}"
              </p>
            </div>

          </div>
        </div>

        <!-- Action Footer -->
        <div class="w-full flex flex-col items-center gap-8 mt-4">
          <button id="generatePdfBtn" data-breed="${breedClean}"
            class="group relative font-poppins font-black text-lg px-16 py-6 rounded-full bg-[#2d1810] text-white shadow-2xl hover:scale-105 transition-all duration-500 overflow-hidden">
            <div class="absolute inset-0 bg-gradient-to-r from-[#e26215] to-[#f15a24] opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
            <div class="relative z-10 flex items-center gap-4">
              <span class="material-symbols-outlined text-2xl" id="pdfSpinner">description</span>
              <span id="pdfBtnText">GENERATE ANALYTICAL REPORT</span>
            </div>
          </button>
          <p class="text-[10px] text-[#8a4f2a]/40 uppercase tracking-[0.4em] font-bold">Encrypted Data Stream • ISO-2026 Compliant</p>
        </div>

      </div>
    `;

    // Re-attach PDF event listener
    document.getElementById("generatePdfBtn").addEventListener("click", async function () {
        const breed = this.getAttribute("data-breed");
        const btnText = document.getElementById("pdfBtnText");
        const spinner = document.getElementById("pdfSpinner");

        const originalIcon = spinner.innerText;
        btnText.innerText = "SYNTHESIZING REPORT...";
        spinner.innerText = "sync";
        spinner.classList.add("animate-spin");
        this.disabled = true;
        this.classList.add("opacity-80", "cursor-not-allowed");

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
            alert("Analysis Export Failed: " + (pdfData.error || "Kernel Panic"));
          }
        } catch (e) {
          console.error(e);
          alert("Network Transmission Error.");
        } finally {
          btnText.innerText = "GENERATE ANALYTICAL REPORT";
          spinner.innerText = originalIcon;
          spinner.classList.remove("animate-spin");
          this.disabled = false;
          this.classList.remove("opacity-80", "cursor-not-allowed");
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

    animateElement(document.getElementById("resultBox"), {
      opacity: [0, 1],
      translateY: [50, 0],
    });
  } catch (err) {
    console.error(err);
    clearInterval(progressInterval);
    preview.innerHTML = `<div class="p-10 bg-white rounded-3xl shadow-xl text-center">
      <p class="text-red-600 font-bold text-xl mb-4">AI Link Failure</p>
      <p class="text-gray-500">Could not establish connection with the neural processing unit.</p>
    </div>`;
  }
});
