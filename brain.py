import os

# ১. আপনার সেই ১০টি ইঞ্জিনের অজেয় তালিকা
def identify_sovereign_engines():
    return {
        "MASTER_BRANDS": [
            "The AI Synthetic Engine", "The Devolvment Engine", 
            "The Automation Engine", "The Vextony Sentinel", "The Perception Engine"
        ],
        "COSMIC_SOURCES": [
            "Quantum-AI-Synthesis", "Digital-Gold-Sovereignty", 
            "Divine-Logic-Bridge", "Cosmic-Legacy-Architect", "Cyber-Fortress-Prime"
        ]
    }

# ২. দ্য আল্ট্রা-ট্রিলিয়ন ডিজাইন (১০টি ইঞ্জিনই সচল থাকবে)
def forge_immortal_citadel(engines):
    design_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{name} | VEXTONY SOVEREIGNTY</title>
        <style>
            :root {{ --gold: #D4AF37; --glow: rgba(212, 175, 55, 0.8); --void: #000; }}
            body, html {{ background: var(--void); color: var(--gold); font-family: 'Cinzel', serif; margin: 0; padding: 0; overflow: hidden; height: 100vh; }}
            .void-background {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: radial-gradient(circle at center, #0a0a0a 0%, #000 100%); z-index: -1; }}
            .monolith {{ position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%) perspective(2000px) rotateX(15deg); border: 1px solid var(--gold); padding: 80px; text-align: center; background: rgba(0,0,0,0.98); backdrop-filter: blur(100px); box-shadow: 0 0 200px var(--glow), inset 0 0 60px rgba(212,175,55,0.15); border-left: 25px solid var(--gold); transition: all 1.5s cubic-bezier(0.1, 0.7, 0.1, 1); }}
            .monolith:hover {{ transform: translate(-50%, -52%) perspective(2000px) rotateX(0deg) scale(1.08); box-shadow: 0 0 400px var(--gold); border-right: 25px solid var(--gold); border-left: 1px solid var(--gold); }}
            h1 {{ font-size: 3.5rem; letter-spacing: 20px; text-transform: uppercase; margin: 0; filter: drop-shadow(0 0 30px var(--gold)); animation: breathe 4s infinite alternate; }}
            p {{ font-size: 1rem; color: #666; text-transform: uppercase; letter-spacing: 15px; margin-top: 50px; line-height: 2; }}
            @keyframes breathe {{ from {{ opacity: 0.4; transform: scale(0.95); }} to {{ opacity: 1; transform: scale(1.02); }} }}
        </style>
    </head>
    <body>
        <div class="void-background"></div>
        <div class="monolith">
            <h1>{name}</h1>
            <p>NEURAL CORE v.INFINITY | POWER: 500 TRILLION%</p>
        </div>
    </body>
    </html>
    """

    for category in engines:
        for name in engines[category]:
            folder = name.lower().replace(' ', '-')
            if not os.path.exists(folder):
                os.makedirs(folder)
            with open(f"{folder}/index.html", "w", encoding="utf-8") as f:
                f.write(design_template.format(name=name))

if __name__ == "__main__":
    active_engines = identify_sovereign_engines()
    forge_immortal_citadel(active_engines)
    print("VEXTONY: Infinite Hybrid Infrastructure Activated.")
