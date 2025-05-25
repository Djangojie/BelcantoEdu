# BelcantoEdu 🎶
**Controllable Singing Voice Generation System for Vocal Education**


---

## 1. Overview
**BelcantoEdu** implements a diffusion-based singing-voice generator that can be *explicitly controlled* by ten bel-canto technique ratings (vibrato depth, resonance position, laryngeal height, breath support, etc.).  
It is the official code release for our paper:

> **“BelcantoEdu: Controllable Singing Voice Generation System for Vocal Education.”**  

The system enables:

* ⚙️ **Technique-conditioned diffusion** — injects a 10-dimensional technique embedding into every denoising step;  
* 🎛 **Timbre conversion module** — morphs synthesized vocals to match any target singer;  
* 🧠 **Transfer-learning pipeline** — fine-tunes on scarce bel-canto datasets;  
* 📊 **Evaluation suite** — automatic Technique-Acc, FAD, MOS scripts;  
* 🌐 **Real-time Gradio demo** for classroom deployment.

---

## 2. Relationship to Upstream Repository
This project is a **fork & re-implementation** of the open-source project  
**“Audio-Diffusion”** by Robert Dargavel Smith ([@teticio](https://github.com/teticio)), available at  
<https://github.com/teticio/audio-diffusion>. :contentReference[oaicite:0]{index=0}

### Key Modifications
| Area | Upstream | BelcantoEdu Additions |
|------|----------|-----------------------|
| Conditioning | Unconditional or text prompts | 10-dimensional bel-canto technique vector **(new)** |
| Model | DDPM (mel-spectrogram→audio) | + Cross-attention injectors, + U-Net blocks for technique |
| Training | Generic music loops | Transfer-learning scripts for bel-canto dataset |
| Inference | Batch | Real-time streaming + timbre convert |
| Eval | N/A | Technique classifier, FAD, MOS utilities |

Full diff is documented in `CHANGELOG.md`.

---

## 3. Quick Start

```bash
# 1) Clone
git clone https://github.com/your-id/belcantoedu.git
cd belcantoedu

# 2) Environment
conda env create -f environment.yml
conda activate belcantoedu     # Python ≥3.9, PyTorch ≥2.2

# 3) Prepare data
bash scripts/download_datasets.sh      # or place your own dataset under data/
python tools/preprocess.py --config configs/preprocess.yaml

# 4) Pre-train or fine-tune
python train_diffusion.py  --config configs/belcanto_pretrain.yaml
python finetune.py         --config configs/belcanto_finetune.yaml

# 5) Inference (waveform out)
python inference.py --checkpoint checkpoints/belcanto.ckpt \
                    --tech_vector 2,4,1,5,3, ... \
                    --out sample.wav
