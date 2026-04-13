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

  preview.innerHTML = `
    <div class="w-full flex flex-col items-center mt-16" id="loadingBox">
      <p class="text-xl text-[#7a3f1a] mb-8 animate-pulse">Analyzing your dog's breed with PawPrint AI...</p>
      <div class="relative w-[100px] h-[100px] flex items-center justify-center">
        <div class="w-16 h-16 border-4 border-[#e26215] border-t-transparent rounded-full animate-spin"></div>
      </div>
    </div>
  `;

  const form = new FormData();
  form.append("image", file);

  try {
    const res = await fetch(PREDICT_URL, {
      method: "POST",
      body: form,
    });

    if (!res.ok) {
      const text = await res.text();
      preview.innerHTML = `<p class="text-red-600">Server error: ${text}</p>`;
      return;
    }

    const data = await res.json();

    if (data.fallback_url) {
      preview.innerHTML = `
        <div class="flex flex-col items-center gap-8 w-full max-w-[600px] mt-12 mx-auto p-10 bg-white rounded-[2rem] shadow-xl border border-[#e26215]/20">
          <div class="w-20 h-20 bg-[#e26215]/10 rounded-full flex items-center justify-center">
            <span class="material-symbols-outlined text-[3rem] text-[#e26215]">info</span>
          </div>
          <div class="text-center">
            <h3 class="text-2xl font-black text-[#e26215] mb-2 font-poppins uppercase">AI Identification Blocked</h3>
            <p class="text-[#8a4f2a]/80 font-medium">Google's safety filters prevented an automatic match. You can still identify your dog using Google Lens below.</p>
          </div>
          <img src="${data.image_url}" class="w-48 h-32 object-cover rounded-xl border-2 border-[#eee]" />
          <a href="${data.fallback_url}" target="_blank" 
             class="w-full py-4 bg-gradient-to-r from-[#e26215] to-[#f15a24] text-white font-bold rounded-full text-center shadow-lg hover:shadow-2xl transition-all transform hover:-translate-y-1">
             SEARCH WITH GOOGLE LENS
          </a>
        </div>
      `;
      return;
    }

    if (data.error) {
      preview.innerHTML = `<p class="text-red-600">Error: ${data.error}</p>`;
      return;
    }

    if (!data.predictions || !data.predictions.length) {
      preview.innerHTML = `<p class="text-red-600">No predictions returned.</p>`;
      return;
    }

    const top = data.predictions[0];
    const confidence = Math.round(top.confidence * 100);
    const desc = top.description || {
      short_desc: "No description available.",
      traits: [],
      fun_fact: "No fun fact available.",
    };
    const breedClean = top.breed.replace(/_/g, " ").toUpperCase();

    const exampleImg = `static/breed_examples/${top.breed}.jpg`;

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
             <img id="breedImage" src="${exampleImg}" alt="${breedClean}"
                onerror="this.src='images/logo.png'"
                class="w-[400px] h-[260px] object-cover rounded-2xl shadow-xl border-4 border-[#e26215]" />
            
            <button id="generatePdfBtn" data-breed="${breedClean}"
                class="btn-ghost font-poppins font-bold text-[18px] px-10 py-4 rounded-full border-4 border-[#e26215] bg-transparent text-[#e26215] transition-all hover:bg-[#e26215] hover:text-white flex items-center justify-center gap-3">
                <span class="material-symbols-outlined hidden" id="pdfSpinner">autorenew</span>
                <span id="pdfBtnText">GENERATE PDF REPORT</span>
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
          btnText.innerText = "GENERATE PDF REPORT";
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