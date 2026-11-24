#!/usr/bin/env python3
"""Gera frames cARCKHÉtograficos de exemplo via ARCKHÉimg (flux2-klein, 16:9).
Idempotente: pula arquivos ja existentes. Tolerante a falhas."""
import base64, json, os, sys, time, urllib.request

API = "http://localhost:8000/generate"
OUT = os.path.dirname(os.path.abspath(__file__))
MODEL = "flux2-klein"
W, H = 1280, 720
NEG = "text, watermark, logo, deformed, low quality, cartoon, illustration, oversaturated"

JOBS = {
 "ex-samurai-bridge": "Lone samurai walking across a long narrow suspension bridge between two mountains, heavy rain and rolling fog filling the deep canyon below, holding a katana, wide cARCKHÉtic shot, 35mm lens, cold desaturated blue-grey color grade, volumetric light, subtle film grain, photorealistic film still",
 "ex-postapoc-wide": "Extreme wide high-angle drone shot of a vast post-apocalyptic desert, cracked dusty road stretching to the horizon, a heavily rusted vintage muscle car half-buried in sand surrounded by debris, a lone older man in a worn leather coat approaching from behind, silent abandoned atmosphere, cold desaturated blue-grey grade, film grain, photorealistic",
 "ex-postapoc-handle": "Over-the-shoulder close-up, a gloved hand firmly pulling the rusty door handle of an old car as the door gives way, dust and rust flakes falling from corroded metal, extreme texture detail on worn leather glove and oxidized metal, shallow depth of field, tense silent moment, cARCKHÉtic photorealistic film still",
 "ex-lighting-rim": "CARCKHÉtic portrait of a rugged man lit only by a thin rim light separating him from a dark background, negative fill, 80/20 lighting ratio, deep controlled shadows, moody mysterious atmosphere, motivated single warm light source, photorealistic, film grain",
 "ex-depth-layers": "CARCKHÉtic three-layer depth composition, sharp foreground branches, a lone figure in the midground, distant misty mountains in the background, atmospheric haze separating the planes, shallow depth of field, teal and amber color contrast, photorealistic film still",
 "ex-particles": "A silhouetted figure backlit by strong volumetric god rays, heavy atmospheric particles, glowing embers and floating dust, drifting fog, cARCKHÉtic depth, warm rim light against cold background, photorealistic film still, film grain",
 "ex-slowmo-action": "High speed dynamic action moment frozen in time, a muscle car drifting on a cracked desert road throwing up a huge dust cloud, low side tracking angle, motion energy, dramatic cARCKHÉtic lighting, photorealistic film still",
 "ex-watchmaker": "An elderly watchmaker with magnifying glasses in a dim dusty old workshop, hundreds of brass clocks on the walls, warm soft light through a dirty window, holding a small rusty mechanical bird, nostalgic calm atmosphere, cARCKHÉtic photorealistic film still, warm golden grade",
 "ex-dialogue-ots": "Over-the-shoulder cARCKHÉtic shot of two characters facing each other in tense emotional conversation, shallow depth of field, soft motivated window light, muted color palette, subtext and quiet tension, photorealistic film still",
 "ex-camera-move": "CARCKHÉtic dolly-in shot of a lone figure standing in a luxury hotel suite at night, city lights through tall windows, dramatic side lighting, strong sense of depth and parallax, photorealistic film still, moody",
}

def gen(name, prompt):
    path = os.path.join(OUT, name + ".png")
    if os.path.exists(path) and os.path.getsize(path) > 10000:
        print("skip", name); return True
    body = json.dumps({"model": MODEL, "prompt": prompt, "width": W, "height": H,
                       "negative_prompt": NEG}).encode()
    req = urllib.request.Request(API, data=body, headers={"Content-Type": "application/json"})
    try:
        t = time.time()
        with urllib.request.urlopen(req, timeout=300) as r:
            data = json.loads(r.read())
        with open(path, "wb") as f:
            f.write(base64.b64decode(data["image"]))
        print(f"OK   {name}  {time.time()-t:.1f}s")
        return True
    except Exception as e:
        print(f"FAIL {name}: {e}")
        return False

if __name__ == "__main__":
    ok = 0
    for name, prompt in JOBS.items():
        if gen(name, prompt): ok += 1
    print(f"\n{ok}/{len(JOBS)} imagens geradas em {OUT}")
